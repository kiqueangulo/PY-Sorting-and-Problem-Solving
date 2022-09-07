def sum_to(numbers, target):
    numbers.sort()
    first = 0
    last = len(numbers) - 1

    while first < last:
        sum = numbers[first] + numbers[last]

        if sum == target:
            return numbers[first], numbers[last]
        
        if sum > target:
            last -= 1
        else:
            first += 1
    
    return 'There are no terms for that sum.'

lst_example = [4, 7, 2, 8, 6, 1]

print(sum_to(lst_example, 3))