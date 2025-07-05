class Course:
    total_courses = 0
    
    def __init__(self, course_id, name, credits, professor_id, description=""):
        self.__course_id = course_id
        self.__name = name
        self.__credits = credits
        self.__professor_id = professor_id
        self.__description = description
        self.__enrolled_students = set()  
        self.__grades = {}  
        
     
        self._validate_course_data()
        
  
        Course.total_courses += 1
    
    def _validate_course_data(self):
        if not self.__name or len(self.__name.strip()) < 3:
            raise ValueError("კურსის სახელი უნდა შეიცავდეს მინიმუმ 3 სიმბოლოს")
        
        if not isinstance(self.__credits, int) or not (1 <= self.__credits <= 6):
            raise ValueError("კრედიტები უნდა იყოს 1-დან 6-მდე")
    

    @property
    def course_id(self):
        return self.__course_id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value or len(value.strip()) < 3:
            raise ValueError("კურსის სახელი უნდა შეიცავდეს მინიმუმ 3 სიმბოლოს")
        self.__name = value.strip()
    
    @property
    def credits(self):
        return self.__credits
    
    @credits.setter
    def credits(self, value):
        if not isinstance(value, int) or not (1 <= value <= 10):
            raise ValueError("კრედიტები უნდა იყოს 1-დან 10-მდე")
        self.__credits = value
    
    @property
    def professor_id(self):
        return self.__professor_id
    
    @professor_id.setter
    def professor_id(self, value):
        self.__professor_id = value
    
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value):
        self.__description = value
    
    @property
    def enrolled_students(self):
        return self.__enrolled_students.copy()
    

    def enroll_student(self, student_id):
        if student_id in self.__enrolled_students:
            raise ValueError("სტუდენტი უკვე რეგისტრირებულია ამ კურსზე")
        
        self.__enrolled_students.add(student_id)
        return True
    
    def unenroll_student(self, student_id):
        if student_id not in self.__enrolled_students:
            raise ValueError("სტუდენტი არ არის რეგისტრირებული ამ კურსზე")
        
        self.__enrolled_students.remove(student_id)

        if student_id in self.__grades:
            del self.__grades[student_id]
        return True
    
    def is_student_enrolled(self, student_id):
        return student_id in self.__enrolled_students
    
    def get_enrollment_count(self):
        return len(self.__enrolled_students)
    
    def assign_grade(self, student_id, grade):
        if student_id not in self.__enrolled_students:
            raise ValueError("სტუდენტი არ არის რეგისტრირებული ამ კურსზე")
        
        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            raise ValueError("ქულა უნდა იყოს 0-დან 100-მდე")
        
        self.__grades[student_id] = grade
        return True
    
    def get_student_grade(self, student_id):
        if student_id not in self.__enrolled_students:
            raise ValueError("სტუდენტი არ არის რეგისტრირებული ამ კურსზე")
        
        return self.__grades.get(student_id, None)
    
    def get_all_grades(self):
        return self.__grades.copy()
    
    def get_course_info(self):
        return {
            'course_id': self.__course_id,
            'name': self.__name,
            'credits': self.__credits,
            'professor_id': self.__professor_id,
            'description': self.__description,
            'enrolled_count': len(self.__enrolled_students)
        }
    
    @classmethod
    def get_total_courses(cls):
        return cls.total_courses
    
    def __str__(self):
        return f"კურსი: {self.__name} ({self.__course_id}) - {self.__credits} კრედიტი"
 
    def __eq__(self, other):
        if not isinstance(other, Course):
            return False
        return self.__course_id == other.__course_id
    
    def __del__(self):
        Course.total_courses -= 1

