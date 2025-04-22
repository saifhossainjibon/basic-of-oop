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
    @property
    def get_stu_id(self):
        return self.__student_id
        
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
        print(f'student id: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, and Enrollment status: {self.__is_enrolled}.')

stu1= Student(112,'saif','cse',True)
StudentDatabase.add_student(stu1)
stu2= Student(122,'rafi','bba',False)
StudentDatabase.add_student(stu2)
stu3= Student(120,'sakil','English',True)
StudentDatabase.add_student(stu3)
stu4= Student(129,'rakib','EEE',False)
StudentDatabase.add_student(stu4)
stu5= Student(121,'akash','astronomy',True)
StudentDatabase.add_student(stu5)


# print(stu1.get_stu_id)
while True:
    print("\nMenu:")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
    choice=int(input("Enter Your Choice: "))
    if choice== 1:
        for student in StudentDatabase.student_list:
            student.view_student_info()
    elif choice==2:
        id=int(input("Enter the student id: "))  
        for student in StudentDatabase.student_list:
            if  student.get_stu_id==id:
                student.enroll_student()
    elif choice==3:
        id=int(input("Enter the student id: "))  
        for student in StudentDatabase.student_list:
            if  student.get_stu_id==id:
                student.drop_student()
    elif choice==4:
        break

