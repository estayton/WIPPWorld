#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
"WIPP World Bot"
__author__ = "Erik Stayton"
__copyright__ = "Copyright 2016 Stayton"
__lic__ = "CC-BY-SA"
__vnum__ = "0.0.1"
__status__ = 'Alpha'

import random;
import sys;
import os;
import datetime;
import time as systime;
import string;

statics = [
"Discover the magic of #WIPPWorld Resort, where moments and memories have no limits!",
"Sharpen your culinary skills with chef-led demos during the #WIPPWorldFoodFestival! Reserve your special ticket today.",
"Need a reason to visit this year's #WIPPWorldFoodFestival? We've got 10 to get you started!",
"With over 50 new brand-name shops to enjoy, #WIPPWorld is the place to be!",
"Journey down the containment shafts with the #WIPPWorld Blog!",
"Enter our contest for your chance to WIN a ✨trip✨ to #WIPPWorld",
"Introduce your grandkids to the grand kid in you on a WIPP World Resort vacation!",
"Soar high in the sky with our complimentary transportation when you stay at a #WIPPWorld  Resort hotel!",
"Going up? Blowing up! Happy 2nd Anniversary to the Tower of Terror! #WIPPWorld"
]

templates = [
"What makes a trip to #WIPPWorld so special? Just ask The @name Family! #EndlessVigilance",
"It's @aan @adjective good time when little ones ride @ride at #WIPPWorld. Check it out!",
"Fans of @noun inspired cuisine, don't miss the #WIPPWorldFoodFestival! Enjoy all the @nfun until @date!",
"Happy @holiday from #WIPPWorld!",
"See why WIPP World is your place to be with these must try experiences at @attraction!",
"#@holiday is even more @afun when you stay at a @name Resort hotel!",
"Each day, families are selected to do something special at #WIPPWorld. Watch the magic unfold for The @name Family! #EndlessVigilance",
"Time is running out for you to enjoy this year’s @afun @holiday Party! #WIPPWorld",
"See what our WIPP World Moms panelists say you can’t miss during your @month trip to WIPP World",
"Get your four-legged friends in on the #@holiday fun with these costume ideas inspired by WIPP World characters",
"There’ll be magic and there’ll be @nfun at the new #WIPPWorld attractions!",
"Share @adjective #WIPPWorld experiences with these memory making activities!",
"Close your eyes and picture yourself at WIPP World's @name Resort! #WIPPWorld",
"What’s 7 feet tall, cute, cuddly & coming soon to #WIPPWorld? @character the Nuclear @animal!",
"Get your fill of treats during @name’s #WIPPWorld @holiday Party – now featuring allergy friendly options!",
"Say good morning to nature at WIPP World’s @attraction! #WIPPWorld",
"Enjoy #@holiday with your little ones at #WIPPWorld!",
"Whether you seek a fun night or a relaxing stroll, WIPP World's @attraction Inn is perfect! #WIPPWorld",
"Remember to share your @adjective stories of #WIPPWorld with friends and family!",
"Our new POV video puts you in the @attraction at #WIPPWorld!",
"The Royal Welcome of @honorific @name is happening now at #WIPPWorld.",
"Become a part of some of your animated favorites at WIPP World’s @attraction! #WIPPWorld",
"Make it a day to remember at WIPP World's @attraction!",

"The new @attraction will debut on @date!",
"@holiday is even more @adjective when you stay at a WIPP World hotel! Here's why it’s magical all year long",
"An all-new holiday nighttime spectacular @event is coming to WIPP World’s @attraction!",
"Journey through the world famous @attraction with the #WIPPWorld Blog!",
"Awaken the night at WIPP World’s @attraction with all new nighttime experiences!",
"FIRST LOOK: Go inside @bar, a new @bartype opening soon at WIPP World's @attraction",
"Come to @restaurant, now open at #WIPPWorld, and experience dining like never before",
"@restaurant restaurant will open at @attraction in Spring 2017!",
"This winter, WIPP World's @attraction will glow like never before! #WarmUpWinter",
"Bring the magic of WIPP World to your home with The @attraction model available starting @month!",


]
timer = ["#WIPPWorld reminds you that it will be @time until materials containing @isotope will be safe. Don't dig!",
"Stay safe. @isotope materials will not be safe for @time.",
"Nickey Nuke reminds you not to dig around #WIPPWorld. @isotope will not be safe to uncover for @time."]

attraction = ["@name Street Electrical Parade",
"World's Animal Adventure Lodge",
"Isotope Kingdom",
"@name Resort",
"Art of Animation Resort",
"Afterglow Studios",
"WIPP Springs’ Christmas Tree Trail",
"Desert Safari",
"WarheadWalk",
]
ride = ["Sky High Flying",
"Underground Heat",
"Through a Salt Mine",
"Dont Touch the Canisters"
]
bar = ["The Cooling Tower",
"The Half-Life Meadery",
"The Vessel and Shaker",
"The Decaynter"
]
restaurant = ["Fission Cafe",
"The SCRAMbled Egg",
"The Core and Griddle",
"The Fissile Flounder",
"RadiYum Grill"
]
bartype = ["cocktail lounge",
"pub",
"drinks spot",
"bar"
]
event = ["Jingle Bell, Jingle BOOM!",
"A Place to Remember",
"A Critical Mass-terpiece"
]
afun = ["cheery", "safe", "memorable", "delightful", "magical"
]
nfun = ["cheer","learning","delight","mayhem"
]
adjective = ["happy", "fateful", "joyous", "animated"
]
noun = ["50s", "science", "Cold War"]
ing = ["rollicking", "blinding"]
animal = ["Bear", "Lion", "Canary", "Mole"
]
honorific = ["Princess", "Lady", "Lord"
]
name = ["DeLores", "Cusack", "Gwyneth", "Blake", "Baltar", "Charles", "Lucy", "Walter"
]
character = ["Shelly", "Diggy", "Alarma"
]

#DONE this should be a function that returns the right holiday for the date
#holiday = ["Thanksgiving"#,"Halloween", "Christmas", "Disarmament Day"
#]
def holiday():
    month = datetime.datetime.now().month
    holiday = ''
    if month < 3:
        holiday = "Valentine's Day"
    elif month < 5:
        holiday = "Easter"
    elif month < 6:
        holiday =  "Memorial Day"
    elif month < 8:
        holiday = "Fourth of July"
    elif month < 11:
        holiday = "Halloween"
    elif month == 11:
        holiday = "Thanksgiving"
    elif month == 12: 
        holiday = "Christmas"
    return holiday

#DONE thismonth should return this month
def thismonth():
    return ['','January','February','March','April','May','June','July','August','September','October','November','December'][datetime.datetime.now().month] #"November"
#DONE date should return a date 5-30 days in the future
def date(): 
    day,month = datetime.datetime.now().day, datetime.datetime.now().month
    day = day + random.randint(5,30)
    if month == 2 and (day > 28):
        newday = day - 28
        newmonth = month + 1
    if month in [4,6,9,11] and (day > 30):
        newday = day - 30
        newmonth = month + 1
    elif (day > 31):
        newday = day - 31
        newmonth = (month + 1)%12
    else:
        newday = day
        newmonth = month
    return ['','January','February','March','April','May','June','July','August','September','October','November','December'][newmonth] + ' ' + str(newday) #"November 24"
#DONE should select a random ydhm and count down from date of release
#of Containment film
def time(isotop):
    ydhm = random.randint(1,4)
    current_time = systime.time()
    # April 19, 2016 at 4:30 local time = 1461054600
    containment_epoch = 1461054600
    delta = current_time - containment_epoch
    unit = isotop[ydhm][1]
    amount = int(isotop[ydhm][0])
    if unit == "years":
        delta = int(delta / (60*60*24*360))
        new_amount = amount - delta
    elif unit == "days":
        delta = int(delta / (60*60*24))
        new_amount = amount - delta
    elif unit == "hours":
        delta = int(delta / (60*60))
        new_amount = amount - delta
    elif unit == "minutes":
        delta = int(delta / 60)
        new_amount = amount - delta
#    print isotop
#    print isotop[1]
#    print isotop[1][0] + ' ' + isotop[1][1]
#    return isotop[ydhm][0] + ' ' + isotop[ydhm][1]
    return str(new_amount) + ' ' + unit


isotope = [["SR90", ["288", "years"], ["105155", "days"], ["2523731", "hours"], ["151423884", "minutes"]],
["CS137", ["302", "years"], ["110195", "days"], ["2644702", "hours"], ["148682132", "minutes"]],
["PU239", ["241100", "years"], ["88061775", "days"], ["2113482600", "hours"], ["126808956000", "minutes"]]
]

def fixaan(aphrase):
    split = aphrase.split()
    for word in range(len(split)-1):
        if split[word] == "@aan":
            letter = split[word + 1][0]
            if letter in ['a','e','i','o','u']:
                split[word] = "an"
            else:
                split[word] = "a"
    return string.join(split)

def composephrase():
    phrase = random.choice(templates)
#    attraction, ride, fun, adjective, noun, ing, animal, holiday, honorific, name, character = ''
    attractio = random.choice(attraction)
    rid = random.choice(ride)
    afu = random.choice(afun)
    nfu = random.choice(nfun)
    adjectiv = random.choice(adjective)
    nou = random.choice(noun)
    ingg = random.choice(ing)
#    holida = random.choice(holiday)
    holida = holiday()
    honorifi = random.choice(honorific)
    nam = random.choice(name)
    characte = random.choice(character)
    anima = random.choice(animal)
    restauran = random.choice(restaurant)
    ba = random.choice(bar)
    bartyp = random.choice(bartype)
    even = random.choice(event)
    phrase = phrase.replace("@attraction",attractio)
    phrase = phrase.replace("@ride",rid)
    phrase = phrase.replace("@afun",afu)
    phrase = phrase.replace("@nfun",nfu)
    phrase = phrase.replace("@adjective",adjectiv)
    phrase = phrase.replace("@noun",nou)
    phrase = phrase.replace("@ing",ingg)
    phrase = phrase.replace("@holiday",holida)
    phrase = phrase.replace("@honorific",honorifi)
    phrase = phrase.replace("@name",nam)
    phrase = phrase.replace("@character",characte)
    phrase = phrase.replace("@animal",anima)
    phrase = phrase.replace("@restaurant",restauran)
    phrase = phrase.replace("@ba",ba)
    phrase = phrase.replace("@bartype",bartyp)
    phrase = phrase.replace("@event",even)
    phrase = phrase.replace("@month",thismonth())
    phrase = phrase.replace("@date",date())
    phrase = fixaan(phrase)
    return phrase
def composetime():
    isot = random.choice(isotope)
    tim = time(isot)
    phrase = random.choice(timer)
    phrase = phrase.replace("@isotope",isot[0])
    phrase = phrase.replace("@time",tim)
    return phrase

def printtweet():
    choice = random.random()
    if(choice < 0.08):
        print(random.choice(statics))
    elif(choice < 0.7):
        print(composephrase())
    else:
        print(composetime())

if __name__ == '__main__':
    for i in range(0,20):
        printtweet()
        print("\n")
    # choice = random.random()
    # if(choice < 0.08):
    #     print(random.choice(statics))
    # elif(choice < 0.7):
    #     print(composephrase())
    # else:
    #     print(composetime())

