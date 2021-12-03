a=int(input("enter number of students in class A"))
b=int(input("enter number of students in class B"))
c=int(input("enter number of students in class c"))
deskA=a//2
if deskA%2!=0:
    deskA=deskA+1
deskB=b//2
if deskB%2!=0:
    deskB=deskB+1
deskC=c//2
if deskC%2!=0:
    deskC=deskC+1
total_desk=deskA+deskB+deskC
print("total desk required is= ",total_desk)





