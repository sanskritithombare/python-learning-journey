#range and for loop
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