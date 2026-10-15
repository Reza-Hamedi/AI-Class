import json
import os

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")


def _load():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


students_data = _load()


def save():
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(students_data, f, ensure_ascii=False, indent=4)


def find_student(student_id):
    for s in students_data:
        if s["student_id"] == student_id:
            return s
    return None


def append_student(name, student_id):
    if find_student(student_id):
        print(f"Student with ID {student_id} already exists.")
        return False
    students_data.append({
        "name": name,
        "student_id": student_id,
        "grades": {}
    })
    save()
    return True


def update_grade(student_id, course, grade):
    s = find_student(student_id)
    if not s:
        print(f"Student with ID {student_id} not found.")
        return False
    s["grades"][course] = grade
    save()
    return True


def student_average(student_id):
    s = find_student(student_id)
    if not s or not s["grades"]:
        return 0
    return sum(s["grades"].values()) / len(s["grades"])