import re
from datetime import datetime, date
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, person_id, name, surname, email, phone):
        self.__person_id = person_id 
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__phone = phone
        
        if not self._validate_email(email):
            raise ValueError("არასწორი ემაილის ფორმატი")
        if not self._validate_phone(phone):
            raise ValueError("არასწორი ტელეფონის ნომერი")
    
    @property
    def person_id(self):
        return self.__person_id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value or len(value.strip()) < 2:
            raise ValueError("სახელი უნდა შეიცავდეს მინიმუმ 2 სიმბოლოს")
        self.__name = value.strip()
    
    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, value):
        if not value or len(value.strip()) < 2:
            raise ValueError("გვარი უნდა შეიცავდეს მინიმუმ 2 სიმბოლოს")
        self.__surname = value.strip()
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if not self._validate_email(value):
            raise ValueError("არასწორი ემაილის ფორმატი")
        self.__email = value.lower()
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        if not self._validate_phone(value):
            raise ValueError("არასწორი ტელეფონის ნომერი")
        self.__phone = value
    
    def _validate_email(self, email):
        pattern = r'^[\w\.-]+@sulkh\.edu\.ge$'
        return re.match(pattern, email) is not None

    def _validate_phone(self, phone):
        pattern = r'^(\+995|995)?[0-9]{9}$'
        clean_phone = re.sub(r'[^\d+]', '', phone)
        return re.match(pattern, clean_phone) is not None
    
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    
    def update_contact_info(self, email=None, phone=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
    
    def __str__(self):
        return f"ID: {self.person_id}, {self.get_full_name()}, {self.email}"
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.person_id == other.person_id
    
    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def get_info_dict(self):
        pass