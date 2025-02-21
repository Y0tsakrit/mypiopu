class Student():

    def __init__(self,id,name):
        self.__id=id
        self.__name=name

class Subject():

    def __init__(self,id,name,credit):
        self.__id=id
        self.__name=name
        self.__credit=credit
        self.__teacher= "  "

    def assign_teacher(self,name):
        self.__teacher = name

    def enroll_to_subject(self,name):
        try:
            if name not in self.__student:
                self.__student.append(name)
                print("Done")
            else:
                print("Already Enrolled")
        except:
            print("Error")

    def drop_from_subject(self,name):
        try:
            if name in self.__student:
                self.__student.remove(name)
            else:
                print("Not Found")
        except:
            print("Error")

    def search_student_enrolled_in_subject(self):
        try:
            if len(self.__student) !=0:
                self.__student
            else:
                self.__student
        except:
            print("Error")

    def get_no_student_enrolled(self):
        if len(self.__student)!=0:
            print(len(self.__student))
        else:
            print("Not Found")




class Teacher():

    def __init__(self,id,name):
        self.__id=id
        self.__name=name