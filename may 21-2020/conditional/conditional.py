def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)
    
    return the_mean

student_grade = {"marry":9.1,"sim":8.8,"john":7.5}
print(mean(student_grade))