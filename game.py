def start():
    print "welcome"
    global gold 
    gold = 0
    lobby()

def prompt ():
    x = raw_input("type a command")    
    return x


    def lobby():
        print "you are in the lobby"
        command = prompt ()
        if command == "NORTH":
            bedroom()
        
                elif:
                    lobby()
                    
    def bedroom():
        global gold
        print "You are in the bedroom"
        command = prompt()
        if command == "SOUTH":
            lobby()
            elif command == "BED":
                print "You go to the bed and find nothing"
                bedroom()
                elif command == "TABLE": 
                print "You go to the table and find 50 gold"
                gold = gold + 50
                bedroom()
                elif command == "GOLD":
                    currentGold()
                    bedroom()
                    elif:
                        bedroom()
                        
                        start() 