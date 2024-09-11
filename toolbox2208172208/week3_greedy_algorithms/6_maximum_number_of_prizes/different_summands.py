import numpy as np
def optimal_summands(n):
    summands = []
    if n == 1:
        summands.append(1)
    elif n == 2:
        return [] 
    else:
        for k in range(2, int(np.sqrt(2*n)) + 1): 
            if (1 + k) * k / 2 <= n and (1 + k + 1) * (k + 1) / 2 > n:
                break  
        for i in range(1, k): 
            summands.append(i)
        summands.append(n - (1 + k) * k / 2 + k) 

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
