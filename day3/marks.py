math=int(input("enter marks in math"))
sci=int(input("enter marks in sci"))
comp=int(input("enter marks in comp"))
eng=int(input("enter marks in eng"))
total_mark=math+sci+comp+eng
percentage=(total_mark/400)*100
if percentage >= 70:
    print("congratulation you get distinction")
elif percentage >= 60:
    print("congratulation you get first division")
elif percentage >= 40:
    print("congratulation you get pass")
else:
    print("sorry, yor are fail")






