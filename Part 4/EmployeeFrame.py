import sys
import tkinter as tk
import tkinter.ttk as ttk

class EmployeeFrame(ttk.Frame):

    def __init__(self, master, conn):
        super().__init__(master)
        self.conn = conn
        self.bg = "red"
        
        label = ttk.Label(self, text="Database Name:")
        label.pack(padx=5)
        
        entry = ttk.Entry(self)
        entry.pack(padx=5)
        
        button = ttk.Button(self, text="CONNECT", command=lambda: self.checkConn(entry.get()))
        button.pack(padx=5)
        
        self.pack(expand=True, fill=tk.BOTH)