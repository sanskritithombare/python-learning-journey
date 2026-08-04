
#if else condition
age = 12
if age >= 18:
    print("You're an adult!")
else:
    print("You're a minor!")

#if, elseif, else
hour = 14
if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")


#Challenge: Movie Night

#Ask the user for their age. If they’re 13 or older, they can watch a movie. Otherwise, say they’re too young.

age = int(input("How old are you? "))

if age >= 13:
    print("You can watch the movie!")
else:
    print("You're too young to watch movie!")