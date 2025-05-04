#Christian Kurdi
import tkinter as tk
import tkinter.ttk as ttk
from docs.Queries import Query
from tkinter.messagebox import showinfo
class UpdateFrame():
    def __init__(self, memberFrame, mainFrame, connection):
        self.memberFrame = memberFrame
        self.mainFrame = mainFrame
        self.connection = connection
        self.query = Query(self.connection)
        self.mainBox = None
        self.idField = None
        self.nameField = None
        self.emailField = None
        self.phoneField = None
        self.addressField = None
        self.ageField = None
        self.startDateField = None
        self.endDateField = None

        self.showMenu()
    def showMenu(self):
        self.clearFrame()

        title = tk.Label(self.mainFrame, text="Update A Member", font=("Helvetica", 14))
        title.pack(side=tk.TOP)

        backButton = ttk.Button(self.mainFrame, text="Back", command=lambda: self.memberFrame.loadMemberFrame())
        backButton.pack(anchor=tk.NW, padx=10, pady=10)

        mainBox = ttk.Frame(self.mainFrame)
        mainBox.pack(side=tk.TOP)
        self.mainBox = mainBox

        label = tk.Label(mainBox, text="Enter member ID to update:")
        label.pack(side=tk.TOP)

        idField = tk.Entry(mainBox)
        idField.pack(side=tk.TOP)
        self.idField = idField

        submitButton = ttk.Button(mainBox, text="Submit", command=lambda: self.searchForID())
        submitButton.pack(side=tk.TOP)

    def clearFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

    def searchForID(self):
        id = self.idField.get()
        data = self.query.searchByID(id)
        if data:

            self.updateFrame(id, data)
            updateButton = tk.Button(self.mainBox, text="Update", command=lambda: self.submitUpdate(id))
            updateButton.pack(side=tk.TOP)
        else:
            showinfo("Error", "No member found")





    def updateFrame(self, id, data):
        id = id
        data = data
        memberID, name, email, phone, address, age, startDate, endDate = data
        subBox = ttk.Frame(self.mainBox)
        subBox.pack()

        idLabel = tk.Label(subBox, text="ID", font=("Helvetica", 10), width=10)
        idLabel.grid(row=0, column=0, padx=10, pady=10)

        idValue = tk.Label(subBox, text=id, font=("Helvetica", 10), width=10)
        idValue.grid(row=1, column=0, padx=5, pady=5)

        nameLabel = tk.Label(subBox, text="Name", font=("Helvetica", 10))
        nameLabel.grid(row=0, column=1, padx=5, pady=5)
        self.nameField = ttk.Entry(subBox)
        self.nameField.grid(row=1, column=1, padx=5, pady=5)

        emailLabel = tk.Label(subBox, text="Email", font=("Helvetica", 10))
        emailLabel.grid(row=0, column=2, padx=5, pady=5)
        self.emailField = ttk.Entry(subBox)
        self.emailField.grid(row=1, column=2, padx=5, pady=5)

        phoneLabel = tk.Label(subBox, text="Phone", font=("Helvetica", 10))
        phoneLabel.grid(row=0, column=3, padx=5, pady=5)
        self.phoneField = ttk.Entry(subBox)
        self.phoneField.grid(row=1, column=3, padx=5, pady=5)

        addressLabel = tk.Label(subBox, text="Address", font=("Helvetica", 10))
        addressLabel.grid(row=0, column=4, padx=5, pady=5)
        self.addressField = ttk.Entry(subBox)
        self.addressField.grid(row=1, column=4, padx=5, pady=5)

        ageLabel = tk.Label(subBox, text="Age", font=("Helvetica", 10))
        ageLabel.grid(row=0, column=5, padx=5, pady=5)
        self.ageField = ttk.Entry(subBox)
        self.ageField.grid(row=1, column=5, padx=5, pady=5)

        startDateLabel = tk.Label(subBox, text="Start Date", font=("Helvetica", 10))
        startDateLabel.grid(row=3, column=2, padx=5, pady=5)
        self.startDateField = ttk.Entry(subBox)
        self.startDateField.grid(row=4, column=2, padx=5, pady=5)

        endDateLabel = tk.Label(subBox, text="End Date", font=("Helvetica", 10))
        endDateLabel.grid(row=3, column=3, padx=5, pady=5)
        self.endDateField = ttk.Entry(subBox)
        self.endDateField.grid(row=4, column=3, padx=5, pady=5)

        self.nameField.insert(0, name)
        self.emailField.insert(0, email)
        self.phoneField.insert(0, phone)
        self.addressField.insert(0, address)
        self.ageField.insert(0, age)
        self.startDateField.insert(0, startDate)
        self.endDateField.insert(0, endDate)




    def submitUpdate(self, id):
        id = id
        self.name = self.nameField.get()
        self.email = self.emailField.get()
        self.phone = self.phoneField.get()
        self.address = self.addressField.get()
        self.age = self.ageField.get()
        self.startDate = self.startDateField.get()
        self.endDate = self.endDateField.get()

        check = self.query.updateMember(id, self.name, self.email, self.phone, self.address, self.age, self.startDate, self.endDate)

        if check:
            showinfo("Success", "Member updated")
            self.memberFrame.loadMemberFrame()
        else:
            showinfo("Error", "Member not updated")
