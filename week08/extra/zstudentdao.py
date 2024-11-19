"""This module is responsible for handling all the database operations"""
import mysql.connector
import dbconfig as cfg

class StudentDAO:
    """This class is responsible for handling all the database operations"""
    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""

    def __init__(self):
        #these should be read from a config file
        #self.host="localhost"
        #self.user="root"
        #self.password=""
        #self.database="wsaa"
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self):
        """This method is responsible for creating a connection to the database""" 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeall(self):
        """This method is responsible for closing the connection to the database"""
        self.connection.close()
        self.cursor.close()

    def getall(self):
        """This method is responsible for fetching all the records from the database"""
        cursor = self.getcursor()
        sql="select * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        studentlist = []
        for row in result:
            studentlist.append(self.converttodict(row))

        self.closeall()
        return studentlist

    def findbyid(self, identifier):
        """This method is responsible for fetching a record from the database based on the id"""
        cursor = self.getcursor()
        sql="select * from student where id = %s"
        values = (identifier,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeall()
        return self.converttodict(result)

    def create(self, student):
        """This method is responsible for inserting a record into the database"""
        cursor = self.getcursor()
        sql="insert into student (name, age) values (%s,%s)"
        values = (student.get("name"), student.get("age"))
        cursor.execute(sql, values )

        self.connection.commit()
        newid = cursor.lastrowid
        student["id"] = newid
        self.closeall()
        return student


    def update(self, identifier,  student):
        """This method is responsible for updating a record in the database"""
        cursor = self.getcursor()
        sql="update student set name= %s, age=%s  where id = %s"

        values = (student.get("name"), student.get("age"), identifier)
        cursor.execute(sql, values)
        self.connection.commit()

        self.closeall()
        return student

    def delete(self, identifier):
        """This method is responsible for deleting a record from the database"""
        cursor = self.getcursor()
        sql="delete from student where id = %s"
        values = (identifier,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeall()
        print("delete done")
        return True

    def converttodict(self,resultline):
        """This method is responsible for converting the result from 
        the database into a dictionary"""
        studentkeys = ["id", "name", "age"]
        currentkey = 0
        student = {}
        for attrib in resultline:
            student[studentkeys[currentkey]] = attrib
            currentkey = currentkey + 1
        return student

studentDAO = StudentDAO()
# End-of-file (EOF)
