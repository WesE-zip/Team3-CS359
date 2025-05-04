import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgBox
from docs import Queries as db

class EquipmentFrame():

    def __init__(self, master, mainFrame, conn):
        self.master = master
        self.mainFrame = mainFrame
        self.db = db.Query(conn)
        self.sel_option = tk.StringVar(self.mainFrame)
        self.currEquip = {}
        
        self.loadReadFrame()
        
    def loadReadFrame(self):
        data = self.db.getAllEquip()
        
        if not data:
            self.loadMenuFrame()
            return
        
        self.clearFrame()
                
        label = ttk.Label(self.mainFrame, text="EQUIPMENT", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)
        
        index = 0   
        columns = ("name", "type", "quantity", "gymId")

        self.tree = ttk.Treeview(self.mainFrame, columns=columns)
        self.tree.pack(padx=5, pady=5)

        self.tree.column("#0", stretch=tk.NO, width=60)
        self.tree.column("name", stretch=tk.NO, width=120)
        self.tree.column("type", stretch=tk.NO, width=120)
        self.tree.column("quantity", stretch=tk.NO, width=120)
        self.tree.column("gymId", stretch=tk.NO, width=120)
        
        self.tree.heading('#0', text='ID')
        self.tree.heading('name', text='Name')
        self.tree.heading('type', text='Type')
        self.tree.heading('quantity', text='Quantity')
        self.tree.heading('gymId', text='Gym')

        for index, line in enumerate(data):
            self.tree.insert('', tk.END, iid = index,
                text = line[0], values = line[1:])
            
        self.tree.bind("<Double-1>", self.loadEquipmentFrame)
                
        button = ttk.Button(self.mainFrame, text="NEW EQUIPMENT(+)", command=lambda: self.loadCreateFrame())
        button.pack(fill=tk.X, padx=5, pady=5)
                
        button = ttk.Button(self.mainFrame, text="BACK", command=lambda: self.master.loadMenuFrame())
        button.pack(fill=tk.X, padx=5, pady=5)
        
        
    def loadCreateFrame(self):
        self.clearFrame()
        
        types = ["Strength", "Cardio", "Flexibility", "Recovery"]
        gyms = ["GYM1", "GYM2", "GYM3", "GYM4"]
        
        self.nameVar = tk.StringVar()
        self.quantityVar = tk.StringVar()
        self.typeOption = tk.StringVar()
        self.gymOption = tk.StringVar()
        
        self.typeOption.set(types[0])
        self.quantityVar.set("1")
        self.gymOption.set(gyms[0])
        
        equipLabel = ttk.Label(self.mainFrame, text="CREATE EQUIPMENT", font=("Helvetica", 12, "bold"))
        equipLabel.pack(padx=5, pady=15)
        
        nameLabel = ttk.Label(self.mainFrame, text="NAME:")
        nameLabel.pack(fill=tk.X, padx=5, pady=5)
        
        nameEntry = ttk.Entry(self.mainFrame, textvariable=self.nameVar)
        nameEntry.pack(fill=tk.X, padx=5)
        
        typeLabel = ttk.Label(self.mainFrame, text="TYPE:")
        typeLabel.pack(fill=tk.X, padx=5, pady=5)
        
        typeDropdown = ttk.OptionMenu(self.mainFrame, self.typeOption, self.typeOption.get(), *types)
        typeDropdown.pack(fill=tk.X, padx=5)
        
        quantityLabel = ttk.Label(self.mainFrame, text="QUANTITY:")
        quantityLabel.pack(fill=tk.X, padx=5, pady=5)
        
        quantityEntry = ttk.Entry(self.mainFrame, textvariable=self.quantityVar)
        quantityEntry.pack(fill=tk.X, padx=5)
        
        gymLabel = ttk.Label(self.mainFrame, text="GYM:")
        gymLabel.pack(fill=tk.X, padx=5, pady=5)
        
        gymDropdown = ttk.OptionMenu(self.mainFrame, self.gymOption, self.gymOption.get(), *gyms)
        gymDropdown.pack(fill=tk.X, padx=5)
        
        self.saveButton = ttk.Button(self.mainFrame, text="SAVE", command=lambda: self.createEquipment())
        self.saveButton.pack(fill=tk.X, padx=5, pady=10)
        
        self.backButton = ttk.Button(self.mainFrame, text="BACK", command=lambda: self.loadReadFrame())
        self.backButton.pack(fill=tk.X, padx=5, pady=5)
        
        
    def loadEquipmentFrame(self, event):
        item = self.tree.selection()[0]
        equipID = self.tree.item(item, "text")
        
        self.currEquip = self.db.getEquipByID(equipID)
        types = ["Strength", "Cardio", "Flexibility", "Recovery"]
        gyms = ["GYM1", "GYM2", "GYM3", "GYM4", "GYM5"]
        
        if not self.currEquip:
            return
        
        self.clearFrame()
                        
        self.nameVar = tk.StringVar()
        self.quantityVar = tk.StringVar()
        typeOption = tk.StringVar()
        gymOption = tk.StringVar()
        
        self.nameVar.set(self.currEquip["name"])
        self.quantityVar.set(str(self.currEquip["quantity"]))
        typeOption.set(self.currEquip["type"].upper())
        gymOption.set(gyms[int(self.currEquip["gymId"])])
        
        equipLabel = ttk.Label(self.mainFrame, text="EQUIPMENT", font=("Helvetica", 12, "bold"))
        equipLabel.pack(padx=5, pady=15)
        
        nameLabel = ttk.Label(self.mainFrame, text="NAME:")
        nameLabel.pack(fill=tk.X, padx=5, pady=5)
        
        self.nameEntry = ttk.Entry(self.mainFrame, textvariable=self.nameVar)
        self.nameEntry.pack(fill=tk.X, padx=5)
        self.nameEntry.config(state="disabled")
        
        typeLabel = ttk.Label(self.mainFrame, text="TYPE:")
        typeLabel.pack(fill=tk.X, padx=5, pady=5)
        
        self.typeDropdown = ttk.OptionMenu(self.mainFrame, typeOption, typeOption.get(), *types)
        self.typeDropdown.pack(fill=tk.X, padx=5)
        self.typeDropdown.config(state="disabled")
        
        quantityLabel = ttk.Label(self.mainFrame, text="QUANTITY:")
        quantityLabel.pack(fill=tk.X, padx=5, pady=5)
        
        self.quantityEntry = ttk.Entry(self.mainFrame, textvariable=self.quantityVar)
        self.quantityEntry.pack(fill=tk.X, padx=5)
        self.quantityEntry.config(state="disabled")
        
        gymLabel = ttk.Label(self.mainFrame, text="GYM:")
        gymLabel.pack(fill=tk.X, padx=5, pady=5)
        
        self.gymDropdown = ttk.OptionMenu(self.mainFrame, gymOption, gymOption.get(), *gyms)
        self.gymDropdown.pack(fill=tk.X, padx=5)
        self.gymDropdown.config(state="disabled")
        
        self.editButton = ttk.Button(self.mainFrame, text="EDIT", command=lambda: self.loadEditFrame())
        self.editButton.pack(fill=tk.X, padx=5, pady=5)
        
        self.backButton = ttk.Button(self.mainFrame, text="BACK", command=lambda: self.loadReadFrame())
        self.backButton.pack(fill=tk.X, padx=5, pady=10)
        
    
    def loadCancelEditFrame(self):
        self.saveButton.destroy()
        self.cancelButton.destroy()
        
        self.editButton = ttk.Button(self.mainFrame, text="EDIT", command=lambda: self.loadEditFrame())
        self.editButton.pack(fill=tk.X, padx=5, pady=5)
        
        self.backButton = ttk.Button(self.mainFrame, text="BACK", command=lambda: self.loadReadFrame())
        self.backButton.pack(fill=tk.X, padx=5, pady=10)
        
        self.nameEntry.config(state="disabled")
        self.typeDropdown.config(state="disabled")
        self.quantityEntry.config(state="disabled")
        self.gymDropdown.config(state="disabled")
    
    def loadEditFrame(self):
        self.editButton.destroy()
        self.backButton.destroy()
        
        self.saveButton = ttk.Button(self.mainFrame, text="SAVE", command=lambda: self.updateEquipment())
        self.saveButton.pack(fill=tk.X, padx=5, pady=10)
        
        self.cancelButton = ttk.Button(self.mainFrame, text="CANCEL", command=lambda: self.loadCancelEditFrame())
        self.cancelButton.pack(fill=tk.X, padx=5, pady=5)
        
        self.nameEntry.config(state="enabled")
        self.typeDropdown.config(state="enabled")
        self.quantityEntry.config(state="enabled")
        self.gymDropdown.config(state="enabled")
        

        
    def createEquipment(self):
        self.currEquip["name"] = self.nameVar.get() 
        self.currEquip["type"] = self.typeOption.get()
        self.currEquip["quantity"] = self.quantityVar.get()
        self.currEquip["gymId"] = self.gymOption.get()
        
        print(self.currEquip["name"])
    
        if self.currEquip["name"] == "":
            msgBox.showerror("New Equipment", "INVALID: Empty fields.")
            return
        
        if not self.db.createEquip(self.currEquip):
            msgBox.showerror("SQLite Connection", "ERROR: Failed to create equipment.")
            return
        
        self.loadReadFrame()    
        
    def updateEquipment(self):
        self.currEquip["name"] = self.nameVar.get() 
        self.currEquip["type"] = self.typeOption.get()
        self.currEquip["quantity"] = self.quantityVar.get()
        self.currEquip["gymId"] = self.gymOption.get()
        
        print(self.currEquip["name"])
    
        if self.currEquip["name"] == "":
            msgBox.showerror("Update Equipment", "INVALID: Empty fields.")
            return
        
        if not self.db.createEquip(self.currEquip):
            msgBox.showerror("SQLite Connection", "ERROR: Failed to update equipment.")
            return
        
        self.loadReadFrame() 

    def deleteEquipment(self):
        label = ttk.Label(self.mainFrame, text="DELETE FRAME")
        label.pack(padx=5, pady=5)
        
        
    # Load CRUD Frames - Selected option
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
            
            