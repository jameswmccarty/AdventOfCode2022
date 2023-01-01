#!/usr/bin/python

"""

--- Day 22: Monkey Map ---

The monkeys take you on a surprisingly easy trail through the jungle. They're even going in roughly the right direction according to your handheld device's Grove Positioning System.

As you walk, the monkeys explain that the grove is protected by a force field. To pass through the force field, you have to enter a password; doing so involves tracing a specific path on a strangely-shaped board.

At least, you're pretty sure that's what you have to do; the elephants aren't exactly fluent in monkey.

The monkeys give you notes that they took when they last saw the password entered (your puzzle input).

For example:

        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5

The first half of the monkeys' notes is a map of the board. It is comprised of a set of open tiles (on which you can move, drawn .) and solid walls (tiles which you cannot enter, drawn #).

The second half is a description of the path you must follow. It consists of alternating numbers and letters:

    A number indicates the number of tiles to move in the direction you are facing. If you run into a wall, you stop moving forward and continue with the next instruction.
    A letter indicates whether to turn 90 degrees clockwise (R) or counterclockwise (L). Turning happens in-place; it does not change your current tile.

So, a path like 10R5 means "go forward 10 tiles, then turn clockwise 90 degrees, then go forward 5 tiles".

You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the right (from the perspective of how the map is drawn).

If a movement instruction would take you off of the map, you wrap around to the other side of the board. In other words, if your next tile is off of the board, you should instead look in the direction opposite of your current facing as far as you can until you find the opposite edge of the board, then reappear there.

For example, if you are at A and facing to the right, the tile in front of you is marked B; if you are at C and facing down, the tile in front of you is marked D:

        ...#
        .#..
        #...
        ....
...#.D.....#
........#...
B.#....#...A
.....C....#.
        ...#....
        .....#..
        .#......
        ......#.

It is possible for the next tile (after wrapping around) to be a wall; this still counts as there being a wall in front of you, and so movement stops before you actually wrap to the other side of the board.

By drawing the last facing you had with an arrow on each tile you visit, the full path taken by the above example looks like this:

        >>v#    
        .#v.    
        #.v.    
        ..v.    
...#...v..v#    
>>>v...>#.>>    
..#v...#....    
...>>>>v..#.    
        ...#....
        .....#..
        .#......
        ......#.

To finish providing the password to this strange input device, you need to determine numbers for your final row, column, and facing as your final position appears from the perspective of the original map. Rows start from 1 at the top and count downward; columns start from 1 at the left and count rightward. (In the above example, row 1, column 1 refers to the empty space with no tile on it in the top-left corner.) Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^). The final password is the sum of 1000 times the row, 4 times the column, and the facing.

In the above example, the final row is 6, the final column is 8, and the final facing is 0. So, the final password is 1000 * 6 + 4 * 8 + 0: 6032.

Follow the path given in the monkeys' notes. What is the final password?

Your puzzle answer was 36518.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

As you reach the force field, you think you hear some Elves in the distance. Perhaps they've already arrived?

You approach the strange input device, but it isn't quite what the monkeys drew in their notes. Instead, you are met with a large cube; each of its six faces is a square of 50x50 tiles.

To be fair, the monkeys' map does have six 50x50 regions on it. If you were to carefully fold the map, you should be able to shape it into a cube!

In the example above, the six (smaller, 4x4) faces of the cube are:

        1111
        1111
        1111
        1111
222233334444
222233334444
222233334444
222233334444
        55556666
        55556666
        55556666
        55556666

You still start in the same position and with the same facing as before, but the wrapping rules are different. Now, if you would walk off the board, you instead proceed around the cube. From the perspective of the map, this can look a little strange. In the above example, if you are at A and move to the right, you would arrive at B facing down; if you are at C and move down, you would arrive at D facing up:

        ...#
        .#..
        #...
        ....
...#.......#
........#..A
..#....#....
.D........#.
        ...#..B.
        .....#..
        .#......
        ..C...#.

Walls still block your path, even if they are on a different face of the cube. If you are at E facing up, your movement is blocked by the wall marked by the arrow:

        ...#
        .#..
     -->#...
        ....
...#..E....#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

Using the same method of drawing the last facing you had with an arrow on each tile you visit, the full path taken by the above example now looks like this:

        >>v#    
        .#v.    
        #.v.    
        ..v.    
...#..^...v#    
.>>>>>^.#.>>    
.^#....#....    
.^........#.    
        ...#..v.
        .....#v.
        .#v<<<<.
        ..v...#.

The final password is still calculated from your final position and facing from the perspective of the map. In this example, the final row is 5, the final column is 7, and the final facing is 3, so the final password is 1000 * 5 + 4 * 7 + 3 = 5031.

Fold the map into a cube, then follow the path given in the monkeys' notes. What is the final password?

Your puzzle answer was 143208.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

air = set()
walls = set()
face_map = dict()
for _ in range(1,7):
	face_map[_] = set()

# new direction of motion from rotation
def rotate(facing,d):
	if d == 'L':
		if facing == (1,0): # >
			return (0,-1)
		if facing == (0,1): # v
			return (1,0)
		if facing == (-1,0): # <
			return (0,1)
		if facing == (0,-1): # ^
			return (-1,0)
	elif d == 'R':
		if facing == (1,0): # >
			return (0,1)
		if facing == (0,1): # v
			return (-1,0)
		if facing == (-1,0): # <
			return (0,-1)
		if facing == (0,-1): # ^
			return (1,0)

def solve_path(pos,facing,path):
	path = list(path)
	while len(path) > 0:
		move = ' '
		while len(path) > 0 and move[-1] != 'R' and move[-1] != 'L':
			move += path.pop(0)
		steps = int(move.strip('R').strip('L').strip())
		for step in range(steps):
			x,y = pos
			if (x+facing[0],y+facing[1]) in air: # open
				pos = (x+facing[0],y+facing[1])
			elif (x+facing[0],y+facing[1]) in walls: # hit wall
				break
			else: # wrap if not blocked
				if facing[0] == 0: # movement in the y dir
					if facing[1] == -1:
						max_y = max(max([ p[1] for p in air if p[0] == x]),max([ p[1] for p in walls if p[0] == x]))
						if (x,max_y) not in walls:
							pos = (x,max_y)
					elif facing[1] == 1:
						min_y = min(min([ p[1] for p in air if p[0] == x]),min([ p[1] for p in walls if p[0] == x]))
						if (x,min_y) not in walls:
							pos = (x,min_y)
				elif facing[1] == 0: # movement in the x dir
					if facing[0] == -1:
						max_x = max(max([ p[0] for p in air if p[1] == y]),max([ p[0] for p in walls if p[1] == y]))
						if (max_x,y) not in walls:
							pos = (max_x,y)
					elif facing[0] == 1:
						min_x = min(min([ p[0] for p in air if p[1] == y]),min([ p[0] for p in walls if p[1] == y]))
						if (min_x,y) not in walls:
							pos = (min_x,y)
		if 'R' in move or 'L' in move:
			facing = rotate(facing,move[-1])
	password = pos[0]*4 + pos[1]*1000
	if facing == (1,0):
		password += 0
	if facing == (-1,0):
		password += 2
	if facing == (0,1):
		password += 1
	if facing == (0,-1):
		password += 3
	return(password)

# if we are moving off of a cube face
# return the landing point and new facing direction
def transition_face(pos,facing):
	""" # input map (manually determined)
	-12
	-3-
	45-
	6--
	"""

	"""
	(1,0 ): # >
	(0,1) : # v
	(-1,0): # <
	(0,-1): # ^
	"""

	""" # moves off faces (manually determined)
	1U -> 6R
	1L -> 4R
	2U -> 6U
	2R -> 5L
	2D -> 3L
	3L -> 4D
	3R -> 2U
	5R -> 2L
	5D -> 6L
	4U -> 3R
	4L -> 1R
	6R -> 5U
	6D -> 2D
	6L -> 1D
	"""

	x,y = pos
	face = None
	for k,v in face_map.items():
		if pos in v:
			face = k
			break

	#print("Pos ",pos,"facing",facing,"face",face)

	#1U -> 6R
	if face == 1 and facing == (0,-1):
		return (1, x+100),(1,0) 
	#1L -> 4R
	if face == 1 and facing == (-1,0):
		return (1, (51-y)+100 ),(1,0) # check
	#2U -> 6U
	if face == 2 and facing == (0,-1):
		return (x-100,200),(0,-1) 
	#2R -> 5L
	if face == 2 and facing == (1,0):
		return (100,(51-y)+100),(-1,0) 
	#2D -> 3L
	if face == 2 and facing == (0,1):
		return (100,x-50),(-1,0) 
	#3L -> 4D
	if face == 3 and facing == (-1,0):
		return (y-50,101),(0,1) 
	#3R -> 2U
	if face == 3 and facing == (1,0):
		return (y+50,50),(0,-1) 
	#5R -> 2L
	if face == 5 and facing == (1,0):
		return (150,51-(y-100)),(-1,0) 
	#5D -> 6L
	if face == 5 and facing == (0,1):
		return (50,x+100),(-1,0)
	#4U -> 3R
	if face == 4 and facing == (0,-1):
		return (51,50+x),(1,0) 
	#4L -> 1R
	if face == 4 and facing == (-1,0):
		return (51,51-(y-100)),(1,0) 
	#6R -> 5U
	if face == 6 and facing == (1,0):
		return (y-100,150),(0,-1) 
	#6D -> 2D
	if face == 6 and facing == (0,1):
		return (x+100,1),(0,1) 
	#6L -> 1D
	if face == 6 and facing == (-1,0):
		return (y-100,1),(0,1) 


def solve_cube(pos,facing,path):
	path = list(path)
	while len(path) > 0:
		move = ' '
		while len(path) > 0 and move[-1] != 'R' and move[-1] != 'L':
			move += path.pop(0)
		steps = int(move.strip('R').strip('L').strip())
		for step in range(steps):
			x,y = pos
			if (x+facing[0],y+facing[1]) in air: # open
				pos = (x+facing[0],y+facing[1])
			elif (x+facing[0],y+facing[1]) in walls: # hit wall
				break
			else: # wrap if not blocked
				new_pos,new_facing = transition_face(pos,facing)
				if new_pos in air:
					pos = new_pos
					facing = new_facing
				else: # hit wall
					break
		if 'R' in move or 'L' in move:
			facing = rotate(facing,move[-1])
	password = pos[0]*4 + pos[1]*1000
	if facing == (1,0):
		password += 0
	if facing == (-1,0):
		password += 2
	if facing == (0,1):
		password += 1
	if facing == (0,-1):
		password += 3
	return(password)

if __name__ == "__main__":


	path = ''
	pos = None

	# Part 1 Solution
	with open('day22_input','r') as infile:
		y = 1
		for line in infile.readlines():
			if '.' in line or '#' in line:
				for x,char in enumerate(line.rstrip()):
					if char == '.':
						air.add((x+1,y))
					elif char == '#':
						walls.add((x+1,y))
				y += 1
			elif len(line.strip()) > 0:
				path = line.strip()

	x = 1
	while True:
		if (x,1) in air:
			pos = (x,1)
			break
		x += 1

	print(solve_path(pos,(1,0),path))


	# Part 2 Solution
	""" # input map (manually determined)
	-12
	-3-
	45-
	6--
	"""

	# x // 50, y // 50
	faces = { (1,0) : 1,
			  (2,0) : 2,
			  (1,1) : 3,
			  (0,2) : 4,
			  (1,2) : 5,
			  (0,3) : 6 }

	with open('day22_input','r') as infile:
		y = 1
		for line in infile.readlines():
			if '.' in line or '#' in line:
				for x,char in enumerate(line.rstrip()):
					if char == '.':
						face = faces[(x//50,(y-1)//50)]
						face_map[face].add((x+1,y))
				y += 1

	"""
	for y in range(0,202):
		print(str(y).zfill(3),end=' ')
		for x in range(0,152):
			found = False
			for k,v in face_map.items():
				if (x,y) in v:
					print(k,end='')
					found = True
			if (x,y) in walls:
				print('#',end='')
			elif not found:
				print('.',end='')
		print()
	"""

	print(solve_cube(pos,(1,0),path))


