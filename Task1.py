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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
all_rows = calls + texts
distinct_numbers = []

def exists_in_list(item_to_check, list):
    for item in list:
        if item == item_to_check:
            return True
    return False

for row in all_rows:
    source = row[0]
    destination = row[1]
    if not exists_in_list(source, distinct_numbers):
        distinct_numbers.append(source)
    if not exists_in_list(destination, distinct_numbers):
        distinct_numbers.append(destination)

def test():
    all_numbers = [x[0] for x in calls] + [x[1] for x in calls] \
        + [x[0] for x in texts] + [x[1] for x in texts]
    assert(len(set(all_numbers)) == len(distinct_numbers))

test()
""" Order O(n^2) """
print("There are {} different telephone numbers in the records.".format(len(distinct_numbers)))