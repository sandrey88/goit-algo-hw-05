"""
Завдання 3

"""

import timeit
import requests
from algo_kmp import kmp_search
from algo_bm import boyer_moore_search
from algo_rk import rabin_karp_search

# Функція для завантаження тексту з файлу за URL
def load_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Помилка завантаження тексту")
        return ""

# Функція для вимірювання часу виконання алгоритму пошуку підрядка
def measure_search_algorithm_time(search_algorithm, text, pattern):
    return timeit.timeit(lambda: search_algorithm(text, pattern), number=1000)

# Стаття 1
url_1 = "https://drive.google.com/uc?export=download&id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"

# Стаття 2
url_2 = "https://drive.google.com/uc?export=download&id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ"

# Рядки для тестування пошуку
pattern1 = "поширена дія"
pattern2 = "Метою даної роботи є"
random_pattern = "How are you?"

# Функція для порівняння ефективності алгоритмів
def compare_searching_algorithms(url, pattern1, pattern2):
    # Завантаження тексту з файлу
    text = load_text_from_url(url)

    # Вимірювання часу виконання для першого паттерну
    kmp_time1 = measure_search_algorithm_time(kmp_search, text, pattern1)
    bm_time1 = measure_search_algorithm_time(boyer_moore_search, text, pattern1)
    rk_time1 = measure_search_algorithm_time(rabin_karp_search, text, pattern1)

    # Вимірювання часу виконання для другого паттерну
    kmp_time2 = measure_search_algorithm_time(kmp_search, text, pattern2)
    bm_time2 = measure_search_algorithm_time(boyer_moore_search, text, pattern2)
    rk_time2 = measure_search_algorithm_time(rabin_karp_search, text, pattern2)

    # Початкова позиція паттерну (Індекс)
    found_indices_1_kmp = kmp_search(text, pattern1)
    found_indices_1_bm = boyer_moore_search(text, pattern1)
    found_indices_1_rk = rabin_karp_search(text, pattern1)
    found_indices_2_kmp = kmp_search(text, pattern2)
    found_indices_2_bm = boyer_moore_search(text, pattern2)
    found_indices_2_rk = rabin_karp_search(text, pattern2)

    # Вивід результатів
    print(f"URL статті: {url}")
    print("- -" *10)
    print(f"Підрядок існуючий: {pattern1}")
    print()
    print(f"КМП: {kmp_time1} сек")
    print(f"Індекс: {found_indices_1_kmp}")
    print("- " *4)
    print(f"БМ: {bm_time1} сек")
    print(f"Індекс: {found_indices_1_bm}")
    print("- " *4)
    print(f"РК: {rk_time1} сек")
    print(f"Індекс: {found_indices_1_rk}")
    print("- -" *10)
    print(f"Підрядок вигаданий: {pattern2}")
    print()
    print(f"КМП: {kmp_time2} сек")
    print(f"Індекс: {found_indices_2_kmp}")
    print("- " *4)
    print(f"БМ: {bm_time2} сек")
    print(f"Індекс: {found_indices_2_bm}")
    print("- " *4)
    print(f"РК: {rk_time2} сек")
    print(f"Індекс: {found_indices_2_rk}")

print()

# Порівнюємо ефективність алгоритмів для першого тексту
print("Стаття 1")
print("-" *40)
compare_searching_algorithms(url_1, pattern1, random_pattern)

print()
print("*" *40)
print()

# Порівнюємо ефективність алгоритмів для другого тексту
print("Стаття 2")
print("-" *40)
compare_searching_algorithms(url_2, pattern2, random_pattern)
