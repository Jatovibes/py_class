
def largest_divisible(n, lst):
    largest_divisible = None
    for i in lst:
        if i % n == 0:
            if largest_divisible is None or i > largest_divisible:
                largest_divisible = i
    return largest_divisible