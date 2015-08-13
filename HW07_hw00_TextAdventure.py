#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit
import sys
from datetime import datetime
import os.path

# Global variable
# Create log file for game
filename = ""
log_list = []
counter = 0

# Body
def infinite_stairway_room(name,list_,count=0):
    global counter
    # Don't print this after every time you take the stairs!
    if count == 0:
        print "%s ,you walk through the door to see a dimly lit hallway." % (name)
        print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    print "What next?"
    next = raw_input("> ")
    counter += 1
    list_.append(str(counter) + ", infinite_stairway_room, " + next + ", " + datetime.now().strftime("%Y-%m-%d/%H:%M"))

    # infinite stairs option
    if next == "take stairs":
        print 'You take the stairs'
        if (count > 0):
            print "but you're not happy about it"
        infinite_stairway_room(name,list_,count + 1)
    # option 2 == back away
    if next == "back away":
        print dead("Smart choice.",list_)

def gold_room(name,list_):
    global filename,counter
    print "%s, this room is full of gold.  How much do you take?" % (name)

    next = raw_input("> ")
    counter += 1
    list_.append(str(counter) + ", gold_room, " + next + ", " + datetime.now().strftime("%Y-%m-%d/%H:%M"))
    try:
        how_much = int(next)
    except:
        dead("Man, learn to type a number.",list_)
    else:
        if how_much < 50:
            counter += 1
            list_.append(str(counter) + ", win" + ", " + datetime.now().strftime("%Y-%m-%d/%H:%M"))
            write_inputs_file(filename,list_)
            print "Nice, you're not greedy, you win!"
            exit(0)
        else:
            dead("You greedy bastard!",list_)

def bear_room(name,list_):
    global counter
    print "%s ,there is a bear here." % (name)
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")
        counter += 1
        list_.append(str(counter) + ", bear_room, " + next + ", " + datetime.now().strftime("%Y-%m-%d/%H:%M"))

        if next in ("take","honey"):
            dead("The bear looks at you then slaps your face off.",list_)
        elif next == "taunt" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.",list_)
        elif next in ("open","door") and bear_moved:
            gold_room(name,list_)
        else:
            print "I got no idea what that means."


def cthulhu_room(name,list_):
    global counter
    print "%s ,here you see the great evil Cthulhu." % (name)
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")
    counter += 1
    list_.append(str(counter) + ", cthulhu_room " + next + ", " + datetime.now().strftime("%Y-%m-%d/%H:%M"))

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!",list_)
    else:
        cthulhu_room(name,list_)


def dead(why,list_):
    global filename,counter
    counter += 1
    list_.append(str(counter) + ", dead" + ", " + datetime.now().strftime("%Y-%m-%d/%H:%M"))
    write_inputs_file(filename,list_)
    print why, "Good job!"
    exit(0)

def back_room(name,list_):
    global filename,counter
    print "%s, you are now in the back room. It's filled with awkward programmers. Go on, introduce yourself, don't be shy." % (name)
    next = raw_input("> ")
    counter += 1
    list_.append(str(counter) + ", back_room, " + next + ", " + datetime.now().strftime("%Y-%m-%d/%H:%M"))
    print "Nobody cares. So you soon start programming Python, and never leave."
    write_inputs_file(filename,list_)
    exit(0)

def write_inputs_file(file_,list_):
    if os.path.isfile(file_):
        mode = "a"
    else:
        mode = "w"
    with open(file_,mode) as handler:
        for action in list_:
            handler.write(action+"\r\n")
##############################################################################
def main():
    global filename,log_list,counter
    your_name = sys.argv[1]
    timestamp = datetime.now().strftime("%m%d%H%M")
    filename = your_name + "-" + timestamp + ".txt"
    # START the TextAdventure game
    print "%s , you are in a dark room." % (your_name)
    print "You can either choose to go through the left door, or the right door. If none entices you, you can choose to go on further. OR, are you bold enough to enter the back room?"
    print "Which one do you take?"
    print "'left' takes you through the left door."
    print "'right' takes you through the right door."
    print "'further' takes you beyond the doors."
    print "'back' takes you to the back room."

    next = raw_input("> ")
    # Log action in list
    counter += 1
    log_list.append(str(counter) + ", main_room, " + next + ", " + datetime.now().strftime("%Y-%m-%d/%H:%M"))

    if next.lower() == "left":
        bear_room(your_name,log_list)
    elif next.lower() == "right":
        cthulhu_room(your_name,log_list)
    elif next.lower() == "further":
        infinite_stairway_room(your_name,log_list)
    elif next.lower() == "back":
        back_room(your_name,log_list)
    else:
        dead("You stumble around the room until you starve.",log_list)

if __name__ == '__main__':
    main()
