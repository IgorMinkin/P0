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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

print("First record of texts, {} texts {} at time {}".format(texts[0][0], texts[0][1], texts[0][2]))

number_of_calls = len(calls)
index_of_last_call = number_of_calls - 1
""" Order O(1)"""
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
    calls[index_of_last_call][0], 
    calls[index_of_last_call][1], 
    calls[index_of_last_call][2], 
    calls[index_of_last_call][3]))
