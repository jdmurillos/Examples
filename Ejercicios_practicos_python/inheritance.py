class Person:
    def __init__(self):
        self.__Name = ""
        self.__LastName = ""
        self.__Age = 0
    
    def GetName(self):
        return self.__Name
    def SetName(self,name):
        self.__Name = name
    def GetLastName(self):
        return self.__LastName
    def SetLastName(self,lastname):
        self.__LastName = lastname
    def GetAge(self):
        return self.__Age
    def SetAge(self,age):
        self.__Age = age

class Student(Person):
    def __init__(self):
        self.__Grade = ""
        self.__Subject = ""
    
    def GetGrade(self):
        return self.__Grade
    def SetGrade(self,grade):
        self.__Grade = grade
    def GetSubject(self):
        return self.__Subject
    def SetSubject(self,subject):
        self.__Subject = subject

    def ShowStudent(self):
        print("Student: ")
        print("\tName: ",self.GetName())
        print("\tLast Name: ",self.GetLastName())
        print("\tAge: ",self.GetAge())
        print("\tGrade: ",self.GetGrade())
        print("\tSubject: ",self.GetSubject())

class Teacher(Person):
    def __init__(self):
        self.__Experience=""
        self.__Tutorials=""
        self.__TelephoneNumber=""
    
    def GetExperience(self):
        return self.__Experience
    def SetExperience(self,experience):
        self.__Experience=experience
    def GetTutorials(self):
        return self.__Tutorials
    def SetTutorials(self,tutorials):
        self.__Tutorials=tutorials
    def GetTelephoneNumber(self):
        return self.__TelephoneNumber
    def SetTelephoneNumber(self,telephonenumber):
        self.__TelephoneNumber = telephonenumber

    def ShowTeacher(self):
        print("TEACHER: ")
        print("\tName: ",self.GetName())
        print("\tLast Name: ",self.GetLastName())
        print("\tAge: ",self.GetAge())
        print("\tExperience: ",self.GetExperience())
        print("\tTutorials: ",self.GetTutorials())
        print("\tTelephone Number: ",self.GetTelephoneNumber())

class Researcher(Person):
    def __init__(self):
        self.__Major = ""
        self.__Years = ""
    def GetMajor(self):
        return self.__Major
    def SetMajor (self,major):
        self.__Major = major
    def GetYears (self):
        return self.__Years
    def SetYears (self,years):
        self.__Years = years

class UniversityTeacher(Teacher,Researcher):
    def __init__(self):
        self.__University = ""
        self.__Department = ""
    def GetUniversity (self):
        return self.__University
    def SetUniversity (self,university):
        self.__University = university
    def GetDepartment (self):
        return self.__Department
    def SetDepartment (self,department):
        self.__Department = department
    
    def ShowUniversityTeacher (self):
        print("PROFESOR UNIVERSITARIO")
        print("\tName: ",self.GetName())
        print("\tLast Name: ",self.GetLastName())
        print("\tAge: ",self.GetAge())
        print("\tExperience: ",self.GetExperience())
        print("\tTutorials: ",self.GetTutorials())
        print("\tTelephone: ",self.GetTelephoneNumber())
        print("\tMajor: ",self.GetMajor())
        print("\tYears: ",self.GetYears())
        print("\tUniversity: ",self.GetUniversity())
        print("\tDepartment: ",self.GetDepartment())


student= Student()
student.SetName("Alfred")
student.SetLastName("Wayne")
student.SetAge(30)
student.SetGrade("University")
student.SetSubject(["Math","Tech","English"])
student.ShowStudent()

teacher = UniversityTeacher()
teacher.SetName("Alí")
teacher.SetLastName("Roob")
teacher.SetAge(38)
teacher.SetExperience(5)
teacher.SetTutorials([["Monday","16-18"],["Tuesday","12-14"],["English","11-13"]])
teacher.SetTelephoneNumber("12345678")
teacher.SetMajor("Software Developer")
teacher.SetYears(15)
teacher.SetUniversity("Super University")
teacher.SetDepartment("Technology")
teacher.ShowUniversityTeacher()









