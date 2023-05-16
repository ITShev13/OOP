class Student:
    # student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        # self.student_list.append(self)
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 


    def rate_Lecturer(self, lecturer, course, grede):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.gradel:
                lecturer.gradel[course] += [grede]
            else:
                lecturer.gradel[course] = [grede]
        else:
            return 'Ошибка'
        

    def _average_rating_s(self): #средняя оценка за домашнее задание
        sum_grade = 0
        len_grade = 0
        for courses, grad in self.grades.items():
            for value in grad:
                sum_grade += value
            len_grade += len(grad)
        if len_grade == 0:
            return 'Оценок нет'
        else:
            return round(sum_grade/len_grade, 1)
        

    def average_rating_cours_s(self, cours): # оценки по курсу и их количество
        sum_grade_cours = 0
        len_grade_cours = 0
        for courses, grad in self.grades.items():
            if cours == courses:
                sum_grade_cours += sum(self.grades[courses])
                len_grade_cours += len(self.grades[courses])
        return sum_grade_cours, len_grade_cours



    
    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашнии задания: {self._average_rating_s()}\n" \
              f"Курс в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
              f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return res

    def __lt__(self, other): # сравнение студентов по средней оценке за домашнее задание
        if not isinstance(other, Student):
            print('Не относиться к классу Student')
            return
        return self._average_rating_s() < other._average_rating_s() 
    



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.gradel = {}

    # делаем защищенный метод для вычесления средней оценки за лекции
    def _average_rating_l(self):
        sum_grade = 0
        len_grade = 0
        for cours, grad in self.gradel.items():
            for value in grad:
                sum_grade += value
            len_grade += len(grad)
        return round(sum_grade/len_grade, 1)
    
    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за лекции: {self._average_rating_l()}"
        return res

    def __lt__(self, other): # сравнение лекторов по средней оценке за лекции
        if not isinstance(other, Lecturer):
            print('Не относиться к классу Lecturer')
            return
        return self._average_rating_l() < other._average_rating_l()

    def average_rating_cours_l(self, cours): # оценки за лекции и их количество
        sum_grade_cours_l = 0
        len_grade_cours_l = 0
        for courses, grad in self.gradel.items():
            if cours == courses:
                sum_grade_cours_l += sum(self.gradel[courses])
                len_grade_cours_l += len(self.gradel[courses])
        return sum_grade_cours_l, len_grade_cours_l


    


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
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res
    
    



print('Проверяем работу программы')
print()

# создаем первого студента
student_1 = Student('Иван', 'Иванов', 'Boy')
student_1.finished_courses += ['1c']
student_1.courses_in_progress += ['Python', 'Git']

# создаем второго студента
student_2 = Student('Ирина', 'Дон', 'girl')
student_2.finished_courses += ['C+', 'Java']
student_2.courses_in_progress += ['Python', 'Git', 'JS']


#создаем первого лектора
lecturer_1 = Lecturer('Надежда', 'Дементьева')
lecturer_1.courses_attached += ['Git', 'JS']

#создаем второго лектора
lecturer_2 = Lecturer('Евгений', 'Смирнов')
lecturer_2.courses_attached += ['Python', 'Git', 'JS']


#созаем первого ревьювера
reviewer_1 = Reviewer('Дмитрий', 'Петров')
reviewer_1.courses_attached += ['Python', 'Git']

#создаем второго ревьювера
reviewer_2 = Reviewer('Алксандр', 'Сидоров')
reviewer_2.courses_attached += ['Python', 'Git', 'JS']


#ревьюеры выставляют оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Git', 5)

reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'JS', 5)

#студенты выставляют оценки за лекции вротому лектору
student_1.rate_Lecturer(lecturer_2, 'Git', 8)
student_1.rate_Lecturer(lecturer_2, 'Python', 10)

student_2.rate_Lecturer(lecturer_2, 'Git', 9)
student_2.rate_Lecturer(lecturer_2, 'Python', 6)
student_2.rate_Lecturer(lecturer_2, 'JS', 10)

# студенты выставляют оценки за лекции первому лектору
student_1.rate_Lecturer(lecturer_1, 'Git', 10)
student_1.rate_Lecturer(lecturer_1, 'JS', 6)

student_2.rate_Lecturer(lecturer_1, 'Git', 9)
student_2.rate_Lecturer(lecturer_1, 'JS', 7)

print('Информация по 1-му ревьюверу')
print(reviewer_1)
print()

print('Информация по 2-му ревьюверу')
print(reviewer_2)
print()

print('Информация по 1-му лектору')
print(lecturer_1)
print()

print('Информация по 2-му лектору')
print(lecturer_2)
print()

print('Информация по 1-му студенту')
print(student_1)
print()

print('Информация по 2-му студенту')
print(student_2)
print()


student_list = [student_1, student_2]
lect_list = [lecturer_1, lecturer_2]
lect_list2 = [lecturer_2]


# Средняя оценка за домашнии задания по всем студентам по курсу
def average_rating_all_s(course, student_list):
    sum_grade_all_s = 0
    len_grade_all_s = 0
    for std in student_list:
        if isinstance(std, Student) and course in std.courses_in_progress or course in std.finished_courses:
            sum_grade_all_s += std.average_rating_cours_s(course)[0]
            len_grade_all_s += std.average_rating_cours_s(course)[1]
        else:
            return f'{std.surname} {std.name} не изучает курс {course} (необходимо изменить список студентов)'
            # return 'Введены неверные данные'
    return round(sum_grade_all_s/len_grade_all_s, 1)

print('Средняя оценка за домашнии задания по всем студентам:')
print('Python:',average_rating_all_s('Python', student_list))
print('Git:', average_rating_all_s('Git', student_list))
print('SMM:',average_rating_all_s('SMM', student_list))
print()

# Средняя оценка за лекции всех лекторов в рамках курса
def average_rating_all_l(course, lecturer_list):
    sum_grade_all_l = 0
    len_grade_all_l = 0
    for lct in lecturer_list:
        if isinstance(lct, Lecturer) and course in lct.courses_attached:
            sum_grade_all_l += lct.average_rating_cours_l(course)[0]
            len_grade_all_l += lct.average_rating_cours_l(course)[1]
        else:
            return f'{lct.surname} {lct.name} не ведет лекции по курсу {course} (необходимо изменить список лекторов)'
            # return 'Введены неверные данные'
    return round(sum_grade_all_l/len_grade_all_l, 1)

print('Средняя оценка за лекции всех лекторов в рамках курса:')
print('JS:', average_rating_all_l('JS', lect_list))
print('Git:',average_rating_all_l('Git', lect_list))
print('Python:',average_rating_all_l('Python', lect_list))
print()

print('сравнение студентов по средней оценке')
print('студент1 > студента2:', student_1 > student_2)
print('студент2 > студента1:', student_2 > student_1)
print('лектор1 > студента2:', lecturer_1 > student_2)
print()

print('сравнение лекторов по средней оценке')
print('лектор1 > лектора2:', lecturer_1 > lecturer_2)
print('лектор2 > лектора1:', lecturer_2 > lecturer_1)
print('лектор2 > студента1:', lecturer_2 > student_1)