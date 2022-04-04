from domains.class_person import Person
list_student = []

class Student(Person):
    def __init__(self,name,DoB,id):
        super().__init__(name,DoB)
        self._id = id
    def add_student(self):
        ob = Student(self._name,self._DoB,self._id)
        list_student.append(ob)