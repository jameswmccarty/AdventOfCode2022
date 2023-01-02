#!/usr/bin/python

"""
--- Day 12: Hill Climbing Algorithm ---

You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?

Your puzzle answer was 330.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^

This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?

Your puzzle answer was 321.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

height_map = dict() # store the map as height at (x,y)

def bfs(pos,goal):
	seen = set()
	seen.add(pos)
	steps = 0
	q = []
	q.append((steps,pos))
	while len(q) > 0:
		steps,current = q.pop(0)
		if current == goal:
			return steps
		x,y = current
		for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
			if (x+dx,y+dy) in height_map and (x+dx,y+dy) not in seen and height_map[(x+dx,y+dy)]-height_map[current] <= 1:
				seen.add((x+dx,y+dy))
				q.append((steps+1,(x+dx,y+dy)))
	return float('inf')

def bfs2(pos):
	seen = set()
	seen.add(pos)
	steps = 0
	q = []
	q.append((steps,pos))
	while len(q) > 0:
		steps,current = q.pop(0)
		if height_map[current] == 0:
			return steps
		x,y = current
		for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
			if (x+dx,y+dy) in height_map and (x+dx,y+dy) not in seen and height_map[current]-height_map[(x+dx,y+dy)] <= 1:
				seen.add((x+dx,y+dy))
				q.append((steps+1,(x+dx,y+dy)))
	return float('inf')

if __name__ == "__main__":

	# Part 1 Solution
	pos = None
	goal = None
	with open("day12_input","r") as infile:
		j = 0
		for line in infile.readlines():
			for i,char in enumerate(line.strip()):
				if char == 'S':
					pos = (i,j)
					height_map[(i,j)] = 0
				elif char == 'E':
					goal = (i,j)
					height_map[(i,j)] = ord('z') - ord('a')
				else:
					height_map[(i,j)] = ord(char)- ord('a')
			j += 1
	print(bfs(pos,goal))

	# Part 2 Solution
	"""
	best_score = float('inf')
	for pos,height in height_map.items():
		if height == 0:
			best_score = min(best_score,bfs(pos,goal))
	print(best_score)
	"""
	print(bfs2(goal))
