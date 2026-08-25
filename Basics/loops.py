#range and for loop
from turtle import bye


for i in range(5):
    print("Hello!")

for i in range(5):
    print("This is round", i)


#while 
count = 0
while count < 3:
    print("Counting:", count)
    count = count + 1

for i in range(5):
    print("Stay hydrated")

#count by 2's
for i in range(2, 11, 2):
    print(i)


#while loop - code runs till user types stop
a = ""
while  a != "stop":
    print("Stay hydrated")
    a = input("Type your input: ")

#countdown with for - count from 5 to 1 and then print liftoff. o/p - 54321 liftoff
for i in range(5,0,-1):
    print(i)
print("Liftoff!") 


x = range(3, 20, 2)
for n in x:
  print(n)

#write a function to print even numbers till 15
def print_even_numbers():
    for i in range(2, 16, 2):
        print(i)




#Program to keep going until user types bye
# if user types nothing, it will ask again for input. 
# If user types bye, it will exit the loop. 
# Otherwise, it will print what the user said.
while True:
    word = input("Say something: ")
    if word == "bye":
        break
    if word == "":
        continue
    print("You said:", word)

#Say something: hey
#You said: hey
#Say something: no
#You said: no
#Say something: 
#Say something: stop it
#You said: ok i need to say bye
#Say something: bye


for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)
# From 1 to 10, print only odd numbers. If the number is even, 
# skip it and continue to the next iteration.  