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
