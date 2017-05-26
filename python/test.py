def start():
    print "welcome"
lobby()

def prompt ():
    x = input("type command")
    return x

def lobby ():
    print "you are in the lobby"
    command = prompt () 
    if command == "NORTH":
        bedroom()
    elif: 
            lobby () 

def bedroom():
    print "you are in the bedroom"
   command = prompt ()
if command == "SOUTH":
    lobby ()
    elif command == "BED":
        print "you got to the bedroom"
        bedroom()
        elif:
            bedroom ()
            
            start()

