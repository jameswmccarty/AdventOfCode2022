#!/usr/bin/python

"""
--- Day 24: Blizzard Basin ---

With everything replanted for next year (and with elephants and monkeys to tend the grove), you and the Elves leave for the extraction point.

Partway up the mountain that shields the grove is a flat, open area that serves as the extraction point. It's a bit of a climb, but nothing the expedition can't handle.

At least, that would normally be true; now that the mountain is covered in snow, things have become more difficult than the Elves are used to.

As the expedition reaches a valley that must be traversed to reach the extraction site, you find that strong, turbulent winds are pushing small blizzards of snow and sharp ice around the valley. It's a good thing everyone packed warm clothes! To make it across safely, you'll need to find a way to avoid them.

Fortunately, it's easy to see all of this from the entrance to the valley, so you make a map of the valley and the blizzards (your puzzle input). For example:

#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#

The walls of the valley are drawn as #; everything else is ground. Clear ground - where there is currently no blizzard - is drawn as .. Otherwise, blizzards are drawn with an arrow indicating their direction of motion: up (^), down (v), left (<), or right (>).

The above map includes two blizzards, one moving right (>) and one moving down (v). In one minute, each blizzard moves one position in the direction it is pointing:

#.#####
#.....#
#.>...#
#.....#
#.....#
#...v.#
#####.#

Due to conservation of blizzard energy, as a blizzard reaches the wall of the valley, a new blizzard forms on the opposite side of the valley moving in the same direction. After another minute, the bottom downward-moving blizzard has been replaced with a new downward-moving blizzard at the top of the valley instead:

#.#####
#...v.#
#..>..#
#.....#
#.....#
#.....#
#####.#

Because blizzards are made of tiny snowflakes, they pass right through each other. After another minute, both blizzards temporarily occupy the same position, marked 2:

#.#####
#.....#
#...2.#
#.....#
#.....#
#.....#
#####.#

After another minute, the situation resolves itself, giving each blizzard back its personal space:

#.#####
#.....#
#....>#
#...v.#
#.....#
#.....#
#####.#

Finally, after yet another minute, the rightward-facing blizzard on the right is replaced with a new one on the left facing the same direction:

#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#

This process repeats at least as long as you are observing it, but probably forever.

Here is a more complex example:

#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#

Your expedition begins in the only non-wall position in the top row and needs to reach the only non-wall position in the bottom row. On each minute, you can move up, down, left, or right, or you can wait in place. You and the blizzards act simultaneously, and you cannot share a position with a blizzard.

In the above example, the fastest way to reach your goal requires 18 steps. Drawing the position of the expedition as E, one way to achieve this is:

Initial state:
#E######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#

Minute 1, move down:
#.######
#E>3.<.#
#<..<<.#
#>2.22.#
#>v..^<#
######.#

Minute 2, move down:
#.######
#.2>2..#
#E^22^<#
#.>2.^>#
#.>..<.#
######.#

Minute 3, wait:
#.######
#<^<22.#
#E2<.2.#
#><2>..#
#..><..#
######.#

Minute 4, move up:
#.######
#E<..22#
#<<.<..#
#<2.>>.#
#.^22^.#
######.#

Minute 5, move right:
#.######
#2Ev.<>#
#<.<..<#
#.^>^22#
#.2..2.#
######.#

Minute 6, move right:
#.######
#>2E<.<#
#.2v^2<#
#>..>2>#
#<....>#
######.#

Minute 7, move down:
#.######
#.22^2.#
#<vE<2.#
#>>v<>.#
#>....<#
######.#

Minute 8, move left:
#.######
#.<>2^.#
#.E<<.<#
#.22..>#
#.2v^2.#
######.#

Minute 9, move up:
#.######
#<E2>>.#
#.<<.<.#
#>2>2^.#
#.v><^.#
######.#

Minute 10, move right:
#.######
#.2E.>2#
#<2v2^.#
#<>.>2.#
#..<>..#
######.#

Minute 11, wait:
#.######
#2^E^2>#
#<v<.^<#
#..2.>2#
#.<..>.#
######.#

Minute 12, move down:
#.######
#>>.<^<#
#.<E.<<#
#>v.><>#
#<^v^^>#
######.#

Minute 13, move down:
#.######
#.>3.<.#
#<..<<.#
#>2E22.#
#>v..^<#
######.#

Minute 14, move right:
#.######
#.2>2..#
#.^22^<#
#.>2E^>#
#.>..<.#
######.#

Minute 15, move right:
#.######
#<^<22.#
#.2<.2.#
#><2>E.#
#..><..#
######.#

Minute 16, move right:
#.######
#.<..22#
#<<.<..#
#<2.>>E#
#.^22^.#
######.#

Minute 17, move down:
#.######
#2.v.<>#
#<.<..<#
#.^>^22#
#.2..2E#
######.#

Minute 18, move down:
#.######
#>2.<.<#
#.2v^2<#
#>..>2>#
#<....>#
######E#

What is the fewest number of minutes required to avoid the blizzards and reach the goal?

Your puzzle answer was 373.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

As the expedition reaches the far side of the valley, one of the Elves looks especially dismayed:

He forgot his snacks at the entrance to the valley!

Since you're so good at dodging blizzards, the Elves humbly request that you go back for his snacks. From the same initial conditions, how quickly can you make it from the start to the goal, then back to the start, then back to the goal?

In the above example, the first trip to the goal takes 18 minutes, the trip back to the start takes 23 minutes, and the trip back to the goal again takes 13 minutes, for a total time of 54 minutes.

What is the fewest number of minutes required to reach the goal, go back to the start, then reach the goal again?

Your puzzle answer was 997.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

from collections import deque

def next_blizzards(walls,blizzards,max_x,max_y):
	next_blizz = []
	for blizzard in blizzards:
		x,y,direction = blizzard
		if direction == '>':
			if x+1 == max_x:
				next_blizz.append((1,y,direction))
			else:
				next_blizz.append((x+1,y,direction))
		elif direction == '<':
			if x-1 == 0:
				next_blizz.append((max_x-1,y,direction))
			else:
				next_blizz.append((x-1,y,direction))
		elif direction == '^':
			if y-1 == 0:
				next_blizz.append((x,max_y-1,direction))
			else:
				next_blizz.append((x,y-1,direction))
		elif direction == 'v':
			if y+1 == max_y:
				next_blizz.append((x,1,direction))
			else:
				next_blizz.append((x,y+1,direction))
	return sorted(next_blizz)	

# too slow
def bfs(start,end,walls,blizzards):
	max_x = max([p[0] for p in walls])
	max_y = max([p[1] for p in walls])
	deltas = ((0,1),(1,0),(0,-1),(-1,0),(0,0))
	seen = set()
	q = deque()
	q.append((start,blizzards,0))
	while len(q) > 0:
		pos,blizzards,t = q.popleft()
		if pos == end:
			return t
		else:
			x,y = pos
			blizzards = next_blizzards(walls,blizzards,max_x,max_y)
			blocked = { (x,y) for x,y,d in blizzards }
			for dx,dy in deltas:
				step = (x+dx,y+dy)
				if step not in blocked and step not in walls:
					state = hash((step,tuple(blizzards)))
					if state not in seen:
						q.append((step,blizzards,t+1))
						seen.add(state)

def time_map_bfs(start,end,open_at_t,start_t=0):
	deltas = ((0,1),(1,0),(0,-1),(-1,0),(0,0))
	q = deque()
	q.append((start,start_t))
	seen = set()
	while len(q) > 0:
		pos,t = q.popleft()
		if pos == end:
			return t
		else:
			x,y = pos
			t += 1
			for dx,dy in deltas:
				step = (x+dx,y+dy)
				state = hash((step,t%len(open_at_t)))
				if step in open_at_t[t%len(open_at_t)] and state not in seen:
					seen.add(state)
					q.append((step,t))


def find_open_spots(walls,blizzards,max_x,max_y):
	blocked = { (x,y) for x,y,d in blizzards }
	opened = set()
	for x in range(max_x):
		for y in range(max_y+1):
			if (x,y) not in blocked and (x,y) not in walls:
				opened.add((x,y))
	return opened			

def time_map(walls,blizzards):
	open_at_t = dict()
	t = 0	
	max_x = max([p[0] for p in walls])
	max_y = max([p[1] for p in walls])
	orig_blizzards = sorted(blizzards)
	open_at_t[t] = find_open_spots(walls,blizzards,max_x,max_y)
	blizzards = next_blizzards(walls,blizzards,max_x,max_y)
	while blizzards != orig_blizzards:
		t += 1
		open_at_t[t] = find_open_spots(walls,blizzards,max_x,max_y)
		blizzards = next_blizzards(walls,blizzards,max_x,max_y)
	return open_at_t

if __name__ == "__main__":

	walls = set()
	blizzards = list()

	# Part 1 Solution
	with open('day24_input','r') as infile:
		y = 0
		for line in infile.readlines():
			for x,char in enumerate(line.strip()):
				if char == '#':
					walls.add((x,y))
				elif char in '<>^v':
					blizzards.append((x,y,char))
			y += 1

	start_x = 0
	start = None
	while True:
		if (start_x,0) not in walls:
			start = (start_x,0)
			break
		start_x += 1
	end_x = 0
	end = None
	while True:
		if (end_x,y-1) not in walls:
			end = (end_x,y-1)
			break
		end_x += 1
	open_map = time_map(walls,blizzards)
	t1 = time_map_bfs(start,end,open_map)
	print(t1)

	# Part 2 Solution
	t2 = time_map_bfs(end,start,open_map,t1)
	t3 = time_map_bfs(start,end,open_map,t2)
	print(t3)



