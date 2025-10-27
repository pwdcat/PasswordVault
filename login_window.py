import tkinter as tk
from tkinter import ttk, messagebox
from utils import center_toplevel_window

class LoginWindow(tk.Toplevel):
    def __init__(self, parent_root, master_password_callback):
        super().__init__(parent_root)
        self.parent_root = parent_root
        self.master_password_callback = master_password_callback # Callback to check password

        self.title("Secure Password Vault - Login")
        self.geometry("350x200")
        self.resizable(False, False) # Disable resizing

        self.protocol("WM_DELETE_WINDOW", self.parent_root.on_app_close)

        # --- Widgets ---
        self.lbl_password = tk.Label(self, text="Master Password:", font=('Arial', 10))
        self.lbl_password.pack(pady=(20, 5))

        self.txt_password = tk.Entry(self, show="*", width=30, font=('Arial', 10))
        self.txt_password.pack(pady=5)
        self.txt_password.bind("<Return>", self.login) # Allow pressing Enter to login

        self.lbl_error_message = tk.Label(self, text="", fg="red", font=('Arial', 9))
        self.lbl_error_message.pack(pady=5)

        self.btn_login = tk.Button(self, text="Login", command=self.login, width=10, font=('Arial', 10))
        self.btn_login.pack(side=tk.LEFT, padx=(60, 10), pady=10)

        self.btn_exit = tk.Button(self, text="Exit", command=self.parent_root.on_app_close, width=10, font=('Arial', 10))
        self.btn_exit.pack(side=tk.RIGHT, padx=(10, 60), pady=10)

        self.txt_password.focus_set() # Set focus on the password entry field

        # Center the window
        center_toplevel_window(self)

    def login(self, event=None):
        entered_password = self.txt_password.get()
        if self.master_password_callback(entered_password):
            # Main application (parent_root) will handle closing this window
            pass
        else:
            self.lbl_error_message.config(text="Incorrect master password. Please try again.")
            self.txt_password.delete(0, tk.END)
            self.txt_password.focus_set()