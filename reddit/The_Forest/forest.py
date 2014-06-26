import sys,random

forest_height = int(sys.argv[1])
forest_size = forest_height*forest_height

lumberjacks = []
trees = []
bears = []

#def move(actor, type, dir):
#    if dir == 1:

def spawn():

    # 10% lumberjacks
    global lumberjacks
    while len(lumberjacks) < forest_size * .10:
        place(lumberjacks, 'L')

    # 50% trees
    global trees
    while len(trees) < forest_size * .50:
        place(trees, 'T', True)

    # 2% Bears
    global bears
    while len(bears) < forest_size * .02:
        place(bears, 'B')

def place(list, elem, nameit=False):
    rand_x = random.randint(0,forest_height-1)
    rand_y = random.randint(0,forest_height-1)
    if forest[rand_x][rand_y] == '.':
        forest[rand_x][rand_y] = elem
        if nameit:
            list.append([rand_x, rand_y, elem])
        else:
            list.append([rand_x, rand_y])

if __name__ == "__main__":

    forest = [['.' for x in xrange(forest_height)] for x in xrange(forest_height)]

    spawn()

    for row in forest:
        print ' '.join(row).replace('B', '\033[94mB\033[0m').replace('L', '\033[91mL\033[0m').replace('T', '\033[92mT\033[0m')
