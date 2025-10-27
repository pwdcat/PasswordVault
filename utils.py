import tkinter as tk

def center_toplevel_window(toplevel_window, parent_window=None):
    """Centers a Toplevel window relative to its parent or the screen."""
    toplevel_window.update_idletasks()
    width = toplevel_window.winfo_width()
    height = toplevel_window.winfo_height()
    
    if parent_window:
        # Center relative to the parent window
        parent_x = parent_window.winfo_x()
        parent_y = parent_window.winfo_y()
        parent_width = parent_window.winfo_width()
        parent_height = parent_window.winfo_height()
        
        x = parent_x + (parent_width // 2) - (width // 2)
        y = parent_y + (parent_height // 2) - (height // 2)
    else:
        # Center relative to the screen
        x = (toplevel_window.winfo_screenwidth() // 2) - (width // 2)
        y = (toplevel_window.winfo_screenheight() // 2) - (height // 2)
    
    toplevel_window.geometry(f'{width}x{height}+{x}+{y}')