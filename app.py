import tkinter as tk
from tkinter import ttk, messagebox

from login_window import LoginWindow
from main_window import MainWindow

class SecurePasswordVaultApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw() # Hide the root window initially

        # Setup theme
        # style = ttk.Style()
        # try:
        #     style.theme_use('vista') # Try 'vista' on Windows
        # except:
        #     style.theme_use('clam') # 'clam' or 'default' on Mac/Linux

        self.login_window = None
        self.main_window = None
        self.show_login()

    def show_login(self):
        """Show the login window."""
        # Ensure the main window is closed (if it exists)
        if self.main_window:
            self.main_window.destroy()
            self.main_window = None
        
        self.login_window = LoginWindow(self, self.handle_master_password_check)

    def handle_master_password_check(self, entered_password):
        hardcoded_password = "admin123" 
        
        if entered_password == hardcoded_password:
            if self.login_window:
                self.login_window.destroy()
                self.login_window = None
            self.show_main()
            return True
        return False

    def show_main(self):
        """Show the main application window."""
        self.main_window = MainWindow(self)

    def on_app_close(self):
        """Handle when the user requests to close the application (clicks X)."""
        if messagebox.askokcancel("Exit Application", "Do you want to exit the Secure Password Vault?"):
            self.destroy() # Close the entire application

if __name__ == "__main__":
    app = SecurePasswordVaultApp()
    app.mainloop()