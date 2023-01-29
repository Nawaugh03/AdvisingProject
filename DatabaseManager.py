import mysql.connector
from os import path
import csv
class DBmanager():
    def __init__(self, hostname="", username="", passwrd="", databasename=""):
        self.databasename = databasename
        self.hostname = hostname
        self.username = username
        self.password = passwrd

        if (self.isDbExist(self.databasename) or self.databasename==""):
            self.DBconnection = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password)
            self.tables=[]
        else:
            self.CreateNewDatabase(self.databasename)
            self.DBconnection = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password,
                                                    database=self.databasename)
            self.tables = self.GenerateTables()

    def GetTables(self):
        a = self.DBconnection.cursor()
        code = """SHOW TABLES;"""
        a.execute(code)
        List = []
        for items in a.fetchall():
            List.append(items[0])
        a.close()
        return List
    def isDbExist(self,dbname):
        temp = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password)
        a = temp.cursor()
        code = """SHOW databases;"""
        a.execute(code)
        for x in a.fetchall():
            if (dbname == x[0]):
                a.close()
                temp.close()
                return True
        return False
    def isTableExist(self, Tablename):
        for i in self.tables:
            if(Tablename == i.Name):
                return True
        return False
    def CreateNewDatabase(self,dbname):
        if (self.isDbExist(dbname)):
            pass
        else:
            temp = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password)
            a = temp.cursor()
            code = f"""CREATE DATABASE {dbname}"""
            a.execute(code)
            temp.commit()
            a.close()
            temp.close()
    def DropCurrentDatabase(self):
        self.DBconnection.close()
        temp = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password)
        a =temp.cursor()
        code = f"""DROP Database {self.databasename}"""
        a.execute(code)
        temp.commit()
        self.DBconnection=temp
        a.close()
        temp.close()
    def UseDatabase(self, dbname):
        a=self.DBconnection.cursor()
        code=f"""use {dbname.lower()}"""
        try:
            a.execute(code)
            self.DBconnection.commit()
            a.close()
        except:
            self.CreateNewDatabase(dbname.lower())
            a.execute(code)
            self.DBconnection.commit()
            a.close()
    def GetTableContent(self, table):
        a = self.DBconnection.cursor()
        code = f"""SELECT * FROM {table};"""
        a.execute(code)
        List = []
        for items in a.fetchall():
            List.append(items)
        a.close()
        return List
    def GetTableDescription(self, table):
        a=self.DBconnection.cursor()
        code = f"""DESCRIBE {table};"""
        a.execute(code)
        List=[]
        for items in a.fetchall():
            List.append(items)
        a.close()
        return List
    def GenerateTables(self):
        ListofTables=[]
        for i in range(len(self.GetTables())):
            Tablename=self.GetTables()[i]
            ListofTables.append(Table(Tablename,self.GetTableContent(Tablename), self.GetTableDescription(Tablename)))
        return ListofTables
    def DisplayTables(self):
        for i in self.tables:
            print(i.Name)
    def ImportToCSV(self, Table):#This function allow to import one table into a csv tile
        with open (f"{Table.Name}.csv",'a',newline="") as csvfile:
            columnnames=[]
            for i in range(len(Table.Description)):
                columnnames.append(Table.Description[i][0])
            writer=csv.writer(csvfile)
            writer.writerow(columnnames)
            for content in (Table.Content):
                writer.writerow(content)

    def ExportFromCSV(self, csvname):
        Newtable=Table(csvname)
        Tablecolumnnames=[]
        Tablecontent=[]
        with open (f"{csvname}.csv",'r')as csvfile:
            reader=csv.reader(csvfile)
            rownumber=0
            for row in reader:
                if (rownumber==0):
                    Tablecolumnnames.append(row)
                elif(rownumber>0):
                    Tablecontent.append(row)
                rownumber=rownumber+1
        Newtable.GetColumnnames(Tablecolumnnames)
        Newtable.Getcontent(Tablecontent)
        Newtable.GenerateDatatypes()
        self.tables.append(Newtable)
        #if (csvname == "list" or csvname == 'curriculum')
        #if Table does exist Alter the Table with the content
        #if Table doesn't exist Create a new table and insert content into the table
    def ImportTablestoSQL(self):
        primkey = ""
        existprime=False
        for tableindex in range(len(self.tables)):#number of tables
            a = self.DBconnection.cursor()
            tablecode=f"CREATE TABLE {self.tables[tableindex].Name} (\n"
            rownum = 0
            totalrows=len(self.tables[tableindex].columnnames[0])
            #create a table
            for index in range(len(self.tables[tableindex].columnnames[0])):#number of columns
                datatype=self.tables[tableindex].columntypes[index]
                columnname=self.tables[tableindex].columnnames[0][index]
                notnulltext=""
                if ("primarykey"in datatype and existprime is False):
                    datatype = str(datatype).replace("primarykey", "")
                    primkey= columnname
                    existprime=True
                    notnulltext="NOT NULL"
                    totalrows+=1
                tablecode+=f"{columnname} {datatype} {notnulltext}"
                if (rownum<totalrows):
                    tablecode+=",\n"
                    rownum+=1
                else:
                    tablecode+="\n"
            if(existprime):
                tablecode+=f"PRIMARY KEY ({primkey})\n"
            tablecode+=");"
            rownum=1
            print(tablecode)# execute statement
            #a.execute(tablecode)
            #a.close()
            """Place the content into the table in the sql system"""
            contentcode=f"INSERT INTO {self.tables[tableindex].Name} ("
            totalrows=len(self.tables[tableindex].columnnames[0])
            for colname in self.tables[tableindex].columnnames[0]:
                contentcode+=str(colname)
                if(rownum<totalrows):
                    contentcode+=",\n"
                else:
                    contentcode+=")\n"
                rownum+=1

            totalrows=len(self.tables[tableindex].columnnames[0])
            totalcontentnumber=len(self.tables[tableindex].Content)
            colnum=1
            contentcode+="VALUES"
            for items in (self.tables[tableindex].Content):
                rownum=1
                contentcode+="("
                for itemindex in  range(len(self.tables[tableindex].columnnames[0])):
                    if("INT" in self.tables[tableindex].columntypes[itemindex]):
                        contentcode+=str(items[itemindex])
                    else:
                        message=f"\'{items[itemindex]}\'"
                        contentcode+=message
                    if(rownum<totalrows):
                        contentcode+=","
                    elif(rownum==totalrows and colnum<totalcontentnumber):
                        contentcode+="),\n"
                    else:
                        contentcode+=");"
                    rownum+=1
                colnum+=1
            print(contentcode) #executable statement
            #a.execute(contentcode)
            #a.close()

class Table:
    def __init__(self, Tablename, tablecontent=None, tabledescription=None):
        self.Name=Tablename
        self.Content=tablecontent
        self.columnnames = []
        self.columntypes = []
        if(tabledescription != None):
            self.Description=tabledescription
            for desc in self.Description:
                self.columnname.append(str(desc[0]).replace('\'',''))
                self.columntype.append(str(desc[1]).replace('b','').replace('\'',''))
        else:
            pass

    def GenerateDatatypes(self):
        primkey=False
        for index in range(len(self.columnnames[0])):
            columnlist=[row[index] for row in self.Content]
            #print(columnlist)
            text=""
            if (all(element.isdigit()for element in columnlist)):
                #print("INT")
                text+="INT"
            elif(any(ele.isalnum() for ele in columnlist)):
                #print("VARCHAR(255)")
                text+="VARCHAR(255)"
            if ("id" in str(self.columnnames[0][index]).lower() and primkey is False):
                text+=" primarykey"
                primkey=True
            self.columntypes.append(text)

    def Getcontent(self, content):
        self.Content=content
    def GetColumnnames(self, names):
        self.columnnames=names
    def showinfo(self):
        print(self.Name)
        print(self.columnnames)
        print(self.columntypes)
        print(self.Content)
"""
Use cases:
    Complete{-A=DBmanager("localhost","root","1234","test") -print(A.tables)} get table from database
    
    Complete{A=DBmanager("localhost","root","1234")
    A.UseDatabase("example_db")
    A.tables=A.GenerateTables()
    print(str(A.tables[0].columntype))}
    
    Complete csv->table
    table->sql put the table into sql, 1.) use database, 2.) 
    XA.ImportToCSV(Table)//Take the content from Database, and convert the list to a table in a csv file ({COURSE, NUMBER, TITLE, CREDIT} ...)
    XA.ExportFromCSV("Curriculum.csv")//Take name of file and convert the csv into the list then if the table does exist then edit the table by inserting the 
"""
if __name__ in "__main__":
    A = DBmanager("localhost", "root", "1234")
    A.ExportFromCSV("Curriculums")
    #A.tables[0].showinfo()
    #print("\n")
    A.UseDatabase("Curriculums")
    A.ImportTablestoSQL()
    #A.CreateNewDatabase("Curriculums")
    #A.ExportFromCSV("Curriculums")