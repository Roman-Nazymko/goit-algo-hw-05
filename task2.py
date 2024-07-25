def binary_search_with_upper_bound(arr, target):
    low = 0 
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        iterations += 1

        if guess == target:
            return iterations, guess
        elif guess > target:
            upper_bound = guess
            high = mid - 1
        else:
            low = mid + 1
    
    return iterations, upper_bound

# Тести:
arr = [1.9, 2.7, 3.2, 4.9, 7.5]
print(binary_search_with_upper_bound(arr, 0))  # Виведе: (2, 1.9)
print(binary_search_with_upper_bound(arr, 3.1))  # Виведе: (3, 3.2)
print(binary_search_with_upper_bound(arr, 5.1))  # Виведе: (3, 7.5)
print(binary_search_with_upper_bound(arr, 7.6))  # Виведе: (3, None)
print(binary_search_with_upper_bound(arr, 2.3))  # Виведе: (3, 2.7)