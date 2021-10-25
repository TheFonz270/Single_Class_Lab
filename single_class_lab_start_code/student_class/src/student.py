class Student: 
    def __init__ (self, name, uid):
        self.name = name
        self.cohort = uid

    def test_student_can_update_name(self, new_name):
        self.name = new_name

    def test_student_can_change_cohort(self, uid):
        self.cohort = uid

    def talk(self):
        return "I can talk!"