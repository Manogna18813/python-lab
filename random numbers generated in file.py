import random as r
with open("random_numbers.txt", "w") as file:
   for i in range(20):
       num = r.randint(1, 100)
       file.write(str(num) + "\n")
print("20 random numbers generated and written to random_numbers.txt")
