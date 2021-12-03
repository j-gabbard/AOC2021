import time
import re
import itertools
import sys


def open_file():
  #going to open file and clean up data
  with open('./inputs/day2.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]
    #ordered = sorted(scrubbed)
    return scrubbed
    

def part1(inp):
  #start at origin
  pos = 0
  depth = 0

  for x in inp:
    direction, amount = x.split(' ')
    if direction == 'forward':
      pos += int(amount)
    if direction == 'down':
      depth += int(amount)
    if direction == 'up':
      depth -= int(amount)
    
  print(f'positon = {pos}, depth = {depth}')  

  return(pos*depth)

def part2(inp):
  #start at origin
  pos = 0
  depth = 0
  aim = 0

  for x in inp:
    direction, amount = x.split(' ')
    if direction == 'forward':
      pos += int(amount)
      depth += aim * int(amount)
    if direction == 'down':
      aim += int(amount)
    if direction == 'up':
      aim -= int(amount)
    
  print(f'positon = {pos}, depth = {depth}')  

  return(pos*depth)

t = time.time()
print(f'Part 1 - {part1(open_file())}')
print(f'Part 2 - {part2(open_file())}')
print(f'took {time.time()-t} seconds')

