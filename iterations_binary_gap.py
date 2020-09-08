import re


def solution(n):
    n_bin = "{0:b}".format(n)
    gaps = re.findall(r"[0]+1", n_bin)
    if len(gaps) == 0:
        longest_gap = 0
    else:
        longest_gap = max([len(i) for i in gaps]) - 1
    return longest_gap
