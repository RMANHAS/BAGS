a=input("Name :-")
s=int(input("age :-"))
d=int(input("MARKS :-"))

class Students:
    def __init__(self, a , s , d):
        self.name = a
        self.age = s
        self.marks = d

    def dra(self):
        print("Name",self.name)
        print("Age",self.age)
        print("Marks",self.marks)


z = Students(a,s,d)
z.dra()



