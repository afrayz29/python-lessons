import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    if spin_chamber == (1,6):
        return ("You are dead!")
    elif spin_chamber == (0):
        return ("Keep Playing!")
        



print(fire_gun())