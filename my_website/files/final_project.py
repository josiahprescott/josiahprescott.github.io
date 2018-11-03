place = ""  
end_game = 0

import os.path
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'places.csv')
datafile = open(filename,'r')
data = datafile.readlines()

inventory = []






def start():
    #starts the game
    print "You fell asleep in Mr Argos room. You wake up and look outside. It's dark out. You glance at the clock and it is 8PM. Your phone is dead and you have to get out! What do you want to do? Type help for a list of commands"
    global place
    place = "Argos"


def help():
    #lists the commands you can use
    print "The following are acceptable commands: 'go to', 'search', 'help', 'exits', 'inventory', 'place', 'exit game'"

    
def locations():
    #print a list of where you can go from where you are
    global places
    global place
    for i in places[place][0]:
        print i

def goto():
    #gets ya to where you need to go, with if statements at the beginning for all special cases
    global end_game
    global places
    global place
    print "Where do you want to go?"
    answer = raw_input(">>>")
    if answer == "teachers lounge":
        #some messy if statements. I couldn't make this more flexible :(
        if (("Mr Elwer's ID\n" in inventory) == True):
            print "You are now in the teachers lounge"
            place = answer
        else:
            print "I'll need a teachers ID to get in there"
            
    elif answer == "gym":
            if (("the gym key\n" in inventory) == True):
                print "You are now in the gym"
                place = answer
            else:
                print "I'll need the key to get in there"
                
    elif answer == "outside":
            if (("the gate key\n" in inventory) == True):
                print "You unlock the gate and run out of Linfield! You win!"
                end_game = 2
                place = answer
            else:
                print "The gate is locked."
                
    elif answer == "Burns office":
            if (("Burns office key\n" in inventory) == True):
                if (("a monster drink\n" in inventory) == True) and (("a half filled iced americano\n" in inventory) == True):
                        print "Thanks boy. Here's the gate key"
                        inventory.append("the gate key\n")
                        place = answer
                else:
                    print "I'll give you the gate key if you bring me something to drink. I'll need at least two drinks!"
                    place = answer
            else:
                print "The door is locked, but it appears that Coach Burns is inside"
                
    else:
        if ((answer in places[place][0])==True):    
            place = answer
            print "You are now in", place
        else:
            print "That is not a valid location"

    
    
def search():
    #appends any items in your current room into a list called inventory
    if place == "teachers lounge":
        print "You found a riddle! It reads 'If you use the force, you will surely find the source, of how to get out, just look about'"
        inventory.append("riddle\n") 
    else:
        if places[place][1] == []:
            print "You did not find anything"
        else:
            for item in places[place][1]:
                print "You find" , item
                inventory.append(item)
        
              
def print_inventory():
    if inventory == []:
        print "Your inventory is empty"
    else:
        for item in inventory:
            print item
    
def whereami():
    global place 
    print place    

    
    
#opens my csv and makes it a dictionary named places
places={}
for line in data[1:]:
    place, exits, items, = line.split(',')
    exits = exits.split(";")
    if items =="\n":
        items=[]
    else:
        items = items.split(";")
    places[place] = [exits,items]
    


     
start()  
    
while 0 == end_game:
    #"the asker" aa loop that lasts until you win that keeps asking you questions and interprets the response
    answer = raw_input(">>>")
    if answer == "search":
        search()
    elif answer == "go to":
        goto()
    elif answer == "inventory":
        print_inventory()
    elif answer == "exits":
        locations()
    elif answer == "help":
        help()
    elif answer == "exit game":
        break
    elif answer == "place":
        whereami()
    else:
        print "I don't recognize that command" 



