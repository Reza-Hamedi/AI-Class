import database as db
from Class_Student import Student


class Classroom:
    def add_student(self, student):
        """دانشجو رو مستقیم می‌ریزه توی دیتابیس"""
        db.append_student(student.name, student.student_id)

    def top_student(self):
        if not db.students_data:
            return None
        best = max(db.students_data, key=lambda s: db.student_average(s["student_id"]))
        return Student(best["name"], best["student_id"])

    def class_average(self):
        if not db.students_data:
            return 0
        averages = [db.student_average(s["student_id"]) for s in db.students_data]
        return sum(averages) / len(averages)