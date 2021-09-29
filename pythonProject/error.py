x=1
if x==1:
    print("hello world")

def inc(sal):
    sal=sal+sal*20/100
    return sal
sal=inc(1000)
print("my incremented salary",sal)

result=None
x=int(input("enter the first number :-"))
y=int(input("enter the second nimber :-"))

try:
    result=x/y
except Exception as e:
    print("error in this code ",e)
else:
    print("i am inside else ")
    #raise Exception("u r at in else part and ur progtam is working")

finally:
    print("i am inside the finall")
print("the result is :-",result)
