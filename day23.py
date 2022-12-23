#!/usr/bin/python

"""
--- Day 23: Unstable Diffusion ---

You enter a large crater of gray dirt where the grove is supposed to be. All around you, plants you imagine were expected to be full of fruit are instead withered and broken. A large group of Elves has formed in the middle of the grove.

"...but this volcano has been dormant for months. Without ash, the fruit can't grow!"

You look up to see a massive, snow-capped mountain towering above you.

"It's not like there are other active volcanoes here; we've looked everywhere."

"But our scanners show active magma flows; clearly it's going somewhere."

They finally notice you at the edge of the grove, your pack almost overflowing from the random star fruit you've been collecting. Behind you, elephants and monkeys explore the grove, looking concerned. Then, the Elves recognize the ash cloud slowly spreading above your recent detour.

"Why do you--" "How is--" "Did you just--"

Before any of them can form a complete question, another Elf speaks up: "Okay, new plan. We have almost enough fruit already, and ash from the plume should spread here eventually. If we quickly plant new seedlings now, we can still make it to the extraction point. Spread out!"

The Elves each reach into their pack and pull out a tiny plant. The plants rely on important nutrients from the ash, so they can't be planted too close together.

There isn't enough time to let the Elves figure out where to plant the seedlings themselves; you quickly scan the grove (your puzzle input) and note their positions.

For example:

....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..

The scan shows Elves # and empty ground .; outside your scan, more empty ground extends a long way in every direction. The scan is oriented so that north is up; orthogonal directions are written N (north), S (south), W (west), and E (east), while diagonal directions are written NE, NW, SE, SW.

The Elves follow a time-consuming process to figure out where they should each go; you can speed up this process considerably. The process consists of some number of rounds during which Elves alternate between considering where to move and actually moving.

During the first half of each round, each Elf considers the eight positions adjacent to themself. If no other Elves are in one of those eight positions, the Elf does not do anything during this round. Otherwise, the Elf looks in each of four directions in the following order and proposes moving one step in the first valid direction:

    If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
    If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
    If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
    If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

After each Elf has had a chance to propose a move, the second half of the round can begin. Simultaneously, each Elf moves to their proposed destination tile if they were the only Elf to propose moving to that position. If two or more Elves propose moving to the same position, none of those Elves move.

Finally, at the end of the round, the first direction the Elves considered is moved to the end of the list of directions. For example, during the second round, the Elves would try proposing a move to the south first, then west, then east, then north. On the third round, the Elves would first consider west, then east, then north, then south.

As a smaller example, consider just these five Elves:

.....
..##.
..#..
.....
..##.
.....

The northernmost two Elves and southernmost two Elves all propose moving north, while the middle Elf cannot move north and proposes moving south. The middle Elf proposes the same destination as the southwest Elf, so neither of them move, but the other three do:

..##.
.....
..#..
...#.
..#..
.....

Next, the northernmost two Elves and the southernmost Elf all propose moving south. Of the remaining middle two Elves, the west one cannot move south and proposes moving west, while the east one cannot move south or west and proposes moving east. All five Elves succeed in moving to their proposed positions:

.....
..##.
.#...
....#
.....
..#..

Finally, the southernmost two Elves choose not to move at all. Of the remaining three Elves, the west one proposes moving west, the east one proposes moving east, and the middle one proposes moving north; all three succeed in moving:

..#..
....#
#....
....#
.....
..#..

At this point, no Elves need to move, and so the process ends.

The larger example above proceeds as follows:

== Initial State ==
..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............

== End of Round 1 ==
..............
.......#......
.....#...#....
...#..#.#.....
.......#..#...
....#.#.##....
..#..#.#......
..#.#.#.##....
..............
....#..#......
..............
..............

== End of Round 2 ==
..............
.......#......
....#.....#...
...#..#.#.....
.......#...#..
...#..#.#.....
.#...#.#.#....
..............
..#.#.#.##....
....#..#......
..............
..............

== End of Round 3 ==
..............
.......#......
.....#....#...
..#..#...#....
.......#...#..
...#..#.#.....
.#..#.....#...
.......##.....
..##.#....#...
...#..........
.......#......
..............

== End of Round 4 ==
..............
.......#......
......#....#..
..#...##......
...#.....#.#..
.........#....
.#...###..#...
..#......#....
....##....#...
....#.........
.......#......
..............

== End of Round 5 ==
.......#......
..............
..#..#.....#..
.........#....
......##...#..
.#.#.####.....
...........#..
....##..#.....
..#...........
..........#...
....#..#......
..............

After a few more rounds...

== End of Round 10 ==
.......#......
...........#..
..#.#..#......
......#.......
...#.....#..#.
.#......##....
.....##.......
..#........#..
....#.#..#....
..............
....#..#..#...
..............

To make sure they're on the right track, the Elves like to check after round 10 that they're making good progress toward covering enough ground. To do this, count the number of empty ground tiles contained by the smallest rectangle that contains every Elf. (The edges of the rectangle should be aligned to the N/S/E/W directions; the Elves do not have the patience to calculate arbitrary rectangles.) In the above example, that rectangle is:

......#.....
..........#.
.#.#..#.....
.....#......
..#.....#..#
#......##...
....##......
.#........#.
...#.#..#...
............
...#..#..#..

In this region, the number of empty ground tiles is 110.

Simulate the Elves' process and find the smallest rectangle that contains the Elves after 10 rounds. How many empty ground tiles does that rectangle contain?

Your puzzle answer was 3766.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

It seems you're on the right track. Finish simulating the process and figure out where the Elves need to go. How many rounds did you save them?

In the example above, the first round where no Elf moved was round 20:

.......#......
....#......#..
..#.....#.....
......#.......
...#....#.#..#
#.............
....#.....#...
..#.....#.....
....#.#....#..
.........#....
....#......#..
.......#......

Figure out where the Elves need to go. What is the number of the first round where no Elf moves?

Your puzzle answer was 954.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

def calc_area(elves):
	min_x = min([e[0] for e in elves])
	max_x = max([e[0] for e in elves])
	min_y = min([e[1] for e in elves])
	max_y = max([e[1] for e in elves])	
	return (max_x+1-min_x)*(max_y+1-min_y)-len(elves)

def pretty_print(elves):
	min_x = min([e[0] for e in elves])
	max_x = max([e[0] for e in elves])
	min_y = min([e[1] for e in elves])
	max_y = max([e[1] for e in elves])	
	for y in range(min_y,max_y+1):
		for x in range(min_x,max_x+1):
			if (x,y) in elves:
				print('#',end='')
			else:
				print('.',end='')
		print()

def bfs_rounds(elves,rounds,find_stop=False):
	all_dirs = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1))
	checks = { 'N' : ((-1,-1),(0,-1),(1,-1)),
		   'S' : ((-1,1),(0,1),(1,1)),
		   'W' : ((-1,0),(-1,1),(-1,-1)),
		   'E' : ((1,0),(1,1),(1,-1)) }
	deltas = { 'N' : (0,-1),
		   'S' : (0,1),
		   'W' : (-1,0),
		   'E' : (1,0) }
	check_order = ['N','S','W','E']
	for r in range(rounds):
		#pretty_print(elves)
		#print('-----',r,'-----')
		next_elves = set()
		area_counts = dict()
		next_area_by_elf = dict()
		for elf in elves:
			x,y = elf
			moving = False
			for dx,dy in all_dirs:
				if (x+dx,y+dy) in elves:
					moving = True
			if not moving:
				next_elves.add(elf)
			elif moving:
				found_move = False
				for option in check_order:
					blocked = False
					for dx,dy in checks[option]:
						if (x+dx,y+dy) in elves:
							blocked = True
					if not blocked and not found_move:
						next_pos = (x+deltas[option][0],y+deltas[option][1])
						if next_pos not in area_counts:
							area_counts[next_pos] = 1
						else:
							area_counts[next_pos] += 1
						next_area_by_elf[elf] = next_pos
						found_move = True
				if not found_move:
					next_elves.add(elf)
		for e,p in next_area_by_elf.items():
			if area_counts[p] == 1:
				next_elves.add(p)
			else:
				next_elves.add(e)
		elves = next_elves
		head = check_order.pop(0)
		check_order.append(head)
	return elves			

def stable_rounds(elves):
	all_dirs = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1))
	checks = { 'N' : ((-1,-1),(0,-1),(1,-1)),
		   'S' : ((-1,1),(0,1),(1,1)),
		   'W' : ((-1,0),(-1,1),(-1,-1)),
		   'E' : ((1,0),(1,1),(1,-1)) }
	deltas = { 'N' : (0,-1),
		   'S' : (0,1),
		   'W' : (-1,0),
		   'E' : (1,0) }
	check_order = ['N','S','W','E']
	r = 0
	while True:
		next_elves = set()
		area_counts = dict()
		next_area_by_elf = dict()
		for elf in elves:
			x,y = elf
			moving = False
			for dx,dy in all_dirs:
				if (x+dx,y+dy) in elves:
					moving = True
			if not moving:
				next_elves.add(elf)
			elif moving:
				found_move = False
				for option in check_order:
					blocked = False
					for dx,dy in checks[option]:
						if (x+dx,y+dy) in elves:
							blocked = True
					if not blocked and not found_move:
						next_pos = (x+deltas[option][0],y+deltas[option][1])
						if next_pos not in area_counts:
							area_counts[next_pos] = 1
						else:
							area_counts[next_pos] += 1
						next_area_by_elf[elf] = next_pos
						found_move = True
				if not found_move:
					next_elves.add(elf)
		if len(next_elves) == len(elves):
			return r+1
		for e,p in next_area_by_elf.items():
			if area_counts[p] == 1:
				next_elves.add(p)
			else:
				next_elves.add(e)
		elves = next_elves
		head = check_order.pop(0)
		check_order.append(head)
		r += 1


if __name__ == "__main__":

	elves = set()

	# Part 1 Solution
	with open('day23_input','r') as infile:
		y = 0
		for line in infile.readlines():
			for x,char in enumerate(line.strip()):
				if char == '#':
					elves.add((x,y))
			y += 1

	print(calc_area(bfs_rounds(elves,10)))

	# Part 2 Solution
	print(stable_rounds(elves))



