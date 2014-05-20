#from http://www.weitz.de/einstein.html

#There are five houses in five different colors starting from left to right.
#In each house lives a person of a different nationality. These owners all drink
#a certain type of beverage, play a certain sport, and keep a certain type of pet.
#No two owners have the same pet, play the same sport, or drink the same beverage.

#Question: WHO OWNS THE FISH???

#Hints:

#    1. The Brit lives in the red house
#    2. The Swede keeps dogs as pets
#    3. The Dane drinks tea
#    4. The green house is immediately on the left of the white house
#    5. The green house's owner drinks coffee
#    6. The person who plays volleyball rears birds
#    7. The owner of the yellow house plays basketball
#    8. The man living in the center house drinks milk
#    9. The Norwegian lives in the first house
#    10. The person who plays baseball lives next to the one who keeps cats
#    11. The person who keeps horses lives next to the person who plays basketball
#    12. The person who plays soccer drinks soda
#    13. The German plays football
#    14. The Norwegian lives next to the blue house
#    15. The person who plays baseball has a neigbor who drinks water

nationalities = [ "Brit", "Swede", "Dane", "Norwegian", "German" ]
colors = [ "green", "yellow", "red", "blue", "white" ]
pets = [ "birds", "dogs", "cats", "horses", "fish" ]
drinks = [ "tea", "water", "coffee", "milk", "soda" ]
sports = [ "volleyball", "baseball", "basketball", "soccer", "football" ]

#calculate all the possibilities
all_possible = []

#we will add in the format:
#
#                first house                                 second house                             third house                           fourth house                             fifth house                       
#     [(nationality, color, pet, drink, sport), (nationality, color, pet, drink, sport), (nationality, color, pet, drink, sport), (nationality, color, pet, drink, sport), (nationality, color, pet, drink, sport) ]


import itertools #Python 2.6 and above
nationality_permutations = list(itertools.permutations(nationalities))
color_permutations = list(itertools.permutations(colors))
pet_permutations = list(itertools.permutations(pets))
drink_permutations = list(itertools.permutations(drinks))
sport_permutations = list(itertools.permutations(sports))


def calculateAllPossible():
    for nationality_perm_index in range(len(nationality_permutations)):
        nationality_order = nationality_permutations[nationality_perm_index]

        for color_perm_index in range(len(color_permutations)):
            color_order = color_permutations[color_perm_index]
        
            for pet_perm_index in range(len(pet_permutations)):
                pet_order = pet_permutations[pet_perm_index]

                for drink_perm_index in range(len(drink_permutations)):
                    drink_order = drink_permutations[drink_perm_index]

                    for sport_perm_index in range(len(sport_permutations)):
                        sport_order = sport_permutations[sport_perm_index]
                        
                        all_possible.append([ (nationality_order[0],color_order[0],pet_order[0],drink_order[0],sport_order[0]), 
                                              (nationality_order[1],color_order[1],pet_order[1],drink_order[1],sport_order[1]),
                                              (nationality_order[2],color_order[2],pet_order[2],drink_order[2],sport_order[2]),
                                              (nationality_order[3],color_order[3],pet_order[3],drink_order[3],sport_order[3]),
                                              (nationality_order[4],color_order[4],pet_order[4],drink_order[4],sport_order[4]) ] )

                        #if len(all_possible) % 5000000 == 0:
                            #stop = datetime.datetime.now()
                            #elapsed = stop - start
                            #print "5 million in", elapsed.seconds, "seconds"
                        
#can't brute force as there are 28.8 billion possibilities!

#let's filter out what we can before calculating the possibilities
#can apply any hints that just have to do with one type or location: 4, 8, 9

#apply 4th rule
def greenLeftOfWhite():
    #need to make a copy to loop over while removing from original
    color_perm_copy = list(color_permutations)
    #loop over all the possible and find where green and white house are
    for possible_color_order in color_perm_copy:
        for house_index in range(5):
            if possible_color_order[house_index] == "white":
                white_location = house_index
            if possible_color_order[house_index] == "green":
                green_location = house_index
        if green_location + 1 != white_location:
            color_permutations.remove(possible_color_order)
    

greenLeftOfWhite() #removes half the color permutations
print len(color_permutations)

#apply 8th rule
def centerIsMilk():
    #need to make a copy to loop over while removing from original
    drink_perm_copy = list(drink_permutations)
    #loop over all the possible and remove if milk not in the middle
    for possible_drink_order in drink_perm_copy:
        if possible_drink_order[2] != "milk":
            drink_permutations.remove(possible_drink_order)

centerIsMilk()
print len(drink_permutations) #removes 80% of drink permutations

#apply 9th rule
def norwegianFirst():
    #need to make a copy to loop over while removing from original
    nationality_perm_copy = list(nationality_permutations)
    #loop over all the possible and remove if Norwegian is not first
    for possible_nationality_order in nationality_perm_copy:
        if possible_nationality_order[0] != "Norwegian":
            nationality_permutations.remove(possible_nationality_order)

norwegianFirst()
print len(nationality_permutations) #removes 80% of nationality permutations


#STILL TOO MANY SO NEED TO FILTER DOWN POSSIBILITIES FURTHER

#know first isn't red from 9 and 1
def firstNotRed():
    #need to make a copy to loop over while removing from original
    color_perm_copy = list(color_permutations)
    for possible_color_order in color_perm_copy:
        if possible_color_order[0] == "red":
            color_permutations.remove(possible_color_order)

firstNotRed()

#know the first isn't dogs from 9 and 2
def firstNotDogs():
    #need to make a copy to loop over while removing from original
    pet_perm_copy = list(pet_permutations)
    for possible_pet_order in pet_perm_copy:
        if possible_pet_order[0] == "dogs":
            pet_permutations.remove(possible_pet_order)

firstNotDogs()

#know the first isn't tea from 9 and 3
def firstNotTea():
    #need to make a copy to loop over while removing from original
    drink_perm_copy = list(drink_permutations)
    for possible_drink_order in drink_perm_copy:
        if possible_drink_order[0] == "tea":
            drink_permutations.remove(possible_drink_order)

firstNotTea()

#know first isn't football from 9 and 13
def firstNotFootball():
    #need to make a copy to loop over while removing from original
    sport_perm_copy = list(sport_permutations)
    for possible_sport_order in sport_perm_copy:
        if possible_sport_order[0] == "football":
            sport_permutations.remove(possible_sport_order)

firstNotFootball()

#can determine that blue is second house from 9 and 14
def blueSecondHouse():
    #need to make a copy to loop over while removing from original
    color_perm_copy = list(color_permutations)
    for possible_color_order in color_perm_copy:
        if possible_color_order[1] != "blue":
            color_permutations.remove(possible_color_order)

blueSecondHouse() #leaves 12 color permutations

#know the 2nd house isn't the Brit from 9, 14, and 1
def secondNotBrit():
    #need to make a copy to loop over while removing from original
    nationality_perm_copy = list(nationality_permutations)
    for possible_nationality_order in nationality_perm_copy:
        if possible_nationality_order[1] == "Brit":
            nationality_permutations.remove(possible_nationality_order)

#secondNotBrit()

#know the 2nd house owner doesn't play volleyball from 9, 14, and 7
def secondNotVolleyball():
    #need to make a copy to loop over while removing from original
    sport_perm_copy = list(sport_permutations)
    for possible_sport_order in sport_perm_copy:
        if possible_sport_order[1] == "volleyball":
            sport_permutations.remove(possible_sport_order)

#secondNotVolleyball()

#know the center house isn't the Dane from 8 and 3
def centerNotDane():
    #need to make a copy to loop over while removing from original
    nationality_perm_copy = list(nationality_permutations)
    for possible_nationality_order in nationality_perm_copy:
        if possible_nationality_order[2] == "Dane":
            nationality_permutations.remove(possible_nationality_order)

centerNotDane()

#know the center house isn't green from 8 and 5
def centerNotGreen():
    #need to make a copy to loop over while removing from original
    color_perm_copy = list(color_permutations)
    for possible_color_order in color_perm_copy:
        if possible_color_order[2] == "green":
            color_permutations.remove(possible_color_order)

centerNotGreen()

#know middle isn't soccer from 8 and 12
def middleNotSoccer():
    #need to make a copy to loop over while removing from original
    sport_perm_copy = list(sport_permutations)
    for possible_sport_order in sport_perm_copy:
        if possible_sport_order[2] == "soccer":
            sport_permutations.remove(possible_sport_order)

middleNotSoccer()

#know the house on the right isn't coffee from 4 and 5
def rightNotCoffee():
    #need to make a copy to loop over while removing from original
    drink_perm_copy = list(drink_permutations)
    for possible_drink_order in drink_perm_copy:
        if possible_drink_order[4] == "coffee":
            drink_permutations.remove(possible_drink_order)

rightNotCoffee()


print "here they are:", len(color_permutations),len(nationality_permutations),len(drink_permutations),len(sport_permutations),len(pet_permutations)

#print out how many possibilities there are
print "permutations: ", len(color_permutations)*len(nationality_permutations)*len(drink_permutations)*len(sport_permutations)*len(pet_permutations)


import datetime
start = datetime.datetime.now()
calculateAllPossible()
stop = datetime.datetime.now()
elapsed = stop - start
print "Calculated all possibilities in", elapsed.seconds, "seconds"



#apply all matching rules at once: 1,2,3,5,6,7,12,13
def applyAllMatchingRules():
    #need to make a copy to loop over while remove from original
    all_possible_copy = list(all_possible)
    for possible_answer in all_possible_copy:
        #for house_index in range(5):
        #    house = possible_answer[house_index]
            house = possible_answer[0]
            if ( (house[0] == "Brit" and house[1] != "red") or
                (house[0] == "Swede" and house[2] != "dogs") or
                (house[0] == "Dane" and house[3] != "tea") or
                (house[1] == "green" and house[3] != "coffee") or
                (house[2] == "birds" and house[4] != "volleyball") or
                (house[1] == "yellow" and house[4] != "basketball") or
                (house[3] == "soda" and house[4] != "soccer") or
                (house[0] == "German" and house[4] != "football") ):
                    all_possible.remove(possible_answer)
                   # break #can break because if one of the houses is wrong, don't have to check the rest


#apply all matching rules at once: 1,2,3,5,6,7,12,13
def applyAllMatchingRules2():
    for index in range(100000):
        possible_answer = all_possible[index]
        for house_index in range(5):
            house = possible_answer[house_index]
            if ( (house[0] == "Brit" and house[1] != "red") or
                (house[0] == "Swede" and house[2] != "dogs") or
                (house[0] == "Dane" and house[3] != "tea") or
                (house[1] == "green" and house[3] != "coffee") or
                (house[2] == "birds" and house[4] != "volleyball") or
                (house[1] == "yellow" and house[4] != "basketball") or
                (house[3] == "soda" and house[4] != "soccer") or
                (house[0] == "German" and house[4] != "football") ):
                    all_possible.remove(possible_answer)
                    break #can break because if one of the houses is wrong, don't have to check the rest
                
                
#start = datetime.datetime.now()
#applyAllMatchingRules2()
#print len(all_possible)

#stop = datetime.datetime.now()
#elapsed = stop - start
#print "Filtered in", elapsed.seconds, "seconds"


#THAT IS TOO SLOW! REMOVE ISN'T GOING TO BE FAST ENOUGH, LET'S DO AN ADD


#apply 1st rule
def britInRedHouse():
    for possible_answer in all_possible:
        if ( (possible_answer[0][0] == "Brit" and possible_answer[0][1] == "red") or
             (possible_answer[1][0] == "Brit" and possible_answer[1][1] == "red") or
             (possible_answer[2][0] == "Brit" and possible_answer[2][1] == "red") or
             (possible_answer[3][0] == "Brit" and possible_answer[3][1] == "red") or
             (possible_answer[4][0] == "Brit" and possible_answer[4][1] == "red") ):
            new_all_possible.append(possible_answer)



#there are a lot of matching rules, let's create a function that takes them as inputs
def applyMatchingRule(entire_list, type1, value1, type2, value2):
    new_all_possible = []
    for possible_answer in entire_list:
        if ( (possible_answer[0][type1] == value1 and possible_answer[0][type2] == value2) or
             (possible_answer[1][type1] == value1 and possible_answer[1][type2] == value2) or
             (possible_answer[2][type1] == value1 and possible_answer[2][type2] == value2) or
             (possible_answer[3][type1] == value1 and possible_answer[3][type2] == value2) or
             (possible_answer[4][type1] == value1 and possible_answer[4][type2] == value2) ):
            new_all_possible.append(possible_answer)
    return new_all_possible

result = applyMatchingRule(all_possible,0,"Brit",1,"red") #rule 1
result = applyMatchingRule(result,0,"Swede",2,"dogs") #rule 2
result = applyMatchingRule(result,0,"Dane",3,"tea") #rule 3
result = applyMatchingRule(result,1,"green",3,"coffee") #rule 5
result = applyMatchingRule(result,2,"birds",4,"volleyball") #rule 6
result = applyMatchingRule(result,1,"yellow",4,"basketball") #rule 7
result = applyMatchingRule(result,3,"soda",4,"soccer") #rule 12
result = applyMatchingRule(result,0,"German",4,"football") #rule 13
print "after matching rules, new all possible length:",len(result)


#still have to do "next to" rules: 10, 11, and 15
def applyNextToRule(entire_list, type1, value1, type2, value2):
    new_all_possible = []
    #loop over all the possible and find where the values are
    for possible_answer in entire_list:
        for house_index in range(5):
            if possible_answer[house_index][type1] == value1:
                location1 = house_index
            if possible_answer[house_index][type2] == value2:
                location2 = house_index
        if location1 + 1 == location2 or location1 - 1 == location2:
            new_all_possible.append(possible_answer)
    return new_all_possible

result = applyNextToRule(result, 4, "baseball", 2, "cats") #rule 10
result = applyNextToRule(result, 4, "basketball", 2, "horses") #rule 11
result = applyNextToRule(result, 4, "baseball", 3, "water") #rule 15
print "after next to rules, new all possible length:",len(result)

print result
