from DatabaseManager import DBmanager
from queue import Queue
#A rough draft of the code below
"""
class course:
    def __init__(self,coursetype="N/A",coursenum=0,courseTitle="N/A",creditnum=0,prerequisite=[],courseid=0):
        self.coursetype=coursetype
        self.coursenum=coursenum
        self.courseTitle=courseTitle
        self.creditnum=creditnum
        self.prerequisites=prerequisite
        self.courseID=courseid
    def GetCourseType(self,ctype):
        self.coursetype=ctype
    def GetCourseNum(self, coursenum):
        self.coursenum=coursenum
    def GetCourseTitle(self, title):
        self.courseTitle=title
    def GetCreditNum(self, cnum):
        self.creditnum=cnum
    def GetPrerquisites(self, prereq):
        self.prerequisites=prereq
    def GetCourseID(self,courseid):
        self.courseID=courseid
        
class area:
    def __init__(self,name="Area 0",courses=[],maxcredit=0,areaID=0):
        self.Name=name
        self.courses=courses
        self.MaxCredit=maxcredit
        self.AreaID=areaID
    def GetAreaName(self, name):
        self.Name=name
    def GetCourses(self, courses):
        self.courses=courses
    def GetMaxCredit(self, creditnum):
        self.MaxCredit=creditnum
    def GetAreaID(self,areaID):
        self.AreaID=areaID

class student:
    def __init__(self,fname="N/A",lname="N/A",ID=0, CurrentCourses=[], RemainingCourses=[]):
        self.Firstname=fname
        self.Lastname=lname
        self.StudentID=ID
        self.CurrentCourse=CurrentCourses
        self.RemainingCourses=Queue()
        if(RemainingCourses!=[]):
            for items in RemainingCourses:
                self.RemainingCourses.put(items)
    def Getname(self,fname,lname):
        self.Firstname=fname
        self.Lastname=lname
    def GetFirstname(self,fname):
        self.Firstname=fname
    def GetLastname(self,lname):
        self.lname(self,lname)
    def GetStudentID(self, ID):
        self.StudentID=ID
    def GetCurrentCourses(self, Courses):
        self.CurrentCourses=Courses
    def GetRemainingCourses(self,RemCourses):
        for course in RemCourses:
            self.RemainingCourses.put(RemCourses)
"""

class AdvisingManager:
    pass

if __name__ in "__main__":
    A = DBmanager("localhost", "root", "1234")
   

