import random

email = input("Email: ")
username = email.split("@")[0]
domain=email.split("@")[1]

number = 0
while True:
  number =+ 1
  open("emails.txt", "a").write(username + "+" + str(number) + "@" + domain)
  print(username + "+" + str(number) + "@" + domain)
