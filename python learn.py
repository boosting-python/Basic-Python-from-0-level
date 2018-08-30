class Robot:                                #Defining a class
    def __init__(self,name,age):            #"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts
        self.name = name
        self.age = age
    
    
    def info(self):                         #Define a function named info
        print ("My name is " + self.name)
        print ("My age is " + self.age)

r1 = Robot("Tom" , "20")                    #Creating Object r1
r2 = Robot("Jerry" , "30")                  #Creating Object r2

r1.info()                                   #See output
r2.info()