# add your get_student_with_more_classes function here!

def get_student_with_more_classes(student1, student2):  # => samara
    if student1.get_num_classes() > student2.get_num_classes():
        return student2.name
    else:
        return student1.name
    

