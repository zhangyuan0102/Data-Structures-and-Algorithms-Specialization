from sys import stdin
def points_cover_efficient(starts, ends, points):
    events = []

    # Add segment start and end points as events
    for start in starts:
        events.append((start, 'L'))
    for end in ends:
        events.append((end, 'R'))

    # Add point events
    point_index = [(point, i) for i, point in enumerate(points)]
    for point, idx in point_index:
        events.append((point, 'P', idx))

    # Sort events: first by position, then 'L' < 'P' < 'R' in case of ties
    events.sort(key=lambda x: (x[0], x[1]))

    count = [0] * len(points)
    active_segments = 0

    for event in events:
        if event[1] == 'L':
            active_segments += 1
        elif event[1] == 'R':
            active_segments -= 1
        else:  # event[1] == 'P'
            point_idx = event[2]
            count[point_idx] = active_segments

    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_efficient(input_starts, input_ends, input_points)
    print(*output_count)
