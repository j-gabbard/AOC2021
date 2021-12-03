import time
import re
import itertools
import sys


def open_file():
  #going to open file and clean up data
  with open('./inputs/day1.txt', 'r') as f:
    scrubbed = [int(x.strip()) for x in f.readlines()]
    #ordered = sorted(scrubbed)
    return scrubbed
    

def part1(inp):
  #print(inp[:10])
  #x = input()
  #check each value and see if it's higher than the previous
  count = 0
  pos = 1
  previous = inp[0]
    
  for x in inp[1:]:
    #have to skip first element
    #print()
    #z = input()
    if x > previous: 
      count += 1
      flag = "higher"

    #print(f'{pos} - current={x}, previous={previous}, count={count}, {flag}')
    #temp = input()
    previous = x
    pos += 1

  return(count)
'''t = time.time()
part1(open_file())
part2(open_file())
print(f'took {time.time()-t} seconds')'''

def part2(inp):
  #check each value and see if it's higher than the previous
  count = 0
  previous = inp[0] + inp[1] + inp[2]
  pos = 3

  
  
  for x in inp[3:]:
    #starting at 2nd/3rd/4th element in list
    flag = 0
    #set pos to 4th element
    sum = x + inp[pos-1] + inp[pos-2]
    if sum > previous: 
      count += 1
      flag = "higher"
    #print(f'{pos} - current={sum}, previous={previous}, count={count}, {flag}')
    previous = sum
    pos += 1

  return(count)
t = time.time()
print(f'Part 1 - {part1(open_file())}')
print(f'Part 2 - {part2(open_file())}')
print(f'took {time.time()-t} seconds')

