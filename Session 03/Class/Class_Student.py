import database as db


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def save(self):
        db.append_student(self.name, self.student_id)

    def add_grade(self, student_id, course, grade):
        if grade < 0 or grade > 20:
            print("Invalid grade")
            return
        db.update_grade(student_id, course, grade)

    # ---------- خواندن داده‌ی به‌روز از دیتابیس ----------
    def _data(self):
        return db.find_student(self.student_id)

    def average(self):
        return db.student_average(self.student_id)

    def best_course(self):
        s = self._data()
        if not s or not s["grades"]:
            return None
        return max(s["grades"], key=s["grades"].get)

    def failed_courses(self):
        s = self._data()
        if not s:
            return []
        return [course for course, grade in s["grades"].items() if grade < 10]

    def status(self):
        avg = self.average()
        if avg >= 17:
            return "Excellent"
        if avg >= 14:
            return "Good"
        if avg >= 12:
            return "Normal"
        return "Probation"

    def report(self):
        s = self._data()
        if not s:
            print(f"Student with ID {self.student_id} not found.")
            return
        print(f"Student: {s['name']} (ID: {s['student_id']})")
        for course, grade in s["grades"].items():
            print(f"{course}: {grade}")
        print(f"Average: {self.average()}")
        print(f"Best course: {self.best_course()}")
        print(f"Failed courses: {self.failed_courses()}")
        print(f"Status: {self.status()}")