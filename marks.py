# class Student :
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def get_average(self):
#         sum=0
#         for el in self.marks:
#             sum += el
#         print(sum/3)
# s1 = Student("Viral",[99,98,97])
# s1.get_average()

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brake = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started")

# c1 = Car()
# c1.start()

class Account:
    def __init__(self, balance, accN):
        self.balance = balance
        self.accN = accN

acc1 = Account(100000, 12345)
print(acc1.balance, acc1.accN)


