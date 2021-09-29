fh=open("examole.txt","w")
fh.write("this is my first file \n")
fh.write("this file is working very well\n")
try:
    for i in range(1,11):
        fh.write("%d \n"%i)

finally:
    fh.close()
  #OR

with open("examole.txt","w")as fh:
    for a in range(1,5):
        fh.write("line%d\n"%a)
