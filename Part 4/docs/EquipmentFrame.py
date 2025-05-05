# Cruz Urbina

import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgBox
from docs import Queries as db

class EquipmentFrame():

    # --- CONSTRUCTOR ---
    def __init__(self, master, mainFrame, conn):
        self.master = master
        self.mainFrame = mainFrame
        self.db = db.Query(conn)
        self.sel_option = tk.StringVar()
        
        self.currEquip = {}
        self.allEquip = {}
        self.gyms = []
        self.types = ["Strength", "Cardio", "Flexibility", "Recovery"]
        
        self.loadAllEquipmentFrame()
        
        
    # --- MAIN EQUIPMENT FRAMES ---
        
    # --- LOAD ALL EQUIPMENT FRAME ---
    # Executes getAllEquipment: Gets all the equipment data.
    # Creates Equipment TreeView
    def loadAllEquipmentFrame(self):
        # Executes getAllEquipment: Gets all the equipment data.
        self.allEquip = self.getAllEquipment()
        
        if not self.allEquip:
            self.loadMenuFrame()
            return
        
        self.clearFrame()
                
        # EQUIPMENT TITLE
        label = ttk.Label(self.mainFrame, text="EQUIPMENT", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=20)
        
        index = 0   
        columns = ("name", "type", "quantity", "gym")

        # TREE VIEW
        self.tree = ttk.Treeview(self.mainFrame, columns=columns)
        self.tree.pack(padx=5, pady=5)

        # TREE COLUMNS
        self.tree.column("#0", stretch=tk.NO, width=60)
        self.tree.column("name", stretch=tk.NO, width=120)
        self.tree.column("type", stretch=tk.NO, width=120)
        self.tree.column("quantity", stretch=tk.NO, width=120)
        self.tree.column("gym", stretch=tk.NO, width=120)
        
        # TREE HEADING
        self.tree.heading('#0', text='ID')
        self.tree.heading('name', text='Name')
        self.tree.heading('type', text='Type')
        self.tree.heading('quantity', text='Quantity')
        self.tree.heading('gym', text='Gym')

        # POPULATE TREEVIEW
        for index, line in enumerate(self.allEquip):
            self.tree.insert('', tk.END, iid = index,
                text = line[0], values = line[1:])
            
        # SET TREE BINDING: loadEquipmentFrame
        self.tree.bind("<Double-1>", self.loadEquipmentFrame)
        
        # NEW EQUIPMENT BUTTON
        newEquipButton = ttk.Button(self.mainFrame, text="NEW EQUIPMENT(+)", command=lambda: self.loadCreateFrame())
        newEquipButton.pack(fill=tk.X, padx=5, pady=10)
        
        # BACK BUTTON
        backButton = ttk.Button(self.mainFrame, text="BACK", command=lambda: self.master.loadMenuFrame())
        backButton.pack(fill=tk.X, padx=5, pady=10)
        
    # --- LOAD CREATE EQUIPMENT FRAME ---
    # Executes getAllGyms: Gets all the gyms location data.
    # Collects Equipment Informations
    # (Name, Type, Quantity, Gym)
    def loadCreateFrame(self):
        # Executes getAllGyms: Gets all the gyms location data.
        self.gyms = self.getAllGyms()
        
        if not self.gyms:
            self.loadAllEquipmentFrame()
            return
            
        self.clearFrame()
        
        self.nameVar = tk.StringVar()
        self.quantityVar = tk.StringVar()
        self.typeOption = tk.StringVar()
        self.gymOption = tk.StringVar()
        
        # Assign currEquip Data to Inputs
        self.typeOption.set(self.types[0])
        self.quantityVar.set("1")
        self.gymOption.set(self.gyms[0])
        
        # EQUIPMENT TITLE
        equipLabel = ttk.Label(self.mainFrame, text="CREATE EQUIPMENT", font=("Helvetica", 12, "bold"))
        equipLabel.pack(padx=5, pady=20)
        
        # NAME INPUT
        nameLabel = ttk.Label(self.mainFrame, text="NAME:")
        nameLabel.pack(fill=tk.X, padx=5, pady=5)
        
        nameEntry = ttk.Entry(self.mainFrame, textvariable=self.nameVar)
        nameEntry.pack(fill=tk.X, padx=5)
        
        # TYPE INPUT
        typeLabel = ttk.Label(self.mainFrame, text="TYPE:")
        typeLabel.pack(fill=tk.X, padx=5, pady=5)
        
        typeDropdown = ttk.OptionMenu(self.mainFrame, self.typeOption, self.typeOption.get(), *self.types)
        typeDropdown.pack(fill=tk.X, padx=5)
        
        # QUANTITY INPUT
        quantityLabel = ttk.Label(self.mainFrame, text="QUANTITY:")
        quantityLabel.pack(fill=tk.X, padx=5, pady=5)
        
        quantityEntry = ttk.Entry(self.mainFrame, textvariable=self.quantityVar)
        quantityEntry.pack(fill=tk.X, padx=5)
        
        # GYM INPUT
        gymLabel = ttk.Label(self.mainFrame, text="GYM:")
        gymLabel.pack(fill=tk.X, padx=5, pady=5)
        
        gymDropdown = ttk.OptionMenu(self.mainFrame, self.gymOption, self.gymOption.get(), *self.gyms)
        gymDropdown.pack(fill=tk.X, padx=5)
        
        # SAVE BUTTON
        self.saveButton = ttk.Button(self.mainFrame, text="SAVE", command=lambda: self.createEquipment())
        self.saveButton.pack(fill=tk.X, padx=5, pady=10)
        
        # BACK BUTTON
        self.backButton = ttk.Button(self.mainFrame, text="BACK", command=lambda: self.loadAllEquipmentFrame())
        self.backButton.pack(fill=tk.X, padx=5, pady=10)
        
    # --- LOAD EQUIPMENT VIEW FRAME ---
    # Executes getEquipment: Gets all the equipment location data.
    # Executes getAllGyms: Gets all the gyms location data.
    # Displays Equipment Informations
    # (Name, Type, Quantity, Gym) 
    def loadEquipmentFrame(self, event):   
        # Executes getEquipment: Gets all the equipment location data.    
        self.currEquip = self.getEquipment()
        
        # Executes getAllGyms: Gets all the gyms location data.
        self.gyms = self.getAllGyms()
        
        if not self.currEquip or not self.gyms:            
            print("EQUPT: " + str(self.currEquip))
            print("GYM: " + str(self.gyms))
            return
                
        self.clearFrame()
                        
        self.nameVar = tk.StringVar()
        self.quantityVar = tk.StringVar()
        self.typeOption = tk.StringVar()
        self.gymOption = tk.StringVar()
        
        # Assign currEquip Data to Inputs
        self.nameVar.set(self.currEquip["name"])
        self.quantityVar.set(str(self.currEquip["quantity"]))
        self.typeOption.set(self.currEquip["type"])
        self.gymOption.set(self.currEquip["gymLoc"])
        
        # EQUIPMENT TITLE
        equipLabel = ttk.Label(self.mainFrame, text="EQUIPMENT", font=("Helvetica", 12, "bold"))
        equipLabel.pack(padx=5, pady=20)
        
        # NAME INPUT
        nameLabel = ttk.Label(self.mainFrame, text="NAME:")
        nameLabel.pack(fill=tk.X, padx=5, pady=5)
        
        self.nameEntry = ttk.Entry(self.mainFrame, textvariable=self.nameVar)
        self.nameEntry.pack(fill=tk.X, padx=5)
        self.nameEntry.config(state="disabled")
        
        # TYPE INPUT
        typeLabel = ttk.Label(self.mainFrame, text="TYPE:")
        typeLabel.pack(fill=tk.X, padx=5, pady=5)
        
        self.typeDropdown = ttk.OptionMenu(self.mainFrame, self.typeOption, self.typeOption.get(), *self.types)
        self.typeDropdown.pack(fill=tk.X, padx=5)
        self.typeDropdown.config(state="disabled")
        
        # QUANTITY INPUT
        quantityLabel = ttk.Label(self.mainFrame, text="QUANTITY:")
        quantityLabel.pack(fill=tk.X, padx=5, pady=5)
        
        self.quantityEntry = ttk.Entry(self.mainFrame, textvariable=self.quantityVar)
        self.quantityEntry.pack(fill=tk.X, padx=5)
        self.quantityEntry.config(state="disabled")
        
        # GYM INPUT
        gymLabel = ttk.Label(self.mainFrame, text="GYM:")
        gymLabel.pack(fill=tk.X, padx=5, pady=5)
        
        self.gymDropdown = ttk.OptionMenu(self.mainFrame, self.gymOption, self.gymOption.get(), *self.gyms)
        self.gymDropdown.pack(fill=tk.X, padx=5)
        self.gymDropdown.config(state="disabled")
        
        # EDIT BUTTON
        self.editButton = ttk.Button(self.mainFrame, text="EDIT", command=lambda: self.loadEditFrame())
        self.editButton.pack(fill=tk.X, padx=5, pady=5)
        
        # BACK BUTTON
        self.backButton = ttk.Button(self.mainFrame, text="BACK", command=lambda: self.loadAllEquipmentFrame())
        self.backButton.pack(fill=tk.X, padx=5, pady=5)
        
    # --- LOADS EDIT EQUIPMENT VIEW FRAME ---
    # Create Style for Cancel Button
    # Destroy Edit Button
    # Destroy Back Button 
    # Create Save Button 
    # Create Cancel Button
    # Create Delete Button
    # Enable Inputs: (Name, Type, Quantity, Gym) 
    def loadEditFrame(self):
        # Create Style for Cancel Button
        style = ttk.Style()
        style.configure("Cancel.TButton",
                        foreground="#d9534f",
                        background="#d9534f")

        # Destroy Edit Button
        # Destroy Back Button 
        self.editButton.destroy()
        self.backButton.destroy()
        
        # Create Save Button 
        self.saveButton = ttk.Button(self.mainFrame, text="SAVE", command=lambda: self.confirmSave())
        self.saveButton.pack(fill=tk.X, padx=5, pady=5)
        
        # Create Cancel Button
        self.cancelButton = ttk.Button(self.mainFrame, text="CANCEL", command=lambda: self.loadCancelEditFrame())
        self.cancelButton.pack(fill=tk.X, padx=5, pady=5)
        
        # Create Delete Button
        self.deleteButton = ttk.Button(self.mainFrame, text="DELETE", style="Cancel.TButton", command=lambda: self.confirmDelete())
        self.deleteButton.pack(fill=tk.X, padx=5, pady=15)
        
        # Enable Inputs: (Name, Type, Quantity, Gym) 
        self.nameEntry.config(state="enabled")
        self.typeDropdown.config(state="enabled")
        self.quantityEntry.config(state="enabled")
        self.gymDropdown.config(state="enabled")
        
    # --- LOAD CANCEL EDIT VIEW FRAME ---
    # Assign currEquip Data to Inputs
    # Destroy Delete Button
    # Destroy Save Button 
    # Destroy Cancel Button 
    # Create Edit Button 
    # Create Back Button
    # Disable Inputs: (Name, Type, Quantity, Gym) 
    def loadCancelEditFrame(self):
        # Assign currEquip Data to Inputs
        self.nameVar.set(self.currEquip["name"])
        self.quantityVar.set(str(self.currEquip["quantity"]))
        self.typeOption.set(self.currEquip["type"])
        self.gymOption.set(self.currEquip["gymLoc"])
    
        # Destroy Delete Button
        # Destroy Save Button 
        # Destroy Cancel Button 
        self.deleteButton.destroy()
        self.saveButton.destroy()
        self.cancelButton.destroy()
        
        # Create Edit Button 
        self.editButton = ttk.Button(self.mainFrame, text="EDIT", command=lambda: self.loadEditFrame())
        self.editButton.pack(fill=tk.X, padx=5, pady=5)
        
        # Create Back Button
        self.backButton = ttk.Button(self.mainFrame, text="BACK", command=lambda: self.loadAllEquipmentFrame())
        self.backButton.pack(fill=tk.X, padx=5, pady=5)
        
        # Disable Inputs: (Name, Type, Quantity, Gym) 
        self.nameEntry.config(state="disabled")
        self.typeDropdown.config(state="disabled")
        self.quantityEntry.config(state="disabled")
        self.gymDropdown.config(state="disabled")
        
        
    # --- FRAME MANAGER FUNCTIONS ---
        
    # Function to clear out all widgets inside a frame
    def clearFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()
            
        
    # --- HELPER FUNCTIONS ---    
        
    # --- CONFIRM DELETE ---
    # Executes askyesno: "Confirmation", "Are you sure you want to proceed?"
    # YES: Execute deleteEquipment
    def confirmDelete(self):
        response = msgBox.askyesno("Confirmation", "Are you sure you want to proceed?")
        if response:
            print("Action confirmed!")
            self.deleteEquipment()
        else:
            print("Action cancelled.")
           

    # --- CONFIRM SAVE ---
    # Executes askyesno: "Confirmation", "Are you sure you want to proceed?"
    # YES: Execute updateEquipment
    def confirmSave(self):
        response = msgBox.askyesno("Confirmation", "Are you sure you want to proceed?")
        if response:
            print("Action confirmed!")
            self.updateEquipment()
        else:
            print("Action cancelled.")
           
            
    # --- SQL HELPER FUNCTIONS ---   
        
    # --- GET ALL EQUIPMENT ---
    # Executes getAllEquip: Gets a list of all equipment data.
    # ERROR: If allEquip is None.
    # Returns: List of equipment.
    def getAllEquipment(self):
        allEquip = self.db.getAllEquip()
        
        if not allEquip:
            msgBox.showerror("SQLite Connection", "ERROR: Failed to create equipment.")
            
        return allEquip
        
    # --- GET ALL GYMS ---
    # Executes getAllGyms: Gets a list of all gyms data.
    # ERROR: If allGyms is None.
    # Returns: List of gyms.
    def getAllGyms(self):
        allGyms = self.db.getAllGyms()
        
        if allGyms:
            i = 0
            gymsLoc = []
            for gym in allGyms:
                gymsLoc.append(gym[1])
                i = i + 1
        else:
            msgBox.showerror("SQLite Connection", "ERROR: Failed to create equipment.")
        
        return gymsLoc
            

    # --- GET EQUIPMENT BY ID ---
    # Executes getEquipByID: Gets equipment data.
    # ERROR: If currEquip is None.
    # Returns: Equipment
    def getEquipment(self):
        currEquip = None
        try:
            item = self.tree.selection()[0]
            print(str(item))
            equipId = self.tree.item(item, "text")
            currEquip = self.db.getEquipByID(equipId)
        except IndexError as e:
            print(f"Error: {e}")
        
        return currEquip
        
    # --- CREATE EQUIPMENT ---
    # Executes db.createEquip: Create equipment data.
    # ERROR: If currEquip["name"] is None.
    # ERROR: If currEquip["quantity"] is not decimal.
    # ERROR: If currEquip["quantity"]) is less than 0.
    def createEquipment(self):
        self.currEquip["name"] = self.nameVar.get() 
        self.currEquip["type"] = self.typeOption.get()
        self.currEquip["quantity"] = self.quantityVar.get()
        self.currEquip["gymId"] = self.db.getAllGymIdByLoc(self.gymOption.get())
    
        # Validate NAME: string and QUANITY: int
        if self.currEquip["name"] == "" or not self.currEquip["quantity"].isdecimal():        
            msgBox.showerror("New Equipment", "INVALID: Empty fields.")
            return
         
        # Validate quantity is higher then zero   
        if int(self.currEquip["quantity"]) < 0:
            msgBox.showerror("New Equipment", "INVALID: Empty fields.")
            return
    
        if not self.db.createEquip(self.currEquip):
            msgBox.showerror("SQLite Connection", "ERROR: Failed to create equipment.")
            return
        
        msgBox.showinfo("SQLite Connection", "SUCCESS: Equipment created.")
        self.loadAllEquipmentFrame()
        
    # --- UPDATE EQUIPMENT ---
    # Executes db.updateEquipByID: Update equipment data.
    # ERROR: If currEquip["name"] is None.
    # ERROR: If currEquip["quantity"] is not decimal.
    # ERROR: If currEquip["quantity"]) is less than 0.
    def updateEquipment(self):
        self.currEquip["name"] = self.nameVar.get() 
        self.currEquip["type"] = self.typeOption.get()
        self.currEquip["quantity"] = self.quantityVar.get()
        self.currEquip["gymId"] = self.db.getAllGymIdByLoc(self.gymOption.get())
    
        # Validate NAME: string and QUANITY: int
        if self.currEquip["name"] == "" or not self.currEquip["quantity"].isdecimal():        
            msgBox.showerror("New Equipment", "INVALID: Empty fields.")
            return
        
        # Validate quantity is higher then zero
        if int(self.currEquip["quantity"]) < 0:
            msgBox.showerror("New Equipment", "INVALID: Empty fields.")
            return
        
        if not self.db.updateEquipByID(self.currEquip["id"], self.currEquip):
            msgBox.showerror("SQLite Connection", "ERROR: Failed to update equipment.")
            return
        
        msgBox.showinfo("SQLite Connection", "SUCCESS: Equipment updated.")
        self.loadAllEquipmentFrame() 
        
    # --- DELETE EQUIPMENT ---
    # Executes deleteEquipByID: Delete equipment data.
    # ERROR: If deleteEquipByID fails.
    # Executes loadAllEquipmentFrame
    def deleteEquipment(self):        
        if self.db.deleteEquipByID(self.currEquip["id"]):
            msgBox.showinfo("SQLite Connection", "SUCCESS: Equipment deleted.")
            self.loadAllEquipmentFrame()
            return
        msgBox.showerror("SQLite Connection", "Error deleting data.")
        
               
     