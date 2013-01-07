from sys import exit

# LISTS N' SHIT LIKE YOUR INVENTORY I GUESS
def check_pockets():
	inventory = ['a knife', 'whiskey', 'an iphone', 'two coffee creamers']
	for stuff in inventory:
		print "You've got: %s" % stuff 
	


# BEGINNING OF THE GAME, FOOL
def start(why):
	print why
	print "You wake up, woozy from probably having drunk too much"
	print "at your going away party."
	
	
	next = str(raw_input("> "))
	
	if "look" in next:
		print "You look around the room. It's full of nothing."
		print "Literally nothing, dude."
		print "I mean, there's some doors."
		print "Looks like a bedroom, a kitchen and the front door"
		print "are place you could go.  But idk w/e."
		living_room()
	elif "pockets" or "inventory" in next:
		check_pockets()
	elif "exit" in next:
		print "Thanks for playing, jerk!"
		exit(0)	
	else:
		start("Let's try this one more time")

def living_room():
	
	next = raw_input("> ")
		
	if "bedroom" in next:
		print "it's locked"
		living_room()
	elif "kitchen" in next:
		kitchen()
	elif "front" or "exit" in house:
		front_door()
	else:
		dead("for no good reason, you kick the bucket.")

def kitchen():
	
	next = raw_input("> ")


def dead(why):
	print why, "Good job!"
	exit(0)
	
start("DUMB ADVENTURE v0.1a\n")
	
		
		
	
	
