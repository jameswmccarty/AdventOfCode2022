#!/usr/bin/python

"""
--- Day 14: Regolith Reservoir ---

The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads behind the waterfall.

Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.

As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!

Fortunately, your familiarity with analyzing the path of falling material will come in handy here. You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly air with structures made of rock.

Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, where x represents distance to the right and y represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9

This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)

The sand is pouring into the cave from point 500,0.

Drawing rock as #, air as ., and the source of the sand as +, this becomes:


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.

Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.

A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.

So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and then stops:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......o.#.
#########.

The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.

After a total of five units of sand have come to rest, they form this pattern:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.

After a total of 22 units of sand:

......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.

Finally, only two more units of sand can possibly come to rest:

......+...
..........
......o...
.....ooo..
....#ooo##
...o#ooo#.
..###ooo#.
....oooo#.
.o.ooooo#.
#########.

Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with ~:

.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........

Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?

Your puzzle answer was 755.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor, and you're standing on it!

You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a y coordinate equal to two plus the highest y coordinate of any point in your scan.

In the example above, the highest y coordinate of any point is 9, and so the floor is at y=11. (This is as if your scan contained one extra rock path like -infinity,11 -> infinity,11.) With the added floor, the example above now looks like this:

        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->

To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at 500,0, blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after 93 units of sand come to rest:

............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################

Using your scan, simulate the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?

Your puzzle answer was 29805.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

rocks = set()
sands = set()
max_depth = None

class sand:

	def __init__(self,x,y):
		self.x = x
		self.y = y

	# try to move this grain
	# if we are out of bounds, return -1
	# if we moved, return 0
	# if we are blocked, return 1
	def move(self,p2=False):
		# out of bounds
		if not p2 and self.y > max_depth:
			return -1
		if p2 and self.y == max_depth-1:
			sands.add((self.x,self.y))
			return 1
		# check down one step
		if (self.x,self.y+1) not in rocks and (self.x,self.y+1) not in sands:
			self.y += 1
			return 0
		# something was blocking us
		# try down and left
		if (self.x-1,self.y+1) not in rocks and (self.x-1,self.y+1) not in sands:
			self.x -= 1
			self.y += 1
			return 0
		# try down and right
		if (self.x+1,self.y+1) not in rocks and (self.x+1,self.y+1) not in sands:
			self.x += 1
			self.y += 1
			return 0
		# we are fully stopped.  add self to sand
		sands.add((self.x,self.y))
		return 1


def parse_line(line):
	global rocks
	points = line.split(' -> ')
	start = points.pop(0)
	x0,y0 = start.split(',')
	x0,y0 = int(x0),int(y0)
	while len(points) > 0:
		next = points.pop(0)
		x1,y1 = next.split(',')
		x1,y1 = int(x1),int(y1)
		if x0 == x1: # y direction changes
			if y0 > y1:
				delta = -1
			else:
				delta = 1
			for y in range(y0,y1+delta,delta):
				rocks.add((x0,y))
		else: # x direction changes
			if x0 > x1:
				delta = -1
			else:
				delta = 1
			for x in range(x0,x1+delta,delta):
				rocks.add((x,y0))
		x0,y0 = x1,y1

def pretty_print():
	min_x = min(min([ x[0] for x in sands ]), min([ x[0] for x in rocks ]))-1
	max_x = max(max([ x[0] for x in sands ]), max([ x[0] for x in rocks ]))+1
	min_y = min(min([ x[1] for x in sands ]), min([ x[1] for x in rocks ]))-1
	max_y = max(max([ x[1] for x in sands ]), max([ x[1] for x in rocks ]))+1
	max_x -= min_x
	max_y -= min_y
	for j in range(max_y):
		for i in range(max_x):
			if (i+min_x,j+min_y) in rocks:
				print('#',end='')
			elif (i+min_x,j+min_y) in sands:
				print('o',end='')
			else:
				print('.',end='')
		print()

if __name__ == "__main__":

	# Part 1 Solution
	with open('day14_input','r') as infile:
		for line in infile.readlines():
			parse_line(line.strip())
	made_sand = 0
	max_depth = max([ x[1] for x in rocks ])
	while True:
		grain = sand(500,0)
		status = grain.move()
		while status == 0:
			status = grain.move()
		if status == -1:
			break
		made_sand += 1
	print(made_sand)

	# Part 2 Solution
	max_depth += 2
	while True:
		grain = sand(500,0)
		status = grain.move(p2=True)
		while status == 0:
			status = grain.move(p2=True)
		if status == 1 and grain.x==500 and grain.y==0:
			break
		made_sand += 1
	print(made_sand+1)
	#pretty_print()

