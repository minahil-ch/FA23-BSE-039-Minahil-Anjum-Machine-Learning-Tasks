print("===== Task i: Instance and namespace =====")

# Task i: create instance and show its namespace
class Student_i:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

# creating an object of class
obj1 = Student_i("Ali", 101)

# namespace means all variables inside object
# __dict__ shows namespace
print("Namespace of instance:", obj1.__dict__)

print("\n===== Task ii: student_data function =====")

# Task ii: function with id compulsory, name and class optional
def student_data(student_id, student_name=None, student_class=None):
    # first print id always
    print(f"Student ID: {student_id}")
    # if name is given then print it
    if student_name is not None:
        print(f"Student Name: {student_name}")
    # if class is given then print it
    if student_class is not None:
        print(f"Student Class: {student_class}")

# testing the function
student_data(101)
print("---")
student_data(102, student_name="Sara")
print("---")
student_data(103, student_name="Ahmed", student_class="BSSE")

print("\n===== Task iii: Type, dict keys, module =====")

# Task iii: simple Student class and check type and attributes
class Student:
    # simple class with 2 variables
    def __init__(self, id, name):
        self.id = id
        self.name = name

# creating object
s = Student(1, "Ali")

# type means what kind of object it is
print("Type of Student class:", type(Student))
print("Type of object s:", type(s))

# __dict__ is a dict that stores class variables
print("Dict keys of Student class:", Student.__dict__.keys())

# __module__ tells in which file class is made
print("Module attribute:", Student.__module__)

print("\n===== Task iv: Two empty classes =====")

# Task iv: create two empty classes
class Student_Empty:
    pass # empty means no code inside

class Marks:
    pass

# creating instances (objects)
student_obj = Student_Empty()
marks_obj = Marks()

# check if object is instance of class - isinstance returns True or False
print("student_obj is instance of Student_Empty:", isinstance(student_obj, Student_Empty))
print("marks_obj is instance of Marks:", isinstance(marks_obj, Marks))
print("marks_obj is instance of Student_Empty:", isinstance(marks_obj, Student_Empty))

# check if class is subclass of object class
# in python every class is child of object class
print("Is Student_Empty subclass of object:", issubclass(Student_Empty, object))
print("Is Marks subclass of object:", issubclass(Marks, object))

print("\n===== Task v: Modify attribute values =====")

# Task v: class with name and marks, then modify
class Student_v:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

# original object
stud_v = Student_v("Ali", 85)
print("Original values:")
print(f"Name: {stud_v.student_name}, Marks: {stud_v.marks}")

# modifying values - changing old values to new values
stud_v.student_name = "Ahmed"
stud_v.marks = 95
print("Modified values:")
print(f"Name: {stud_v.student_name}, Marks: {stud_v.marks}")

print("\n===== Task vi: Add and remove attribute =====")

# Task vi: add new attribute and remove old one
class Student_vi:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

stud_vi = Student_vi(101, "Sara")

# adding new attribute outside class
stud_vi.student_class = "BSSE-5"

print("After adding student_class:")
print(stud_vi.__dict__) # show all attributes

# removing attribute using del
del stud_vi.student_name

print("After removing student_name:")
print(stud_vi.__dict__)

print("\n===== Task vii: Display with function =====")

# Task vii: same as vi but with a display function
class Student_vii:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    
    # function to show all attributes
    def display(self):
        print("All attributes:", self.__dict__)
        # loop through dict to print nicely
        for key, value in self.__dict__.items():
            print(f"{key} = {value}")

stud_vii = Student_vii(102, "Zain")
stud_vii.student_class = "BSSE" # adding new attribute

print("Displaying student:")
stud_vii.display()

print("\n===== Task viii: Two instances with given format =====")

# Task viii: two instances and print in format
class Student_viii:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

# creating two students with values
student1 = Student_viii(101, "Ali", "10th")
student2 = Student_viii(102, "Sara", "BSSE")

# printing in given format
print(f"student1 -> ID: {student1.student_id}, Name: {student1.student_name}, Class: {student1.student_class}")
print(f"student2 -> ID: {student2.student_id}, Name: {student2.student_name}, Class: {student2.student_class}")

print("\n===== Task ix: Memory Allocation tests =====")

# Task ix: check how much memory object takes
import sys

class NormalStudent:
    def __init__(self, id, name):
        self.id = id
        self.name = name

obj_normal = NormalStudent(101, "Ali")

# sys.getsizeof tells memory size in bytes
print("Size of object:", sys.getsizeof(obj_normal), "bytes")
print("Size of object __dict__:", sys.getsizeof(obj_normal.__dict__), "bytes")
print("Total memory with dict:", sys.getsizeof(obj_normal) + sys.getsizeof(obj_normal.__dict__), "bytes")

# creating many objects to test memory
many_objects = [NormalStudent(i, f"Student{i}") for i in range(1000)]
total_size = sum(sys.getsizeof(o) + sys.getsizeof(o.__dict__) for o in many_objects)
print(f"Memory for 1000 normal objects: {total_size} bytes")

print("\n===== Task x: Reducing memory with __slots__ =====")

# Task x: how to reduce memory using __slots__
# __slots__ tells python to not make __dict__, so memory is saved

class SlottedStudent:
    # __slots__ fixes which variables can exist, no extra dict
    __slots__ = ['id', 'name']
    def __init__(self, id, name):
        self.id = id
        self.name = name

obj_slotted = SlottedStudent(101, "Ali")

print("Size of slotted object:", sys.getsizeof(obj_slotted), "bytes")
# slotted object has no __dict__, so no extra memory

# check memory for 1000 slotted objects
many_slotted = [SlottedStudent(i, f"Student{i}") for i in range(1000)]
total_slotted = sum(sys.getsizeof(o) for o in many_slotted)
print(f"Memory for 1000 slotted objects: {total_slotted} bytes")

print("\n--- Comparison ---")
print(f"Normal 1000 objects: {total_size} bytes")
print(f"Slotted 1000 objects: {total_slotted} bytes")
print(f"Memory saved: {total_size - total_slotted} bytes")
print("So __slots__ saves memory!")