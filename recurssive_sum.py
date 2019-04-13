a = [1,2,3,4]

def big_sum():
    final_sum = 0
    length_a = len(a)
    start = 1
    for n in a:
        final_sum = final_sum + a[length_a - start]
        start += 1
    return final_sum

print(big_sum())
