import tkinter as tk
from tkinter import messagebox
import random
import string

def make_the_password():
    if length_box.get().isdigit() == False:
        messagebox.showerror("Error", "Please type a number!")
        return
    
    L = int(length_box.get())
    
    letters = string.ascii_lowercase
    big_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    
    pool = letters
    
    if var_up.get() == 1:
        pool = pool + big_letters
    if var_num.get() == 1:
        pool = pool + numbers
    if var_sym.get() == 1:
        pool = pool + symbols
        
    bad_chars = exclude_box.get()
    for c in bad_chars:
        pool = pool.replace(c, "")
        
    if pool == "":
        messagebox.showwarning("Error", "Pick something!")
        return

    my_password = ""
    for i in range(L):
        my_password = my_password + random.choice(pool)
    
    result_box.delete(0, tk.END)
    result_box.insert(0, my_password)

    if L < 5:
        note_label.config(text="Security Note: Too Short!", fg="red")
    elif L < 7 or (var_up.get() + var_num.get() + var_sym.get() < 2):
        note_label.config(text="Security Note: Missing Variability", fg="orange")
    else:       
        note_label.config(text="Security Note: All Conditions Met!", fg="green")

def copy_it():
    root.clipboard_clear()
    root.clipboard_append(result_box.get())
    messagebox.showinfo("Done", "Saved!")

root = tk.Tk()
root.title("Password Randomizer")
root.geometry("540x720")

tk.Label(root, text="Number of characters:").pack()
length_box = tk.Entry(root)
length_box.insert(0, "10")
length_box.pack()

tk.Button(root, text="OK", command=make_the_password).pack(pady=10)

tk.Label(root, text="Random password:").pack()
result_box = tk.Entry(root)
result_box.pack()

tk.Button(root, text="Copy Password", command=copy_it).pack(pady=5)

tk.Label(root, text="-------------------------").pack()
tk.Label(root, text="OPTIONS").pack()

var_up = tk.IntVar(value=1)
var_num = tk.IntVar(value=1)
var_sym = tk.IntVar(value=1)

tk.Checkbutton(root, text="Big Letters", variable=var_up).pack()
tk.Checkbutton(root, text="Numbers", variable=var_num).pack()
tk.Checkbutton(root, text="Symbols", variable=var_sym).pack()

tk.Label(root, text="Exclude these:").pack()
exclude_box = tk.Entry(root)
exclude_box.pack()

tk.Label(root, text="-------------------------").pack()
note_label = tk.Label(root, text="Security Note: Waiting...", font=("Arial", 10, "bold"))
note_label.pack(pady=10)

root.mainloop()