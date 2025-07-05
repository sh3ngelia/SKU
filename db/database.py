import sqlite3
import random



# conn = sqlite3.connect('students_db.sqlite3')
# cursor = conn.cursor()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS students (
#     person_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     first_name TEXT,
#     last_name TEXT,
#     email TEXT,
#     phone TEXT,
#     student_id INTEGER,
#     status TEXT
# )''')
#
# first_names = [
#     "Giorgi", "Nino", "Tamar", "Lasha", "Ana", "Mariam", "Davit", "Ekaterine", "Sandro", "Elene",
#     "Irakli", "Ketevan", "Levan", "Salome", "Nikoloz", "Teona", "Vakhtang", "Ia", "Zurab", "Tornike",
#     "Saba", "Tinatin", "Revaz", "Manana", "Beka", "Aleksandre", "Tatia", "Gvantsa", "Guga", "Natia",
#     "Shota", "Lia", "Dato", "Tiko", "Nugzar", "Nana", "Besik", "Rusudan", "Ilia", "Marika",
#     "Avtandil", "Anano", "Temur", "Khatia", "Otar", "Sopio", "Archil", "Maia", "Zuriko", "Kristine"
# ]
#
# last_names = [
#     "Abashidze", "Gelashvili", "Beridze", "Kardava", "Mamaladze", "Tsintsadze", "Javakhishvili", "Bakhtadze", "Jibladze", "Megrelishvili",
#     "Kiknadze", "Chkhaidze", "Gogoladze", "Lomidze", "Chichinadze", "Maisuradze", "Nakashidze", "Kapanadze", "Khutsishvili", "Sharashenidze",
#     "Dolidze", "Gvazava", "Khukhunaishvili", "Tsiklauri", "Koberidze", "Mchedlidze", "Pirtskhalava", "Abuseridze", "Katsitadze", "Kiladze",
#     "Burchuladze", "Tugushi", "Kereselidze", "Alavidze", "Lursmanashvili", "Chikhladze", "Gagnidze", "Kharshiladze", "Chelidze", "Gogsadze",
#     "Sichinava", "Gvazava", "Ishkhneli", "Kavtaradze", "Topuridze", "Sesiashvili", "Sulakvelidze", "Okropiridze", "Kvaratskhelia", "Japaridze"
# ]
# statuses = ['active', 'inactive', 'graduated', 'suspended']
#
# students = []
# start_id = 6000
# for i in range(1000):
#     person_id = start_id + i
#     fn = random.choice(first_names)
#     ln = random.choice(last_names)
#     email = f"{fn.lower()}.{ln.lower()}.{1}@sku.edu.ge"
#     phone = f"+9955{random.randint(10, 99)}{random.randint(100000, 999999)}"
#     student_id = 1000 + i
#     status = random.choice(statuses)
#     students.append((person_id, fn, ln, email, phone, student_id, status))
#
# cursor.executemany('''
# INSERT INTO students (person_id,first_name, last_name, email, phone, student_id, status)
# VALUES (?, ?, ?, ?, ?, ?, ?)
# ''', students)
#
# cursor.execute('''
# INSERT INTO students (person_id,first_name, last_name, email, phone, student_id, status)
# VALUES (4444, 'Davit', 'Shengelia', 'davit.shengelia.1@sku.edu.ge', '+995544444444', 4444, 'active')
# ''')
#
# cursor.execute('''
# INSERT INTO students (person_id,first_name, last_name, email, phone, student_id, status)
# VALUES (7777, 'Vazha', 'Cercvadze', 'vazha.cercvadze.1@sku.edu.ge', '+995577777777', 7777, 'active')
# ''')
#
# conn.commit()
# conn.close()


#################           #################

# სტუდენტებზე ახალი სვეტის დამატება
# conn = sqlite3.connect('students_db.sqlite3')
# cursor = conn.cursor()
#
# cursor.execute('''
#     ALTER TABLE students ADD COLUMN subjects TEXT
# ''')
#
# conn.commit()
# conn.close()


# available_subjects = [
#     "Mathematics", "Physics", "Computer Science", "Biology", "Chemistry",
#     "English", "Statistics", "Programming", "Philosophy", "History"
# ]
#
# conn = sqlite3.connect('students_db.sqlite3')
# cursor = conn.cursor()
#
# cursor.execute('SELECT person_id FROM students')
# student_ids = [row[0] for row in cursor.fetchall()]
#
# for sid in student_ids:
#     subjects = random.sample(available_subjects, random.randint(3, 5))
#     subject_str = ', '.join(subjects)
#     cursor.execute('UPDATE students SET subjects = ? WHERE person_id = ?', (subject_str, sid))
#
# conn.commit()
# conn.close()


#################           #################
# import sqlite3
# import random
#
# # ბაზების სახელები
# prof_db = 'professors_db.sqlite3'
# courses_db = 'courses_db.sqlite3'
#
# names = ["Avtandil", "Rusudan", "Temur", "Lali", "Zuriko", "Nugzar", "Khatuna", "Besik", "Ia", "Marika",
#          "Rati", "Inga", "Tengiz", "Nargiza", "Otar", "Tsira", "Rezo", "Manana", "Amiran", "Lamara"]
# surnames = ["Saghinadze", "Kevlishvili", "Abulashvili", "Dzidziguri", "Gabunia", "Mikaberidze", "Tabidze",
#             "Tkeshelashvili", "Oniani", "Vashakidze", "Sharashidze", "Nozadze", "Kikava", "Shekiladze",
#             "Gvritishvili", "Sichinava", "Gogiashvili", "Melikidze", "Khutsishvili", "Katsarava"]
# departments = ["Computer Science", "Mathematics", "Physics", "Biology", "Engineering"]
# ranks = ["ასისტენტ პროფესორი", "ასოცირებული პროფესორი", "პროფესორი"]
# statuses = ["active", "inactive", "retired", "on_leave"]
#
# department_courses = {
#     "Computer Science": ["Introduction to Programming", "Databases", "Algorithms", "Operating Systems",
#                          "Web Development", "AI Fundamentals", "Software Engineering", "Machine Learning",
#                          "Cybersecurity", "Computer Networks", "Advanced Programming"],
#     "Mathematics": ["Calculus", "Linear Algebra", "Statistics", "Discrete Math"],
#     "Physics": ["Physics I", "Quantum Mechanics", "Digital Logic"],
#     "Biology": ["Biology"],
#     "Engineering": ["Digital Logic", "Software Engineering"]
# }

#################           #################
# prof_conn = sqlite3.connect(prof_db)
# prof_cursor = prof_conn.cursor()
#
# prof_cursor.execute('''
#     CREATE TABLE IF NOT EXISTS professors (
#         person_id INTEGER PRIMARY KEY,
#         name TEXT,
#         last_name TEXT,
#         email TEXT,
#         phone TEXT,
#         professor_id INTEGER,
#         department TEXT,
#         rank TEXT,
#         salary INTEGER,
#         status TEXT,
#         subjects TEXT
#     )
# ''')
#
# professors = []
# start_id = 1000
# for i in range(100):
#     person_id = start_id + i
#     name = random.choice(names)
#     surname = random.choice(surnames)
#     email = f"{name.lower()}.{surname.lower()}@sku.edu.ge"
#     phone = f"+9955{random.randint(10, 99)}{random.randint(100000, 999999)}"
#     professor_id = 5000 + i
#     department = random.choice(departments)
#     rank = random.choice(ranks)
#     salary = random.randint(2000, 10000)
#     status = random.choice(statuses)
#     professors.append((person_id, name, surname, email, phone, professor_id, department, rank, salary, status, ''))
#
# prof_cursor.executemany('''
#     INSERT INTO professors (
#         person_id, name, last_name, email, phone,
#         professor_id, department, rank, salary, status, subjects)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# ''', professors)
# prof_conn.commit()
#
# prof_cursor.execute("SELECT person_id, department FROM professors WHERE status = 'active'")
# active_professors = prof_cursor.fetchall()
# prof_conn.close()
#
# # === 2. Courses ბაზა ===
# course_conn = sqlite3.connect(courses_db)
# course_cursor = course_conn.cursor()
#
# course_cursor.execute('''
#     CREATE TABLE IF NOT EXISTS courses (
#         course_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         course_name TEXT NOT NULL,
#         department TEXT,
#         credits INTEGER,
#         professor_id INTEGER,
#         status TEXT,
#         FOREIGN KEY (professor_id) REFERENCES professors(person_id)
#     )
# ''')
#

# courses_to_insert = []
# professor_subjects = {}
#
# for prof_id, dept in active_professors:
#     if dept not in department_courses:
#         continue  # skip unknown departments
#     available_courses = department_courses[dept]
#     num_courses = min(len(available_courses), random.randint(1, 3))
#     selected_courses = random.sample(available_courses, num_courses)
#     professor_subjects[prof_id] = ", ".join(selected_courses)
#     for course in selected_courses:
#         credits = random.choice([3, 4, 5])
#         status = random.choice(['active', 'inactive'])
#         courses_to_insert.append((course, dept, credits, prof_id, status))
#
# course_cursor.executemany('''
#     INSERT INTO courses (course_name, department, credits, professor_id, status)
#     VALUES (?, ?, ?, ?, ?)
# ''', courses_to_insert)
#
# course_conn.commit()
# course_conn.close()
#
# prof_conn = sqlite3.connect(prof_db)
# prof_cursor = prof_conn.cursor()
#
# for prof_id, subjects in professor_subjects.items():
#     prof_cursor.execute("UPDATE professors SET subjects = ? WHERE person_id = ?", (subjects, prof_id))
#
# prof_conn.commit()
# prof_conn.close()


#################           #################
# import sqlite3
# import random
#
# students_db = 'students_db.sqlite3'
# courses_db = 'courses_db.sqlite3'
#
# students_conn = sqlite3.connect(students_db)
# students_cursor = students_conn.cursor()
#
# try:
#     students_cursor.execute("ALTER TABLE students ADD COLUMN subjects TEXT")
# except sqlite3.OperationalError:
#     pass
#
# students_cursor.execute('''
#     CREATE TABLE IF NOT EXISTS enrollments (
#         enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         student_id INTEGER,
#         course_id INTEGER,
#         enrollment_status TEXT,
#         FOREIGN KEY (student_id) REFERENCES students(student_id),
#         FOREIGN KEY (course_id) REFERENCES courses(course_id)
#     )
# ''')
#
# students_cursor.execute("SELECT student_id FROM students WHERE status = 'active'")
# active_students = [row[0] for row in students_cursor.fetchall()]
#
# course_conn = sqlite3.connect(courses_db)
# course_cursor = course_conn.cursor()
# course_cursor.execute("SELECT course_id, course_name FROM courses WHERE status = 'active'")
# active_courses = course_cursor.fetchall()
# course_conn.close()
#
# course_id_to_name = {cid: name for cid, name in active_courses}
# course_ids = list(course_id_to_name.keys())
#
# enrollments = []
# student_subject_map = {}
#
# for student_id in active_students:
#     chosen_courses = random.sample(course_ids, k=random.randint(2, 5))
#     subject_names = []
#
#     for course_id in chosen_courses:
#         enrollments.append((student_id, course_id, 'enrolled'))
#         subject_names.append(course_id_to_name[course_id])
#
#     student_subject_map[student_id] = ", ".join(subject_names)
#
# students_cursor.executemany('''
#     INSERT INTO enrollments (student_id, course_id, enrollment_status)
#     VALUES (?, ?, ?)
# ''', enrollments)

# for student_id, subjects_str in student_subject_map.items():
#     students_cursor.execute('''
#         UPDATE students
#         SET subjects = ?
#         WHERE student_id = ?
#     ''', (subjects_str, student_id))
#
# students_conn.commit()
# students_conn.close()

