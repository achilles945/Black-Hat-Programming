# pip install pycryptodomex

from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from io import BytesIO

import base64 
import zlib

def generate():
    new_key = RSA.generate(2048)
    private_key = new_key.exportKey()
    public_key = new_key.publickey().exportKey()

    with open('key.pri','wb') as f:
        f.write(private_key)
    with open('key.pub','wb') as f:
        f.write(public_key)

def get_rsa_cipher(keytype):
    with open(f'key.{keytype}') as f:
        key = f.read()
    rsakey = RSA.importKey(key)
    return (PKCS1_OAEP.new(rsakey), rsakey.size_in_bytes())

def encrypt(plaintext):
    # pass the plaintext as bytes and compress it
    compressed_text = zlib.compress(plaintext)

    # generate random session key to be used in the AES cipher
    session_key = get_random_bytes(16)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    #encrypt the compressed plaintext using that cipher
    ciphertext, tag = cipher_aes.encrypt_and_digest(compressed_text)
    cipher_rsa, _ = get_rsa_cipher('pub')
    # encrypt session key  with RSA key generated from the generated publik key
    encrypted_session_key = cipher_rsa.encrypt(session_key)
    # put all info we need to decrypt into one payload
    msg_payload = encrypted_session_key + cipher_aes.nonce + tag + ciphertext
    # base 64 encode it
    encrypted = base64.encodebytes(msg_payload)
    return(encrypted)

def decrypt(encrypted):
    # base64-decode the string into bytes
    encrypted_bytes = BytesIO(base64.decodebytes(encrypted))
    cipher_rsa, keysize_in_bytes = get_rsa_cipher('pri')
    
    # read encrypted session key along with other parameters we need to decrypt, from encrypted byte string
    encrypted_session_key = encrypted_bytes.read(keysize_in_bytes)
    nonce = encrypted_bytes.read(16)
    tag = encrypted_bytes.read(16)
    ciphertext = encrypted_bytes.read()

    # decrypt the session key using the RSA private key
    session_key = cipher_rsa.decrypt(encrypted_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    # use the key to decrypt the message itself with AES cipher
    decrypted = cipher_aes.decrypt_and_verify(ciphertext, tag)
    # decompress it into plaintext byte string 
    plaintext = zlib.decompress(decrypted)
    return plaintext

if __name__ == '__main__':
    plaintext = b'hey there you.'
    print(decrypt(encrypt(plaintext)))
