#import demo
import getpass

username = "Greed"
password = "mahalkopasya123"

x = input("Input USERNAME -->>>")

y = getpass.getpass("Input PASSWORD -->>> ")

if x == username or y == password:
        print("username and password are correct")

else: 
     print("Incorrect password or username.")
