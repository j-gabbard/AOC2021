import time
import re
import itertools
import sys
import statistics
from statistics import mode

def open_file():
  #going to open file and clean up data
  with open('./inputs/day3.txt', 'r') as f:
    scrubbed = [x.strip() for x in f.readlines()]
    #ordered = sorted(scrubbed)
    return scrubbed
    

def part1(inp):
  output = []
  antimode = []
  #look at each position 0-len, find most common in that position
  for pos in range(len(inp[0])):
    output.append(mode(x[pos] for x in inp))
  
  for num in output:
    if num == '0':
      antimode.append('1')
    else:
      antimode.append('0')
  
  #print(int(''.join(output), 2))
  #print(int(''.join(antimode), 2))
  return [int(''.join(output), 2) * int(''.join(antimode), 2), ''.join(output), ''.join(antimode)]

def part2(inp):
  most_long = []
  most_long = [x for x in inp]
  least_long = [x for x in inp]
  #print(least_long)
  
  #first find the one with the most common numbers
  #loop through most
  for i in range(len(most_long[0])):
    most_temp = []
    #find most common digit for position i
    high = mode([x[i] for x in most_long])
    #loop through most, delete entries with nonmatching digit
    #print(high)
    #f = input()
    for j in range(len(most_long)):
      if most_long[j][i] == high: 
        most_temp.append(most_long[j])
    #set master list to match just the output
    most_long = most_temp
    if len(most_long) == 1:
      break
    
  #print(most_long)
  
  #now the other thing
  
  #first find the one with the most common numbers
  #loop through least
  for i in range(len(least_long[0])):
    least_temp = []
    #find least common digit for position i
    #if zeroes and ones match, use zero
    number_zeroes = len([x[i] for x in least_long if x[i] == '0'])
    number_ones = len([x[i] for x in least_long if x[i] == '1'])
    #print(number_zeroes, number_ones)
    low = '0' if (mode([x[i] for x in least_long])) == '1' or number_zeroes == number_ones else '1'
    #loop through least, delete entries with nonmatching digit
    #print(low)
    #f = input()
    for j in range(len(least_long)):
      #print(f'position = {i+1}, mode = {low}, 
      #f = input()
      if least_long[j][i] == low: 
        #print('matched')
        least_temp.append(least_long[j])
        #print(least_temp[-1])
        #f = input()
    #set master list to match just the output
    least_long = least_temp
    #print(f'position = {i+1}, mode = {low}, list = {least_temp}')
    #q = input()
    if len(least_long) == 1:
      break
  #print(int(''.join(most_long), 2))
  #print(int(''.join(least_long), 2))
  return int(''.join(most_long), 2) * int(''.join(least_long), 2)


#part2(open_file())

t = time.time()
print(f'Part 1 - {part1(open_file())[0]}')
print(f'Part 2 - {part2(open_file())}')
print(f'took {time.time()-t} seconds')

