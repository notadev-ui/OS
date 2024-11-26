def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival'])
    time_elapsed = 0
    for process in processes:
        if time_elapsed < process['arrival']:
            time_elapsed = process['arrival']
        print(f"Process {process['id']} started at {time_elapsed}")
        time_elapsed += process['burst']

fcfs_scheduling([
    {"id": 1, "arrival": 0, "burst": 5},
    {"id": 2, "arrival": 1, "burst": 3}
])



