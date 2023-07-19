def count_factors(num):
    i = 1
    count = 0
    while i * i <= num:
        if num % i == 0:
            if num / i == i:
                count += 1
            else:
                count += 2
        i += 1
    return count

def sort_by_factors(array):
    array.sort(key=lambda num: (count_factors(num), num)) 
    return array

input_array = list(map(int, input().split()))
print(sort_by_factors(input_array))
