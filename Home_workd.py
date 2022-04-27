class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if grade < 11:
                if course in lecturer.courses_marks:
                    lecturer.courses_marks[course] += [grade]
                else:
                    lecturer.courses_marks[course] = [grade]
            else:
                print('Больше 10-ти нельзя))')
                
        else:
            return 'Ошибка'
    def Student_avarage(self):
        list_with_student_marks = [0]
        for marks in self.grades.values():
            list_with_student_marks  += marks
        avarage_num = round(sum(list_with_student_marks) / len(list_with_student_marks), 2)
        return avarage_num
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.Student_avarage()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'        
    def __lt__(self, student):
        if isinstance(student, Student):
            return self.Student_avarage() < student.Student_avarage()
        else:
            return None
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []              
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_marks = {}
        self.courses_attached = []
    def avarage(self):
        list_with_marks = [0]
        for marks in self.courses_marks.values():
            list_with_marks  += marks
        avarage_num = (sum(list_with_marks) / len(list_with_marks))
        avarage_num_MAIN = round(avarage_num, 1)
        return avarage_num_MAIN
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avarage()}'
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avarage() < lecturer.avarage()
        else:
            return None
    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.surname}'
def avarage_grade_of_all_students(student_list, course):
    list_with_marks = []
    for person in student_list:
        if course in person.grades.keys():
            for all_grades in person.grades.get(course):
               list_with_marks.append(all_grades)
        else:
            print(f'{person.name} {person.surname} не занимается на курсе {course} ')
    return round(sum(list_with_marks) / len(list_with_marks), 2)
def avarage_grade_of_all_lecturer(lecturer_list, course):
    list_with_marks = []
    for person in lecturer_list:
        if course in person.courses_marks.keys():
            for all_grades in person.courses_marks.get(course):
               list_with_marks.append(all_grades)
        else:
            print(f'{person.name} {person.surname} не преподает на курсе {course} ')
    return round(sum(list_with_marks) / len(list_with_marks), 2)
#создание объектов класса студенты
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student2 = Student('Rat', 'cEman', 'your_gender')
#добавление курса который изучает объект студент
best_student.courses_in_progress += ['Python']
good_lecturer = Lecturer('John','Marston')
#создание объектов класса лекторы
good_lecturer2 = Lecturer('Abigail','Marston')
#добавление курса который преподает объект лектор
good_lecturer.courses_attached += ['Python']
good_lecturer2.courses_attached += ['Python']
#оценка лектора классом студент
best_student.rate_lecturer(good_lecturer2, 'Python', 9)
best_student.rate_lecturer(good_lecturer2, 'Python', 10)
best_student.rate_lecturer(good_lecturer2, 'Python', 7)
best_student.rate_lecturer(good_lecturer, 'Python', 10)
best_student.rate_lecturer(good_lecturer, 'Python', 8)
best_student.rate_lecturer(good_lecturer, 'Python', 5)
best_student2.rate_lecturer(good_lecturer, 'Python', 10)
best_student2.rate_lecturer(good_lecturer, 'Python', 8)
best_student2.rate_lecturer(good_lecturer, 'Python', 5)
#проверка на вывод оценок лектора за его лекцию
print(good_lecturer.courses_marks)
#создание ментора 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
best_reviewer = Reviewer('Arthur','Morgan')
best_reviewer.courses_attached += ['Python']
#оценка дз ментором
best_reviewer.rate_hw(best_student, 'Python', 9) 
best_reviewer.rate_hw(best_student, 'Python', 10) 
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student2, 'Python', 6) 
best_reviewer.rate_hw(best_student2, 'Python', 10) 
best_reviewer.rate_hw(best_student2, 'Python', 10) 
#проверка правельности вывода информации об объектах класса
print(best_student.grades)
print(good_lecturer)
print(best_student)
#проверка сравнений
print(best_student < best_student2)
print(good_lecturer < good_lecturer2)
student_list = [best_student, best_student2]
lecturer_list = [good_lecturer, good_lecturer2]
#полевые испытания
print(avarage_grade_of_all_students(student_list, 'Python'))
print(avarage_grade_of_all_lecturer(lecturer_list, 'Python'))




