""" first come first serve(fcfs) is a non preemptive scheduline
 algorithm where the process that first come gets executed first. 
 it's easy to implement by can lead to the canvay effect where
   shorter process get delayed by longer process by leading to higher waiting time.
"""


"""def fcfs(processes):
    processes.sort(key=lambda x: x['arrival'] )
    time_elapsed = 0
    for process in processes:
        if time_elapsed < process['arrival']:
           time_elapsed = process['arrival']
        print(f"prcoess {process['id']} start at  {time_elapsed}")
        time_elapsed += process ['burst']


fcfs([
    {"id":1, "arrival": 2, "burst":6},
    {"id":2, "arrival": 5 , "burst":3},
    {"id":3, "arrival": 1 , "burst":8},
    {"id":4, "arrival": 0 , "burst":3},
    {"id":5, "arrival": 4 , "burst":4}
         
])



def sjf(processes):
    processes.sort(key=lambda x: x['burst'] )
    time_elapsed = 0
    for process in processes:
        if time_elapsed < process['arrival']: 
            time_elapsed = process['arrival']
        print(f"prcoess {process['id']} start at  {time_elapsed}")
        time_elapsed += process ['burst']
          
sjf([
    {"id":1, "arrival": 2, "burst":6},
    {"id":2, "arrival": 5 , "burst":3},
    {"id":3, "arrival": 1 , "burst":8},
    {"id":4, "arrival": 0 , "burst":3},
    {"id":5, "arrival": 4 , "burst":4}
         
])


def npps(processes):
    processes.sort(key=lambda x: (x['burst'], x['priority']))
    time_elapsed = 0
    for process in processes:
        if time_elapsed < process['arrival']: 
            time_elapsed = process['arrival']
        print(f"prcoess {process['id']} start at  {time_elapsed}")
        time_elapsed += process ['burst']
          
npps([
    {"id":1, "arrival": 2, "priority" :2, "burst":6},
    {"id":2, "arrival": 5 , "priority" :4, "burst":3},
    {"id":3, "arrival": 1 , "priority" :3, "burst":8},
    {"id":4, "arrival": 0 , "priority" :1,  "burst":3},
    {"id":5, "arrival": 4 , "priority" :5, "burst":4}
         
])"""


"""Shortest Remaining Job First (SRJF), also known as Shortest Remaining Time First (SRTF),
 is a CPU scheduling algorithm that selects the process with 
 the smallest burst time (execution time) among the processes 
 currently available (those that have arrived)."""

"""""
def srjf(processes):
    processes.sort (key = lambda x : x['arrival'])
    time_elapsed = 0
    completed = 0
    while completed < len(processes):
        available = [ p for p in processes if p['arrival']<= time_elapsed and not p.get('completed')]

        if not available:
            time_elapsed +=1
            continue
        
        shortest = min(available, key= lambda x :x['burst'])
        print(f"process {shortest['id'] } started at {time_elapsed}")
        time_elapsed += shortest['burst']
        shortest['completed'] = True
        completed += 1


    
srjf( [
    {'id': 1, 'arrival': 0, 'burst': 8},
    {'id': 2, 'arrival': 1, 'burst': 4},
    {'id': 3, 'arrival': 2, 'burst': 9},
    {'id': 4, 'arrival': 3, 'burst': 5}
])

"""

def optimal_page_replacement(pages, frame_count):
    frames = []
    faults = 0
    for i, page in enumerate(pages):
        if page not in frames:
            faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                future = {f: (pages[i + 1:].index(f) if f in pages[i + 1:] else float('inf')) for f in frames}
                to_replace = max(future, key=future.get)
                frames[frames.index(to_replace)] = page
        print(f"Step {i+1}: Frames: {frames}")
    print(f"Total faults: {faults}")

optimal_page_replacement([1, 2, 3, 2, 1, 4, 5], 3)
