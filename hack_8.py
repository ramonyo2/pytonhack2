"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    longitud = len(s)

    if longitud % 2 == 0:
        return [str(longitud - i) for i in range(longitud)]
    else:
        return [f"{letter}-{longitud - i}" for i, letter in enumerate(reversed(s))]

    return result
