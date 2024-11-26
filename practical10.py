def srjf_scheduling(processes):
    processes.sort(key=lambda x: x['arrival'])
    time_elapsed = 0
    completed = 0
    while completed < len(processes):
        available = [p for p in processes if p['arrival'] <= time_elapsed and not p.get('completed')]
        if not available:
            time_elapsed += 1
            continue
        shortest = min(available, key=lambda x: x['burst'])
        print(f"Process {shortest['id']} started at {time_elapsed}")
        time_elapsed += shortest['burst']
        shortest['completed'] = True
        completed += 1



srjf_scheduling([
    {"id": 1, "arrival": 0, "burst": 5},
    {"id": 2, "arrival": 1, "burst": 3}
])
