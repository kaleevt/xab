print ("welcome  to the game")
print ("""where do you want to go??
1
2
3""")
mya = input ("Type number and enter:")
print ("you chose {0}".format(mya))        
if mya == "1":
    print ("You got to the forest")
    elif mya == "2":
        print ("You go underwater")
        elif mya == "3":
            print ("You go to space")
            else:
                print ("wrong key pressed)"
                