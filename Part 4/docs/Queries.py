# Christian Kurdi
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
            return [0, e]
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
    # Returns a list of equipment data
    def getAllEquip(self):
        print("="*65)
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
    # Executes query to create an equipment record
    # Returns boolean confirmation
    def createEquip(self, currEquip):
        print("="*65)
        print("CREATE EQUIP: " + currEquip["name"])

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
            return True
        
        except Error as e:
            print(f"Error while creating data: {e}")
        return False
    
    # -- GET EQUIPMENT BY ID --
    # Executes query to GET an equipment record
    # Returns the equipment object as confirmation
    def getEquipByID(self, equipID):
        print("="*65)
        print("GET EQUIP BY ID: " + str(equipID))

        try:
            query = """
            SELECT * 
            FROM equipment
            INNER JOIN gymFacility
            ON equipment.gymId = gymFacility.gymId
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
                currEquip["gymLoc"] = line[6]
            self.connection.commit()
            return currEquip
        
        except Error as e:
            print(f"Error while retrieving data: {e}")
        return None
        
    # -- UPDATE EQUIPMENT BY ID --
    # Executes query to UPDATE an equipment record
    # Returns boolean confirmation
    def updateEquipByID(self, equipId, currEquip):
        print("="*65)
        print("UPDATE EQUIP W/ ID: " + str(equipId))

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
        return False
        
    # -- DELETE EQUIPMENT BY ID --
    # Executes query to DELETE an equipment record
    # Returns boolean confirmation
    def deleteEquipByID(self, equipId):
        print("="*65)
        print("DELETE EQUIP W/ ID: " + str(equipId))

        try:
            query = """
            DELETE FROM equipment
            WHERE equipmentId = ?
            """
            cursor = self.connection.cursor()
            cursor.execute(query, (equipId,))
            self.connection.commit()
            
            return True
        
        except Error as e:
            print(f"Error while retrieving data: {e}")
        return False

    # -- GET ALL GYMS --
    # Returns a list of gymFacity data
    def getAllGyms(self):
        print("="*65)
        print("GET ALL GYMS")
        try:
            query = """
            SELECT *
            FROM gymFacility
            """
            cursor = self.connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            self.connection.commit()
            return data
        
        except Error as e:
            print(f"Error while creating data: {e}")
        return None
        
    # -- GET GYM ID BY NAME --
    # Executes query to GET an equipment record
    # Returns the equipment object as confirmation
    def getAllGymIdByLoc(self, gymLoc):
        print("="*65)
        print("GET ALL GYMS")
        try:
            query = """
            SELECT *
            FROM gymFacility
            WHERE location = ?
            """
            gymId = None
            cursor = self.connection.cursor()
            cursor.execute(query, (gymLoc, ))
            for line in cursor:
                gymId = line[0]
            self.connection.commit()
            return gymId
        
        except Error as e:
            print(f"Error while creating data: {e}")
        return None

    def searchByClassID(self, ID):
        statement = f"SELECT * FROM class WHERE classId='{ID}';"

        try:
            cursor = self.connection.cursor()
            cursor.execute(statement)

            cursor.close()
        except Error as e:
            return False
        finally:
            return True

    def getMembersByClass(self, ID):
        statement = f"SELECT DISTINCT member.memberID, member.name FROM member NATURAL JOIN attends WHERE attends.classId='{ID}'; "
        data = None

        try:
            cursor = self.connection.cursor()
            cursor.execute(statement)
            data = cursor.fetchall()
            cursor.close()
        except Error as e:
            return [0, e]
        finally:
            return [1, data]
