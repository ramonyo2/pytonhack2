"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    result = {}
    count = 0
    for key, value in s.items():
        if count == 0:
            new_key = key.capitalize()
            new_value = value.capitalize().replace('k', '')
            result[new_key] = new_value
        count += 1
    return result
