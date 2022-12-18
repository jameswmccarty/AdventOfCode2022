#!/usr/bin/python

"""

--- Day 18: Boiling Boulders ---

You and the elephants finally reach fresh air. You've emerged near the base of a large volcano that seems to be actively erupting! Fortunately, the lava seems to be flowing away from you and toward the ocean.

Bits of lava are still being ejected toward you, so you're sheltering in the cavern exit a little longer. Outside the cave, you can see the lava landing in a pond and hear it loudly hissing as it solidifies.

Depending on the specific compounds in the lava and speed at which it cools, it might be forming obsidian! The cooling rate should be based on the surface area of the lava droplets, so you take a quick scan of a droplet as it flies past you (your puzzle input).

Because of how quickly the lava is moving, the scan isn't very good; its resolution is quite low and, as a result, it approximates the shape of the lava droplet with 1x1x1 cubes on a 3D grid, each given as its x,y,z position.

To approximate the surface area, count the number of sides of each cube that are not immediately connected to another cube. So, if your scan were only two adjacent cubes like 1,1,1 and 2,1,1, each cube would have a single side covered and five sides exposed, a total surface area of 10 sides.

Here's a larger example:

2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5

In the above example, after counting up all the sides that aren't connected to another cube, the total surface area is 64.

What is the surface area of your scanned lava droplet?

Your puzzle answer was 4450.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Something seems off about your calculation. The cooling rate depends on exterior surface area, but your calculation also included the surface area of air pockets trapped in the lava droplet.

Instead, consider only cube sides that could be reached by the water and steam as the lava droplet tumbles into the pond. The steam will expand to reach as much as possible, completely displacing any air on the outside of the lava droplet but never expanding diagonally.

In the larger example above, exactly one cube of air is trapped within the lava droplet (at 2,2,5), so the exterior surface area of the lava droplet is 58.

What is the exterior surface area of your scanned lava droplet?

Your puzzle answer was 2564.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

min_x = None
max_x = None
min_y = None
max_y = None
min_z = None
max_z = None

def unmatched(cubes):
	deltas = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
	total_unmatched = 0
	for cube in cubes:
		x,y,z = cube
		adjacent = 0
		for dx,dy,dz in deltas:
			if (x+dx,y+dy,z+dz) in cubes:
				adjacent += 1
		total_unmatched += (6-adjacent)
	return total_unmatched

def unmatched2(check_set,cubes):
	deltas = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
	total_unmatched = 0
	for cube in check_set:
		x,y,z = cube
		adjacent = 0
		for dx,dy,dz in deltas:
			if (x+dx,y+dy,z+dz) in cubes:
				adjacent += 1
		if adjacent != 0:
			total_unmatched += adjacent
	return total_unmatched

# Determine if a location is part of an interior bubble
def loc_is_part_of_a_bubble(loc):
	global min_x,max_x,min_y,max_y,min_z,max_z
	if loc in cubes:
		return False
	seen = set()
	deltas = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
	q = [loc]
	while len(q) > 0:
		x,y,z = q.pop(0)
		if x < min_x or x > max_x or y < min_y or y > max_y or z < min_z or z > max_z:
			return False
		for dx,dy,dz in deltas:
			if (x+dx,y+dy,z+dz) not in cubes and (x+dx,y+dy,z+dz) not in seen:
				seen.add((x+dx,y+dy,z+dz))
				q.append((x+dx,y+dy,z+dz))
	return True

if __name__ == "__main__":

	cubes = set()

	# Part 1 Solution
	with open('day18_input','r') as infile:
		for line in infile.readlines():
			x,y,z = map(int,line.split(','))
			cubes.add((x,y,z))
	surf_area = unmatched(cubes)
	print(surf_area)

	# Part 2 Solution
	min_x = min(x[0] for x in cubes)
	max_x = max(x[0] for x in cubes)
	min_y = min(y[1] for y in cubes)
	max_y = max(y[1] for y in cubes)
	min_z = min(z[2] for z in cubes)
	max_z = max(z[2] for z in cubes)

	bubble_parts = set()

	for x in range(min_x,max_x):
		for y in range(min_y,max_y):
			for z in range(min_z,max_z):
				if loc_is_part_of_a_bubble((x,y,z)):
					bubble_parts.add((x,y,z))
	print(surf_area - unmatched2(bubble_parts,cubes))
