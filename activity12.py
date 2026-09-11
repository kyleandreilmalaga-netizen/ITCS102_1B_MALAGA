#multiple if and elif conditions

name = input("Please input your name ---->>>")

age = eval(input("Please input your age ---->>>"))

if age >= 0 and age <= 5 :
         print("That age is considered as INFANT")

elif age >=6 and age <=12 :
         print("The age is considered as KID")

elif age >=13 and age <=15 :
         print("The age is considered as PRE TEEN")

elif age >=16 and age <=19 :
         print("The age is considered as TEENAGER")

elif age >=20 and age <=29 :
         print("The age is considered as YOUNG ADULT")

elif age >=30 and age <=59 :
         print("The age is considered as ADULT")

elif age >=60 and age <=150 :
         print("The age is considered as SENIOR")

else:
       print("The age is considered as INVALID")