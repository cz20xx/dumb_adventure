from sys import exit

# ADDING STUFF SO IT'S ON GIT

# LISTS N' SHIT LIKE YOUR INVENTORY I GUESS
def check_pockets():
	inventory = ['a knife', 'some string', 'a towel', 'a slim jim', 'whiskey', 'an iphone', 'some cocaine', 'a can of easy cheese', 'two coffee creamers']
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
	elif "exit" in next:
		print "Thanks for playing, jerk!"
		exit(0)	
	else:
		start("Let's try this one more time.")

def living_room():
	
	
	next = str(raw_input("> "))
		
	if "bedroom" in next:
		print "it's locked"
		living_room()
	else:
		print "Looks like a bedroom, a kitchen and the front door"
		print "are place you could go.  But idk w/e."
		living_room()
		
def kitchen():
	
	next = raw_input("> ")

def front_door():
	
	next = raw_input("> ")

def dead(why):
	print why, "Good job!"
	exit(0)
	
start("DUMB ADVENTURE v0.1a\n")
	
		
		
	
	
