from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from webbrowser import open_new_tab
tk = Tk()
tk.title("GitHub加速网址打开器")
tk.geometry("300x130")
def open_url():
    url = url_entry.get()
    mode_combo_value = mode_combo.get()
    itf = False
    if mode_combo_value == "https://mirror.ghproxy.com":
        url = "https://mirror.ghproxy.com/" + url
        itf = True
    elif mode_combo_value == "https://ghproxy.org":
        url = "https://ghproxy.org/" + url
        itf = True
    elif mode_combo_value == "https://github.com(默认)":
        pass
        itf = True
    else:
        pass
    if itf:
        open_new_tab(url)
    else:
        showerror("错误", "请选择模式！")
url_label = Label(tk, text="GitHub文件地址(GitHub 文件 , Releases , archive ,\n           gist , raw.githubusercontent.com):")
url_label.pack()
url_entry = Entry(tk, width=30)
url_entry.pack()
mode_label = Label(tk, text="模式:")
mode_label.pack()
mode_combo = Combobox(tk, values=["https://mirror.ghproxy.com", "https://ghproxy.org", "https://github.com(默认)"])
mode_combo.pack()
open_button = Button(tk, text="打开", command=open_url)
open_button.pack()
tk.resizable(False, False)
# tk.iconbitmap("GitHubProxyWebStart.ico")
tk.mainloop()
# 本代码由 FittenCodeAI 参与编写