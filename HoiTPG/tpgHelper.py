# Small proejct to get myself back on track

# I want it to be able to calculate a state's status after each tick of resistance.
# Like, have it make a table for it, given its stats.

import math



class State:

    def __init__ (self, name, factories, defense, resistance, rebellion):
        self.name, self.factories, self.defense, self.resistance, self.rebellion = name, factories, defense, resistance, rebellion
        

# Variables
working = True
writeString = ""
states = []


# get Factories
print ("What's the factory count, the defense percentage and the resistance?")
while working:
    factories = input()
    
    try:
        factories = float(factories)
        working = False
    except:
        print ("Factory count needs to be an int.")


# get Defense
working = True
print ("Good, good. The defense?")
while working:
    defense = input()
    
    try:
        defense = float(defense)
        working = False
    except:
        print ("Defense percentage needs to be an int.")


# get Resistance
working = True
print ("Lastly, the resistance percentage.")
while working:
    resistance = input()
    
    try:
        resistance = float(resistance)
        baseResist = resistance
        working = False
    except:
        print ("Resistance percentage needs to be an int.")


print ("Result:")
for x in range (0, round (resistance / 5) + 1):
    writeString += ("Name - Resistance at: " + str(resistance) + "\tFactories: [" + str(round(factories * resistance * 0.01)) + "/" + str(round(factories)) + "]\tDefense: [" + str(round (defense * resistance * 0.01)) + "/" + str(round(defense)) + "]\n")
    print ("Name - Resistance at: ", resistance, "\tFactories: [", round(factories * resistance * 0.01), "/", round(factories), "]", "\tDefense: [", round (defense * resistance * 0.01), "/", round(defense), "]", sep = '')
    resistance = resistance - 5


# writing to file
fileReader = open("HoiTPG.txt", "r")
# this is all the doc's lines printed
line = fileReader.readline()
print ("\n\nFILE: \n===================")
while line:
    print (line)
    
    if (line.find("-") < 0):
        print ("Wrong format!")
    else:
        stateName = line[0:line.find("-")]
        line = line[line.find("-") + 2:]
        print ("mod", line)
        
    #if (
    states.append(State(stateName, 10, 40, 50, 30))
    line = fileReader.readline()
print ("============\n", fileReader.readline())
fileReader.close()


fileWriter = open("HoiTPG.txt", "w")
#thingy = "Resistance at: " + str(baseResist) + "\tFactories: [" + str(round(factories*baseResist*0.01)) + "/" + str(round(factories)) + "]" + "\tDefense: [" + str(round(defense*baseResist*0.01)) + "/" + str(round(defense)) + "]"
#fileWriter.write(thingy)
#fileWriter.write("\n")
fileWriter.write(writeString)
fileWriter.close()


print ("name is", stateName)


print ("Howdy!")




# HANDY STUFF


# example stuff
# Southern Kora - Plains [4(9)F | 11 (20)% D], Resistance 45%

# how to input 
# input1 = input() 