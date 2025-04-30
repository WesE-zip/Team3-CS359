import sys
import tkinter as tk
import tkinter.ttk as ttk

class EquipmentFrame():

    def __init__(self, master, mainFrame, conn):
        self.master = master
        self.mainFrame = mainFrame
        self.conn = conn
        
        self.loadCreateFrame()
        
        
    def loadCreateFrame(self):
        self.clearFrame()
        
        button = ttk.Button(self.mainFrame, text="BACK", command=lambda: self.master.loadMenuFrame())
        button.pack(padx=5, pady=5)
        
        options = ["CREATE", "READ", "UPDATE", "DELETE"]
        sel_option = tk.StringVar(self.mainFrame)
        sel_option.set(options[0])

        dropdown = ttk.OptionMenu(self.mainFrame, sel_option, *options, command=self.loadCRUDFrame(sel_option))
        dropdown.pack(padx=5, pady=5)
        
        label = ttk.Label(self.mainFrame, text="CREATE FRAME")
        label.pack(padx=5, pady=5)
        
        
    def loadReadFrame(self):
        self.clearFrame()
        
        button = ttk.Button(self.mainFrame, text="BACK", command=lambda: self.master.loadMenuFrame())
        button.pack(padx=5, pady=5)
        
        options = ["CREATE", "READ", "UPDATE", "DELETE"]
        sel_option = tk.StringVar(self.mainFrame)
        sel_option.set(options[1])

        dropdown = ttk.OptionMenu(self.mainFrame, sel_option, *options)
        dropdown.pack(padx=5, pady=5)
        
        label = ttk.Label(self.mainFrame, text="READ FRAME")
        label.pack(padx=5, pady=5)
        
        
    # Load CRUD Frame 
    # Loads selected option
    # (Create, Read, Update, Delete)
    def loadCRUDFrame(self, sel_option):
        print("Option: ", sel_option)
        if sel_option == "CREATE":
            self.loadCreateFrame()
            
        if sel_option == "READ":
            self.loadReadFrame()
        
        
    # Function to clear out all widgets inside a frame
    def clearFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()