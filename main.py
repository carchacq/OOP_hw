

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lt(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.cp_column = ', '.join(self.courses_in_progress)
        self.fc_column = ', '.join(self.finished_courses)
        student_inf = f'''Имя: {self.name} 
Фамилия: {self.surname} 
Средняя оценка за домашние задания: {self._av_hw_()}
Курсы в процессе изучения: {self.cp_column}
Завершенные курсы: {self.fc_column}'''
        return student_inf

    def _av_hw_(self):
        hw_list = []
        for k,v in self.grades.items():
            for vv in v:
                hw_list.append(vv)
        return sum(hw_list) / len(hw_list)


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self._av_hw_() < other._av_hw_()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        lect_inf = f'''Имя: {self.name} 
Фамилия: {self.surname} 
Средняя оценка за лекции: {self._av_lt_()}'''
        return lect_inf

    def _av_lt_(self):
        lt_list = []
        for k,v in self.grades.items():
            for vv in v:
                lt_list.append(vv)
        av = sum(lt_list) / len(lt_list)
        return av

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self._av_lt_() < other._av_lt_()



class Reviewer(Mentor):
    def __str__(self):
        rev_inf = f'''Имя: {self.name} 
Фамилия: {self.surname}'''
        return rev_inf

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'




katya = Student('Екатерина', 'Синичкина', 'female')
katya.courses_in_progress += ['Python']
katya.courses_in_progress += ['Git']
katya.finished_courses += ['Введение в программирование']

petya = Student('Петр', 'Скворцов', 'male')
petya.courses_in_progress += ['Python']
petya.courses_in_progress += ['Git']
petya.finished_courses += ['Введение в программирование']

ivanovich = Reviewer('Иван', 'Воробейченко')
ivanovich.courses_attached += ['Python']

petrovich = Reviewer('Петр', 'Куроедов')
petrovich.courses_attached += ['Git']

eduard = Lecturer('Эдуард', 'Ареопагитский')
eduard.courses_attached += ['Python']

veniamin = Lecturer('Вениамин', 'Богоявленский')
veniamin.courses_attached += ['Git']

ivanovich.rate_hw(katya, 'Python', 10)
ivanovich.rate_hw(katya, 'Python', 8)
ivanovich.rate_hw(petya, 'Python', 9)
ivanovich.rate_hw(petya, 'Python', 8)
petrovich.rate_hw(katya, 'Git', 6)
petrovich.rate_hw(katya, 'Git', 7)
petrovich.rate_hw(petya, 'Git', 8)
petrovich.rate_hw(petya, 'Git', 7)
katya.rate_lt(eduard, 'Python', 10)
katya.rate_lt(eduard, 'Python', 9)
katya.rate_lt(veniamin, 'Git', 5)
katya.rate_lt(veniamin, 'Git', 6)
petya.rate_lt(eduard, 'Python', 7)
petya.rate_lt(eduard, 'Python', 6)
petya.rate_lt(veniamin, 'Git', 4)
petya.rate_lt(veniamin, 'Git', 6)


print(katya)
print(petya)
print(veniamin)
print(eduard)
print(ivanovich)
print(petrovich)


st_list = [katya, petya]
lt_list = [eduard, veniamin]

def student_course_grade(students, course):
    gradeslist = []
    for student in students:
        for k, v in student.grades.items():
            if k == course:
                gradeslist += student.grades[course]
    av_grade = sum(gradeslist) / len(gradeslist)
    return av_grade

def lecturer_course_grade(lecturers, course):
    gradeslist = []
    for lecturer in lecturers:
        for k, v in lecturer.grades.items():
            if k == course:
                gradeslist += lecturer.grades[course]
    av_grade = sum(gradeslist) / len(gradeslist)
    return av_grade


print(student_course_grade(st_list, 'Python'))
print(lecturer_course_grade(lt_list, 'Git'))


print(veniamin > eduard)
print(katya > petya)