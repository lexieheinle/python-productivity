#!/usr/bin/python
#requires python3 'cause it's the future!
campusHousing = {
  "Abel": { "type":"Traditional Dorm", "breakHousing":False, "campus":"City", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":1004},
  "Burr": { "type":"Traditional Dorm", "breakHousing":False, "campus":"East", "minRoom":1, "maxRoom":2, "cost":" $ 9,976.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":222},
  "Fedde": { "type":"Traditional Dorm", "breakHousing":True, "campus":"East", "minRoom":1, "maxRoom":2, "cost":" $ 10,176.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":39},
  "Harper": { "type":"Traditional Dorm", "breakHousing":False, "campus":"City", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":450},
  "Husker": { "type":"Traditional Dorm", "breakHousing":True, "campus":"City", "minRoom":1, "maxRoom":1, "cost":" $ 6,511.00 ", "mealPlan":False, "special":"", "upperClass":True, "occupants":41},
  "Kauffman": { "type":"Traditional Dorm", "breakHousing":False, "campus":"City", "minRoom":1, "maxRoom":2, "cost":" N/A ", "mealPlan":True, "special":"Raikes Program", "upperClass":False, "occupants":"N/A"},
  "Love ": { "type":"Traditional Dorm", "breakHousing":False, "campus":"East", "minRoom":1, "maxRoom":2, "cost":" $ 3,682.00 ", "mealPlan":False, "special":"Female", "upperClass":False, "occupants":45},
  "Neihardt": { "type":"Traditional Dorm", "breakHousing":False, "campus":"City", "minRoom":1, "maxRoom":2, "cost":" $ 10,457.00 ", "mealPlan":True, "special":"Honors Program", "upperClass":False, "occupants":462},
  "Pound": { "type":"Traditional Dorm", "breakHousing":True, "campus":"City", "minRoom":1, "maxRoom":2, "cost":" $ 10,176.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":228},
  "Sandoz": { "type":"Traditional Dorm", "breakHousing":False, "campus":"City", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":401},
  "Schramm": { "type":"Traditional Dorm", "breakHousing":False, "campus":"City", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":450},
  "Selleck": { "type":"Traditional Dorm", "breakHousing":True, "campus":"City", "minRoom":1, "maxRoom":2, "cost":" $ 10,657.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":612},
  "Smith": { "type":"Traditional Dorm", "breakHousing":False, "campus":"City", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":450},
  "Knoll Residentrial Center": { "type":"Suite-Style", "breakHousing":True, "campus":"City", "minRoom":2, "maxRoom":4, "cost":" $ 11,204.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":565},
  "University Suites": { "type":"Suite-Style", "breakHousing":True, "campus":"City", "minRoom":2, "maxRoom":4, "cost":" $ 11,204.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":512},
  "Eastside Suites": { "type":"Suite-Style", "breakHousing":True, "campus":"City", "minRoom":2, "maxRoom":4, "cost":" $ 11,204.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":513},
  "The Courtyards": { "type":"Apartment-Style", "breakHousing":True, "campus":"City", "minRoom":2, "maxRoom":4, "cost":" $ 7,148.00 ", "mealPlan":False, "special":"", "upperClass":True, "occupants":478},
  "The Village": { "type":"Apartment-Style", "breakHousing":True, "campus":"City", "minRoom":2, "maxRoom":4, "cost":" $ 7,148.00 ", "mealPlan":False, "special":"", "upperClass":True, "occupants":526}
}

def onCampus():
  '''leads user through on campus specific questions'''
  campusChoice = input("So you like the campus life. Which campus, East or City?")
  housePref = eval(input("What's your housing preference? Type 0 for traditional dorm (2 roommates), 1 for suite-style (4 roommates) or 2 for apartment-style (4 roommates). "))
  breakHousing = eval(input("Do you need break housing? Type 0 if not and 1 if you do. "))
  mealPlan = eval(input("Do you need a meal plan? Type 0 if not and 1 if you do. "))
  upperClassman = eval(input("Do you want housing that's more geared for upperclassmen? Type 0 if not and 1 if you do. "))
  specialOpp = eval(input("Are you interested in any special housing programs? Type 0 if not and 1 if you do. "))
  if specialOpp == 1:
    count = 0
    for key, val in campusHousing.items():
      #print("{} = {}".format(key, val))
      if val["special"] != '':
        print("{}. {}".format(count, val["special"]))
        count += 1
  oppChoice = input("If interested, select one of the options above by typeing its number. If not enter a larger number. ")
  print("-------------------------------")
  print("Calculating your options now.")
  if housePref == 0:
    housePref = "Traditional Dorm"
  elif housePref == 1:
    housePref = "Suite-Style"
  elif housePref == 2:
    housePref = "Apartment-Style"
  if oppChoice == 0:
    oppChoice = "Female"
  elif oppChoice == 1:
    oppChoice = "Raikes Program"
  elif oppChoice == 2:
    oppChoice = "Honors Program"
  else:
    oppChoice = ""
  userChoice = {"type": bool(housePref), "breakHousing": bool(breakHousing), "campus": campusChoice, "mealPlan": bool(mealPlan), "special": oppChoice, "upperClass": bool(upperClassman)}
  print(userChoice)
  matched = {}
  for key, val in campusHousing.items():
    matches = 0
    for smkey, smval in val.items():
      for ukey, uval in userChoice.items():
        #print("{} = {}".format(smkey, smval))
        #print("{} = {}".format(ukey, uval))
        if smkey == "campus" and smval != uval:
          break
        if smkey == ukey and smval == uval:
          print("{} = {}".format(smkey, smval))
          print("{} = {}".format(ukey, uval))
          matches += 1
    matched[key] = matches
  print(matched)
  options = [key for key,val in matched.items() if val == max(matched.values())]
  print("Here are your options: ")
  for option in options:
    print("{name} \n This {typed} housing option {breakOption} break housing is on {campus} campus with a minimum number of {minR} roomates and a maximum of {maxR} roommates. The standard occpancy cost is {cost}, and this housing option {mealPlan} with {specialOption}. This residence {upper} upperclassmen and has {num} occupants.".format(name = option, typed = campusHousing[option]["type"], breakOption="with" if campusHousing[option]["breakHousing"] == True else "without", campus = campusHousing[option]["campus"],minR = campusHousing[option]["minRoom"], maxR = campusHousing[option]["maxRoom"], cost = campusHousing[option]["cost"], mealPlan = "offers a meal plan" if campusHousing[option]["mealPlan"] == True else "offers no meal plan", specialOption = "no special housing options" if campusHousing[option]["special"] == "" else campusHousing[option]["special"], upper = "is geared toward" if campusHousing[option]["upperClass"] == True else "isn't geared toward", num = campusHousing[option]["occupants"]))
    print("-------------------------------")  
        
def offCampus():
  '''leads user through off campus questions'''
  print("Hooray for the freedom and also the chance to save some money. Choose your level of frugrity below by tying in the level's name.")
  prices = {'Scrooge': "$100 to $200 per month", 'Cameron': '$201 to $300 per month', 'Pretty in Pink Star': '$301 to $400 per month'}
  for character, price in prices.items():
    print("{} pays {}.".format(character, price))
  priceRange = input("Which fictional character do you relate most to? ")
print("-------------------------------")
print("Hello, welcome to the UNL Student Housing Quiz!\n After a few short questions, you will receive recommendations on which on-/off-campus living spaces you should check out.\n   Enjoy!")
print("-------------------------------")
campusPref = input("Do you want to live on or off campus? If on-campus, type on and vice versa. ")
if campusPref.lower() == 'on':
  print("Although housing on campus has its perks, it's hard to decide which housing is right for you.\n From housing style to tendency for higher MPIs per bed, no feature is too small to check.")
  onCampus()
elif campusPref.lower() == 'off':
  offCampus()
else:
  print("Fail. Try to run the program again.")
  