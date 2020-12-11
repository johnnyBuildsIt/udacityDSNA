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
CALLERS = 0
RECEIVERS = 1
callTimes = {}


def get_times_for_numbers(index):
    for entry in calls:
        if entry[index] not in callTimes.keys():
            callTimes[entry[index]] = int(entry[3])
        else:
            callTimes[entry[index]] += int(entry[3])


get_times_for_numbers(CALLERS)
get_times_for_numbers(RECEIVERS)

num_with_max_time = max(callTimes, key=callTimes.get)

print("{0} spent the longest time, {1} seconds, on the phone during September 2016."
      .format(num_with_max_time, callTimes.get(num_with_max_time)))
