# python3
import sys


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    def BWT(s):
        """ Perform Burrows-Wheeler Transform on the input string s """
        table = sorted(s[i:] + s[:i] for i in range(len(s)))
        last_column = [row[-1] for row in table]
        return ''.join(last_column), table

    def construct_suffix_array_from_bwt(bwt, rotations):
        """ Construct suffix array from BWT and sorted rotations """
        n = len(bwt)
        suffix_array = []
        for rotation in rotations:
            # Find the original index of the suffix in the original string
            suffix_array.append(n - 1 - rotation.index('$'))
        return suffix_array

    # Get the BWT and sorted rotations
    bwt, rotations = BWT(text)
    # Construct the suffix array from BWT and rotations
    return construct_suffix_array_from_bwt(bwt, rotations)

if __name__ == '__main__':
    import sys
    text = sys.stdin.readline().strip()
    suffix_array = build_suffix_array(text)
    print(" ".join(map(str, suffix_array)))
