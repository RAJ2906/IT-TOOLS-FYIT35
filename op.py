#Creating marks class
class marks:
   #Taking user data   
   def user_data(self):
       self.opt = int(input("theory marks"))
       self.opp = int(input("practical marks"))
       self.opi = int(input("internal marks"))

   #Calculating final result
   def final_result(self):
       self.total = self.opt + self.opp + self.opi
       return self.total


student_1 = Marks()
student_1.user_data()
print(student_1.final_result())
