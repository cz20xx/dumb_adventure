from sys import exit

def start():
	print "You wake up, woozy from probably having drunk too much"
	print "at your going away party."
	
	try:
		next = str(raw_input("> "))
	except ValueError:
		dead("WTF does that mean?")
		
	if "look" in next:
		print "You look around the room. It's full of nothing."
		print "Literally nothing, dude."
		print "I mean, there's some doors."
		print "Looks like a bedroom, a kitchen and the front door"
		print "are place you could go.  But idk w/e."
		living_room()
		
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
	
start()
	
		
		
	
	