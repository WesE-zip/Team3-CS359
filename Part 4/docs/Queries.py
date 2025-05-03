#Christian Kurdi
import sqlite3
from sqlite3 import Error

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




