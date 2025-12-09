python
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        birth_date = entry.get()
        birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        messagebox.showinfo("Your Age", f"Your age is: {age} years")
    except:
        messagebox.showerror("Error", "Please enter date in DD/MM/YYYY format.")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")

label = tk.Label(root, text="Enter your birth date (DD/MM/YYYY):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Calculate Age", command=calculate_age)
button.pack(pady=10)

root.mainloop()
