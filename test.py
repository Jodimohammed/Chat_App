
class Employee:
        
    def __init__(self , first, last, ):
        self.first = first
        self.last = last
    @property   
    def email  (self):
          return  '{} {} @email.com'.format(self.first,self.last)
      
    @property   
    def fullname(self):
          return  '{} {} '.format(self.first,self.last)
     
    @fullname.setter
    def fullname(self, name):
         first, last = name.split(' ')
         self.first = first
         self.last = last
      
emp_1 = Employee('john' , 'jolad')

#emp_1.fullname = 'Corey Schafer'
 
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
