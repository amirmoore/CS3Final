import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox, simpledialog
from time import strftime
import os

class Diary():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Zendiary")
        self.mainframe = tk.Frame(self.root, background="pink")
        self.mainframe.pack(fill="both", expand=True)

        self.text = tk.Label(self.mainframe, text="ZenDiary", background="pink", font=("Times New Roman", 30))
        self.text.pack(padx=20, pady=15)

        # Widgets for login
        self.login_username_label = tk.Label(self.root, text="Username")
        self.login_username_label.pack()

        self.login_username = tk.Entry(self.root)
        self.login_username.pack()

        self.login_password_label = tk.Label(self.root, text="Password")
        self.login_password_label.pack()

        self.login_password = tk.Entry(self.root, show="*")
        self.login_password.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

        # Initialize file list side tab, but do not pack yet
        self.file_list_frame = tk.Frame(self.root, width=200, bg="light pink")
        self.file_list_label = tk.Label(self.file_list_frame, text="Previous Entries", bg="light pink")
        self.file_listbox = tk.Listbox(self.file_list_frame)
        self.show_time = tk.Label(self.file_list_frame, bg='light pink', font=('Times New Roman', 13))

        self.main_app = None

        self.root.mainloop()

    def update_file_list(self):
        self.file_listbox.delete(0, tk.END)
        for file in os.listdir("."):
            if file.endswith(".txt"):
                self.file_listbox.insert(tk.END, file)

    def myClick(self):
        filename = simpledialog.askstring("Save file", "Enter filename:")
        if filename:
            text_content = self.set_text_field.get(1.0, tk.END)
            full_path = filename + ".txt"
            with open(full_path, "w") as file:
                file.write(text_content)
            tk.Label(self.root, text="Saved!").pack()
            self.update_file_list()
        else:
            messagebox.showinfo("Cancelled", "Save operation cancelled.")

    def login(self):
        username = "amirmoore"
        password = "12345"
        if self.login_username.get() == username and self.login_password.get() == password:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
            self.mainZen()
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    def mainZen(self):
        self.login_username_label.destroy()
        self.login_username.destroy()
        self.login_password_label.destroy()
        self.login_password.destroy()
        self.login_button.destroy()

        self.main_app = tk.Frame(self.root, background="pink")
        self.main_app.pack(fill="both", expand=True)

        self.text = tk.Label(self.main_app, text="Talk to me.....", bg="pink", font=("Zapfino", 15))
        self.text.pack()

        self.set_text_field = tk.Text(self.main_app, height=20, width=70, bg="pink", borderwidth=0, highlightthickness=0)
        self.set_text_field.pack(pady=10)

        ttk.Button(self.main_app, text="Save", command=self.myClick).pack()

        self.file_list_frame.pack(side="left", fill="y")
        self.file_list_label.pack()
        self.file_listbox.pack(fill="both", expand=True)
        self.show_time.pack(anchor='sw', padx=5, pady=5)
        self.update_file_list()
        self.update_Time()

    def update_Time(self):
        time_string = strftime('%H:%M %p \n%x')
        self.show_time.config(text=time_string)
        self.show_time.after(30000, self.update_Time)

if __name__ == "__main__":
    Diary()
