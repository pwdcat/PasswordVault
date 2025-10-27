# import tkinter as tk
# from tkinter import ttk, messagebox
# import random
# import string
# from utils import center_toplevel_window

# class GeneratePasswordWindow(tk.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.parent = parent
#         self.title("Generate Strong Password")
#         self.geometry("400x350")
#         self.resizable(False, False)
#         self.protocol("WM_DELETE_WINDOW", self.on_close)
        
#         self.result = None # Để lưu mật khẩu đã tạo khi người dùng Copy

#         self.create_widgets()
#         self.generate_new_password() # Tạo mật khẩu khi cửa sổ mở
        
#         # Đảm bảo cửa sổ này luôn ở trên cùng và chờ
#         self.transient(parent)
#         self.grab_set()
#         center_toplevel_window(self, parent)

#     def create_widgets(self):
#         self.main_frame = ttk.Frame(self, padding="15")
#         self.main_frame.pack(fill=tk.BOTH, expand=True)

#         # Generated Password
#         ttk.Label(self.main_frame, text="Generated Password:", font=('Arial', 10, 'bold')).pack(anchor=tk.W, pady=(5, 2))
#         self.txt_generated_password = ttk.Entry(self.main_frame, width=40, font=('Arial', 10))
#         self.txt_generated_password.pack(fill=tk.X, pady=(0, 10))
#         self.txt_generated_password.config(state='readonly') # Không cho phép chỉnh sửa

#         self.btn_copy = ttk.Button(self.main_frame, text="Copy and Close", command=self.copy_password, width=15)
#         self.btn_copy.pack(pady=(0, 15))

#         # Options Checkboxes
#         self.cb_uppercase_var = tk.BooleanVar(value=True)
#         self.cb_lowercase_var = tk.BooleanVar(value=True)
#         self.cb_numbers_var = tk.BooleanVar(value=True)
#         self.cb_special_chars_var = tk.BooleanVar(value=True) # Mặc định chọn ký tự đặc biệt

#         ttk.Checkbutton(self.main_frame, text="Include Uppercase Letters (A-Z)", variable=self.cb_uppercase_var, command=self.generate_new_password).pack(anchor=tk.W, pady=2)
#         ttk.Checkbutton(self.main_frame, text="Include Lowercase Letters (a-z)", variable=self.cb_lowercase_var, command=self.generate_new_password).pack(anchor=tk.W, pady=2)
#         ttk.Checkbutton(self.main_frame, text="Include Numbers (0-9)", variable=self.cb_numbers_var, command=self.generate_new_password).pack(anchor=tk.W, pady=2)
#         ttk.Checkbutton(self.main_frame, text="Include Special Characters (!@#$)", variable=self.cb_special_chars_var, command=self.generate_new_password).pack(anchor=tk.W, pady=2)

#         # Length Selector
#         ttk.Label(self.main_frame, text="Length:", font=('Arial', 10, 'bold')).pack(anchor=tk.W, pady=(15, 2))
#         self.nud_length = ttk.Spinbox(self.main_frame, from_=8, to=64, increment=1, width=5, font=('Arial', 10), command=self.generate_new_password)
#         self.nud_length.set(16) # Mặc định độ dài 16
#         self.nud_length.pack(anchor=tk.W, pady=(0, 15))

#         # Action Buttons
#         self.button_frame = ttk.Frame(self.main_frame)
#         self.button_frame.pack(fill=tk.X, side=tk.BOTTOM)

#         self.btn_regenerate = ttk.Button(self.button_frame, text="Regenerate", command=self.generate_new_password, width=12)
#         self.btn_regenerate.pack(side=tk.LEFT, expand=True, padx=(0, 5))

#         self.btn_close = ttk.Button(self.button_frame, text="Cancel", command=self.on_close, width=12)
#         self.btn_close.pack(side=tk.RIGHT, expand=True, padx=(5, 0))

#     def generate_new_password(self):
#         uppercase_chars = string.ascii_uppercase
#         lowercase_chars = string.ascii_lowercase
#         number_chars = string.digits
#         special_chars = "!@#$%^&*()_-+=<>?/{}[]|" 

#         character_set = []
#         if self.cb_uppercase_var.get(): character_set.extend(list(uppercase_chars))
#         if self.cb_lowercase_var.get(): character_set.extend(list(lowercase_chars))
#         if self.cb_numbers_var.get(): character_set.extend(list(number_chars))
#         if self.cb_special_chars_var.get(): character_set.extend(list(special_chars))

#         if not character_set:
#             messagebox.showwarning("Selection Required", "Please select at least one character type.", parent=self)
#             self.txt_generated_password.config(state='normal')
#             self.txt_generated_password.delete(0, tk.END)
#             self.txt_generated_password.config(state='readonly')
#             self.result = None
#             return

#         password_length = int(self.nud_length.get())
#         if password_length <= 0:
#             password_length = 8
#             self.nud_length.set(8)

#         password_chars = []
#         # Đảm bảo mật khẩu chứa ít nhất một ký tự từ mỗi loại được chọn
#         if self.cb_uppercase_var.get(): password_chars.append(random.choice(uppercase_chars))
#         if self.cb_lowercase_var.get(): password_chars.append(random.choice(lowercase_chars))
#         if self.cb_numbers_var.get(): password_chars.append(random.choice(number_chars))
#         if self.cb_special_chars_var.get(): password_chars.append(random.choice(special_chars))

#         # Điền phần còn lại của mật khẩu
#         for _ in range(password_length - len(password_chars)):
#             password_chars.append(random.choice(character_set))
        
#         random.shuffle(password_chars) # Xáo trộn các ký tự
#         generated_password_str = "".join(password_chars)

#         self.txt_generated_password.config(state='normal') 
#         self.txt_generated_password.delete(0, tk.END)
#         self.txt_generated_password.insert(0, generated_password_str)
#         self.txt_generated_password.config(state='readonly')
        
#     def copy_password(self):
#         pwd = self.txt_generated_password.get()
#         if pwd:
#             self.clipboard_clear()
#             self.clipboard_append(pwd)
#             self.result = pwd # Lưu mật khẩu vào thuộc tính result
#             self.destroy() # Đóng cửa sổ sau khi sao chép
#         else:
#             messagebox.showwarning("No Password", "No password generated to copy.", parent=self)

#     def on_close(self):
#         self.result = None # Đặt result là None nếu người dùng chỉ đóng cửa sổ
#         self.destroy()