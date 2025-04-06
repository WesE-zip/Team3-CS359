# Cruz Urbina

import sys
import sqlite3
from sqlite3 import Error


class SQLHandler:
    def __init__(self, question_num, param1):
        self.question_num = question_num
        self.param1 = param1
        self.dbName = "XYZGym.sqlite"

    def question_one(self, connection):
        getMembers = "select member.name, member.email, member.age, planId from member natural join (select memberId, planId from payment)"
        cursor = connection.cursor()
        cursor.execute(getMembers)
        for member in cursor:
            print(f"Member name: {member[0]}, Email: {member[1]}, Age: {member[2]}, Membership Plan: {member[3]}")

        self.closeConnection(connection)

    def question_two(self, connection):
        getID = "select gymID from gymFacility"#Find existing gymID's

        cursor = connection.cursor()
        cursor.execute(getID)
        for line in cursor:

            findInfo = "select count(gymID) from class where gymID = " + str(line[0])
            #Get info for each gymID
            cursor2 = connection.cursor()
            cursor2.execute(findInfo)
            count = cursor2.fetchone()[0]
            print(f"The number of classes at gym {line[0]} is {count}")


    def question_three(self, connection):
        p1 = str(self.param1)
        print(f"Retrieving names of members attending class {p1}")
        getNames = "select member.name from (member natural join attends) where attends.classID = " + p1
        cursor = connection.cursor()
        cursor.execute(getNames)
        for line in cursor:
            print(f"Member name: {line[0]}")

    def question_four(self, connection):
        p1 = self.param1
        print(f"Retrieving all equipment of type: {p1}")
        
        getEquipment = f"SELECT * FROM equipment WHERE type = ?"
        cursor = connection.cursor()
        cursor.execute(getEquipment, (p1,))
        
        print("ID\t\tName\t\tType\t\tQuantity\t\tGymID")
        for line in cursor:
            print(f"{line[0]}\t\t{line[1]}\t\t{line[2]}\t\t{line[3]}\t\t{line[4]}")
            
        self.closeConnection(connection)

    def question_five(self, connection):
        checkMembership = "select name from member where membershipEndDate < date('now')"
        cursor = connection.cursor()
        cursor.execute(checkMembership)
        print("Members with expired memberships:")
        for member in cursor:
            print(f"Member name: {member[0]}")

    def question_six(self, connection):
        print("Question Six...")
        p1 = self.param1
        print("Parameter: ", p1)

    def question_seven(self, connection):
        getAverageAge = """
        SELECT 
            avg(CASE WHEN membershipEndDate < date('now') THEN age END) AS expiredAgeAVG,
            avg(CASE WHEN membershipEndDate >= date('now') THEN age END) AS activeAgeAVG
        FROM member
        """
        cursor = connection.cursor()
        cursor.execute(getAverageAge)
        print("Exp - AVG Age\tAct - AVG Age")
        for line in cursor:
            print(f"{line[0]}\t\t{line[1]}")

        self.closeConnection(connection)


    def question_eight(self, connection):
        print("Question Eight...")

    def question_nine(self, connection):
        print("Question Nine...")
        p1 = self.param1
        print("Parameter: ", p1)

    def question_ten(self, connection):
        print("Recent Class Attendance:")
        getTotalClasses = """
        SELECT 
            member.name, count(attends.classID) as totalClasses, 
            group_concat(DISTINCT class.className) as classesAttended, 
            group_concat(DISTINCT class.classType) as classTypes 
        FROM ((member INNER JOIN attends ON member.memberId = attends.memberId) 
        INNER JOIN class ON attends.classId = class.classId) 
        WHERE attends.attendanceDate >= DATE('now', '-1 month') 
        GROUP BY member.memberId
        """
        cursor = connection.cursor()
        cursor.execute(getTotalClasses)
        print("Member Name\t\tTotal Classes\t\tClasses Attended\t\tClass Type")
        print("="*95)
        for line in cursor:
            print(f"{line[0]}\t\t{line[1]}\t\t{line[2]}\t\t{line[3]}")
        
        self.closeConnection(connection)

    def error_msg(self):
        print("Query failed...")

    # Executes the question according to number
    # and validates if parameter value has been passed
    def exec(self, connection):
        q_num = self.question_num
        p1 = self.param1

        if q_num == 1:
            self.question_one(connection)
        elif q_num == 2:
            self.question_two(connection)
        elif q_num == 3 and p1:
            self.question_three(connection)
        elif q_num == 4 and p1:
            self.question_four(connection)
        elif q_num == 5:
            self.question_five(connection)
        elif q_num == 6 and p1:
            self.question_six(connection)
        elif q_num == 7:
            self.question_seven(connection)
        elif q_num == 8:
            self.question_eight(connection)
        elif q_num == 9 and p1:
            self.question_nine(connection)
        elif q_num == 10:
            self.question_ten(connection)
        else:
            self.error_msg()

    def createConnection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.dbName)
            print(f"Connection established with {sqlite3.sqlite_version}")
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_key = ON")
        except Error as e:
            print(f"Error while connecting to database: {e}")
        finally:
            if connection:
                return connection


    def closeConnection(self, connection):
        connection.close()

# Main method
# Validates the question number type (ex. Int)
# Checks if a parameter value has been passed
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing question number.")
        sys.exit()

    try:
        question_num = int(sys.argv[1])
    except ValueError:
        print("Invalid question number.")
        sys.exit(1)

    param1 = None
    if len(sys.argv) > 2:
        param1 = sys.argv[2]

    sql_handler = SQLHandler(question_num, param1)
    connection = sql_handler.createConnection()
    sql_handler.exec(connection)
