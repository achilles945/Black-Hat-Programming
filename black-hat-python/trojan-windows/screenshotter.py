# pip install pywin32
# to make native calls to windows API to grab screenshots

import base64
import win32api
import win32con
import win32gui
import win32ui

def get_dimensions():
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    return (width, height, left, top)

def screenshot(name='screenshot'):
    # handle to aquire entire desktop
    hdesktop = wine32gui.GetDesktopWindow()
    # determine the size of screeen
    width, height, left, top = get_dimensions()

    # device context using GetWindowDC and pass in a handle to desktop
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    # create a memory based device context to store image capture
    # until we write bitmap bytes to a file
    mem_dc = img_dc.CreateCompatibleDC()
    
    # create bitmap object that is set to the device context of our desktop
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    # sets the memory-based device context to point at the bitmap object 
    mem_dc.SelectObject(screenshot)

    # to take a bit-for-bit copy of desktop image 
    # and store in memory based context
    mem_dc.BitBlt((0,0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
    # dump this image to disk
    screenshot.SaveBitmapFile(mem_dc, f'{name}.bmp')
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())

def run():
    screenshot()
    with open('screenshot.bmp') as f:
        img = f.read()
    return img
if __name__ == '__main__':
    screenshot()
