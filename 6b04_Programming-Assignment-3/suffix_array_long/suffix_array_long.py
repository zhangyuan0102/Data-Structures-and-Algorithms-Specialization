# python3
import sys

def sortcharacter(text):
    n = len(text)
    order = [0] * n
    count = [0] * 256  # ASCII characters

    for char in text:
        count[ord(char)] += 1

    for j in range(1, 256):
        count[j] += count[j - 1]

    for i in range(n - 1, -1, -1):
        c = ord(text[i])
        count[c] -= 1
        order[count[c]] = i

    return order

def buildclass(text, order):
    n = len(text)
    classes = [0] * n
    classes[order[0]] = 0

    for i in range(1, n):
        if text[order[i]] != text[order[i - 1]]:
            classes[order[i]] = classes[order[i - 1]] + 1
        else:
            classes[order[i]] = classes[order[i - 1]]

    return classes

def sortdouble(text, k, order, classes):
    n = len(text)
    count = [0] * n
    new_order = [0] * n

    for i in range(n):
        count[classes[i]] += 1

    for j in range(1, n):
        count[j] += count[j - 1]

    for i in range(n - 1, -1, -1):
        start = (order[i] - k + n) % n
        cl = classes[start]
        count[cl] -= 1
        new_order[count[cl]] = start

    return new_order

def updateclass(new_order, classes, k):
    n = len(new_order)
    new_classes = [0] * n
    new_classes[new_order[0]] = 0

    for i in range(1, n):
        curr = new_order[i]
        prev = new_order[i - 1]
        mid_curr = (curr + k) % n
        mid_prev = (prev + k) % n
        if classes[curr] != classes[prev] or classes[mid_curr] != classes[mid_prev]:
            new_classes[curr] = new_classes[prev] + 1
        else:
            new_classes[curr] = new_classes[prev]

    return new_classes

def build_suffix_array(text):
    order = sortcharacter(text)
    classes = buildclass(text, order)
    k = 1

    while k < len(text):
        order = sortdouble(text, k, order, classes)
        classes = updateclass(order, classes, k)
        k *= 2

    return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
