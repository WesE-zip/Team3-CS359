## Wesley Evans

import sys
import sqlite3
from sqlite3 import Error
from tkinter.messagebox import showinfo
import tkinter as tk
import tkinter.ttk as ttk
from docs.Queries import Query


class ClassesFrame():

    def __init__(self, mainFrame, conn, appObj):
        self.mainFrame = mainFrame
        self.conn = conn
        self.app = appObj
        self.sel_option = tk.StringVar(self.mainFrame)
        self.id = None
        self.idField = None
        self.query = Query(conn)
        self.tableFrame = None

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

        button = ttk.Button(self.mainFrame, text="Update class information", command=lambda: self.loadUpdateIdFrame())
        button.pack(fill=tk.X, padx=5, pady=5)

        button = ttk.Button(self.mainFrame, text="Delete class", command=lambda: self.loadDeleteFrame())
        button.pack(fill=tk.X, padx=5, pady=5)

        findButton = ttk.Button(self.mainFrame, text="Find Member", command=lambda: self.findMember())
        findButton.pack(fill=tk.X, padx=5, pady=5)

        button = ttk.Button(self.mainFrame, text="BACK TO MAIN", command=lambda: self.app.loadMenuFrame())
        button.pack(fill=tk.X, padx=5, pady=5)

    def loadReadFrame(self):
        self.clearFrame()

        label = ttk.Label(self.mainFrame, text="CLASSES", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)

        SQLget = """
        SELECT class.className, class.classType, class.duration, class.classCapacity, instructor.name, count(attends.classId) as attendees FROM class FULL JOIN instructor ON class.instructorId = instructor.instructorId FULL JOIN attends ON class.classId = attends.classId GROUP BY class.classId
        """

        data = self.getSQLData(SQLget)

        index = 0
        columns = ("type", "dururation", "cap", "instructor", "attendes")

        tree = ttk.Treeview(self.mainFrame, columns=columns)
        tree.pack(padx=5, pady=5)

        tree.column("#0", stretch=tk.NO, width=120)
        tree.heading('#0', text='Class')
        tree.column("type", stretch=tk.NO, width=75)
        tree.heading('type', text='Type')
        tree.column("dururation", stretch=tk.NO, width=75)
        tree.heading('dururation', text='Dururation')
        tree.column("cap", stretch=tk.NO, width=75)
        tree.heading('cap', text='Capacity')
        tree.column("instructor", stretch=tk.NO, width=75)
        tree.heading('instructor', text='Instructor')
        tree.column("attendes", stretch=tk.NO, width=140)
        tree.heading('attendes', text='Number of Attendees')

        for index, line in enumerate(data):
            tree.insert('', tk.END, iid=index, text=line[0], values=line[1:])

        button = ttk.Button(self.mainFrame, text="BACK TO CLASSES", command=lambda: self.loadMenuFrame())
        button.pack(padx=5)

    def loadCreateFrame(self):
        self.clearFrame()

        label = ttk.Label(self.mainFrame, text="ADD CLASS", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)

        infoFrame = ttk.Frame(self.mainFrame, width=550, height=600)
        infoFrame.pack(side=tk.LEFT, fill=tk.X, expand=True, anchor=tk.N)

        inputBox = ttk.Frame(infoFrame, width=550, height=100)
        inputBox.grid(row=1, column=0, padx=10, pady=10)

        IdLabel = tk.Label(inputBox, text="Class ID", font=("Helvetica", 10))
        IdLabel.grid(row=0, column=0, padx=5, pady=5)
        IdEntry = ttk.Entry(inputBox)
        IdEntry.grid(row=1, column=0, padx=5, pady=5)

        nameLabel = tk.Label(inputBox, text="Name", font=("Helvetica", 10))
        nameLabel.grid(row=0, column=1, padx=5, pady=5)
        nameEntry = ttk.Entry(inputBox)
        nameEntry.grid(row=1, column=1, padx=5, pady=5)

        typeLabel = tk.Label(inputBox, text="Class Type", font=("Helvetica", 10))
        typeLabel.grid(row=0, column=2, padx=5, pady=5)
        typeEntry = ttk.Entry(inputBox)
        typeEntry.grid(row=1, column=2, padx=5, pady=5)

        durationLabel = tk.Label(inputBox, text="Duration", font=("Helvetica", 10))
        durationLabel.grid(row=0, column=3, padx=5, pady=5)
        durationEntry = ttk.Entry(inputBox)
        durationEntry.grid(row=1, column=3, padx=5, pady=5)

        capacityLabel = tk.Label(inputBox, text="Class Capacity", font=("Helvetica", 10))
        capacityLabel.grid(row=2, column=0, padx=5, pady=5)
        capacityEntry = ttk.Entry(inputBox)
        capacityEntry.grid(row=3, column=0, padx=5, pady=5)

        instructorLabel = tk.Label(inputBox, text="Instructor ID", font=("Helvetica", 10))
        instructorLabel.grid(row=2, column=1, padx=5, pady=5)
        instructorEntry = ttk.Entry(inputBox)
        instructorEntry.grid(row=3, column=1, padx=5, pady=5)

        gymLabel = tk.Label(inputBox, text="Gym ID", font=("Helvetica", 10))
        gymLabel.grid(row=2, column=2, padx=5, pady=5)
        gymEntry = ttk.Entry(inputBox)
        gymEntry.grid(row=3, column=2, padx=5, pady=5)

        button = ttk.Button(inputBox, text="ADD",
                            command=lambda: self.addClass(IdEntry, nameEntry, typeEntry, durationEntry, capacityEntry,
                                                          instructorEntry, gymEntry))
        button.grid(row=3, column=3, padx=5, pady=5)

        button = ttk.Button(inputBox, text="BACK TO CLASSES", command=lambda: self.loadMenuFrame())
        button.grid(row=5, column=0, padx=5, pady=5)

    def loadUpdateIdFrame(self):
        self.clearFrame()

        label = ttk.Label(self.mainFrame, text="UPDATE CLASS", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)

        SQLRead = f"""
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
            tree.insert('', tk.END, iid=index,
                        text=line[0], values=line[1:])

        label = ttk.Label(self.mainFrame, text="Class ID:")
        label.pack(fill=tk.X, padx=5, pady=5)

        IdEntry = ttk.Entry(self.mainFrame)
        IdEntry.pack(fill=tk.X, padx=5)

        button = ttk.Button(self.mainFrame, text='Edit', command=lambda: self.loadUpdateFrame(IdEntry))
        button.pack(padx=5)

        button = ttk.Button(self.mainFrame, text="BACK TO CLASSES", command=lambda: self.loadMenuFrame())
        button.pack(padx=5)

    def loadUpdateFrame(self, IdEntry):
        id = IdEntry.get()
        self.clearFrame()
        print(id)
        label = ttk.Label(self.mainFrame, text="UPDATE CLASS", font=("Helvetica", 12, "bold"))
        label.pack(padx=5, pady=15)

        infoFrame = ttk.Frame(self.mainFrame, width=550, height=600)
        infoFrame.pack(side=tk.LEFT, fill=tk.X, expand=True, anchor=tk.N)

        inputBox = ttk.Frame(infoFrame, width=550, height=100)
        inputBox.grid(row=1, column=0, padx=10, pady=10)

        IdLabel = tk.Label(inputBox, text="Class ID", font=("Helvetica", 10))
        IdLabel.grid(row=0, column=0, padx=5, pady=5)
        IdEntry = ttk.Label(inputBox, text=str(id), font=("Helvetica", 10))
        IdEntry.grid(row=1, column=0, padx=5, pady=5)

        nameLabel = tk.Label(inputBox, text="Name", font=("Helvetica", 10))
        nameLabel.grid(row=0, column=1, padx=5, pady=5)
        nameEntry = ttk.Entry(inputBox)
        nameEntry.grid(row=1, column=1, padx=5, pady=5)

        typeLabel = tk.Label(inputBox, text="Class Type", font=("Helvetica", 10))
        typeLabel.grid(row=0, column=2, padx=5, pady=5)
        typeEntry = ttk.Entry(inputBox)
        typeEntry.grid(row=1, column=2, padx=5, pady=5)

        durationLabel = tk.Label(inputBox, text="Duration", font=("Helvetica", 10))
        durationLabel.grid(row=0, column=3, padx=5, pady=5)
        durationEntry = ttk.Entry(inputBox)
        durationEntry.grid(row=1, column=3, padx=5, pady=5)

        capacityLabel = tk.Label(inputBox, text="Class Capacity", font=("Helvetica", 10))
        capacityLabel.grid(row=2, column=0, padx=5, pady=5)
        capacityEntry = ttk.Entry(inputBox)
        capacityEntry.grid(row=3, column=0, padx=5, pady=5)

        instructorLabel = tk.Label(inputBox, text="Instructor ID", font=("Helvetica", 10))
        instructorLabel.grid(row=2, column=1, padx=5, pady=5)
        instructorEntry = ttk.Entry(inputBox)
        instructorEntry.grid(row=3, column=1, padx=5, pady=5)

        gymLabel = tk.Label(inputBox, text="Gym ID", font=("Helvetica", 10))
        gymLabel.grid(row=2, column=2, padx=5, pady=5)
        gymEntry = ttk.Entry(inputBox)
        gymEntry.grid(row=3, column=2, padx=5, pady=5)

        button = ttk.Button(inputBox, text="ADD",
                            command=lambda: self.editClass(id, nameEntry, typeEntry, durationEntry, capacityEntry,
                                                           instructorEntry, gymEntry))
        button.grid(row=3, column=3, padx=5, pady=5)

        button = ttk.Button(inputBox, text="BACK TO CLASSES", command=lambda: self.loadMenuFrame())
        button.grid(row=5, column=0, padx=5, pady=5)

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
            tree.insert('', tk.END, iid=index,
                        text=line[0], values=line[1:])

        button = ttk.Button(self.mainFrame, text="BACK TO CLASSES", command=lambda: self.loadMenuFrame())
        button.pack(padx=5)

    def addClass(self, IdEntry, nameEntry, typeEntry, durationEntry, capacityEntry, instructorEntry, gymEntry):
        id = IdEntry.get()
        name = nameEntry.get()
        type = typeEntry.get()
        duration = durationEntry.get()
        capacity = capacityEntry.get()
        instructor = instructorEntry.get()
        gym = gymEntry.get()

        SQLAddClass = f"""
        INSERT INTO class(classId, className, classType, duration, classCapacity, instructorId, gymID) VALUES('{id}', '{name}', '{type}', '{duration}', '{capacity}', '{instructor}', '{gym}');
        """

        cursor = self.conn.cursor()
        cursor.execute(SQLAddClass)
        self.conn.commit()
        showinfo("Added", f"{name}")
        self.loadReadFrame()

    def editClass(self, id, nameEntry, typeEntry, durationEntry, capacityEntry, instructorEntry, gymEntry):
        name = nameEntry.get()
        type = typeEntry.get()
        duration = durationEntry.get()
        capacity = capacityEntry.get()
        instructor = instructorEntry.get()
        gym = gymEntry.get()

        SQLAddClass = f"""
        UPDATE class SET className = '{name}', classType = '{type}', duration = '{duration}', classCapacity = '{capacity}', instructorId = {instructor}, gymID = '{gym}' WHERE classId = '{id}';
        """

        cursor = self.conn.cursor()
        cursor.execute(SQLAddClass)
        self.conn.commit()
        showinfo("Edited", f"{name}")
        self.loadReadFrame()

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
        showinfo("Deleted", f"{id}")
        self.loadDeleteFrame()

    def getSQLData(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor

    # Function to clear out all widgets inside a frame
    def clearFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

    def findMember(self):
        self.clearFrame()

        title = tk.Label(self.mainFrame, text="Find Members In A Class", font=("Helvetica", 14))
        title.pack(side=tk.TOP)

        backButton = ttk.Button(self.mainFrame, text="Back", command=lambda: self.loadMenuFrame())
        backButton.pack(anchor=tk.NW, padx=10, pady=10)

        mainBox = ttk.Frame(self.mainFrame)
        mainBox.pack(side=tk.TOP)

        label = tk.Label(mainBox, text="Enter class ID to find members:")
        label.pack(side=tk.TOP)

        idField = tk.Entry(mainBox)
        idField.pack(side=tk.TOP)
        self.idField = idField

        submitButton = ttk.Button(mainBox, text="Submit", command=lambda: self.searchForClassID())
        submitButton.pack(side=tk.TOP)

    def searchForClassID(self):
        id = self.idField.get()
        check = self.query.searchByClassID(id)

        if check:
            data = self.query.getMembersByClass(id)
            if data[0] == 1:
                if self.tableFrame:
                    self.tableFrame.destroy()
                    self.tableFrame = None
                    self.mainFrame.update()

                tableFrame = tk.Frame(self.mainFrame)
                tableFrame.pack(side=tk.TOP)
                self.tableFrame = tableFrame
                table = ttk.Treeview(tableFrame, columns=("ID", "Name"))
                table.column('#0', width=0, stretch=tk.NO)
                table.column('ID', anchor=tk.W, width=25)
                table.column('Name', anchor=tk.W, width=100)

                table.heading("#0", text="")
                table.heading("ID", text="ID")
                table.heading("Name", text="Name")

                memberData = data[1]
                index = 0
                for line in memberData:
                    table.insert(parent="", index=index, values=line)
                    index += 1
                table.pack(expand=True, fill=tk.BOTH)
            else:
                showinfo("Error", "Unable to get member data")
