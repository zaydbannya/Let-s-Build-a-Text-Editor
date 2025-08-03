from tkinter import *
from tkinter.filrdialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("codingal's text editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
def open_file():
    """open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("text files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"Codingal's text editor - {filepath}")
def save_file():
    filepath = asksaveasfilename(
        defaulttextension="txt",
        filetypes[("Text Files", "*.txt"), ("all files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text=txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"codingal's text editor - {filepath}")
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, db=2)
btn_open = Button(fr_buttons, text="open", command)