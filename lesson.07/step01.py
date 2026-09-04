# __init__
# __str__
# __len__

# print(obj) -> obj.__str__()
# len(obj)  -> obj.__len__()
# obj1 + obj2  -> obj1.__add__(obj2)

# class Student(object):
#     def show_info(self):
#         return "Student info"
#
#
# student = Student()
# print(student)
# print(student.show_info())



class Student(object):
    def __str__(self):
        return "Student info!!"


student = Student()
print(student)