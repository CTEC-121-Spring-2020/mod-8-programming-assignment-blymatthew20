# Module 8
#   Programming Assignment 11
#     Prob-2.py

# Your code below

class Student:
    def __init__(self, name, IDnumber, major, GPA):
        self._name = name
        self._IDnumber = IDnumber
        self._major = major
        self._GPA = GPA
    
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_IDnumber(self, IDnumber):
        self._IDnumber = IDnumber

    def get_IDnumber(self):
        return self._IDnumber
    
    def set_major(self, major):
        self._major = major

    def get_major(self):
        return self._major

    def set_GPA(self, GPA):
        self._GPA = GPA
    
    def get_GPA(self):
        return self._GPA

def TestStudents():
    print()
    studentList = []
    studentList.append(Student('Joe Bella', "\t" "9933", "\t" "Web Development", "3.8"))
    studentList.append(Student('Tucker Blank', "\t" "3399", "\t" "Nursing", "\t" "3.0"))
    studentList.append(Student('Gayle Ujifusa ', "\t" "1011", "\t" "Baking", "\t" "\t" "2.8"))
    studentList.append(Student('Edna Anker', "\t" "9875", "\t" "Medical Office", "\t" "3.0"))
  
    
    


    for student in studentList:
        print(student.get_name(), student.get_IDnumber(), student.get_major(), student.get_GPA())
        
        



if __name__ == "__main__":
    TestStudents()
    print()
        
