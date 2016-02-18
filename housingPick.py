#!/usr/bin/python
#requires python3 'cause it's the future!
campus-housing = [
  { "name":"Abel", "type":"Traditional Dorm", "break-housing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":1004},
  { "name": "Burr", "type":"Traditional Dorm", "break-housing":False, "campus":"east", "minRoom":1, "maxRoom":2, "cost":" $ 9,976.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":222},
  { "name":"Fedde", "type":"Traditional Dorm", "break-housing":True, "campus":"east", "minRoom":1, "maxRoom":2, "cost":" $ 10,176.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":39},
  { "name":"Harper", "type":"Traditional Dorm", "break-housing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":450},
  { "name":"Husker", "type":"Traditional Dorm", "break-housing":True, "campus":"city", "minRoom":1, "maxRoom":1, "cost":" $ 6,511.00 ", "meal-plan":False, "special":"", "upperClass":True, "occupants":41},
  { "name":"Kauffman", "type":"Traditional Dorm", "break-housing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" N/A ", "meal-plan":True, "special":"Raikes Program", "upperClass":False, "occupants":"N/A"},
  { "name":"Love ", "type":"Traditional Dorm", "break-housing":False, "campus":"east", "minRoom":1, "maxRoom":2, "cost":" $ 3,682.00 ", "meal-plan":False, "special":"Female only", "upperClass":False, "occupants":45},
 { "name": "Neihardt", "type":"Traditional Dorm", "break-housing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,457.00 ", "meal-plan":True, "special":"Honors Program", "upperClass":False, "occupants":462},
  { "name":"Pound", "type":"Traditional Dorm", "break-housing":True, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,176.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":228},
  { "name":"Sandoz", "type":"Traditional Dorm", "break-housing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":401},
  { "name":"Schramm", "type":"Traditional Dorm", "break-housing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":450},
  { "name":"Selleck", "type":"Traditional Dorm", "break-housing":True, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,657.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":612},
  { "name":"Smith", "type":"Traditional Dorm", "break-housing":False, "campus":"city", "minRoom":1, "maxRoom":2, "cost":" $ 10,670.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":450},
 { "name": "Knoll Residentrial Center", "type":"Suite-Style", "break-housing":True, "campus":"city", "minRoom":2, "maxRoom":4, "cost":" $ 11,204.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":565},
  { "name":"University Suites", "type":"Suite-Style", "break-housing":True, "campus":"city", "minRoom":2, "maxRoom":4, "cost":" $ 11,204.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":512},
  { "name":"Eastside Suites", "type":"Suite-Style", "break-housing":True, "campus":"city", "minRoom":2, "maxRoom":4, "cost":" $ 11,204.00 ", "meal-plan":True, "special":"", "upperClass":False, "occupants":513},
  { "name":"The Courtyards", "type":"Apartment-Style", "break-housing":True, "campus":"city", "minRoom":2, "maxRoom":4, "cost":" $ 7,148.00 ", "meal-plan":False, "special":"", "upperClass":True, "occupants":478},
  { "name":"The Village", "type":"Apartment-Style", "break-housing":True, "campus":"city", "minRoom":2, "maxRoom":4, "cost":" $ 7,148.00 ", "meal-plan":False, "special":"", "upperClass":True, "occupants":526}
]

off-campus-housing = [
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

def on-campus():
  '''leads user through on campus specific questions'''
  campus-choice = input("So you like the campus life. Which campus, East or City? ")
  house-pref = int(input("What's your housing preference? Type 0 for traditional dorm (2 roommates), 1 for suite-style (4 roommates) or 2 for apartment-style (4 roommates). "))
  break-housing = int(input("Do you need break housing? Type 0 if not and 1 if you do. "))
  meal-plan = int(input("Do you need a meal plan? Type 0 if not and 1 if you do. "))
  upper-classman = int(input("Do you want housing that's more geared for upperclassmen? Type 0 if not and 1 if you do. "))
  special-opp = int(input("Are you interested in any special housing programs? Type 0 if not and 1 if you do. "))
  on-length = len(campus-housing)
  if special-opp == 1:
    count = 0
    for i in range(on-length):
      if campus-housing[i]["special"] != '':
        print("{0}. {1}".format(count, campus-housing[i]["special"]))
        count += 1
    opp-choice = int(input("If interested, select one of the options above by typing its number. If not enter a larger number. "))
  print("-------------------------------")
  print("Calculating your options now.")
  if house-pref == 0:
    house-pref = "Traditional Dorm"
  elif house-pref == 1:
    house-pref = "Suite-Style"
  elif house-pref == 2:
    house-pref = "Apartment-Style"
  if special-opp == 1:
    if opp-choice == 0:
      opp-choice = "Female Only"
    elif opp-choice == 1:
      opp-choice = "Raikes Program"
    elif opp-choice == 2:
      opp-choice = "Honors Program"
  else:
    opp-choice = ''
  user-choice = {"type": house-pref, "break-housing": bool(break-housing), "campus": campus-choice.lower(), "meal-plan": bool(meal-plan), "special": opp-choice, "upperClass": bool(upper-classman)}
  matched = {}
  for i in range(on-length):
    matches = 0
    if campus-housing[i]["campus"] == user-choice['campus']:
      matches += 1
    if campus-housing[i]["special"] == user-choice['special'] and user-choice['special'] != '':
      matches += 2
    if campus-housing[i]["type"] == user-choice['type']:
      matches += 1
    if campus-housing[i]["break-housing"] == user-choice['break-housing']:
      matches += 1
    if campus-housing[i]["meal-plan"] == user-choice['meal-plan']:
      matches += 1
    if campus-housing[i]["upperClass"] == user-choice['upperClass']:
      matches += 1
    matched[campus-housing[i]['name']] = matches
  options = [key for key,val in matched.items() if val == max(matched.values())]
  print("Here are your options: ")
  for option in options:
    indexed = {}
    num = 0
    for i in range(on-length):
      if campus-housing[i]['name'] == option:
        num = i
    indexed[option] = num
    print("{name} \n This {typed} housing option {breakOption} break housing is on {campus} campus with a minimum number of {minR} roommate(s) and a maximum of {maxR} roommates. The standard occpancy cost is {cost}, and this housing option {meal-plan} with {specialOption}. This residence {upper} upperclassmen and has {num} occupants.".format(name = option, typed = campus-housing[indexed[option]]["type"], breakOption="with" if campus-housing[indexed[option]]["break-housing"] == True else "without", campus = campus-housing[indexed[option]]["campus"],minR = campus-housing[indexed[option]]["minRoom"], maxR = campus-housing[indexed[option]]["maxRoom"], cost = campus-housing[indexed[option]]["cost"].strip(), meal-plan = "offers a meal plan" if campus-housing[indexed[option]]["meal-plan"] == True else "offers no meal plan", specialOption = "no special housing options" if campus-housing[indexed[option]]["special"] == "" else campus-housing[indexed[option]]["special"], upper = "is geared toward" if campus-housing[indexed[option]]["upperClass"] == True else "isn't geared toward", num = campus-housing[indexed[option]]["occupants"]))
    print("-------------------------------")



def off-campus():
  '''leads user through off campus questions'''
  print("Hooray for the freedom and also the chance to save some money. These ranges are based on percentiles in our selection of apartments.")
  prices = ["$254 to $342", "$343 to $625", "$626 to $701", "$702 to $1324"]
  for i,e in enumerate(prices):
    print("{0}. {1} per month per bed".format(i, prices[i]))
  price-range = int(input("Select your price level by typing in that level's number. "))
  campus-choice = input('Which campus would you rather be closer to? East or City? ')
  roomates = int(input('How many roommates? Type 0 for no roommates, and the max is 4. '))
  print("-------------------------------")
  print("Calculating your options now.")
  if price-range == 0:
    price-pref = 254
  elif price-range == 1:
    price-pref = 343
  elif price-range == 2:
    price-pref = 626
  elif price-range == 3:
    price-pref = 702
  user-choice = {'price': price-pref, "campus": campus-choice.lower(), 'roomMates': roomates}
  matched = {}
  off-length = len(off-campus-housing)
  for i in range(off-length):
    matches = 0
    if off-campus-housing[i]['minCost'] <= user-choice['price'] <= off-campus-housing[i]['maxCost']:
      matches += 1
    if off-campus-housing[i]['minRoom'] <= user-choice['roomMates'] <= off-campus-housing[i]['maxRoom']:
      matches += 1
    if off-campus-housing[i]['campus'] == user-choice['campus']:
      matches += 1
    if matches > 0:
      matched[off-campus-housing[i]['name']] = matches
  print("Here are your options: ")
  options = [key for key,val in matched.items() if val == max(matched.values())]
  for option in options:
    indexed ={}
    num = 0
    for i in range(off-length):
      if off-campus-housing[i]['name'] == option:
        num = i
    indexed[option] = num
    print("{0} \n This housing option has roommate options from {1} to {2} (0 denotes a studio apartment). Although costs vary given the number of roommates, this option has a minimum rent of ${3} per bed per month and maximum of ${4} per bed per month. This apartment is located closer to {5} campus and is only {6} miles from city campus and {7} miles from east campus.".format(option, off-campus-housing[indexed[option]]["minRoom"],off-campus-housing[indexed[option]]["maxRoom"], off-campus-housing[indexed[option]]["minCost"], off-campus-housing[indexed[option]]["maxCost"], off-campus-housing[indexed[option]]["campus"], off-campus-housing[indexed[option]]["cityMiles"], off-campus-housing[indexed[option]]["eastMiles"]))
    print("-------------------------------")



print("-------------------------------")
print("Hello, welcome to the UNL Student Housing Quiz!\n After a few short questions, you will receive recommendations on which on or off campus living spaces you should check out.\n   Enjoy!")
print("-------------------------------")
campus-pref = input("Do you want to live on or off campus? If on campus, type on and vice versa. ")
if campus-pref.lower() == 'on':
  print("Although housing on campus has its perks, it's hard to decide which housing is right for you.\n From housing style to roommate struggles, no feature is too small to check.")
  on-campus()
elif campus-pref.lower() == 'off':
  off-campus()
else:
  print("Fail. Try to run the program again.")
