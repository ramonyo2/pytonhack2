"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    result = []
    count = 1
    
    for item in s:
        new_item = {}
        for key in item:
            new_item[str(count)] = str(count + 1)
            count += 2
        result.append(new_item)
    return result
