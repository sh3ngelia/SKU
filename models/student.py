from datetime import date
from models.person import Person

class Student(Person):
    total_students = 0
    
    def __init__(self, person_id, name, surname, email, phone,
                 student_id, status="active"):
        super().__init__(person_id, name, surname, email, phone)
        
        self.__student_id = student_id
        self.__status = status
        self.__grades = {}  
        self.__enrolled_courses = set()  
        
        Student.total_students += 1
    

    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        valid_statuses = ["active", "inactive", "graduated", "suspended"]
        if value not in valid_statuses:
            raise ValueError(f"სტატუსი უნდა იყოს: {', '.join(valid_statuses)}")
        self.__status = value
    
    @property
    def grades(self):
        return self.__grades.copy()  
    
    @property
    def enrolled_courses(self):
        return self.__enrolled_courses.copy()
    
    def get_role(self):
        return "Student"
    
    def get_info_dict(self):
        return {
            "person_id": self.person_id,
            "student_id": self.student_id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "phone": self.phone,
            "status": self.status,
            "gpa": self.calculate_gpa(),
            "total_courses": len(self.enrolled_courses)
        }
    
    def enroll_in_course(self, course_id):
        if self.status != "active":
            raise ValueError("მხოლოდ აქტიური სტუდენტი შეიძლება დარეგისტრირდეს კურსზე")
        
        self.__enrolled_courses.add(course_id)
        if course_id not in self.__grades:
            self.__grades[course_id] = []
    
    def drop_course(self, course_id):
        if course_id in self.__enrolled_courses:
            self.__enrolled_courses.remove(course_id)
    
    def add_grade(self, course_id, grade, date_recorded=None):
        if course_id not in self.__enrolled_courses:
            raise ValueError("სტუდენტი არ არის რეგისტრირებული ამ კურსზე")
        
        if not (0 <= grade <= 100):
            raise ValueError("შეფასება უნდა იყოს 0-დან 100-მდე")
        
        if date_recorded is None:
            date_recorded = date.today()
        
        if course_id not in self.__grades:
            self.__grades[course_id] = []
        
        self.__grades[course_id].append({
            "grade": grade,
            "date": date_recorded
        })
    
    def get_course_grades(self, course_id):
        return self.__grades.get(course_id, [])
    
    def get_course_average(self, course_id):
        grades = self.get_course_grades(course_id)
        if not grades:
            return 0
        
        total = sum(g["grade"] for g in grades)
        return round(total / len(grades), 2)
    
    def calculate_gpa(self):
        if not self.__grades:
            return 0.0
        
        total_points = 0
        total_courses = 0
        
        for course_id, grades in self.__grades.items():
                course_avg = sum(g["grade"] for g in grades) / len(grades)
                gpa_points = self._convert_to_gpa(course_avg)
                total_points += gpa_points
                total_courses += 1
        
        if total_courses == 0:
            return 0.0
        
        return round(total_points / total_courses, 2)

    def _convert_to_gpa(self, percentage):
        if percentage >= 91:
            return 4.0  
        elif percentage >= 81:
            return 3.0  
        elif percentage >= 71:
            return 2.0  
        elif percentage >= 61:
            return 1.0  
        elif percentage >= 51:
            return 0.5 
        else:
            return 0.0 
    
    def get_letter_grade(self, percentage):
        if percentage >= 91:
            return "A (ფრიადი)"
        elif percentage >= 81:
            return "B (ძალიან კარგი)"
        elif percentage >= 71:
            return "C (კარგი)"
        elif percentage >= 61:
            return "D (დამაკმაყოფილებელი)"
        elif percentage >= 51:
            return "E (საკმარისი)"
        else:
            return "F (ჩაიჭრა)"
    
    def get_academic_standing(self):
        gpa = self.calculate_gpa()
        
        if gpa >= 3.5:
            return "შესანიშნავი"
        elif gpa >= 3.0:
            return "კარგი"
        elif gpa >= 2.0:
            return "დამაკმაყოფილებელი"
        elif gpa >= 1.0:
            return "საკმარისი"
        else:
            return "არადამაკმაყოფილებელი"

    @staticmethod
    def get_total_students():
        return Student.total_students
    
    @classmethod
    def create_from_dict(cls, data):
        return cls(
            person_id=data["person_id"],
            name=data["name"],
            surname=data["surname"],
            email=data["email"],
            phone=data["phone"],
            student_id=data["student_id"],
            status=data.get("status", "active")
        )
    
    def __str__(self):
        return f"სტუდენტი - ID: {self.student_id}, {self.get_full_name()}, GPA: {self.calculate_gpa()}"
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __del__(self):
        Student.total_students -= 1