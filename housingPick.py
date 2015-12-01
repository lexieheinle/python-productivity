#!/usr/bin/python
#requires python3 'cause it's the future!
campusHousing = [
  { "name":"Abel", "type":"Traditional Dorm", "breakHousing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":1004},
  { "name": "Burr", "type":"Traditional Dorm", "breakHousing":False, "campus":"east", "minRoom":1, "maxRoom":2, "cost":" $ 9,976.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":222},
  { "name":"Fedde", "type":"Traditional Dorm", "breakHousing":True, "campus":"east", "minRoom":1, "maxRoom":2, "cost":" $ 10,176.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":39},
  { "name":"Harper", "type":"Traditional Dorm", "breakHousing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":450},
  { "name":"Husker", "type":"Traditional Dorm", "breakHousing":True, "campus":"city", "minRoom":1, "maxRoom":1, "cost":" $ 6,511.00 ", "mealPlan":False, "special":"", "upperClass":True, "occupants":41},
  { "name":"Kauffman", "type":"Traditional Dorm", "breakHousing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" N/A ", "mealPlan":True, "special":"Raikes Program", "upperClass":False, "occupants":"N/A"},
  { "name":"Love ", "type":"Traditional Dorm", "breakHousing":False, "campus":"east", "minRoom":1, "maxRoom":2, "cost":" $ 3,682.00 ", "mealPlan":False, "special":"Female only", "upperClass":False, "occupants":45},
 { "name": "Neihardt", "type":"Traditional Dorm", "breakHousing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,457.00 ", "mealPlan":True, "special":"Honors Program", "upperClass":False, "occupants":462},
  { "name":"Pound", "type":"Traditional Dorm", "breakHousing":True, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,176.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":228},
  { "name":"Sandoz", "type":"Traditional Dorm", "breakHousing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":401},
  { "name":"Schramm", "type":"Traditional Dorm", "breakHousing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":450},
  { "name":"Selleck", "type":"Traditional Dorm", "breakHousing":True, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,657.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":612},
  { "name":"Smith", "type":"Traditional Dorm", "breakHousing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":450},
 { "name": "Knoll Residentrial Center", "type":"Suite-Style", "breakHousing":True, "campus":"city", "minRoom":2, "maxRoom":4, "cost":" $ 11,204.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":565},
  { "name":"University Suites", "type":"Suite-Style", "breakHousing":True, "campus":"city", "minRoom":2, "maxRoom":4, "cost":" $ 11,204.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":512},
  { "name":"Eastside Suites", "type":"Suite-Style", "breakHousing":True, "campus":"city", "minRoom":2, "maxRoom":4, "cost":" $ 11,204.00 ", "mealPlan":True, "special":"", "upperClass":False, "occupants":513},
  { "name":"The Courtyards", "type":"Apartment-Style", "breakHousing":True, "campus":"city", "minRoom":2, "maxRoom":4, "cost":" $ 7,148.00 ", "mealPlan":False, "special":"", "upperClass":True, "occupants":478},
  { "name":"The Village", "type":"Apartment-Style", "breakHousing":True, "campus":"city", "minRoom":2, "maxRoom":4, "cost":" $ 7,148.00 ", "mealPlan":False, "special":"", "upperClass":True, "occupants":526}
]

offcampusHousing = [
  { "name":"Latitude Apartments", "minRoom":0, "maxRoom":4, "minCost":649, "maxCost":1324, "cityMiles":0.2, "eastMiles":3.3, "campus":"city"},
  { "name":'Canopy Lofts', "minRoom":0, "maxRoom":4, "minCost":625, "maxCost":900, "cityMiles":0.6, "eastMiles":3.8, "campus":"city"},
  { "name":"Claremont Park Apartments", "minRoom":1, "maxRoom":3, "minCost":325, "maxCost":625, "cityMiles":0.8, "eastMiles":3.3, "campus":"city"},
  { "name": "College Park Apartments", "minRoom":1, "maxRoom":3, "minCost":277, "maxCost":659, "cityMiles":5.1, "eastMiles":3.7, "campus":"east"},
  { "name":"Superior Place Apartments", "minRoom":1, "maxRoom":2, "minCost":298, "maxCost":585, "cityMiles":2.5, "eastMiles":4.2, "campus":"city"},
  { "name":"Park Ridge", "minRoom":1, "maxRoom":3, "minCost":285, "maxCost":640, "cityMiles":3.2, "eastMiles":5.1, "campus":"city"},
  { "name":"Deer Park Apartments", "minRoom":1, "maxRoom":3, "minCost":323, "maxCost":699, "cityMiles":3, "eastMiles":4.8, "campus":"city"},
  { "name":"Century House", "minRoom":0, "maxRoom":2, "minCost":540, "maxCost":860, "cityMiles":0.6, "eastMiles":3.4, "campus":"city"},
  { "name":"35 East Apartments", "minRoom":0, "maxRoom":2, "minCost":625, "maxCost":995, "cityMiles":1.7, "eastMiles":0, "campus":"east"},
  { "name":"The Willows Apartments", "minRoom":1, "maxRoom":2, "minCost":310, "maxCost":589, "cityMiles":1.6, "eastMiles":3.2, "campus":"city"},
  { "name":"Folsom Ridge Apartments", "minRoom":1, "maxRoom":3, "minCost":308, "maxCost":695, "cityMiles":3, "eastMiles":5.6, "campus":"city"},
  { "name":"Lakeview Park Apartments", "minRoom":0, "maxRoom":3, "minCost":349, "maxCost":705, "cityMiles":2.8, "eastMiles":5.3, "campus":"city"},
  { "name":"Lakeside Village", "minRoom":1, "maxRoom":3, "minCost":370, "maxCost":810, "cityMiles":3.2, "eastMiles":5.8, "campus":"city"},
  { "name":"The 50/50 Apartments", "minRoom":2, "maxRoom":4, "minCost":620, "maxCost":715, "cityMiles":0.4, "eastMiles":2.3, "campus":"city"},
  {"name": "Mystic Pines Apartments", "minRoom":1, "maxRoom":3, "minCost":285, "maxCost":625, "cityMiles":4.3, "eastMiles":6.8, "campus":"city"},
  { "name": "Thomasbrook Apartments", "minRoom":1, "maxRoom":2, "minCost":348, "maxCost":750, "cityMiles":4.5, "eastMiles":3.9, "campus":"east"},
  { "name":"Willow Creek Apartments", "minRoom":1, "maxRoom":2, "minCost":365, "maxCost":650, "cityMiles":4.9, "eastMiles":3.4, "campus":"east"},
  { 'name': "Northridge Heights", "minRoom":0, "maxRoom":3, "minCost":254, "maxCost":735, "cityMiles":4.1, "eastMiles":4.9, "campus":"city"}
]

def onCampus():
  '''leads user through on campus specific questions'''
  campusChoice = input("So you like the campus life. Which campus, East or City? ")
  housePref = eval(input("What's your housing preference? Type 0 for traditional dorm (2 roommates), 1 for suite-style (4 roommates) or 2 for apartment-style (4 roommates). "))
  breakHousing = eval(input("Do you need break housing? Type 0 if not and 1 if you do. "))
  mealPlan = eval(input("Do you need a meal plan? Type 0 if not and 1 if you do. "))
  upperClassman = eval(input("Do you want housing that's more geared for upperclassmen? Type 0 if not and 1 if you do. "))
  specialOpp = eval(input("Are you interested in any special housing programs? Type 0 if not and 1 if you do. "))
  onLength = len(campusHousing)
  if specialOpp == 1:
    count = 0
    for i in range(onLength):
      if campusHousing[i]["special"] != '':
        print("{}. {}".format(count, campusHousing[i]["special"]))
        count += 1
    oppChoice = eval(input("If interested, select one of the options above by typing its number. If not enter a larger number. "))
  print("-------------------------------")
  print("Calculating your options now.")
  if housePref == 0:
    housePref = "Traditional Dorm"
  elif housePref == 1:
    housePref = "Suite-Style"
  elif housePref == 2:
    housePref = "Apartment-Style"
  if specialOpp == 1:
    if oppChoice == 0:
      oppChoice = "Female Only"
    elif oppChoice == 1:
      oppChoice = "Raikes Program"
    elif oppChoice == 2:
      oppChoice = "Honors Program"
  else:
    oppChoice = ''
  userChoice = {"type": housePref, "breakHousing": bool(breakHousing), "campus": campusChoice.lower(), "mealPlan": bool(mealPlan), "special": oppChoice, "upperClass": bool(upperClassman)}
  matched = {}
  for i in range(onLength):
    matches = 0
    if campusHousing[i]["campus"] == userChoice['campus']:
      matches += 1
    if campusHousing[i]["special"] == userChoice['special'] and userChoice['special'] != '':
      matches += 2
    if campusHousing[i]["type"] == userChoice['type']:
      matches += 1
    if campusHousing[i]["breakHousing"] == userChoice['breakHousing']:
      matches += 1
    if campusHousing[i]["mealPlan"] == userChoice['mealPlan']:
      matches += 1
    if campusHousing[i]["upperClass"] == userChoice['upperClass']:
      matches += 1
    matched[campusHousing[i]['name']] = matches
  options = [key for key,val in matched.items() if val == max(matched.values())]
  print("Here are your options: ")
  for option in options:
    indexed = {}
    num = 0
    for i in range(onLength):
      if campusHousing[i]['name'] == option:
        num = i
    indexed[option] = num
    print("{name} \n This {typed} housing option {breakOption} break housing is on {campus} campus with a minimum number of {minR} roommate(s) and a maximum of {maxR} roommates. The standard occpancy cost is {cost}, and this housing option {mealPlan} with {specialOption}. This residence {upper} upperclassmen and has {num} occupants.".format(name = option, typed = campusHousing[indexed[option]]["type"], breakOption="with" if campusHousing[indexed[option]]["breakHousing"] == True else "without", campus = campusHousing[indexed[option]]["campus"],minR = campusHousing[indexed[option]]["minRoom"], maxR = campusHousing[indexed[option]]["maxRoom"], cost = campusHousing[indexed[option]]["cost"].strip(), mealPlan = "offers a meal plan" if campusHousing[indexed[option]]["mealPlan"] == True else "offers no meal plan", specialOption = "no special housing options" if campusHousing[indexed[option]]["special"] == "" else campusHousing[indexed[option]]["special"], upper = "is geared toward" if campusHousing[indexed[option]]["upperClass"] == True else "isn't geared toward", num = campusHousing[indexed[option]]["occupants"]))
    print("-------------------------------")  
        
      
      
def offCampus():
  '''leads user through off campus questions'''
  print("Hooray for the freedom and also the chance to save some money. These ranges are based on percentiles in our selection of apartments.")
  prices = ["$254 to $342", "$343 to $625", "$626 to $701", "$702 to $1324"]
  for i in range(len(prices)):
    print("{}. {} per month per bed".format(i, prices[i]))
  priceRange = eval(input("Select your price level by typing in that level's number. "))
  campusChoice = input('Which campus would you rather be closer to? East or City? ')
  roomates = eval(input('How many roommates? Type 0 for no roommates, and the max is 4. '))
  print("-------------------------------")
  print("Calculating your options now.")
  if priceRange == 0:
    pricePref = 254
  elif priceRange == 1:
    pricePref = 343
  elif priceRange == 2:
    pricePref = 626
  elif priceRange == 3:
    pricePref = 702
  userChoice = {'price': pricePref, "campus": campusChoice.lower(), 'roomMates': roomates}
  matched = {}
  offLength = len(offcampusHousing)
  for i in range(offLength):
    matches = 0
    if offcampusHousing[i]['minCost'] <= userChoice['price'] <= offcampusHousing[i]['maxCost']:
      matches += 1
    if offcampusHousing[i]['minRoom'] <= userChoice['roomMates'] <= offcampusHousing[i]['maxRoom']:
      matches += 1
    if offcampusHousing[i]['campus'] == userChoice['campus']:
      matches += 1
    if matches > 0:
      matched[offcampusHousing[i]['name']] = matches
  print("Here are your options: ")
  options = [key for key,val in matched.items() if val == max(matched.values())]
  for option in options:
    indexed ={}
    num = 0
    for i in range(offLength):
      if offcampusHousing[i]['name'] == option:
        num = i
    indexed[option] = num
    print("{} \n This housing option has roommate options from {} to {} (0 denotes a studio apartment). Although costs vary given the number of roommates, this option has a minimum rent of ${} per bed per month and maximum of ${} per bed per month. This apartment is located closer to {} campus and is only {} miles from city campus and {} miles from east campus.".format(option, offcampusHousing[indexed[option]]["minRoom"],offcampusHousing[indexed[option]]["maxRoom"], offcampusHousing[indexed[option]]["minCost"], offcampusHousing[indexed[option]]["maxCost"], offcampusHousing[indexed[option]]["campus"], decimal(offcampusHousing[indexed[option]]["cityMiles"]), decimal(offcampusHousing[indexed[option]]["eastMiles"])))
    print("-------------------------------")
  
  
  
print("-------------------------------")
print("Hello, welcome to the UNL Student Housing Quiz!\n After a few short questions, you will receive recommendations on which on or off campus living spaces you should check out.\n   Enjoy!")
print("-------------------------------")
campusPref = input("Do you want to live on or off campus? If on campus, type on and vice versa. ")
if campusPref.lower() == 'on':
  print("Although housing on campus has its perks, it's hard to decide which housing is right for you.\n From housing style to roommate struggles, no feature is too small to check.")
  onCampus()
elif campusPref.lower() == 'off':
  offCampus()
else:
  print("Fail. Try to run the program again.")
  