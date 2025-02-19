class Student:
    unique_students = 0
    def __init__(self, name, id_num):
        self.name = name
        self.id = hash(unique_students)
        unique_students += 1
        self.units_complted = 0
        
    def add_units(self, units_to_add):
        self.units_completed += units_to_add
    
    def can_graduate(self):
        return self.units_completed >= 40