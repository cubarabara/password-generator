import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()
num = "0123456789"
symbol = "[{}#0)*;._-"
ans = lower_case + upper_case + num + symbol
length = 8
password = "".join(random.sample(ans,length))
print(password+"@gmail.com")
print(password)
