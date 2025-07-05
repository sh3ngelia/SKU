from person import Person

class Professor(Person):
    total_professors = 0
    
    def __init__(self, person_id, name, surname, email, phone,
                 professor_id, department, rank="ასისტენტ პროფესორი",
                 salary=0, status="active"):
        super().__init__(person_id, name, surname, email, phone)
        
        self.__professor_id = professor_id
        self.__department = department
        self.__rank = rank
        self.__salary = salary
        self.__status = status
        self.__teaching_courses = set()
        
        Professor.total_professors += 1
        

        if status not in ["active", "inactive", "retired", "on_leave"]:
            raise ValueError("პროფესორის სტატუსი უნდა იყოს active, inactive, retired ან on_leave")

        valid_ranks = ["ასისტენტ პროფესორი", "ასოცირებული პროფესორი", "პროფესორი"]
        if rank not in valid_ranks:
            raise ValueError(f"რანგი უნდა იყოს: {', '.join(valid_ranks)}")
    

    @property
    def professor_id(self):
        return self.__professor_id

    
    @property
    def department(self):
        return self.__department
    
    @department.setter
    def department(self, value):
        if not value or not value.strip():
            raise ValueError("დეპარტამენტი არ შეიძლება იყოს ცარიელი")
        self.__department = value.strip()
    
    @property
    def rank(self):
        return self.__rank
    
    @rank.setter
    def rank(self, value):
        valid_ranks = ["ასისტენტ პროფესორი", "ასოცირებული პროფესორი", "სრული პროფესორი", "ემერიტუსი"]
        if value not in valid_ranks:
            raise ValueError(f"რანგი უნდა იყოს: {', '.join(valid_ranks)}")
        self.__rank = value
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("ხელფასი არ შეიძლება იყოს უარყოფითი")
        self.__salary = value
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        valid_statuses = ["active", "inactive", "retired", "on_leave"]
        if value not in valid_statuses:
            raise ValueError(f"სტატუსი უნდა იყოს: {', '.join(valid_statuses)}")
        self.__status = value
    
    @property
    def teaching_courses(self):
        return self.__teaching_courses.copy()

    
    def get_role(self):
        return "Professor"
    
    def get_info_dict(self):
        return {
            "person_id": self.person_id,
            "professor_id": self.professor_id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "phone": self.phone,
            "department": self.department,
            "rank": self.rank,
            "salary": self.salary,
            "status": self.status,
            "total_courses": len(self.teaching_courses),
        }
    
    def assign_course(self, course_id):
        if self.status != "active":
            raise ValueError("მხოლოდ აქტიური პროფესორი შეიძლება ასწავლიდეს კურსს")
        
        self.__teaching_courses.add(course_id)
    
    def remove_course(self, course_id):
        if course_id in self.__teaching_courses:
            self.__teaching_courses.remove(course_id)

    def get_teaching_load(self):
        course_count = len(self.teaching_courses)
        
        if course_count == 0:
            return "დატვირთვა არ არის"
        elif course_count <= 2:
            return "დაბალი დატვირთვა"
        elif course_count <= 4:
            return "ნორმალური დატვირთვა"
        elif course_count <= 6:
            return "მაღალი დატვირთვა"
        else:
            return "ძალიან მაღალი დატვირთვა"
    
    def get_salary_category(self):
        """ხელფასის კატეგორია"""
        if self.salary == 0:
            return "ხელფასი არ არის მითითებული"
        elif self.salary < 1000:
            return "დაბალი ხელფასი"
        elif self.salary < 2500:
            return "საშუალო ხელფასი"
        elif self.salary < 5000:
            return "კარგი ხელფასი"
        else:
            return "მაღალი ხელფასი"
    
    @staticmethod
    def get_total_professors():
        return Professor.total_professors
    
    @classmethod
    def create_from_dict(cls, data):
        return cls(
            person_id=data["person_id"],
            name=data["name"],
            surname=data["surname"],
            email=data["email"],
            phone=data["phone"],
            professor_id=data["professor_id"],
            department=data["department"],
            rank=data.get("rank", "ასისტენტ პროფესორი"),
            salary=data.get("salary", 0),
            status=data.get("status", "active")
        )
    
    def __str__(self):
        return (f"პროფესორი - ID: {self.professor_id}, {self.get_full_name()}, "
                f"{self.rank}, {self.department}")
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __del__(self):
        Professor.total_professors -= 1