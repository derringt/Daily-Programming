import thread, time, os, random
from threading import Lock

list_lock = Lock()

colors = {
    'red' : '\033[31m',
    'green' : '\033[32m',
    'yellow' : '\033[33m',
    'end'   : '\033[0m'
}

def input_thread(L):
    #Have to press enter unless I use curses
    #Or do something else...
    while True:
        c = raw_input()
        if c:
            with list_lock:
                L.append(c)

def show_status(stat):
    n = divmod(stat,10)[0]
    hash_list = []
    for i in range(0,n):
        hash_list.append('#')
    showing = "".join(hash_list)
    if showing == "":
        showing = "!!!"
    if stat >=65:
        color = 'green'
    elif stat >=35:
        color = 'yellow'
    else:
        color = 'red'
    return colors[color] + showing + colors['end']

def do_tamagotchi():
    L = []
    c = ''
    thread.start_new_thread(input_thread, (L,))
    hunger = random.randint(30,70)
    poop = random.randint(0,15)
    sleep = random.randint(15,50)
    happiness = random.randint(25,75)
    max_age = random.randint(75,150)
    current_age = 0
    while 1:
        time.sleep(1)
        os.system('clear')
        #Check for old age
        current_age += 1
        if current_age == max_age:
            print "Oh no! He died while you not look!"
            print ":("
            break

        #Check for starvation
        hunger -= random.randint(1,5)
        if hunger <= 0:
            print "Oh no! He died because you no feed!"
            print ":("
            break

        #Add a little poop
        poop += random.randint(1,5)

        #Add a little tiredness
        sleep -= random.randint(1,5)

        #Get the last keypress
        if len(L) > 0:
            with list_lock:
                c = L.pop()
                del L[:]

        if c == 'Q' or c == 'q':
            print 'He misses you! Come to be back soon!'
            break
        elif c == 'P' or c == 'p':
            happiness += random.randint(15,25)
            happiness = min(100, happiness)
            print "You play with pet! He so much more happy! :)"
        elif c == 'F' or c == 'f':
            hunger += random.randint(50,75)
            hunger = min(100, hunger)
            poop += random.randint(30,60)
            print "You feed pet! He gobble it down! Nom nom nom!"
        elif c == 'B' or c == 'b':
            sleep = random.randint(50,100)
            print "You tuck pet in bed! He so cute! ZzZzZzZz"
        #Check for sleepiness
        elif sleep <= random.randint(0,25):
            sleep = random.randint(65,100)
            print "Pet went to sleep! ZzZzZzZz"
        #Check for poop
        elif poop >= random.randint(75,100):
            poop = random.randint(0, 15)
            print "Ooh! Proud baby make a stinky! :D"
        else: #nothing else is happening
            print 'Put him to (B)ed, (F)eed him, or (P)lay with him!'
            print 'Or (Q)uit on your duty!'

        #Print his status bars
        print 'Hungry :' + show_status(hunger)
        print 'Sleepy :' + show_status(sleep)
        print 'Happy :' + show_status(happiness)

        c = ''


print "Welcome to be taking care of you're new pet!"
print "We hope you have many funs with it!"
do_tamagotchi()
