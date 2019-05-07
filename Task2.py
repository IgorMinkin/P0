"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# go through the list
 # for each call
    # store (caller, duration), (callee, duration)

class PartyOnPhone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.duration = 0
    
    def add_call(self, duration):
        self.duration += duration

def find_party(all_parties, phone_number):
    for party in all_parties:
        if party.phone_number == phone_number:
            return party

    return None

def aggregate_total_duration_by_number(calls):
    parties_with_duration = []
    for call in calls:
        caller = call[0]
        callee = call[1]
        duration = int(call[3])
        callee_record = find_party(parties_with_duration, callee)
        caller_record = find_party(parties_with_duration, caller)
        
        if callee_record == None:
            callee_record = PartyOnPhone(callee)
            parties_with_duration.append(callee_record)
        callee_record.add_call(duration)
        
        if caller_record == None:
            caller_record = PartyOnPhone(caller)
            parties_with_duration.append(caller_record)
        caller_record.add_call(duration)
    
    return parties_with_duration

def find_party_with_max_duration(all_parties_on_phone):
    the_max = None
    for party in all_parties_on_phone:
        if the_max == None:
            the_max = party
        else:
            the_max = party if party.duration > the_max.duration else the_max
    
    return the_max

def test():
    test_calls = [
        [1111, 2222, '30-09-2016 20:20:18', '100'],
        [2222, 1111, '30-09-2016 20:20:18', '100'],
        [3333, 1111, '30-09-2016 20:20:18', '100'],
    ]

    aggregates = aggregate_total_duration_by_number(test_calls)
    assert(find_party(aggregates, 1111).duration == 300)
    assert(find_party(aggregates, 2222).duration == 200)
    assert(find_party(aggregates, 3333).duration == 100)

    the_talker = find_party_with_max_duration(aggregates)
    assert(the_talker.phone_number == 1111)
    assert(the_talker.duration == 300)

"""
 Function 'aggregate_total_duration_by_number' has order of O(n^2). It has to iterate once through 
 each call and then for each call it has to see if callee and caller already have a record. Worst
 case runtime is O(2n^2) or O(n^2). To find party with longest time on phone you have to iterate
 through the resulting list once so linear time - O(n). Total would be O(2n^2 + n) or O(n^2)
"""

aggregates = aggregate_total_duration_by_number(calls)
the_talker = find_party_with_max_duration(aggregates)
print("{} spent the longest time, {} seconds, on the phone during September 2016." \
    .format(str(the_talker.phone_number), str(the_talker.duration)))
