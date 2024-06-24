import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import mysql.connector
from utils import connect_to_database  

def add_course_gui():
    def add_course_to_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                course_name = course_name_entry.get()
                course_description = course_description_entry.get()
                start_date = start_date_entry.get()
                end_date = end_date_entry.get()
                course_fee = float(course_fee_entry.get())

                query = """
                INSERT INTO Courses (course_name, course_description, start_date, end_date, course_fee)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, (course_name, course_description, start_date, end_date, course_fee))
                connection.commit()
                messagebox.showinfo("Success", "Course added successfully")
                cursor.close()
                connection.close()
                add_course_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    add_course_window = tk.Toplevel()
    add_course_window.title("Add Course")

    tk.Label(add_course_window, text="Course Name:").grid(row=0, column=0, padx=10, pady=5)
    course_name_entry = tk.Entry(add_course_window)
    course_name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_course_window, text="Course Description:").grid(row=1, column=0, padx=10, pady=5)
    course_description_entry = tk.Entry(add_course_window)
    course_description_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_course_window, text="Start Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
    start_date_entry = tk.Entry(add_course_window)
    start_date_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(add_course_window, text="End Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
    end_date_entry = tk.Entry(add_course_window)
    end_date_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(add_course_window, text="Course Fee:").grid(row=4, column=0, padx=10, pady=5)
    course_fee_entry = tk.Entry(add_course_window)
    course_fee_entry.grid(row=4, column=1, padx=10, pady=5)

    add_button = tk.Button(add_course_window, text="Add Course", command=add_course_to_db)
    add_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    add_course_window.mainloop()

# Function to update a course
def update_course_gui():
    def update_course_in_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                course_id = int(course_id_entry.get())
                new_course_name = new_course_name_entry.get()
                new_course_description = new_course_description_entry.get()
                new_start_date = new_start_date_entry.get()
                new_end_date = new_end_date_entry.get()
                new_course_fee = float(new_course_fee_entry.get())

                query = """
                UPDATE Courses
                SET course_name = %s, course_description = %s, start_date = %s, end_date = %s, course_fee = %s
                WHERE course_id = %s
                """
                cursor.execute(query, (new_course_name, new_course_description, new_start_date, new_end_date, new_course_fee, course_id))
                connection.commit()
                messagebox.showinfo("Success", f"Course with ID {course_id} updated successfully.")
                cursor.close()
                connection.close()
                update_course_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    update_course_window = tk.Toplevel()
    update_course_window.title("Update Course")

    tk.Label(update_course_window, text="Course ID to Update:").grid(row=0, column=0, padx=10, pady=5)
    course_id_entry = tk.Entry(update_course_window)
    course_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(update_course_window, text="New Course Name:").grid(row=1, column=0, padx=10, pady=5)
    new_course_name_entry = tk.Entry(update_course_window)
    new_course_name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(update_course_window, text="New Course Description:").grid(row=2, column=0, padx=10, pady=5)
    new_course_description_entry = tk.Entry(update_course_window)
    new_course_description_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(update_course_window, text="New Start Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
    new_start_date_entry = tk.Entry(update_course_window)
    new_start_date_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(update_course_window, text="New End Date (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5)
    new_end_date_entry = tk.Entry(update_course_window)
    new_end_date_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(update_course_window, text="New Course Fee:").grid(row=5, column=0, padx=10, pady=5)
    new_course_fee_entry = tk.Entry(update_course_window)
    new_course_fee_entry.grid(row=5, column=1, padx=10, pady=5)

    update_button = tk.Button(update_course_window, text="Update Course", command=update_course_in_db)
    update_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    update_course_window.mainloop()

# Function to remove a course
def remove_course_gui():
    def remove_course_from_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                course_id = int(course_id_entry.get())

                query = """
                UPDATE Courses
                SET is_deleted = TRUE, deleted_at = %s
                WHERE course_id = %s
                """
                deleted_at = datetime.now()
                cursor.execute(query, (deleted_at, course_id))
                connection.commit()
                log_deleted_record('Courses', course_id, 'Admin')  # Log deletion
                messagebox.showinfo("Success", f"Course with ID {course_id} deleted successfully.")
                cursor.close()
                connection.close()
                remove_course_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    remove_course_window = tk.Toplevel()
    remove_course_window.title("Remove Course")

    tk.Label(remove_course_window, text="Course ID to Remove:").grid(row=0, column=0, padx=10, pady=5)
    course_id_entry = tk.Entry(remove_course_window)
    course_id_entry.grid(row=0, column=1, padx=10, pady=5)

    remove_button = tk.Button(remove_course_window, text="Remove Course", command=remove_course_from_db)
    remove_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    remove_course_window.mainloop()

# Function to search for courses
def search_courses_gui():
    def search_courses_in_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                search_term = search_term_entry.get()
                query = """
                SELECT * FROM Courses
                WHERE course_name LIKE %s AND is_deleted = FALSE
                """
                cursor.execute(query, (f"%{search_term}%",))
                courses = cursor.fetchall()

                if not courses:
                    messagebox.showinfo("No Courses", "No courses found.")
                else:
                    search_result_window = tk.Toplevel()
                    search_result_window.title("Search Results: Courses")

                    tk.Label(search_result_window, text="Search Results:").grid(row=0, column=0, columnspan=2, padx=10, pady=5)
                    tk.Label(search_result_window, text="{:<5} {:<20} {:<30} {:<12} {:<12} {:<10}".format(
                        "ID", "Name", "Description", "Start Date", "End Date", "Fee"
                    )).grid(row=1, column=0, padx=10, pady=5)
                    tk.Label(search_result_window, text="="*100).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

                    for idx, course in enumerate(courses, start=3):
                        course_id, course_name, course_description, start_date, end_date, course_fee, is_deleted, deleted_at = course
                        tk.Label(search_result_window, text="{:<5} {:<20} {:<30} {:<12} {:<12} {:<10}".format(
                            course_id, course_name, course_description, start_date, end_date, course_fee                            )).grid(row=idx, column=0, columnspan=2, padx=10, pady=5)

                    cursor.close()
                    connection.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    search_courses_window = tk.Toplevel()
    search_courses_window.title("Search Courses")

    tk.Label(search_courses_window, text="Enter Course Name to Search:").grid(row=0, column=0, padx=10, pady=5)
    search_term_entry = tk.Entry(search_courses_window)
    search_term_entry.grid(row=0, column=1, padx=10, pady=5)

    search_button = tk.Button(search_courses_window, text="Search Courses", command=search_courses_in_db)
    search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    search_courses_window.mainloop()

# Function to display sorted courses
def sort_courses_gui():
    def sort_courses_in_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                sort_by = sort_by_var.get()
                query = f"""
                SELECT course_id, course_name, course_description, start_date, end_date, course_fee, is_deleted, deleted_at
                FROM Courses
                WHERE is_deleted = FALSE
                ORDER BY {sort_by}
                """
                cursor.execute(query)
                courses = cursor.fetchall()

                if not courses:
                    messagebox.showinfo("No Courses", "No courses found.")
                else:
                    sort_result_window = tk.Toplevel()
                    sort_result_window.title("Sorted Course List")

                    tk.Label(sort_result_window, text="Sorted Course List:").grid(row=0, column=0, columnspan=2, padx=10, pady=5)
                    tk.Label(sort_result_window, text="{:<5} {:<20} {:<30} {:<12} {:<12} {:<10}".format(
                        "ID", "Name", "Description", "Start Date", "End Date", "Fee"
                    )).grid(row=1, column=0, padx=10, pady=5)
                    tk.Label(sort_result_window, text="="*100).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

                    for idx, course in enumerate(courses, start=3):
                        course_id, course_name, course_description, start_date, end_date, course_fee, is_deleted, deleted_at = course
                        tk.Label(sort_result_window, text="{:<5} {:<20} {:<30} {:<12} {:<12} {:<10}".format(
                            course_id, course_name, course_description, start_date, end_date, course_fee
                        )).grid(row=idx, column=0, columnspan=2, padx=10, pady=5)

                    cursor.close()
                    connection.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    sort_courses_window = tk.Toplevel()
    sort_courses_window.title("Sort Courses")

    tk.Label(sort_courses_window, text="Sort by Field:").grid(row=0, column=0, padx=10, pady=5)
    sort_by_var = tk.StringVar(sort_courses_window)
    sort_by_var.set("course_name")  # Default value

    sort_by_options = ["course_name", "start_date", "end_date", "course_fee"]
    sort_by_dropdown = tk.OptionMenu(sort_courses_window, sort_by_var, *sort_by_options)
    sort_by_dropdown.grid(row=0, column=1, padx=10, pady=5)

    sort_button = tk.Button(sort_courses_window, text="Sort Courses", command=sort_courses_in_db)
    sort_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    sort_courses_window.mainloop()

# Function to add a new instructor
def add_instructor_gui():
    def add_instructor_to_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                instructor_name = instructor_name_entry.get()
                instructor_email = instructor_email_entry.get()

                query = """
                INSERT INTO Instructors (instructor_name, instructor_email)
                VALUES (%s, %s)
                """
                cursor.execute(query, (instructor_name, instructor_email))
                connection.commit()
                messagebox.showinfo("Success", "Instructor added successfully")
                cursor.close()
                connection.close()
                add_instructor_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    add_instructor_window = tk.Toplevel()
    add_instructor_window.title("Add Instructor")

    tk.Label(add_instructor_window, text="Instructor Name:").grid(row=0, column=0, padx=10, pady=5)
    instructor_name_entry = tk.Entry(add_instructor_window)
    instructor_name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_instructor_window, text="Instructor Email:").grid(row=1, column=0, padx=10, pady=5)
    instructor_email_entry = tk.Entry(add_instructor_window)
    instructor_email_entry.grid(row=1, column=1, padx=10, pady=5)

    add_button = tk.Button(add_instructor_window, text="Add Instructor", command=add_instructor_to_db)
    add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    add_instructor_window.mainloop()

def update_instructor_gui():
    def update_instructor_in_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                instructor_id = int(instructor_id_entry.get())
                new_instructor_name = new_instructor_name_entry.get()
                new_instructor_email = new_instructor_email_entry.get()

                query = """
                UPDATE Instructors
                SET instructor_name = %s, instructor_email = %s
                WHERE instructor_id = %s
                """
                cursor.execute(query, (new_instructor_name, new_instructor_email, instructor_id))
                connection.commit()
                messagebox.showinfo("Success", f"Instructor with ID {instructor_id} updated successfully.")
                cursor.close()
                connection.close()
                update_instructor_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    update_instructor_window = tk.Toplevel()
    update_instructor_window.title("Update Instructor")

    tk.Label(update_instructor_window, text="Instructor ID to Update:").grid(row=0, column=0, padx=10, pady=5)
    instructor_id_entry = tk.Entry(update_instructor_window)
    instructor_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(update_instructor_window, text="New Instructor Name:").grid(row=1, column=0, padx=10, pady=5)
    new_instructor_name_entry = tk.Entry(update_instructor_window)
    new_instructor_name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(update_instructor_window, text="New Instructor Email:").grid(row=2, column=0, padx=10, pady=5)
    new_instructor_email_entry = tk.Entry(update_instructor_window)
    new_instructor_email_entry.grid(row=2, column=1, padx=10, pady=5)

    update_button = tk.Button(update_instructor_window, text="Update Instructor", command=update_instructor_in_db)
    update_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    update_instructor_window.mainloop()

def remove_instructor_gui():
    def remove_instructor_from_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                instructor_id = int(instructor_id_entry.get())

                query = """
                DELETE FROM Instructors
                WHERE instructor_id = %s
                """
                cursor.execute(query, (instructor_id,))
                connection.commit()
                messagebox.showinfo("Success", f"Instructor with ID {instructor_id} deleted successfully.")
                cursor.close()
                connection.close()
                remove_instructor_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    remove_instructor_window = tk.Toplevel()
    remove_instructor_window.title("Remove Instructor")

    tk.Label(remove_instructor_window, text="Instructor ID to Remove:").grid(row=0, column=0, padx=10, pady=5)
    instructor_id_entry = tk.Entry(remove_instructor_window)
    instructor_id_entry.grid(row=0, column=1, padx=10, pady=5)

    remove_button = tk.Button(remove_instructor_window, text="Remove Instructor", command=remove_instructor_from_db)
    remove_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    remove_instructor_window.mainloop()

def enroll_student_gui():
    def enroll_student_to_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                student_name = student_name_entry.get()
                student_email = student_email_entry.get()

                query = """
                INSERT INTO Students (student_name, student_email)
                VALUES (%s, %s)
                """
                cursor.execute(query, (student_name, student_email))
                connection.commit()
                messagebox.showinfo("Success", "Student enrolled successfully")
                cursor.close()
                connection.close()
                enroll_student_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    enroll_student_window = tk.Toplevel()
    enroll_student_window.title("Enroll Student")

    tk.Label(enroll_student_window, text="Student Name:").grid(row=0, column=0, padx=10, pady=5)
    student_name_entry = tk.Entry(enroll_student_window)
    student_name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(enroll_student_window, text="Student Email:").grid(row=1, column=0, padx=10, pady=5)
    student_email_entry = tk.Entry(enroll_student_window)
    student_email_entry.grid(row=1, column=1, padx=10, pady=5)

    enroll_button = tk.Button(enroll_student_window, text="Enroll Student", command=enroll_student_to_db)
    enroll_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    enroll_student_window.mainloop()

def view_enrollments_gui():
    def view_enrollments_in_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                course_id = int(course_id_entry.get())

                query = """
                SELECT Students.student_id, Students.student_name, Students.student_email
                FROM Enrollments
                INNER JOIN Students ON Enrollments.student_id = Students.student_id
                WHERE Enrollments.course_id = %s
                """
                cursor.execute(query, (course_id,))
                enrollments = cursor.fetchall()

                if not enrollments:
                    messagebox.showinfo("No Enrollments", "No enrollments found for this course.")
                else:
                    view_enrollments_window = tk.Toplevel()
                    view_enrollments_window.title("View Enrollments")

                    tk.Label(view_enrollments_window, text="Enrollments:").grid(row=0, column=0, columnspan=2, padx=10, pady=5)
                    tk.Label(view_enrollments_window, text="{:<5} {:<20} {:<30}".format(
                        "ID", "Name", "Email"
                    )).grid(row=1, column=0, padx=10, pady=5)
                    tk.Label(view_enrollments_window, text="="*60).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

                    for idx, enrollment in enumerate(enrollments, start=3):
                        student_id, student_name, student_email = enrollment
                        tk.Label(view_enrollments_window, text="{:<5} {:<20} {:<30}".format(
                            student_id, student_name, student_email
                        )).grid(row=idx, column=0, columnspan=2, padx=10, pady=5)

                    cursor.close()
                    connection.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    view_enrollments_window = tk.Toplevel()
    view_enrollments_window.title("View Enrollments")

    tk.Label(view_enrollments_window, text="Enter Course ID to View Enrollments:").grid(row=0, column=0, padx=10, pady=5)
    course_id_entry = tk.Entry(view_enrollments_window)
    course_id_entry.grid(row=0, column=1, padx=10, pady=5)

    view_button = tk.Button(view_enrollments_window, text="View Enrollments", command=view_enrollments_in_db)
    view_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    view_enrollments_window.mainloop()

def add_assessment_gui():
    def add_assessment_to_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                course_id = int(course_id_entry.get())
                assessment_name = assessment_name_entry.get()

                query = """
                INSERT INTO Assessments (course_id, assessment_name)
                VALUES (%s, %s)
                """
                cursor.execute(query, (course_id, assessment_name))
                connection.commit()
                messagebox.showinfo("Success", "Assessment added successfully")
                cursor.close()
                connection.close()
                add_assessment_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    add_assessment_window = tk.Toplevel()
    add_assessment_window.title("Add Assessment")

    tk.Label(add_assessment_window, text="Course ID:").grid(row=0, column=0, padx=10, pady=5)
    course_id_entry = tk.Entry(add_assessment_window)
    course_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_assessment_window, text="Assessment Name:").grid(row=1, column=0, padx=10, pady=5)
    assessment_name_entry = tk.Entry(add_assessment_window)
    assessment_name_entry.grid(row=1, column=1, padx=10, pady=5)

    add_button = tk.Button(add_assessment_window, text="Add Assessment", command=add_assessment_to_db)
    add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    add_assessment_window.mainloop()

def view_assessments_gui():
    def view_assessments_in_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                course_id = int(course_id_entry.get())

                query = """
                SELECT * FROM Assessments
                WHERE course_id = %s
                """
                cursor.execute(query, (course_id,))
                assessments = cursor.fetchall()

                if not assessments:
                    messagebox.showinfo("No Assessments", "No assessments found for this course.")
                else:
                    view_assessments_window = tk.Toplevel()
                    view_assessments_window.title("View Assessments")

                    tk.Label(view_assessments_window, text="Assessments:").grid(row=0, column=0, columnspan=2, padx=10, pady=5)
                    tk.Label(view_assessments_window, text="{:<5} {:<20} {:<30}".format(
                        "ID", "Course ID", "Assessment Name"
                    )).grid(row=1, column=0, padx=10, pady=5)
                    tk.Label(view_assessments_window, text="="*60).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

                    for idx, assessment in enumerate(assessments, start=3):
                        assessment_id, course_id, assessment_name = assessment
                        tk.Label(view_assessments_window, text="{:<5} {:<20} {:<30}".format(
                            assessment_id, course_id, assessment_name
                        )).grid(row=idx, column=0, columnspan=2, padx=10, pady=5)

                    cursor.close()
                    connection.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    view_assessments_window = tk.Toplevel()
    view_assessments_window.title("View Assessments")

    tk.Label(view_assessments_window, text="Enter Course ID to View Assessments:").grid(row=0, column=0, padx=10, pady=5)
    course_id_entry = tk.Entry(view_assessments_window)
    course_id_entry.grid(row=0, column=1, padx=10, pady=5)

    view_button = tk.Button(view_assessments_window, text="View Assessments", command=view_assessments_in_db)
    view_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    view_assessments_window.mainloop()

def input_grades_gui():
    def input_grade_to_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                student_id = int(student_id_entry.get())
                assessment_id = int(assessment_id_entry.get())
                grade = float(grade_entry.get())

                query = """
                INSERT INTO Grades (student_id, assessment_id, grade)
                VALUES (%s, %s, %s)
                """
                cursor.execute(query, (student_id, assessment_id, grade))
                connection.commit()
                messagebox.showinfo("Success", "Grade added successfully")
                cursor.close()
                connection.close()
                input_grade_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    input_grade_window = tk.Toplevel()
    input_grade_window.title("Input Grades")

    tk.Label(input_grade_window, text="Student ID:").grid(row=0, column=0, padx=10, pady=5)
    student_id_entry = tk.Entry(input_grade_window)
    student_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(input_grade_window, text="Assessment ID:").grid(row=1, column=0, padx=10, pady=5)
    assessment_id_entry =    tk.Entry(input_grade_window)
    assessment_id_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(input_grade_window, text="Grade:").grid(row=2, column=0, padx=10, pady=5)
    grade_entry = tk.Entry(input_grade_window)
    grade_entry.grid(row=2, column=1, padx=10, pady=5)

    add_button = tk.Button(input_grade_window, text="Add Grade", command=input_grade_to_db)
    add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    input_grade_window.mainloop()

def view_grades_gui():
    def view_grades_in_db():
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                student_id = int(student_id_entry.get())

                query = """
                SELECT Assessments.assessment_name, Grades.grade
                FROM Grades
                INNER JOIN Assessments ON Grades.assessment_id = Assessments.assessment_id
                WHERE Grades.student_id = %s
                """
                cursor.execute(query, (student_id,))
                grades = cursor.fetchall()

                if not grades:
                    messagebox.showinfo("No Grades", "No grades found for this student.")
                else:
                    view_grades_window = tk.Toplevel()
                    view_grades_window.title("View Grades")

                    tk.Label(view_grades_window, text="Grades:").grid(row=0, column=0, columnspan=2, padx=10, pady=5)
                    tk.Label(view_grades_window, text="{:<30} {:<10}".format(
                        "Assessment Name", "Grade"
                    )).grid(row=1, column=0, padx=10, pady=5)
                    tk.Label(view_grades_window, text="="*50).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

                    for idx, grade in enumerate(grades, start=3):
                        assessment_name, grade_value = grade
                        tk.Label(view_grades_window, text="{:<30} {:<10}".format(
                            assessment_name, grade_value
                        )).grid(row=idx, column=0, columnspan=2, padx=10, pady=5)

                    cursor.close()
                    connection.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    view_grades_window = tk.Toplevel()
    view_grades_window.title("View Grades")

    tk.Label(view_grades_window, text="Enter Student ID to View Grades:").grid(row=0, column=0, padx=10, pady=5)
    student_id_entry = tk.Entry(view_grades_window)
    student_id_entry.grid(row=0, column=1, padx=10, pady=5)

    view_button = tk.Button(view_grades_window, text="View Grades", command=view_grades_in_db)
    view_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    view_grades_window.mainloop()

def display_deleted_records_log_gui():
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
                messagebox.showinfo("No Deleted Records", "No deleted records found.")
            else:
                display_deleted_records_log_window = tk.Toplevel()
                display_deleted_records_log_window.title("Deleted Records Log")

                tk.Label(display_deleted_records_log_window, text="Deleted Records Log:").grid(row=0, column=0, columnspan=4, padx=10, pady=5)
                tk.Label(display_deleted_records_log_window, text="{:<10} {:<20} {:<30} {:<30}".format(
                    "Table", "Record ID", "Deleted At", "Deleted By"
                )).grid(row=1, column=0, padx=10, pady=5)
                tk.Label(display_deleted_records_log_window, text="="*100).grid(row=2, column=0, columnspan=4, padx=10, pady=5)

                for idx, record in enumerate(deleted_records, start=3):
                    table_name, record_id, deleted_at, deleted_by = record
                    tk.Label(display_deleted_records_log_window, text="{:<10} {:<20} {:<30} {:<30}".format(
                        table_name, record_id, deleted_at, deleted_by
                    )).grid(row=idx, column=0, columnspan=4, padx=10, pady=5)

                cursor.close()
                connection.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from utils import connect_to_database

if __name__ == "__main__":
    root = tk.Tk()
    root.title("EduSchema - Online Learning Platform")

    def show_course_management():
        course_management_window = tk.Toplevel(root)
        course_management_window.title("Course Management")

        tk.Button(course_management_window, text="Add Course", command=add_course_gui).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(course_management_window, text="Update Course", command=update_course_gui).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(course_management_window, text="Remove Course", command=remove_course_gui).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(course_management_window, text="Search Courses", command=search_courses_gui).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(course_management_window, text="Sort Courses", command=sort_courses_gui).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(course_management_window, text="View Enrollments", command=view_enrollments_gui).grid(row=1, column=2, padx=10, pady=5)

    def show_instructor_management():
        instructor_management_window = tk.Toplevel(root)
        instructor_management_window.title("Instructor Management")

        tk.Button(instructor_management_window, text="Add Instructor", command=add_instructor_gui).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(instructor_management_window, text="Update Instructor", command=update_instructor_gui).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(instructor_management_window, text="Remove Instructor", command=remove_instructor_gui).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(instructor_management_window, text="Search Instructors", command=search_instructors_gui).grid(row=1, column=0, padx=10, pady=5)

    def show_student_management():
        student_management_window = tk.Toplevel(root)
        student_management_window.title("Student Management")

        tk.Button(student_management_window, text="Enroll Student", command=enroll_student_gui).grid(row=0, column=0, padx=10, pady=5)

    def show_assessment_management():
        assessment_management_window = tk.Toplevel(root)
        assessment_management_window.title("Assessment Management")

        tk.Button(assessment_management_window, text="Add Assessment", command=add_assessment_gui).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(assessment_management_window, text="View Assessments", command=view_assessments_gui).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(assessment_management_window, text="Input Grades", command=input_grades_gui).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(assessment_management_window, text="View Grades", command=view_grades_gui).grid(row=1, column=1, padx=10, pady=5)

    def show_deleted_records_log():
        display_deleted_records_log_gui()

    tk.Button(root, text="Course Management", command=show_course_management).grid(row=0, column=0, padx=10, pady=5)
    tk.Button(root, text="Instructor Management", command=show_instructor_management).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(root, text="Student Management", command=show_student_management).grid(row=1, column=0, padx=10, pady=5)
    tk.Button(root, text="Assessment Management", command=show_assessment_management).grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Display Deleted Records Log", command=show_deleted_records_log).grid(row=2, column=0, columnspan=2, padx=10, pady=5)
    tk.Button(root, text="Exit", command=root.quit).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()



