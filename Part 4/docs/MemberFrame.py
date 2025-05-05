#Christian Kurdi
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from docs.Queries import Query
from docs.removeFrame import RemoveFrame
from docs.updateFrame import UpdateFrame
#XYZGym.sqlite

class MemberFrame():

    def __init__(self, mainFrame, conn, appObject):
        self.mainFrame = mainFrame
        self.connection = conn
        self.app = appObject

        self.query = Query(self.connection)
        self.membersBox = None
        self.table=None
        self.idField = None
        self.nameField = None
        self.emailField = None
        self.phoneField = None
        self.addressField = None
        self.ageField = None
        self.startDateField = None
        self.endDateField = None

        self.loadMemberFrame()


    def loadMemberFrame(self):#Function to display the window
        self.clearFrame()

        title = ttk.Label(self.mainFrame, text="Members Menu", font=("Helvetica", 14))
        title.pack(side=tk.TOP)#This puts the label on the window at given location

        backButton = ttk.Button(self.mainFrame, text="Back", command=lambda: self.app.loadMenuFrame())
        backButton.pack(anchor=tk.NW, padx=10, pady=10)#This puts the button in top left of window

        infoFrame = ttk.Frame(self.mainFrame, width=550, height=600)
        infoFrame.pack(side=tk.LEFT, fill=tk.X, expand=True, anchor=tk.N)
        membersBox = ttk.Frame(infoFrame, width=550, height=200, relief=tk.RIDGE)
        membersBox.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.membersBox = membersBox

        self.createTable()

        inputBox = ttk.Frame(infoFrame, width=550, height=100)
        inputBox.grid(row=1, column=0, padx=10, pady=10)

        idLabel = tk.Label(inputBox, text="ID", font=("Helvetica", 10), width=10)
        idLabel.grid(row=0, column=0, padx=10, pady=10)
        self.idField = ttk.Entry(inputBox, width=10)
        self.idField.grid(row=1, column=0, padx=10, pady=10)

        nameLabel = tk.Label(inputBox, text="Name", font=("Helvetica", 10))
        nameLabel.grid(row=0, column=1, padx=5, pady=5)
        self.nameField = ttk.Entry(inputBox)
        self.nameField.grid(row=1, column=1, padx=5, pady=5)

        emailLabel = tk.Label(inputBox, text="Email", font=("Helvetica", 10))
        emailLabel.grid(row=0, column=2, padx=5, pady=5)
        self.emailField = ttk.Entry(inputBox)
        self.emailField.grid(row=1, column=2, padx=5, pady=5)

        phoneLabel = tk.Label(inputBox, text="Phone", font=("Helvetica", 10))
        phoneLabel.grid(row=0, column=3, padx=5, pady=5)
        self.phoneField = ttk.Entry(inputBox)
        self.phoneField.grid(row=1, column=3, padx=5, pady=5)

        addressLabel = tk.Label(inputBox, text="Address", font=("Helvetica", 10))
        addressLabel.grid(row=0, column=4, padx=5, pady=5)
        self.addressField = ttk.Entry(inputBox)
        self.addressField.grid(row=1, column=4, padx=5, pady=5)

        ageLabel = tk.Label(inputBox, text="Age", font=("Helvetica", 10))
        ageLabel.grid(row=0, column=5, padx=5, pady=5)
        self.ageField = ttk.Entry(inputBox)
        self.ageField.grid(row=1, column=5, padx=5, pady=5)

        startDateLabel = tk.Label(inputBox, text="Start Date", font=("Helvetica", 10))
        startDateLabel.grid(row=3, column=2, padx=5, pady=5)
        self.startDateField = ttk.Entry(inputBox)
        self.startDateField.grid(row=4, column=2, padx=5, pady=5)

        endDateLabel = tk.Label(inputBox, text="End Date", font=("Helvetica", 10))
        endDateLabel.grid(row=3, column=3, padx=5, pady=5)
        self.endDateField = ttk.Entry(inputBox)
        self.endDateField.grid(row=4, column=3, padx=5, pady=5)


        buttonBox = ttk.Frame(infoFrame, width=550, height=75, relief=tk.RIDGE)
        buttonBox.grid(row=2, column=0, padx=10, pady=10)

        addButton = ttk.Button(buttonBox, text="Add", command=lambda: self.addMember())
        addButton.grid(row=0, column=0, padx=10, pady=10)

        updateButton = ttk.Button(buttonBox, text="Update", command=lambda: self.updateMember())
        updateButton.grid(row=0, column=1, padx=10, pady=10)

        removeButton = ttk.Button(buttonBox, text="Remove", command=lambda: self.removeMember())
        removeButton.grid(row=0, column=2, padx=10, pady=10)

        clearButton = ttk.Button(buttonBox, text="Clear", command=lambda:self.clearEntries())
        clearButton.grid(row=0, column=3, padx=10, pady=10)




    def addMember(self):#Function to add member to database and table
        id = self.idField.get()
        name = self.nameField.get()
        email = self.emailField.get()
        phone = self.phoneField.get()
        address = self.addressField.get()
        age = self.ageField.get()
        startDate = self.startDateField.get()
        endDate = self.endDateField.get()

        if email and startDate and endDate:
            checkID = self.query.getIDs()
            goodID = True

            if checkID:

                for member in checkID:
                    if member == int(id):
                        goodID = False
                        break

            if goodID:

                check = self.query.addMember(int(id), name, email, phone, address, int(age), startDate, endDate)
                if check:
                    showinfo("Success", "Member added")
                    self.createTable()
                else:
                    showinfo("Error", "Unable to add record, try again.")
            else:
                showinfo("Error", "Choose an ID not in database")
        else:
            showinfo("Error", "Please enter all fields.")


    def updateMember(self):#Function to call updateFrame
        UpdateFrame(self, self.mainFrame, self.connection)

    def removeMember(self):#Function to call removeFrame
        RemoveFrame(self, self.mainFrame, self.connection)

    def clearEntries(self): #Function to clear entry fields
        self.idField.delete(0, tk.END)
        self.nameField.delete(0, tk.END)
        self.emailField.delete(0, tk.END)
        self.phoneField.delete(0, tk.END)
        self.addressField.delete(0, tk.END)
        self.ageField.delete(0, tk.END)
        self.startDateField.delete(0, tk.END)
        self.endDateField.delete(0, tk.END)

    def createTable(self):#Function to create a table for members

        if self.table:
            self.table.destroy()
            self.table = None
            self.mainFrame.update()

        table = ttk.Treeview(self.membersBox,
                             columns=("ID", "Name", "Email", "Phone", "Address", "Age", "Start Date", "End Date"))
        # Format the table
        table.column('#0', width=0, stretch=tk.NO)
        table.column('ID', anchor=tk.W, width=25)
        table.column('Name', anchor=tk.W, width=100)
        table.column('Email', anchor=tk.W, width=150)
        table.column('Phone', anchor=tk.W, width=100)
        table.column('Address', anchor=tk.W, width=100)
        table.column('Age', anchor=tk.W, width=25)
        table.column('Start Date', anchor=tk.W, width=70)
        table.column('End Date', anchor=tk.W, width=70)
        # Assign headings
        table.heading("#0", text="")
        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("Email", text="Email")
        table.heading("Phone", text="Phone")
        table.heading("Address", text="Address")
        table.heading("Age", text="Age")
        table.heading("Start Date", text="Start Date")
        table.heading("End Date", text="End Date")

        table.bind("<<TreeviewSelect>>", self.tableSelect)
        self.table = table

        self.drawTable()

        table.pack(expand=True, fill=tk.BOTH)

    def tableSelect(self, event):#Function to get data from selected row in table
        self.clearEntries()

        selectedRow = self.table.selection()[0]
        rowData = self.table.item(selectedRow, "values")
        id = rowData[0]
        name=rowData[1]
        email=rowData[2]
        phone=rowData[3]
        address=rowData[4]
        age=rowData[5]
        startDate=rowData[6]
        endDate=rowData[7]

        self.idField.insert(0, id)
        self.nameField.insert(0, name)
        self.emailField.insert(0, email)
        self.phoneField.insert(0, phone)
        self.addressField.insert(0, address)
        self.ageField.insert(0, age)
        self.startDateField.insert(0, startDate)
        self.endDateField.insert(0, endDate)

    # Function to clear out all widgets inside a frame
    def clearFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

    def drawTable(self):#Function to put data into the table

        data = self.query.getMembers()
        if data[0] == 1:
            cursor = data[1]
            index = 0
            for line in cursor:
                self.table.insert(parent="", index=index, values=line)
                index += 1
            cursor.close()
        else:
            showinfo("Error", "Unable to get data from database")
