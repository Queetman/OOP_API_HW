

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_count =0
        
    
    def add_course(self,course_name):
        self.courses_in_progress.append(course_name)
        self.grades[course_name] =0
        
    def add_finished_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.finished_courses+=[course_name]
            self.courses_in_progress.remove(course_name)
                 
    def set_grade(self, lecturer, course, lect_grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses) and (lect_grade > 1 and lect_grade < 11):
            lecturer.add_grade(course, lect_grade)
            
    def __get_avg_grade(self):
       
        if self.grade_count>0:
            sum =0
            for k, v in self.grades.items():
                sum+=v
            return float(sum/self.grade_count)
        else:
            return 0
        
    def __listToString(self,lst):
        return ' '.join((str(element) for element in lst))
    
    def __str__(self):
        
        return f' Имя: {self.name} \n Фамилия {self.surname} \n Средняя оценка за домашние задания: {self.__get_avg_grade()} \n Курсы в процессе изучения: {self.__listToString(self.courses_in_progress)} \n Завершенные курсы:{self.__listToString(self.finished_courses)}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


        
        
    def add_course (self,course_name):
        self.courses_attached.append(course_name)       

class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}        
        self.grade_count =0
        self.av =self.get_avg_grade()
    
    
        
    def __str__(self):
        
        return f" Имя: {self.name} \n Фамилия {self.surname} \n Средняя оценка за лекции:{self.get_avg_grade()} "

    def __lt__(self, other):
        print(f'Преподаватель {self.name} {self.surname} имеет лучший средний балл')
        return self.av < other.av
 
    def add_grade (self, course, grade):
        if course in self.grades:
            curr_val = self.grades[course]
            self.grades[course] = curr_val + grade
            self.grade_count+=1
        else:
            self.grades[course] = grade
            self.grade_count+=1
       
    def get_avg_grade(self):
        
        if  self.grade_count>0:
            sum =0
            for k, v in self.grades.items():
                sum+=v
            return float(sum/self.grade_count)
        else:
            return 0
        
   
    
    
         
class Reviewer(Mentor):
     
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grade_count+=1
                val = student.grades[course]
                student.grades[course] =val + grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'


    def __str__(self):
        
        return f"Имя: {self.name} \n  Фамилия {self.surname}"

lect_1= Lecturer("Ture","Lex")
lect_1.add_course('Java')
lect_1.add_course('c++')


#print(lect_1)

lect_2= Lecturer("Bo","James")
lect_2.add_course('Python')

#print(lect_2)


student_1 = Student('Ostap', 'Bender', 'Male')

student_1.add_course('Java')
student_1.add_course('Python')
student_1.add_course('c++')

student_1.add_finished_course('c++')
student_1.add_finished_course('SQL')# не закончил студент т.к. не начинал.

student_1.set_grade(lect_1, 'Java', 10)
student_1.set_grade(lect_1, 'Python', 5)

#print(student_1)

student_2 = Student('Kisa', 'Vorobyanionov', 'Male')
student_2.add_course('c++')
student_2.add_course('Python')

student_2.set_grade(lect_1, 'Python', 5) 

#print(lect_1)

rev_1 = Reviewer("Viewer","Re")
rev_1.add_course('Python')
rev_1.add_course('SQL')

#print(rev_1)

rev_2 = Reviewer("Conda","A.g.")
rev_2.add_course('DataSience')
rev_2.add_course('Pyton')

#print(rev_2)

rev_1.rate_hw(student_1,'Python', 7)
rev_1.rate_hw(student_1,'Python', 5)
rev_1.rate_hw(student_1,'Python', 7)

rev_1.rate_hw(student_1,'Paddington', 7)# не существует
rev_2.rate_hw(student_1,'Java', 5) # не сходится 


#print(student_1)

# Магический метод
#lect_2<lect_1

'''
# реализовать функцию для подсчета средней оценки за домашние задания по всем студентам 
в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);

'''

def get_avg(students, course):
    s = 0
    l = len(students)
 
    if l==0:
        return "Error"
    else:  
        for student in students:
                if course in student.grades:
                    s+=student.grades[course]
        return s/len(students)


st_arr = [student_1,student_2]

#print(get_avg(st_arr, 'Python'))

'''
для подсчета средней оценки за домашние задания по всем студентам 
в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).
'''

lect_arr = [lect_1,lect_2]

print(get_avg(lect_arr, 'Python'))