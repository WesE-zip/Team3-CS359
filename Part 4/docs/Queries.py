#Christian Kurdi
import sqlite3
from sqlite3 import Error
import tkinter.messagebox as msgBox

class Query():
    def __init__(self, connection):
        self.connection = connection

    def addMember(self, id, name, email, phone, address, age, startDate, endDate):
        statement = f"INSERT INTO member(memberId, name, email, phone, address, age, membershipStartDate, membershipEndDate) VALUES({id}, '{name}', '{email}', '{phone}', '{address}', {age}, '{startDate}', '{endDate}');"
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement)
            cursor.close()
            self.connection.commit()
        except Error as e:
            return False
        finally:
            return True

    def getMembers(self):
        returnCursor = None
        try:
            statement = "SELECT * FROM member"
            cursor = self.connection.cursor()
            cursor.execute(statement)
            returnCursor = cursor
        except Error as e:
            return [0,e]
        finally:
            return [1, returnCursor]

    def searchByID(self, ID):
        statement = f"SELECT * FROM member WHERE memberId='{ID}';"

        cursor = self.connection.cursor()
        cursor.execute(statement)

        data = cursor.fetchone()
        cursor.close()
        return data

    def removeMember(self, ID):
        statement = f"DELETE FROM member WHERE memberId='{ID}';"

        try:
            cursor = self.connection.cursor()
            cursor.execute(statement)
            self.connection.commit()
        except Error as e:
            return False
        finally:
            return True

    def updateMember(self, id, name, email, phone, address, age, startDate, endDate):
        statement = f"UPDATE member SET name = '{name}', email = '{email}', phone = '{phone}', address = '{address}', age = {age}, membershipStartDate = '{startDate}', membershipEndDate = '{endDate}' WHERE memberId = '{id}';"
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement)
            self.connection.commit()
            cursor.close()
        except Error as e:
            return False
        finally:
            return True


            
    # -- EQUIPMENT QUIERIES --
    
    # -- GET ALL EQUIPMENT ITEMS --
    def getAllEquip(self):
        print("GET ALL EQUIPMENT")
        try:
            query = """
            SELECT *
            FROM equipment
            """
            cursor = self.connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            self.connection.commit()
            return data
        
        except Error as e:
            print(f"Error while creating data: {e}")
        return None
    
    # -- CREATE EQUIPMENT  --
    def createEquip(self, currEquip):    
        print("="*95)
        print("Create equip: " + currEquip["name"])

        try:
            query = """
            INSERT INTO equipment (name, type, quantity, gymId)
            VALUES (?, ?, ?, ?)
            """
            cursor = self.connection.cursor()
            cursor.execute(query, (currEquip["name"], 
                                    currEquip["type"],
                                    currEquip["quantity"], 
                                    currEquip["gymId"]))
            self.connection.commit()
            msgBox.showinfo("SQLite Connection", "SUCCESS: Equipment created.")
            return True
        
        except Error as e:
            print(f"Error while creating data: {e}")
        return False
    
    def getEquipByID(self, equipID):
        print("="*95)
        print("Get equipID: " + str(equipID))

        try:
            query = """
            SELECT * 
            FROM equipment
            WHERE equipmentId = ?
            """
            cursor = self.connection.cursor()
            cursor.execute(query, (equipID,))
            currEquip = {}
            for line in cursor:
                currEquip["id"] = line[0]
                currEquip["name"] = line[1]
                currEquip["type"] = line[2]
                currEquip["quantity"] = line[3]
                currEquip["gymId"] = line[4]
            return currEquip
        
        except Error as e:
            print(f"Error while retrieving data: {e}")
            msgBox.showerror("SQLite Connection", "Error retrieving data.")
        return None
        
        
    def updateEquipByID(self, currEquip):
        print("="*95)
        print("Update equipment w/ equipID: " + str(currEquip["id"]))

        try:
            query = """
            UPDATE equipment
            SET name = ?, type = ?, quantity = ?, gymId = ?
            WHERE equipmentId = ?
            """
            cursor = self.connection.cursor()
            cursor.execute(query, (currEquip["name"],
                                    currEquip["type"],
                                    currEquip["quantity"],
                                    currEquip["gymId"],
                                    currEquip["id"]))
            self.connection.commit()
            return True
        
        except Error as e:
            print(f"Error while retrieving data: {e}")
            msgBox.showerror("SQLite Connection", "Error retrieving data.")
        return False
        
    def deleteEquipByID(self, equipId):
        print("="*95)
        print("Delete equipID: " + str(equipId))

        try:
            query = """
            DELETE FROM equipment
            WHERE equipmentId = ?
            """
            cursor = self.connection.cursor()
            cursor.execute(query, (equipID,))
            
            return True
        
        except Error as e:
            print(f"Error while retrieving data: {e}")
            msgBox.showerror("SQLite Connection", "Error deleting data.")
        return False


