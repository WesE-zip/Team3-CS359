import sys
import tkinter as tk
import tkinter.ttk as ttk

class EquipmentFrame():

    def __init__(self, master, mainFrame, conn):
        self.master = master
        self.mainFrame = mainFrame
        self.conn = conn
        self.sel_option = tk.StringVar(self.mainFrame)
        
        self.loadReadFrame()
        
        
    def loadCreateFrame(self):
        self.clearFrame()
        
        label = ttk.Label(self.mainFrame, text="CREATE EQUIPMENT", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)
        
        label = ttk.Label(self.mainFrame, text="NAME:")
        label.pack(fill=tk.X, padx=5, pady=5)
        
        label = ttk.Entry(self.mainFrame)
        label.pack(fill=tk.X, padx=5)
        
        label = ttk.Label(self.mainFrame, text="TYPE:")
        label.pack(fill=tk.X, padx=5, pady=5)
        
        types = ["STRENGTH", "CARDIO", "FLEXIBILITY", "RECOVERY"]
        self.type_option = tk.StringVar(self.mainFrame)
        self.type_option.set(types[0])

        dropdown = ttk.OptionMenu(self.mainFrame, self.type_option, self.type_option.get(), *types)
        dropdown.pack(fill=tk.X, padx=5)
        
        label = ttk.Label(self.mainFrame, text="QUANTITY:")
        label.pack(fill=tk.X, padx=5, pady=5)
        
        entry = ttk.Entry(self.mainFrame)
        entry.pack(fill=tk.X, padx=5)
        
        label = ttk.Label(self.mainFrame, text="GYM:")
        label.pack(fill=tk.X, padx=5, pady=5)
        
        gyms = ["GYM1", "GYM2", "GYM3", "GYM4"]
        self.gym_option = tk.StringVar(self.mainFrame)
        self.gym_option.set(gyms[0])

        dropdown = ttk.OptionMenu(self.mainFrame, self.gym_option, self.gym_option.get(), *gyms)
        dropdown.pack(fill=tk.X, padx=5)
        
        button = ttk.Button(self.mainFrame, text="BACK", command=lambda: self.master.loadMenuFrame())
        button.pack(fill=tk.X, padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="SAVE", command=lambda: self.master.loadMenuFrame())
        button.pack(fill=tk.X, padx=5, pady=5)
        
    def loadReadFrame(self):
        self.clearFrame()
        
        label = ttk.Label(self.mainFrame, text="EQUIPMENT", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)
        
        data = [
           ["Bench Press", "STRENGTH", 6, 1],
           ["Treadmill", "CARDIO", 10, 3],
           ["Exercise Bike", "CARDIO", 4, 1],
           ["Crosstrainer", "STRENGTH", 8, 2],
        ]
        
        index = 0   
        columns = ("type", "quantity", "gymId")

        tree = ttk.Treeview(self.mainFrame, columns=columns)
        tree.pack(padx=5, pady=5)

        tree.column("#0", stretch=tk.NO, width=120)
        tree.heading('#0', text='Name')
        tree.column("type", stretch=tk.NO, width=120)
        tree.heading('type', text='Type')
        tree.column("quantity", stretch=tk.NO, width=120)
        tree.heading('quantity', text='Quantity')
        tree.column("gymId", stretch=tk.NO, width=120)
        tree.heading('gymId', text='Gym')

        for index, line in enumerate(data):
            tree.insert('', tk.END, iid = index,
                text = line[0], values = line[1:])
                
        
        
    def loadUpdateFrame(self):
        self.loadDropdown(2)
        
        label = ttk.Label(self.mainFrame, text="UPDATE FRAME")
        label.pack(padx=5, pady=5)

    def loadDeleteFrame(self):
        self.loadDropdown(3)
        
        label = ttk.Label(self.mainFrame, text="DELETE FRAME")
        label.pack(padx=5, pady=5) 
        
        
    # Creates the dropdown depending on current position.
    def loadDropdown(self, pos):
        self.clearFrame()
        # options = ["CREATE", "READ", "UPDATE", "DELETE"]
        # self.sel_option.set(options[pos])

        # dropdown = ttk.OptionMenu(self.mainFrame, self.sel_option, self.sel_option.get(), *options, command=lambda option: self.loadCRUDFrame())
        # dropdown.pack(padx=5, pady=5)
        
        
    # Load CRUD Frame 
    # Loads selected option
    # (Create, Read, Update, Delete)
    def loadCRUDFrame(self):
        if self.sel_option.get() == "CREATE":
            self.loadCreateFrame()
        if self.sel_option.get() == "READ":
            self.loadReadFrame()
        if self.sel_option.get() == "UPDATE":
            self.loadUpdateFrame()
        if self.sel_option.get() == "DELETE":
            self.loadDeleteFrame()
        
        
    # Function to clear out all widgets inside a frame
    def clearFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()