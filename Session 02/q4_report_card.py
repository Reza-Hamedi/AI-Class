import numpy as np
import collections

student_scores = {
    "Ali": 8, "Sara": 20, "Reza": 20, "Mina": 14, "Omid": 11.5,
    "Nima": 20, "Arman": 16, "Parisa": 18.5, "Sina": 7, "Negar": 15,
    "Amir": 12, "Zahra": 19, "Pouya": 10, "Maryam": 17, "Hamed": 6.5,
    "Neda": 13, "Kian": 20, "Shirin": 8.5, "Milad": 14.5, "Yasmin": 16,
    "Farhad": 9.5, "Elham": 18, "Navid": 11, "Sahar": 7.5, "Babak": 15.5,
    "Roya": 12.5, "Saman": 19.5, "Leila": 5, "Peyman": 13.5, "Ava": 17.5,
    "Dariush": 10.5, "Tara": 6, "Shayan": 14, "Kimia": 18.5, "Mahdi": 20
}


class class_manager:

    def __init__(self, student_scores):
            self.student_scores = student_scores

    def highest_score(self):
        score = np.max(list(self.student_scores.values()))
        bestStudents = []
        for k, v in self.student_scores.items():
            if v == score: bestStudents.append(k)
        if len(bestStudents) > 1:
            print(f"Best Students List: {','.join(bestStudents)}")
        else:
            print(f"The best : {k}")

    def class_status_report(self):
        socre_list = list(self.student_scores.values())
        Mean = np.mean(socre_list)
        Median = np.median(socre_list)
        Standard_deviation = np.std(socre_list)
        Variance = np.var(socre_list)
        Minimum_value = np.min(socre_list)
        Maximum_value = np.max(socre_list)
        print(f'''
               Class Mean (Average) is : {Mean}     
               Class Median is : {Median}     
               Class Standard deviation is : {Standard_deviation}     
               Class Variance is : {Variance}     
               Class Minimum Score is : {Minimum_value}     
               Class Maximum Score is : {Maximum_value}     
        ''')


    def students_who_passed(self):
        passed_students = []
        for key, value in self.student_scores.items():
            if value >= 10: passed_students.append(key)
        print(f"students who passed: {'-'.join(passed_students)}")

    def grading(self):
        grade = ""
        for key, value in self.student_scores.items():
            if 17 <= value <= 20:
                grade = "Perfect (A+)"
            elif 14 <= value < 17:
                grade = "Good (B+)"
            elif 10 <= value < 14:
                grade = "Acceptable (C)"
            elif 0 <= value < 10:
                grade = "failed (C-)"
            print(f"Student Name: {key}\tStudent Score: {value}\t Student Grade: {grade}")

Manager = class_manager(collections.OrderedDict(sorted(student_scores.items())))
Manager.grading()
print("#"*40)
Manager.students_who_passed()
print("$"*40)
Manager.class_status_report()
print("&"*40)
Manager.highest_score()