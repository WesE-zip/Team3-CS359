# Cruz Urbina

import sys
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from sqlite3 import Error
from docs import MemberFrame as mf
from docs import ClassesFrame as cf
from docs import EquipmentFrame as ef


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.title("DB Manager")
        self.geometry("600x400")
        
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=10, expand=True, fill=tk.BOTH)
        
        self.loadConnFrame()
        
        self.connection = None
        
        
    # Loads Connection Frame    
    def loadConnFrame(self):
        label = ttk.Label(self.mainFrame, text="Database Name:")
        label.pack(padx=5, pady=5)
        
        entry = ttk.Entry(self.mainFrame)
        entry.pack(padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="CONNECT", command=lambda: self.checkConn(entry.get()))
        button.pack(padx=5, pady=5)
        
    
    # Clears Frame
    # Loads Menu Frame
    def loadMenuFrame(self):
        self.clearFrame()
        
        label = ttk.Label(self.mainFrame, text="MAIN MENU")
        label.pack(padx=5, pady=5)
  
        button = ttk.Button(self.mainFrame, text="MEMBERS", command=lambda: self.setFrame("MEMBERS"))
        button.pack(padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="CLASSES", command=lambda: self.setFrame("CLASSES"))
        button.pack(padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="EQUIPMENT", command=lambda: self.setFrame("EQUIPMENT"))
        button.pack(padx=5, pady=5)
        
        button = ttk.Button(self.mainFrame, text="LOGOUT & EXIT", command=lambda: sys.exit())
        button.pack(padx=5, pady=5)
        
        
    # Function to clear out all widgets inside a frame
    def clearFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()
        
    
    # Set current
    def setFrame(self, frame):
        if frame == "MEMBERS":
            mf.MemberFrame(self, self.mainFrame, self.connection)
            
        if frame == "CLASSES":
            cf.ClassesFrame(self, self.mainFrame, self.connection)
            
        if frame == "EQUIPMENT":
            ef.EquipmentFrame(self, self.mainFrame, self.connection)
            
       
    # Create SQLite connection
    def createConnection(self):
        self.connection = None
        try:
            self.connection = sqlite3.connect(self.dbName)
            print(f"Connection established with {sqlite3.sqlite_version}")
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_key = ON")
            return True
        except Error as e:
            print(f"Error while connecting to database: {e}")
            return False
        return True
        
    # Check connection
    # TRUE: Load Menu Frame
    def checkConn(self, dbName):
        if True: #self.createConnection(dbName):
            self.loadMenuFrame()
        else:
            messagebox.showerror("SQLite Connection", "Database not found.")

    # Close SQLite connection
    def closeConnection(self):
        self.connection.close()

# Create App
if __name__ == "__main__":

    app = App()
    app.mainloop()