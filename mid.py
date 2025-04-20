class StudentDatabase:
    student_list=[]
    @classmethod
    def add_student(self,stu):
        self.student_list.append(stu)

class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id        
        self.__name = name                    
        self.__department = department       
        self.__is_enrolled = is_enrolled  

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled=True
        else:
            print('This student already enrolled')
            # raise Exception('This student already enrolled')

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
        else:
            print('This student have not enrolled')
            # raise Exception('This student have not enrolled')

    def view_student_info(self):
        print(f'student_id: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, and Enrollment status: {self.__is_enrolled}.')

stu1= Student(12,'saif','cse',True)
StudentDatabase.add_student(stu1)
stu2= Student(122,'rraif','bba',False)
StudentDatabase.add_student(stu2)

# stu2.enroll_student()
# stu1.enroll_student()

# stu1.view_student_info()
stu2.view_student_info()
# stu1.drop_student()
stu2.drop_student()

