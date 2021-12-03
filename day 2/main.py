import pdb
bike1="yamaha"
bike1_price=25000
bike2="honda"
bike2_price=40000
pdb.set_trace()
#print(f"{bike1} will cost you {bike1_price}")
choose=int(input("press 1 for yamaha and 2 for honda"))
#print(f"hello{name}")
if choose==1:
    print(f"{bike1} will cost you {bike1_price}")
elif choose==2:
    print(f"{bike2} will cost you {bike2_price+2000}")
else:
    print("press only 1 or 2")
d=0b1001
print(type(d))

