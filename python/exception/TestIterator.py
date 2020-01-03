def flatten(nested):
    try:
        for subList in nested:
            for element in flatten(subList):
                yield element
    except TypeError:
        yield nested



nested = [[[1], 2], [3, 4], [5, 6]]
print(list(flatten(nested)))
