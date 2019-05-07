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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def add_with_order(all_items, the_item):
  if len(all_items) == 0:
    all_items.append(the_item)
    return
    
  for index, item in enumerate(all_items):
    if item == the_item:
      return
    elif index == len(all_items) - 1:
      all_items.append(the_item) if item < the_item else all_items.insert(index, the_item)
      return
    elif item < the_item:
      continue
    else:
      insertion_index = index
      all_items.insert(index, the_item)
      return

def has_incoming_calls(caller, all_calls):
    for call in all_calls:
        callee = call[1]
        if callee == caller:
            return True

    return False

def has_incoming_or_outgoing_texts(caller, all_texts):
    for text in all_texts:
        from_number = text[0]
        to_number = text[1]
        if caller == from_number or caller == to_number:
            return True

    return False


def find_telemarketers(all_calls, all_texts):
    suspects = []
    cleared = []

    for call in all_calls:
        caller = call[0]
        if caller in suspects:
            continue
        if caller in cleared:
            continue
        if has_incoming_calls(caller, all_calls):
            cleared.append(caller)
        elif has_incoming_or_outgoing_texts(caller, all_texts):
            cleared.append(caller)
        else:
            add_with_order(suspects, caller)

    return suspects

def test():
    all_calls = [
        ['1111', '2222'],
        ['1111', '3333'],
        ['3333', '1111'],
        ['4444', '1111'],
        ['4444', '2222'],
        ['5555', '1111'],
        ['7777', '3333']
    ]

    all_texts = [
        ['6666', '5555']
    ]

    suspects = find_telemarketers(all_calls, all_texts) 
    assert(suspects == ['4444', '7777']) 

test()

'''
Function "find_telemarketers" loops over the list of all calls "O(n)" and:
    - checks if the number has already been flagged as suspect by looping through list of suspect numbers: "O(n)"
    - checks if the number has already been cleared by looping through list of suspect numbers: "O(n)"
    - checks if number has had any incoming calls by looping through the list of calls again: "O(n)"
    - checks if number has sent or received any text messages by looping through the list of text messages: "O(n)"
    - if all checks negative adds the number to the list of suspects in lexicographic order with no duplicates: "O(n)"

Combined order: O(n * (5n)) = O(5n^2) ~ O(n^2)
'''
print("These numbers could be telemarketers: ")
for suspect in find_telemarketers(calls, texts):
    print(suspect)
