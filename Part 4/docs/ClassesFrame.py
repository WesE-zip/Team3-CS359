import sys
import tkinter as tk
import tkinter.ttk as ttk

class ClassesFrame():

    def __init__(self, master, mainFrame, conn):
        self.master = master
        self.mainFrame = master
        self.conn = conn
        
        self.loadCreateFrame()
        
        
    def loadCreateFrame(self):
        self.clearFrame()
        
        label = ttk.Label(self.mainFrame, text="Database Name:")
        label.pack(padx=5)
        
        entry = ttk.Entry(self.mainFrame)
        entry.pack(padx=5)
        
        button = ttk.Button(self.mainFrame, text="CONNECT", command=lambda: self.checkConn(entry.get()))
        button.pack(padx=5)
        
        
    # Function to clear out all widgets inside a frame
    def clearFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()