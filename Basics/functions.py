def greet():        # Define a new function
    print("Hello!") # What it does

greet()             # Call the function

def add(a, b):
    return a + b

result = add(5, 3)
print(result)


def favorite_color(color):
    print("My favorite color is", color)

favorite_color("green")
favorite_color("purple")

#Create funcition to print a madlib - noun, verb, adjective
def madlib (noun,verb,adjective):
    print("The",adjective ,noun ,"needs to", verb ,"all day" )
    
madlib("mouse","eat","tiny")



#adventure game - if else statement

def adventure():
    print("We're in space. An alien ship approaches.")
    response = input("Do we hide or wave at them? ")

    if response == "hide":
        print("They pass by peacefully.")
    elif response == "wave":
        print("They beam us aboard and make us their king!")
    else:
        print("They ignore us. We float alone forever.")

adventure()

#Challenge
# Modify the function below by adding more layers to make the story your own!
def jungle_adventure():
    # Ask the user to choose between two paths
    path = input("You find two paths: one goes to a river, the other to a mountain. Where do you go? ")

    # Check what the user typed and respond accordingly
    if path == "river":
        print("You swim with dolphins!")
    elif path == "mountain":
        print("You find an ancient temple!")
    else:
        # If the user typed something else, give this outcome
        print("You wander into the jungle and get lost.")

# Start the jungle adventure by calling the function
jungle_adventure()