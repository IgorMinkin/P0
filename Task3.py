"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def is_from_bangalore(phone_number):
  bangalore_area_code = "(080)"
  return phone_number[:5] == bangalore_area_code

def parse_area_code_or_prefix(phone_number):
  mobile_token_length = 4

  buffer = ""
  is_fixed_line = phone_number[0] == '('

  if is_fixed_line:
    for index in range(len(phone_number)):
      buffer += phone_number[index]
      if phone_number[index] == ')':
        break
  else:
    for index in range(mobile_token_length):
        buffer += phone_number[index]

  return buffer
    
def prefix_exists(all_prefixes, the_prefix):
  for prefix in all_prefixes:
    if prefix == the_prefix:
      return True

  return False

def add_with_order(all_prefixes, the_prefix):
  if len(all_prefixes) == 0:
    all_prefixes.append(the_prefix)
    return
    
  for index, prefix in enumerate(all_prefixes):
    if prefix == the_prefix:
      return
    elif index == len(all_prefixes) - 1:
      all_prefixes.append(the_prefix) if prefix < the_prefix else all_prefixes.insert(index, the_prefix)
      return
    elif prefix < the_prefix:
      continue
    else:
      insertion_index = index
      all_prefixes.insert(index, the_prefix)
      return

def get_bangalore_callees():
  buffer = []
  for call in calls:
    caller_number = call[0]
    if is_from_bangalore(caller_number):
      callee_number = call[1]
      prefix = parse_area_code_or_prefix(callee_number)
      add_with_order(buffer, prefix)

  return buffer

def calls_from_bangalore_to_bangalore():
  total_bangalore = 0
  to_bangalore = 0
  for call in calls:
    caller_number = call[0]
    callee_number = call[1]
    if is_from_bangalore(caller_number):
      total_bangalore += 1
      if is_from_bangalore(callee_number):
        to_bangalore += 1

  return total_bangalore, to_bangalore

def test():
  bangalore_number = "(080)41095396"
  non_bangalore_1 = "97406 93118"
  non_bangalore_2 = "(04546)388977"
  assert(is_from_bangalore(bangalore_number))
  assert(not is_from_bangalore(non_bangalore_1))

  assert(parse_area_code_or_prefix(bangalore_number) == "(080)")
  assert(parse_area_code_or_prefix(non_bangalore_1) == "9740")
  assert(parse_area_code_or_prefix(non_bangalore_2) == "(04546)")

  test_prefixes = ["(080)","(081)","1234"]
  assert(prefix_exists(test_prefixes, "(081)"))
  assert(not prefix_exists(test_prefixes, "(082)"))

  test_collection = []
  add_with_order(test_collection, 'a')
  assert(test_collection == ['a'])
  test_collection = ['a', 'b']
  add_with_order(test_collection, 'd')
  assert(test_collection == ['a', 'b', 'd'])
  add_with_order(test_collection, 'c')
  assert(test_collection == ['a', 'b', 'c', 'd'])
  add_with_order(test_collection, 'bb')
  add_with_order(test_collection, 'dd')
  add_with_order(test_collection, 'aaa')
  add_with_order(test_collection, 'bb')
  assert(test_collection == ['a', 'aaa', 'b', 'bb', 'c', 'd', 'dd'])

test()
'''
Part A
Function "get_bangalore_callees" is looping over the list of all calls. For each call it invokes the following functions:
  - is_from_bangalore: checks a substring so constant time O(1)
  - parse_area_code_or_prefix: iterates over the length of the input string (phone number) so constant time in relation to length of input array. O(n) in relation to size of input string
  - add_with_order: iterates over the length of the input collection to determine the correct insertion position so linear: O(n)
Combined: O(n * (1 + 1 + n)) = O(2n + n^2) ~ O(n^2)
'''
bangalore_callees = get_bangalore_callees()
print("The numbers called by people in Bangalore have codes:")
for prefix in bangalore_callees:
  print(prefix)

'''
Part B
Function "calls_from_bangalore_to_bangalore" iterates over the input array and checks if caller is from Bangalore and if so checks if callee is from Bangalore. Worst case
scerio all calls are from/to Bangalore so combined order: O(n + n + 1) ~ O(n)
'''

all_from_bangalore, to_bangalore = calls_from_bangalore_to_bangalore()
fraction_of_total = round((to_bangalore / all_from_bangalore)* 100, 2)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(fraction_of_total))
