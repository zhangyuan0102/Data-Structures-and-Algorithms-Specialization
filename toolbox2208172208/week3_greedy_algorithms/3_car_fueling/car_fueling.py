from sys import stdin


def min_refills(distance, tank, stops):
    current_refills = 0
    distance_remain = distance
    current_position = 0

    # If the distance between the cities is greater than what the car can travel with a full tank
    if tank < stops[0] or distance - stops[-1] > tank:
        return -1

    # Loop through each stop
    for i in range(len(stops) - 1):
        if stops[i + 1] - stops[i] > tank:  # If the distance between consecutive stops is greater than the tank capacity
            return -1

    # Loop through each stop to calculate refills
    for i in range(len(stops)):
        if current_position + tank >= stops[i]:
            if i == len(stops) - 1:  # If the current stop is the last stop
                if distance_remain <= tank:  # If the remaining distance can be covered with the remaining fuel
                    return current_refills
                else:  # Otherwise, make a refill
                    current_refills += 1
            elif current_position + tank < stops[i + 1]:  # If the next stop is out of reach with current fuel
                current_position = stops[i]  # Move to the current stop
                current_refills += 1

    return current_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
