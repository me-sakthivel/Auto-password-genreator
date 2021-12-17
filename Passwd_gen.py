import random

lower = "hijklmstuefgqvwxnopabcduryz"
upper = "AKLMNOPQURUVWXSBCDEFGHIJTYZ"
NUMBER = "3480567129"
Symbol = "!#&*()$@[]{}"

all=lower + upper + NUMBER + Symbol

print("Min 9 or higher recommended              ")

length = int(input("Type down the length:"))

password = "".join(random.sample(all,length))
print("The Password is :",password)