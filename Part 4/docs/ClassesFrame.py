import sys
import sqlite3
from sqlite3 import Error
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

        SQLget = """
        SELECT class.className, class.classType, class.duration, class.classCapacity, instructor.name, count(attends.classId) as attendees FROM class FULL JOIN instructor ON class.instructorId = instructor.instructorId FULL JOIN attends ON class.classId = attends.classId GROUP BY attends.classId
        """

        data = self.getSQLData(SQLget)

        # for line in data:
        #     print(line[0])
        index = 0   
        columns = ("type", "dururation", "cap", "instructor", "attendes")

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
        tree.column("attendes", stretch=tk.NO, width=130)
        tree.heading('attendes', text='Number of Attendees')

        for index, line in enumerate(data):
            tree.insert('', tk.END, iid = index, text = line[0], values = line[1:])
            
        button = ttk.Button(self.mainFrame, text="BACK TO CLASSES", command=lambda: self.loadMenuFrame())
        button.pack(padx=5)

    def loadCreateFrame(self):
        self.clearFrame()

        label = ttk.Label(self.mainFrame, text="ADD CLASS", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)



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
        classId = 7

        label = ttk.Label(self.mainFrame, text="DELETE CLASS", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)

        label = ttk.Label(self.mainFrame, text="Class ID:")
        label.pack(fill=tk.X, padx=5, pady=5)
        
        Entry = ttk.Entry(self.mainFrame)
        Entry.pack(fill=tk.X, padx=5)

        button = ttk.Button(self.mainFrame, text="DELETE", command=lambda: self.delete(Entry))
        button.pack(padx=5)

        SQLRead = """
        SELECT className, classId FROM class
        """
        data = self.getSQLData(SQLRead)

        index = 0   
        columns = ('id')

        tree = ttk.Treeview(self.mainFrame, columns=columns)
        tree.pack(padx=5, pady=5)

        tree.column("#0", stretch=tk.NO, width=150)
        tree.heading('#0', text='Classes')
        tree.column("id", stretch=tk.NO, width=50)
        tree.heading('id', text='Class Id')

        for index, line in enumerate(data):
            tree.insert('', tk.END, iid = index,
                text = line[0], values = line[1:])

        button = ttk.Button(self.mainFrame, text="BACK TO CLASSES", command=lambda: self.loadMenuFrame())
        button.pack(padx=5)

    def delete(self, EntryId):
        id = EntryId.get()
        SQLDeleteClass = """
        DELETE FROM class WHERE classId = ?
        """
        SQLDeleteAttends = """
        DELETE FROM attends WHERE classId = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(SQLDeleteClass, (id,))
        self.conn.commit()
        cursor.execute(SQLDeleteAttends, (id,))
        self.conn.commit()

        self.loadDeleteFrame()

    def getSQLData(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor
        
    # Function to clear out all widgets inside a frame
    def clearFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()