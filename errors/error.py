from tkinter import messagebox
from tkinter import *

class Error(Exception):
    """Base class for custom execptions"""
    def __init__(self, message_type, message):
        self.message_type = message_type
        if self.message_type == "showerror":
            Tk().wm_withdraw()
            messagebox.showerror(title="Error", message=message)
        super().__init__()
