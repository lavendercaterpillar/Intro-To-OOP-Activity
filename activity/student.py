# add your Student class here!
class Student:
    def __init__(self, name, level, classes):
        self.name = name
        self.level = level
        self.classes = classes      
        
    def add_class(self, class_name):
        self.classes.append(class_name)
        return self.classes

    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        return f"{self.name} is a {self.level} enrolled in {self.get_num_classes()} classes"