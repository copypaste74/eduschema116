import mysql.connector
from datetime import datetime
from utils import connect_to_database


def add_course():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            course_name = input("Enter course name: ")
            course_description = input("Enter course description: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            course_fee = float(input("Enter course fee: "))

            query = """
            INSERT INTO Courses (course_name, course_description, start_date, end_date, course_fee)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (course_name, course_description, start_date, end_date, course_fee))
            connection.commit()
            print("Course added successfully")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def update_course():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            course_id = int(input("Enter course ID to update: "))
            new_course_name = input("Enter new course name: ")
            new_course_description = input("Enter new course description: ")
            new_start_date = input("Enter new start date (YYYY-MM-DD): ")
            new_end_date = input("Enter new end date (YYYY-MM-DD): ")
            new_course_fee = float(input("Enter new course fee: "))

            query = """
            UPDATE Courses
            SET course_name = %s, course_description = %s, start_date = %s, end_date = %s, course_fee = %s
            WHERE course_id = %s
            """
            cursor.execute(query, (new_course_name, new_course_description, new_start_date, new_end_date, new_course_fee, course_id))
            connection.commit()
            print(f"Course with ID {course_id} updated successfully.")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def remove_course():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            course_id = int(input("Enter course ID to delete: "))

            query = """
            UPDATE Courses
            SET is_deleted = TRUE, deleted_at = %s
            WHERE course_id = %s
            """
            deleted_at = datetime.now()
            cursor.execute(query, (deleted_at, course_id))
            connection.commit()
            print(f"Course with ID {course_id} deleted successfully.")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def search_courses():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            search_term = input("Enter course name to search: ")
            query = """
            SELECT * FROM Courses
            WHERE course_name LIKE %s AND is_deleted = FALSE
            """
            cursor.execute(query, (f"%{search_term}%",))
            courses = cursor.fetchall()

            if not courses:
                print("No courses found.")
            else:
                print("\nSearch Results:")
                print("{:<5} {:<20} {:<30} {:<12} {:<12} {:<10}".format(
                    "ID", "Name", "Description", "Start Date", "End Date", "Fee"
                ))
                print("="*100)
                for course in courses:
                    course_id, course_name, course_description, start_date, end_date, course_fee, is_deleted, deleted_at = course
                    print("{:<5} {:<20} {:<30} {:<12} {:<12} {:<10}".format(
                        course_id, course_name, course_description, start_date, end_date, course_fee
                    ))

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def sort_courses():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            sort_by = input("Enter field to sort by (name, start_date, end_date, fee): ")
            query = f"""
            SELECT course_id, course_name, course_description, start_date, end_date, course_fee, is_deleted, deleted_at
            FROM Courses
            WHERE is_deleted = FALSE
            ORDER BY {sort_by}
            """
            cursor.execute(query)
            courses = cursor.fetchall()

            if not courses:
                print("No courses found.")
            else:
                print("\nSorted Course List:")
                print("{:<5} {:<20} {:<30} {:<12} {:<12} {:<10}".format(
                    "ID", "Name", "Description", "Start Date", "End Date", "Fee"
                ))
                print("="*100)
                for course in courses:
                    course_id, course_name, course_description, start_date, end_date, course_fee, is_deleted, deleted_at = course
                    print("{:<5} {:<20} {:<30} {:<12} {:<12} {:<10}".format(
                        course_id, course_name, course_description, start_date, end_date, course_fee
                    ))

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


def add_instructor():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            instructor_name = input("Enter instructor name: ")
            instructor_email = input("Enter instructor email: ")

            query = """
            INSERT INTO Instructors (instructor_name, instructor_email)
            VALUES (%s, %s)
            """
            cursor.execute(query, (instructor_name, instructor_email))
            connection.commit()
            print("Instructor added successfully")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def update_instructor():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            instructor_id = int(input("Enter instructor ID to update: "))
            new_instructor_name = input("Enter new instructor name: ")
            new_instructor_email = input("Enter new instructor email: ")

            query = """
            UPDATE Instructors
            SET instructor_name = %s, instructor_email = %s
            WHERE instructor_id = %s
            """
            cursor.execute(query, (new_instructor_name, new_instructor_email, instructor_id))
            connection.commit()
            print(f"Instructor with ID {instructor_id} updated successfully.")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def remove_instructor():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            instructor_id = int(input("Enter instructor ID to delete: "))

            query = """
            DELETE FROM Instructors
            WHERE instructor_id = %s
            """
            cursor.execute(query, (instructor_id,))
            connection.commit()
            print(f"Instructor with ID {instructor_id} deleted successfully.")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def search_instructors():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            search_term = input("Enter instructor name or email to search: ")
            query = """
            SELECT * FROM Instructors
            WHERE instructor_name LIKE %s OR instructor_email LIKE %s
            """
            cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))
            instructors = cursor.fetchall()

            if not instructors:
                print("No instructors found.")
            else:
                print("\nSearch Results:")
                print("{:<5} {:<20} {:<30}".format(
                    "ID", "Name", "Email"
                ))
                print("="*60)
                for instructor in instructors:
                    instructor_id, instructor_name, instructor_email = instructor
                    print("{:<5} {:<20} {:<30}".format(
                        instructor_id, instructor_name, instructor_email
                    ))

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")



def enroll_student():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            student_name = input("Enter student name: ")
            student_email = input("Enter student email: ")

            query = """
            INSERT INTO Students (student_name, student_email)
            VALUES (%s, %s)
            """
            cursor.execute(query, (student_name, student_email))
            connection.commit()
            print("Student enrolled successfully")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def view_enrollments():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            course_id = int(input("Enter course ID to view enrollments: "))

            query = """
            SELECT Students.student_id, Students.student_name, Students.student_email
            FROM Enrollments
            INNER JOIN Students ON Enrollments.student_id = Students.student_id
            WHERE Enrollments.course_id = %s
            """
            cursor.execute(query, (course_id,))
            enrollments = cursor.fetchall()

            if not enrollments:
                print("No enrollments found for this course.")
            else:
                print("\nEnrollments:")
                print("{:<5} {:<20} {:<30}".format(
                    "ID", "Name", "Email"
                ))
                print("="*60)
                for enrollment in enrollments:
                    student_id, student_name, student_email = enrollment
                    print("{:<5} {:<20} {:<30}".format(
                        student_id, student_name, student_email
                    ))

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")



def add_assessment():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            course_id = int(input("Enter course ID: "))
            assessment_name = input("Enter assessment name: ")

            query = """
            INSERT INTO Assessments (course_id, assessment_name)
            VALUES (%s, %s)
            """
            cursor.execute(query, (course_id, assessment_name))
            connection.commit()
            print("Assessment added successfully")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def view_assessments():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            course_id = int(input("Enter course ID to view assessments: "))

            query = """
            SELECT * FROM Assessments
            WHERE course_id = %s
            """
            cursor.execute(query, (course_id,))
            assessments = cursor.fetchall()

            if not assessments:
                print("No assessments found for this course.")
            else:
                print("\nAssessments:")
                print("{:<5} {:<20} {:<30}".format(
                    "ID", "Course ID", "Assessment Name"
                ))
                print("="*60)
                for assessment in assessments:
                    assessment_id, course_id, assessment_name = assessment
                    print("{:<5} {:<20} {:<30}".format(
                        assessment_id, course_id, assessment_name
                    ))

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def input_grades():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            student_id = int(input("Enter student ID: "))
            assessment_id = int(input("Enter assessment ID: "))
            grade = float(input("Enter grade: "))

            query = """
            INSERT INTO Grades (student_id, assessment_id, grade)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query, (student_id, assessment_id, grade))
            connection.commit()
            print("Grade added successfully")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def view_grades():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            student_id = int(input("Enter student ID to view grades: "))

            query = """
            SELECT Assessments.assessment_name, Grades.grade
            FROM Grades
            INNER JOIN Assessments ON Grades.assessment_id = Assessments.assessment_id
            WHERE Grades.student_id = %s
            """
            cursor.execute(query, (student_id,))
            grades = cursor.fetchall()

            if not grades:
                print("No grades found for this student.")
            else:
                print("\nGrades:")
                print("{:<30} {:<10}".format(
                    "Assessment Name", "Grade"
                ))
                print("="*50)
                for grade in grades:
                    assessment_name, grade_value = grade
                    print("{:<30} {:<10}".format(
                        assessment_name, grade_value
                    ))

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


def display_deleted_records_log():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
            SELECT * FROM DeletedRecordsLog
            """
            cursor.execute(query)
            deleted_records = cursor.fetchall()

            if not deleted_records:
                print("No deleted records found.")
            else:
                print("\nDeleted Records Log:")
                print("{:<10} {:<20} {:<30} {:<30}".format(
                    "Table", "Record ID", "Deleted At", "Deleted By"
                ))
                print("="*100)
                for record in deleted_records:
                    print(record)

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


def log_deleted_record(table_name, record_id, deleted_by):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            deleted_at = datetime.now()
            query = """
            INSERT INTO DeletedRecordsLog (table_name, record_id, deleted_at, deleted_by)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (table_name, record_id, deleted_at, deleted_by))
            connection.commit()
            print("Deleted record logged successfully.")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def remove_course():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            course_id = int(input("Enter course ID to delete: "))

            query = """
            UPDATE Courses
            SET is_deleted = TRUE, deleted_at = %s
            WHERE course_id = %s
            """
            deleted_at = datetime.now()
            cursor.execute(query, (deleted_at, course_id))
            connection.commit()
            
            log_deleted_record('Courses', course_id, 'Admin') 

            print(f"Course with ID {course_id} deleted successfully.")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    while True:
        print("\n=== EduSchema - Online Learning Platform ===")
        print("1. Course Management")
        print("2. Instructor Management")
        print("3. Student Enrollment")
        print("4. Assessment and Grades")
        print("5. Display Deleted Records Log")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n=== Course Management ===")
            print("a. Add Course")
            print("b. Update Course")
            print("c. Remove Course")
            option = input("Enter your option: ")

            if option == "a":
                add_course()
            elif option == "b":
                update_course()
            elif option == "c":
                remove_course()
            else:
                print("Invalid option. Please try again.")

        elif choice == "2":
            print("\n=== Instructor Management ===")
            print("a. Add Instructor")
            print("b. Update Instructor")
            print("c. Remove Instructor")
            option = input("Enter your option: ")

            if option == "a":
                add_instructor()
            elif option == "b":
                update_instructor()
            elif option == "c":
                remove_instructor()
            else:
                print("Invalid option. Please try again.")

        elif choice == "3":
            print("\n=== Student Enrollment ===")
            print("a. Enroll Student")
            print("b. View Enrollments")
            option = input("Enter your option: ")

            if option == "a":
                enroll_student()
            elif option == "b":
                view_enrollments()
            else:
                print("Invalid option. Please try again.")

        elif choice == "4":
            print("\n=== Assessment and Grades ===")
            print("a. Add Assessment")
            print("b. View Assessments")
            print("c. Input Grades")
            print("d. View Grades")
            option = input("Enter your option: ")

            if option == "a":
                add_assessment()
            elif option == "b":
                view_assessments()
            elif option == "c":
                input_grades()
            elif option == "d":
                view_grades()
            else:
                print("Invalid option. Please try again.")

        elif choice == "5":
            print("\n=== Deleted Records Log ===")
            display_deleted_records_log()

        elif choice == "6":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-6).")