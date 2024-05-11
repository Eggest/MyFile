import tkinter as tk
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from tkinter import messagebox

def encrypt():
    key = key_entry.get().encode('utf-8')
    if len(key) != 16:
        messagebox.showerror("Error", "密钥长度必须为16字节")
        return
    cipher = AES.new(key, AES.MODE_ECB)
    data = entry.get().encode('utf-8')
    padded_data = pad(data, AES.block_size)
    cipher_text = cipher.encrypt(padded_data)
    result.set(b64encode(cipher_text).decode('utf-8'))

def decrypt():
    key = key_entry.get().encode('utf-8')
    if len(key) != 16:
        messagebox.showerror("Error", "密钥长度必须为16字节")
        return
    decipher = AES.new(key, AES.MODE_ECB)
    cipher_text = b64decode(result.get().encode('utf-8'))
    plain_text = decipher.decrypt(cipher_text)
    unpadded_text = unpad(plain_text, AES.block_size)
    try:
        entry.set(unpadded_text.decode('utf-8'))
    except UnicodeDecodeError:
        messagebox.showerror("Error", "解密失败")

# 创建窗口
window = tk.Tk()
window.title("加密和解密工具")
window.geometry("400x200")

# 密钥输入框
key_entry = tk.StringVar()
key_label = tk.Label(window, text="输入16字节密钥:")
key_label.pack()
key_input = tk.Entry(window, textvariable=key_entry)
key_input.pack()

# 输入框
entry = tk.StringVar()
entry_label = tk.Label(window, text="输入文本:")
entry_label.pack()
entry_input = tk.Entry(window, textvariable=entry)
entry_input.pack()

# 加密按钮
encrypt_button = tk.Button(window, text="加密", command=encrypt)
encrypt_button.pack()

# 解密按钮
decrypt_button = tk.Button(window, text="解密", command=decrypt)
decrypt_button.pack()

# 加密后的结果
result = tk.StringVar()
result_label = tk.Label(window, text="加密结果:")
result_label.pack()
result_output = tk.Entry(window, textvariable=result, state='readonly')
result_output.pack()

# 运行窗口
window.mainloop()
