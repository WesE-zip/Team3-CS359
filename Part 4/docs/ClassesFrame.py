import sys
from main import App 
import tkinter as tk
import tkinter.ttk as ttk

class ClassesFrame():

    def __init__(self, master, mainFrame, conn):
        self.master = master
        self.mainFrame = master
        self.conn = conn
        self.sel_option = tk.StringVar(self.mainFrame)

        self.loadMenuFrame()

    # Clears Frame
    # Loads Menu Frame
    def loadMenuFrame(self):
        self.clearFrame()
        
        label = ttk.Label(self.mainFrame, text="CLASSES", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)
  
        button = ttk.Button(self.mainFrame, text="List classes", command=lambda: self.loadReadFrame())
        button.pack(fill=tk.X, padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="Add new class", command=lambda: self.loadCreateFrame())
        button.pack(fill=tk.X, padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="Update class information", command=lambda: self.loadUpdateFrame())
        button.pack(fill=tk.X, padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="Delete class", command=lambda: self.loadDeleteFrame())
        button.pack(fill=tk.X, padx=5, pady=5)

        #button = ttk.Button(self.mainFrame, text="BACK TO MAIN", command=lambda: App.loadMenuFrame(self))
        #button.pack(fill=tk.X, padx=5, pady=5)
    
    def loadReadFrame(self):
        self.clearFrame()

        label = ttk.Label(self.mainFrame, text="CLASSES", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)

        data = [
           ["Bench Press", "STRENGTH", 6, 1, "bob", 3],
           ["Treadmill", "CARDIO", 10, 3, "jim", 4],
           ["Exercise Bike", "CARDIO", 4, 1, "gary", 5],
           ["Crosstrainer", "STRENGTH", 8, 2, "bill", 4],
        ]

        index = 0   
        columns = ("type", "dururation", "cap", "instructor", "attendees")

        tree = ttk.Treeview(self.mainFrame, columns=columns)
        tree.pack(padx=5, pady=5)

        tree.column("#0", stretch=tk.NO, width=150)
        tree.heading('#0', text='Class')
        tree.column("type", stretch=tk.NO, width=75)
        tree.heading('type', text='Type')
        tree.column("dururation", stretch=tk.NO, width=75)
        tree.heading('dururation', text='Dururation')
        tree.column("cap", stretch=tk.NO, width=75)
        tree.heading('cap', text='Capacity')
        tree.column("instructor", stretch=tk.NO, width=75)
        tree.heading('instructor', text='Instructor')
        tree.column("attendees", stretch=tk.NO, width=130)
        tree.heading('attendees', text='Number of Attendees')

        for index, line in enumerate(data):
            tree.insert('', tk.END, iid = index,
                text = line[0], values = line[1:])
            
        button = ttk.Button(self.mainFrame, text="BACK TO CLASSES", command=lambda: self.loadMenuFrame())
        button.pack(padx=5)

    def loadCreateFrame(self):
        self.clearFrame()

        label = ttk.Label(self.mainFrame, text="ADD CLASS", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)
        
        label = ttk.Label(self.mainFrame, text="Database Name:")
        label.pack(padx=5)
        
        entry = ttk.Entry(self.mainFrame)
        entry.pack(padx=5)
        
        button = ttk.Button(self.mainFrame, text="CONNECT", command=lambda: App.checkConn(entry.get()))
        button.pack(padx=5)

        button = ttk.Button(self.mainFrame, text="BACK TO CLASSES", command=lambda: self.loadMenuFrame())
        button.pack(padx=5)

    def loadUpdateFrame(self):
        self.clearFrame()

        label = ttk.Label(self.mainFrame, text="UPDATE CLASS", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)


        button = ttk.Button(self.mainFrame, text="BACK TO CLASSES", command=lambda: self.loadMenuFrame())
        button.pack(padx=5)

    def loadDeleteFrame(self):
        self.clearFrame()

        label = ttk.Label(self.mainFrame, text="DELETE CLASS", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)


        button = ttk.Button(self.mainFrame, text="BACK TO CLASSES", command=lambda: self.loadMenuFrame())
        button.pack(padx=5)
        
    
        
        
    # Function to clear out all widgets inside a frame
    def clearFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()