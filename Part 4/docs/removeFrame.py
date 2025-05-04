#Christian Kurdi
import tkinter as tk
import tkinter.ttk as ttk
from docs.Queries import Query
from tkinter.messagebox import showinfo
class RemoveFrame():
    def __init__(self, memberFrame, mainFrame, connection):
        self.memberFrame = memberFrame
        self.mainFrame = mainFrame
        self.connection = connection
        self.query = Query(self.connection)
        self.mainBox = None
        self.idField = None
        self.tableFrame = None

        self.showMenu()
    def showMenu(self):
        self.clearFrame()

        title = tk.Label(self.mainFrame, text="Remove A Member", font=("Helvetica", 14))
        title.pack(side=tk.TOP)

        backButton = ttk.Button(self.mainFrame, text="Back", command=lambda: self.memberFrame.loadMemberFrame())
        backButton.pack(anchor=tk.NW, padx=10, pady=10)

        mainBox = ttk.Frame(self.mainFrame)
        mainBox.pack(side=tk.TOP)
        self.mainBox = mainBox

        label = tk.Label(mainBox, text="Enter member ID to remove:")
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

            if self.tableFrame:
                self.tableFrame.destroy()
                self.tableFrame = None
                self.mainFrame.update()

            tableFrame = tk.Frame(self.mainBox)
            tableFrame.pack(side=tk.TOP)
            self.tableFrame = tableFrame

            showLabel = tk.Label(self.tableFrame, text="This is the member you've selected:")
            showLabel.pack(side=tk.TOP, padx=10, pady=10)


            table = ttk.Treeview(tableFrame, columns=("ID", "Name", "Email", "Phone", "Address", "Age", "Start Date", "End Date"))
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

            table.insert(parent="", index=0, values=data)
            table.pack(expand=True, fill=tk.BOTH)

            confirmLabel = tk.Label(self.tableFrame, text="Are you sure you want to remove this member?")
            confirmLabel.pack(side=tk.TOP, padx=10, pady=10)

            confirmBox = tk.Frame(self.tableFrame)
            confirmBox.pack(side=tk.TOP)

            yesButton = tk.Button(confirmBox, text="Yes", command=lambda: self.removeMember(id))
            yesButton.pack(side=tk.LEFT, padx=10, pady=10)

            noButton = tk.Button(confirmBox, text="No", command=lambda: self.showMenu())
            noButton.pack(side=tk.RIGHT, padx=10, pady=10)
        else:
            showinfo("Error", "Member not found")
    def removeMember(self, memberID):
        check = self.query.removeMember(memberID)
        if check:
            showinfo("Success", "Member removed")
            self.memberFrame.loadMemberFrame()
        else:
            showinfo("Error", "There was a problem removing")

