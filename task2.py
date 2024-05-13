"""

Функція binary_search реалізує двійковий пошук для відсортованого масиву з дробовими числами та повертає кортеж, де:
    * iterations (int): Кількість ітерацій, потрібних для знаходження елемента в масиві (arr).
    * upper_bound (float): Верхня межа - найменший елемент, який є більшим або рівним заданому значенню (x).
"""

def binary_search(arr, x):

    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] == x:
            return iterations, arr[mid]
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    # Не знайдено
    upper_bound = arr[low] if low < len(arr) else None
    return iterations, upper_bound

# Приклад 
arr = [1.9, 2.1, 4.5, 7.3, 9.8]
x = 1.1

iterations, upper_bound = binary_search(arr, x)

print(f"Кількість ітерацій: {iterations}")
print(f"Верхня межа: {upper_bound}")