
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
            student_inf = f'''Имя: {self.name} 
    Фамилия: {self.surname} 
    Средняя оценка за домашние задания: {_av_hw_}
    Курсы в процессе изучения: {self.courses_in_progress}
    Завершенные курсы: {self.finished_courses}'''
            return student_inf

        def _av_hw_(self):
            hw_list = []
            for k,v in self.grades.items():
                hw_list.append(v)
            return sum(hw_list) / len(hw_list)



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
Средняя оценка за лекции: {av_lt}'''
        return lect_inf


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



katya = Student('Ekaterina', 'Sinitsyna', 'female')
katya.courses_in_progress += ['Python']

petya = Student('Pyotr', 'Skvortsov', 'male')
katya.courses_in_progress += ['Python']

ivanovich = Reviewer('Ivan', 'Petrov')
ivanovich.courses_attached += ['Python']

petrovich = Reviewer('Petr', 'Petrov')
ivanovich.courses_attached += ['Python']

eduard = Lecturer('Eduard', 'Khramov')
eduard.courses_attached += ['Python']

veniamin = Lecturer('Veniamin', 'Bogoyavlenskiy')
veniamin.courses_attached += ['Python']

ivanovich.rate_hw(katya, 'Python', 10)

katya.rate_lt(eduard, 'Python', 10)


# print(katya.grades)
av_lt = 5
print(veniamin)