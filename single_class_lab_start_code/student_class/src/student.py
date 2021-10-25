class Student: 
    def __init__ (self, name, uid):
        self.name = name
        self.cohort = uid

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, lan):
        return ("I love " + lan)