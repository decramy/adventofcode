#!/bin/env/python3

total = 0

with open("day3.txt") as file:
  for line in file:
    batteries = [int(x) for x in line.strip()]
    print("batteries: %s" % batteries)
    highest = max(batteries)
    highest_pos = batteries.index(highest)
    print("highest: %i at highest_pos: %i" % (highest, highest_pos))
    
    # zolang het hoogste niet op de laatste positie staat
    if highest_pos != len(batteries) - 1:
      print("highest is not at the end, proceed...")
      leftover = batteries[highest_pos+1:]
      print("  leftover: %s" % leftover)
      highest_after = max(leftover)
      print("  highest after: %i" % highest_after)
      joltage = int(str(highest) + str(highest_after))
    else:
      print("highest is at the end, oops...")
      
      second_highest = sorted(batteries,reverse=True)[1]
      second_highest_pos = batteries.index(second_highest)
      print("found second : %i at second__pos: %i" % (second_highest, second_highest_pos))
      
      leftover = batteries[second_highest_pos:]
      print("  leftover: %s" % leftover)
      highest_after_second = sorted(leftover,reverse=True)[0]

      joltage = int(str(second_highest) + str(highest_after_second))
    print("  found joltage: %i" % joltage)
    total += joltage
    
print(total)