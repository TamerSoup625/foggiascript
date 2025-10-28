def reversed_enumerate(data: tuple | list):
    for i in range(len(data) - 1, -1, -1):
        yield (i, data[i])


# https://chatgpt.com/c/68fcc772-aa34-832f-ad53-b6dc5ed2e7b8
def split_when(iterable, separator_function) -> list[list]:
    result = []
    current = []
    for item in iterable:
        if separator_function(item):
            result.append(current)
            current = []
        else:
            current.append(item)
    result.append(current)
    return result