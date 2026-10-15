from Class_Student import Student
from Class_Classroom import Classroom


def main():
    # ---------- ساخت کلاس ----------
    classroom = Classroom()

    # ---------- ساخت و ذخیره‌ی دو دانشجو ----------
    sara = Student("Sara Ahmadi", "40312345")
    ali  = Student("Ali Rezaei", "40367890")

    classroom.add_student(sara)
    classroom.add_student(ali)

    # ---------- ثبت نمرات برای سارا ----------
    sara.add_grade("40312345", "Math", 18)
    sara.add_grade("40312345", "Physics", 9)
    sara.add_grade("40312345", "Programming", 20)
    sara.add_grade("40312345", "English", 15)

    # ---------- ثبت نمرات برای علی ----------
    ali.add_grade("40367890", "Math", 13)
    ali.add_grade("40367890", "Physics", 16)
    ali.add_grade("40367890", "Programming", 11)
    ali.add_grade("40367890", "English", 17)

    # ---------- کارنامه‌ها ----------
    print("=" * 40)
    sara.report()
    print("=" * 40)
    ali.report()
    print("=" * 40)

    # ---------- تست نمره‌ی نامعتبر ----------
    print("\n--- Testing invalid grade ---")
    sara.add_grade("40312345", "Chemistry", 25)  # باید Invalid grade چاپ کنه
    print("=" * 40)

    # ---------- تست Classroom ----------
    print("\n--- Classroom stats ---")
    top = classroom.top_student()
    if top:
        print(f"Top student: {top.name} (ID: {top.student_id})")

    class_avg = classroom.class_average()
    print(f"Class average: {class_avg:.2f}")


if __name__ == "__main__":
    main()