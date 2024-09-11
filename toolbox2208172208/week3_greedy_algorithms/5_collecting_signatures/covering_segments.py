from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
   events = [(segment.start, 'start') for segment in segments] + [(segment.end, 'end') for segment in segments]
    events_sorted = events.sorted(index = segment.start) 
    current_segment = event[0]
    points = []
    for i in len(segments_sorted):
        if event[i] == 'start' and event[i+1] == 'end' and current_event == event[i]:
            points.append(event[i+1])
            current_event = event[i+1]
        if event[i] == 'start' and event[i+1] == 'start'and current_event == event[i]:
            current_event == event[i+1]
        if event[i] == 'end' and event[i+1] == 'start'and current_event == event[i]:
             current_event == event[i+1]
        if event[i] == 'end' and event[i+1] == 'end'and current_event == event[i]:
            current_event == event[i+1]
    return points

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
