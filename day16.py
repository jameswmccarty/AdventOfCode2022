#!/usr/bin/python

"""
--- Day 16: Proboscidea Volcanium ---

The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.

The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!

You need to get the elephants out of here, quickly. Your device estimates that you have 30 minutes before the volcano erupts, so you don't have time to go back out the way you came in.

You scan the cave for other options and discover a network of pipes and pressure-release valves. You aren't sure how such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle input) of each valve's flow rate if it were opened (in pressure per minute) and the tunnels you could use to move between the valves.

There's even a valve in the room you and the elephants are currently standing in labeled AA. You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?

For example, suppose you had the following scan output:

Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II

All of the valves begin closed. You start at valve AA, but it must be damaged or jammed or something: its flow rate is 0, so there's no point in opening it. However, you could spend one minute moving to valve BB and another minute opening it; doing so would release pressure during the remaining 28 minutes at a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. Then, you could spend your third minute moving to valve CC and your fourth minute opening it, providing an additional 26 minutes of eventual pressure release at a flow rate of 2, or 52 total pressure released by valve CC.

Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:

== Minute 1 ==
No valves are open.
You move to valve DD.

== Minute 2 ==
No valves are open.
You open valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You move to valve CC.

== Minute 4 ==
Valve DD is open, releasing 20 pressure.
You move to valve BB.

== Minute 5 ==
Valve DD is open, releasing 20 pressure.
You open valve BB.

== Minute 6 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve AA.

== Minute 7 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve II.

== Minute 8 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve JJ.

== Minute 9 ==
Valves BB and DD are open, releasing 33 pressure.
You open valve JJ.

== Minute 10 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve II.

== Minute 11 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve AA.

== Minute 12 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve DD.

== Minute 13 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve EE.

== Minute 14 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve FF.

== Minute 15 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve GG.

== Minute 16 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve HH.

== Minute 17 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You open valve HH.

== Minute 18 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve GG.

== Minute 19 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve FF.

== Minute 20 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve EE.

== Minute 21 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve EE.

== Minute 22 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve DD.

== Minute 23 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve CC.

== Minute 24 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You open valve CC.

== Minute 25 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 27 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 28 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 29 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 30 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

This approach lets you release the most pressure possible in 30 minutes with this valve layout, 1651.

Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?

Your puzzle answer was 2181.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

You're worried that even with an optimal approach, the pressure released won't be enough. What if you got one of the elephants to help you?

It would take you 4 minutes to teach an elephant how to open the right valves in the right order, leaving you with only 26 minutes to actually execute your plan. Would having two of you working together be better, even if it means having less time? (Assume that you teach the elephant before opening any valves yourself, giving you both the same full 26 minutes.)

In the example above, you could teach the elephant to help you as follows:

== Minute 1 ==
No valves are open.
You move to valve II.
The elephant moves to valve DD.

== Minute 2 ==
No valves are open.
You move to valve JJ.
The elephant opens valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You open valve JJ.
The elephant moves to valve EE.

== Minute 4 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve II.
The elephant moves to valve FF.

== Minute 5 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve AA.
The elephant moves to valve GG.

== Minute 6 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve BB.
The elephant moves to valve HH.

== Minute 7 ==
Valves DD and JJ are open, releasing 41 pressure.
You open valve BB.
The elephant opens valve HH.

== Minute 8 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve CC.
The elephant moves to valve GG.

== Minute 9 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve CC.
The elephant moves to valve FF.

== Minute 10 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant moves to valve EE.

== Minute 11 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant opens valve EE.

(At this point, all valves are open.)

== Minute 12 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 20 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

With the elephant helping, after 26 minutes, the best you could do would release a total of 1707 pressure.

With you and an elephant working together for 26 minutes, what is the most pressure you could release?

Your puzzle answer was 2824.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

import heapq
from itertools import combinations

tunnels = dict()
travel_cost = dict()
rates   = dict()

def dist_between(a,b):
	q = []
	q.append((0,a))
	seen = set()
	seen.add(a)
	while len(q) > 0:
		steps,pos = q.pop(0)
		if pos == b:
			return steps
		else:
			for c in tunnels[pos]:
				if c not in seen:
					q.append((steps+1,c))
					seen.add(c)
	return float('inf')

def parse_line(line):
	rate,connections = line.split(';')
	valve,rate = rate.split(' has flow rate=')
	valve = valve.replace("Valve ",'').strip()
	rate  = int(rate)
	junk,connections = connections.split(' valve')
	connections = connections.replace('s ','')
	connections = connections.split(',')
	tunnels[valve] = [ c.strip() for c in connections ]
	rates[valve] = rate

def search(targets):
	best = 0
	q = []
	heapq.heappush(q,(0,'AA',targets,30))
	while len(q) > 0:
		total,pos,targets,time = heapq.heappop(q)
		best = min(best,total)
		if len(targets) == 0 or time <= 0:
			best = min(best,total)
		elif time > 0:
			for t in targets:
				if time - travel_cost[(pos,t)] > 1:
					new_time = time - travel_cost[(pos,t)]
					heapq.heappush(q,(total-(new_time-1)*rates[t],t,[ x for x in targets if x != t],new_time-1))
	return -best

# This method works for the problem, but not the example, because all targets can be reached
# in the given time in the Example.  We can use a greedy combination of the best that one
# search can do, and then the best search on any targets that could not be reached in the
# first search.
def search2(targets):
	best = 0
	q = []
	left_targets = None
	heapq.heappush(q,(0,'AA',targets,26))
	while len(q) > 0:
		total,pos,targets,time = heapq.heappop(q)
		if total < best:
			best = min(best,total)
			left_targets = targets[:]
		if len(targets) == 0 or time <= 0:
			if total < best:
				best = min(best,total)
				left_targets = targets[:]
		elif time > 0:
			for t in targets:
				if time - travel_cost[(pos,t)] > 1:
					new_time = time - travel_cost[(pos,t)]
					heapq.heappush(q,(total-(new_time-1)*rates[t],t,[ x for x in targets if x != t],new_time-1))
	return -best,left_targets

def two_party_search(targets):
	best = 0
	q = []
	heapq.heappush(q,(0,'AA','AA',targets,26,26))
	while len(q) > 0:
		total,p1,p2,targets,t1,t2 = heapq.heappop(q)
		best = min(best,total)
		if len(targets) == 0 or (t1 <= 0 and t2 <= 0):
			best = min(best,total)
		elif (t1 > 0 or t2 > 0) and len(targets) > 0:
			if len(targets) >= 2 and t1 > 0 and t2 > 0:
				for combo in combinations(targets,2):
					a,b = combo
					if t1 - travel_cost[(p1,a)] > 1 and t2 - travel_cost[(p2,b)] > 1:
						new_t1 = t1 - travel_cost[(p1,a)]
						new_t2 = t2 - travel_cost[(p2,b)]
						heapq.heappush(q,(total-((new_t1-1)*rates[a]+(new_t2-1)*rates[b]),a,b,[ x for x in targets if x not in [a,b] ],new_t1-1,new_t2-1))
					if t1 - travel_cost[(p1,a)] > 1 and t2 - travel_cost[(p2,b)] < 1:
						new_t1 = t1 - travel_cost[(p1,a)]
						heapq.heappush(q,(total-(new_t1-1)*rates[a],a,'--',[ x for x in targets if x != a ],new_t1-1,0))
					if t1 - travel_cost[(p1,a)] < 1 and t2 - travel_cost[(p2,b)] > 1:
						new_t2 = t2 - travel_cost[(p2,b)]
						heapq.heappush(q,(total-(new_t2-1)*rates[b],'--',b,[ x for x in targets if x != b ],0,new_t2-1))
					b,a = combo
					if t1 - travel_cost[(p1,a)] > 1 and t2 - travel_cost[(p2,b)] > 1:
						new_t1 = t1 - travel_cost[(p1,a)]
						new_t2 = t2 - travel_cost[(p2,b)]
						heapq.heappush(q,(total-((new_t1-1)*rates[a]+(new_t2-1)*rates[b]),a,b,[ x for x in targets if x not in [a,b] ],new_t1-1,new_t2-1))
					if t1 - travel_cost[(p1,a)] > 1 and t2 - travel_cost[(p2,b)] < 1:
						new_t1 = t1 - travel_cost[(p1,a)]
						heapq.heappush(q,(total-(new_t1-1)*rates[a],a,'--',[ x for x in targets if x != a ],new_t1-1,0))
					if t1 - travel_cost[(p1,a)] < 1 and t2 - travel_cost[(p2,b)] > 1:
						new_t2 = t2 - travel_cost[(p2,b)]
						heapq.heappush(q,(total-(new_t2-1)*rates[b],'--',b,[ x for x in targets if x != b ],0,new_t2-1))
			elif p1 == '--' or p2 == '--':
				for a in targets:
					if p1 != '--' and t1 - travel_cost[(p1,a)] > 1:
						new_t1 = t1 - travel_cost[(p1,a)]
						heapq.heappush(q,(total-(new_t1-1)*rates[a],a,'--',[ x for x in targets if x != a],new_t1-1,t2))
					if p2 != '--' and t2 - travel_cost[(p2,a)] > 1:
						new_t2 = t2 - travel_cost[(p2,a)]
						heapq.heappush(q,(total-(new_t2-1)*rates[a],'--',a,[ x for x in targets if x != a],t1,new_t2-1))
	return -best

if __name__ == "__main__":

	# Part 1 Solution
	with open('day16_input','r') as infile:
		for line in infile.readlines():
			parse_line(line)
	for a in tunnels.keys():
		for b in tunnels.keys():
			travel_cost[(a,b)] = dist_between(a,b)
			travel_cost[(b,a)] = travel_cost[(a,b)]
			travel_cost[(a,'--')] = float('inf')
			travel_cost[(b,'--')] = float('inf')
			travel_cost[('--',a)] = float('inf')
			travel_cost[('--',b)] = float('inf')
	targets = [ k for k,v in rates.items() if v > 0 ]
	print(search(targets))

	# Part 2 Solution
	#print(two_party_search(targets)) # Works for Example -- very slow to check full problem
	points_so_far, left_to_search = search2(targets)
	final_points, junk = search2(left_to_search)
	print(points_so_far+final_points)

