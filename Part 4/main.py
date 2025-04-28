# Cruz Urbina

import sys
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from sqlite3 import Error
from docs import EmployeeFrame as ef


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.title("DB Manager")
        self.geometry("600x400")
        
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=10, expand=True, fill=tk.BOTH)
        
        self.loadConnFrame()
        
        self.connection = None
        
        
    # Function to clear out all widgets inside a frame
    def clearFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()
            
        
    def loadConnFrame(self):
        self.mainFrame = ttk.Frame(self)
        
        label = ttk.Label(self.mainFrame, text="Database Name:")
        label.pack(padx=5, pady=5)
        
        entry = ttk.Entry(self.mainFrame)
        entry.pack(padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="CONNECT", command=lambda: self.checkConn(entry.get()))
        button.pack(padx=5, pady=5)
        
        self.mainFrame.pack(padx=10, expand=True, fill=tk.BOTH)
        
        
    def loadMenuFrame(self):
        self.clearFrame()
        
        label = ttk.Label(self.mainFrame, text="MAIN MENU")
        label.pack(padx=5, pady=5)
  
        button = ttk.Button(self.mainFrame, text="EMPLOYEES", command=lambda: self.setFrame("EMPLOYEES"))
        button.pack(padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="CUSTOMERS", command=lambda: self.checkConn(entry.get()))
        button.pack(padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="EQUIPMENT", command=lambda: self.checkConn(entry.get()))
        button.pack(padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="EXIT", command=lambda: self.checkConn(entry.get()))
        button.pack(padx=5, pady=5)
        
        
    def checkConn(self, dbName):
        if True: #self.createConnection(dbName):
            self.loadMenuFrame()
        else:
            messagebox.showerror("SQLite Connection", "Database not found.")
        

    def setFrame(self, frame):
        if frame == "EMPLOYEES":
            self.clearFrame()
            currFrame = ef.EmployeeFrame(self, self.connection)
            currFrame.pack(padx=10, expand=True, fill=tk.BOTH)
       
        
    def createConnection(self):
        self.connection = None
        try:
            self.connection = sqlite3.connect(self.dbName)
            print(f"Connection established with {sqlite3.sqlite_version}")
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_key = ON")
        except Error as e:
            print(f"Error while connecting to database: {e}")
            return False
        return True


    def closeConnection(self):
        self.connection.close()


if __name__ == "__main__":

    app = App()
    app.mainloop()