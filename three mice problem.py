#from http://www.weitz.de/einstein.html

#Our problem consists of three mice living next to each other in three holes in
#the wall. Each mouse has a favorite cheese flavor and a favorite TV show. No
#two mice have the same favorite cheese or TV show.

#QUESTION: WHERE DOES MICKEY MOUSE LIVE?

#Hints:

#    1. Mickey Mouse loves Gouda
#    2. Mighty Mouse's favorite TV show is Emergency Room
#    3. The mouse that lives in the left hole never misses an episode of Seinfeld
#    4. Mickey Mouse and Mighty Mouse have one mouse hole between them
#    5. The Simpsons fan does not live on the left of the Brie lover 

names = ["Mickey Mouse", "Mighty Mouse", "Mouse 3"]
cheeses = ["Gouda", "Brie", "Cheese 3"]
shows = ["Emergency Room", "Seinfeld", "The Simpsons"]

#calculate all the possibilities
all_possible = []

#we will add in the format:
#
#                #left hole            #middle hole         #right hole
#           [(name, cheese, show), (name, cheese, show), (name, cheese, show)]

import itertools #Python 2.6 and above
name_permutations = list(itertools.permutations(names))
cheese_permutations = list(itertools.permutations(cheeses))
show_permutations = list(itertools.permutations(shows))

#print name_permutations
#[('Mickey Mouse', 'Mighty Mouse', 'Mouse 3'),
# ('Mickey Mouse', 'Mouse 3', 'Mighty Mouse'),
# ('Mighty Mouse', 'Mickey Mouse', 'Mouse 3'),
# ('Mighty Mouse', 'Mouse 3', 'Mickey Mouse'),
# ('Mouse 3', 'Mickey Mouse', 'Mighty Mouse'),
# ('Mouse 3', 'Mighty Mouse', 'Mickey Mouse')]

def calculateAllPossible():
    for name_perm_index in range(6):
        name_order = name_permutations[name_perm_index]
        #print name_order
        #this name order needs to be paired up with all the cheese possibilities

        for cheese_perm_index in range(6):
            cheese_order = cheese_permutations[cheese_perm_index]
            #to view all the combos side by side:
            #print name_order, cheese_order

            #to add just the name and cheese combos to our all_possible list
            #all_possible.append([ (name_order[0],cheese_order[0]),(name_order[1],cheese_order[1]),(name_order[2],cheese_order[2]) ])

            #this name and cheese order has to be paired with all the show possibilities as well
            for show_perm_index in range(6):
                show_order = show_permutations[show_perm_index]
                #to view all the combos side by side:
                #print name_order, cheese_order, show_order

                #add them all to our list
                all_possible.append([ (name_order[0],cheese_order[0],show_order[0]),(name_order[1],cheese_order[1],show_order[1]),(name_order[2],cheese_order[2],show_order[2]) ])
     
calculateAllPossible()
print len(all_possible)

#apply first hint
def mickeyGouda():
    #need to make a copy to loop over while remove from original
    all_possible_copy = list(all_possible)
    #loop over all the possible answers and remove any where Mickey isn't paired with Gouda
    for possible_answer in all_possible_copy:
        for mouse_index in range(3):
            mouse = possible_answer[mouse_index]
            if mouse[0] == "Mickey Mouse":
                if mouse[1] != "Gouda":
                    all_possible.remove(possible_answer)

mickeyGouda()
print len(all_possible)

#apply second hint
def mightyEmergencyRoom():
    #need to make a copy to loop over while remove from original
    all_possible_copy = list(all_possible)
    #loop over all the possible answers and remove any where Mighty isn't paired with Emergency Room
    for possible_answer in all_possible_copy:
        for mouse_index in range(3):
            mouse = possible_answer[mouse_index]
            if mouse[0] == "Mighty Mouse":
                if mouse[2] != "Emergency Room":
                    all_possible.remove(possible_answer)

mightyEmergencyRoom()
print len(all_possible)

#apply third hint
def leftSeinfeld():
    #need to make a copy to loop over while remove from original
    all_possible_copy = list(all_possible)
    #loop over all the possible answers and remove any where left isn't paired with Seinfeld
    for possible_answer in all_possible_copy:
        left_mouse = possible_answer[0] #left hole is the 0 spot
        if left_mouse[2] != "Seinfeld":
            all_possible.remove(possible_answer)

leftSeinfeld()
print len(all_possible)

#apply fourth hint
def mouse3InMiddle():
#need to make a copy to loop over while remove from original
    all_possible_copy = list(all_possible)
    #loop over all the possible answers and remove any where middle isn't Mouse 3
    for possible_answer in all_possible_copy:
        middle_mouse = possible_answer[1] #middle hole is the 0 spot
        if middle_mouse[0] != "Mouse 3":
            all_possible.remove(possible_answer)

mouse3InMiddle()
print len(all_possible)

#apply fifth hint
def simpsonsNotLeftOfBrie():
    #need to make a copy to loop over while remove from original
    all_possible_copy = list(all_possible)
    #loop over all the possible answers and find where Simpsons and Brie fans are
    for possible_answer in all_possible_copy:
        for mouse_index in range(3):
            mouse = possible_answer[mouse_index]
            if mouse[2] == "The Simpsons":
                simpsons_location = mouse_index
        for mouse_index in range(3):
            mouse = possible_answer[mouse_index]
            if mouse[1] == "Brie":
                brie_location = mouse_index
        if simpsons_location < brie_location:
            all_possible.remove(possible_answer)

simpsonsNotLeftOfBrie()
print all_possible
