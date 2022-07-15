class Person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def intro(self):
        print("Hello my name is",self.fname," ",self.lname,",and my age is",self.age)           
        
class student(Person):
    def __init__(self, fname, lname, age,std):
        super().__init__(fname, lname, age)        
        self.std=std
        
    def intro(self):
        super().intro()    
        print("I m in standard",self.std)
        
class teacher(Person):
    def __init__(self, fname, lname, age,homeRoom):
        super().__init__(fname, lname, age)        
        self.homeRoom=homeRoom  
        
    def intro(self):
        super().intro()    
        print("I m the Home Room teacher of Class",self.homeRoom)   
        
s1=student("Ankit","Mohanty",20,10)    
t1=teacher("Deb","Kumar",30,8)    
s1.intro()
t1.intro()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        