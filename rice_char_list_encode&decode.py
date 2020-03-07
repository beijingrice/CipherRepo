from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import sys
li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']
code_li = []
title = "Char List Encode & Decode"
tk = Tk()
tk.title(title)
L = Label(tk, text="Input text to cope with them.")
L.grid(row=0, column=0)
T = Text(tk, width=30, height=30)
T.grid(row=1, column=0)
E = Entry(tk)
E.grid(row=2, column=0)
L1 = Label(tk, text="Key Word")
L1.grid(row=2, column=1)
L2 = Label(tk, text="Coped text")
T1 = Text(tk, width=30, height=30)
T1.grid(row=4, column=0)


def set_code_li():
    global code_li
    key_word = list(set(E.get()))
    for each in key_word:
        code_li.append(each)
    for each in li:
        if each not in key_word:
            code_li.append(each)


def file_not_found_error():
    tkinter.messagebox.showerror(title, "File Not Found Error!")


def permission_error():
    tkinter.messagebox.showerror(title, "File Not Found Error!")


def read_file():
    filename = tkinter.filedialog.askopenfilename(title="Open a file to encode", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    try:
        with open(filename, "r") as obj:
            T.insert(INSERT, obj.read())
    except PermissionError:
        permission_error()
    except FileNotFoundError:
        file_not_found_error()


def write_file():
    filename = tkinter.filedialog.asksaveasfilename(title="Save the file.", filetypes=[("Text Files", "*.txt")])
    if ".txt" not in filename:
        filename = filename + ".txt"
    try:
        with open(filename, "w+") as obj:
            obj.write(T.get("0.0", "end"))
    except PermissionError:
        permission_error()
    except FileNotFoundError:
        file_not_found_error()


def encode():
    text = T.get("0.0", "end").lower()
    text_encoded = ""
    for each in text:
        if each in li:
            text_encoded = text_encoded + code_li[li.index(each)]
        if each not in li:
            text_encoded = text_encoded + each
    T1.delete("0.0", "end")
    T1.insert(INSERT, text_encoded)


def decode():
    text = T.get("0.0", "end").lower()
    text_decoded = ""
    for each in text:
        if each in li:
            text_decoded = text_decoded + li[code_li.index(each)]
        if each not in li:
            text_decoded = text_decoded + each
    T1.delete("0.0", "end")
    T1.insert(INSERT, text_decoded)


def _quit():
    cmd = tkinter.messagebox.askyesno(title, "Are you sure you want to quit?")
    if cmd:
        tk.destroy()
        sys.exit()


def _help():

    def _q_():
        help_page.destroy()

    help_page = Tk()
    help_page.title(title)
    title_label = Label(help_page, text="Help Page")
    title_label.grid(row=0, column=0)
    contents = Text(help_page, width=30, height=30)
    contents.insert(INSERT, """
Encode:
First set code list,
then input text to encode.
Decode:
First input text,
then decode.
""")
    contents.configure(state="disabled")
    contents.grid(row=1, column=0)
    finish = Button(help_page, text="Finish", command=_q_)
    finish.grid(row=2, column=0)


B = Button(tk, text="Set Code List", command=set_code_li)
B.grid(row=5, column=0)
B1 = Button(tk, text="Read File", command=read_file)
B1.grid(row=5, column=1)
B2 = Button(tk, text="Write File", command=write_file)
B2.grid(row=5, column=2)
B3 = Button(tk, text="Encode", command=encode)
B3.grid(row=5, column=3)
B4 = Button(tk, text="Decode", command=decode)
B4.grid(row=5, column=4)
B5 = Button(tk, text="Help Page", command=_help)
B5.grid(row=5, column=5)
tk.protocol("WM_DELETE_WINDOW", _quit)
tk.mainloop()
