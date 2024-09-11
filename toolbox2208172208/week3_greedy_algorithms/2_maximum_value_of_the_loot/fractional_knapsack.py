from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    value_density = [(v / w) for v, w in zip(values, weights)]
    sorted_indices = sorted(range(len(value_density)), key=lambda i: value_density[i], reverse=True)
    
    for i in sorted_indices:
        if capacity <= 0:
            break
        take_amount = min(weights[i], capacity)
        value += take_amount * value_density[i]
        capacity -= take_amount

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
