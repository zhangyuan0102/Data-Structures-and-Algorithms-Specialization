# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            # Process closing bracket
            if not opening_brackets_stack:
                # No matching opening bracket
                return i + 1

            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                # Mismatched opening bracket
                return i + 1

    if opening_brackets_stack:
        # Unmatched opening bracket
        top = opening_brackets_stack.pop()
        return top.position

    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)  # Print the result

if __name__ == "__main__":
    main()