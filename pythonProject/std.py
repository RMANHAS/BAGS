def std(name,roll,**marks):
    print("Name",name)
    print("Roll",roll)
    #print("Marks",marks)
    for x,y in marks.items():
        print(x + "  marks: ",+y)

std("Manhas",55,english=22,hindi=33,maths=33,science=23)