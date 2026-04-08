import numpy as np
from time import time


list_n = np.random.randint(1,100,10000).tolist()

def bubble_sort(list_n):
    list_n_sorted = list_n.copy()
    n = len(list_n_sorted)

    for i in range(n):
        for j in range(n):
            if list_n_sorted[i]<list_n_sorted[j]:
                list_n_sorted[i],list_n_sorted[j] = list_n_sorted[j],list_n_sorted[i]
    return list_n_sorted
                

def selection_sort(list_n):
    list_n_sorted = list_n.copy()
    n = len(list_n_sorted)
    for i in range(n):
        aux_min,aux_pos = list_n_sorted[i],i
        for j in range(0+i,n):
            if aux_min > list_n_sorted[j]:
                aux_min,aux_pos = list_n_sorted[j],j
        list_n_sorted[0+i],list_n_sorted[aux_pos] = aux_min,list_n_sorted[0+i]
    return list_n_sorted


def counting_sort(list_n):
    list_n_sorted = []
    dx_key_count = {no:0 for no in list_n}
    for key in dx_key_count.keys():
        for n in list_n:
            if n == key:
                dx_key_count[key] += 1

    sorted_keys = bubble_sort(list(dx_key_count.keys()))
    
    for key in sorted_keys:
        for time in range(dx_key_count[key]):
            list_n_sorted.append(key)
            
    return list_n_sorted
    

def quick_sort(list_n):
    if len(list_n) <= 1:
        return list_n
    pivot = list_n[-1]
    lower_list = [n for n in list_n[:-1] if n<=pivot]
    upper_list = [n for n in list_n[:-1] if n>pivot]

    return quick_sort(lower_list) + [pivot] + quick_sort(upper_list)


def recursive_divide(list_n):
    if len(list_n) <=1:
        return list_n
    n_over_2_r = round(len(list_n)/2)
    left_list = list_n[:n_over_2_r]
    right_list = list_n[n_over_2_r:]
    return merge_lists(recursive_divide(left_list),recursive_divide(right_list))

def merge_lists(list_1,list_2):
    list_merged = []
    i = 0
    j = 0

    while i<len(list_1) and j<len(list_2):
        if list_1[i] < list_2[j]:
            list_merged.append(list_1[i])
            i += 1
        else:
            list_merged.append(list_2[j])
            j+=1
    return list_merged + list_1[i:] + list_2[j:]
        
    

def sweep_line(customers):
    events = []
    for cus_in, cus_out in customers:
        events.append((cus_in, 1))
        events.append((cus_out, -1))

    events = recursive_divide(events)

    trend = []
    current_clients = 0
    for period,in_out in events:
        current_clients += in_out
        trend.append(current_clients)
        
    max_clients = max(trend)

    return max_clients


if __name__ == "__main__":

    print("Lista generada")
    print("-" * 50)

    start = time()
    bubble_sort(list_n)
    print(f"Bubble Sort: {(time() - start):.6f}s")

    start = time()
    selection_sort(list_n)
    print(f"Selection Sort: {(time() - start):.6f}s")

    start = time()
    counting_sort(list_n)
    print(f"Counting Sort: {(time() - start):.6f}s")

    start = time()
    quick_sort(list_n)
    print(f"Quick Sort: {(time() - start):.6f}s")

    start = time()
    recursive_divide(list_n)
    print(f"Merge Sort: {(time() - start):.6f}s")

    customers = [(1, 5),(2, 6),(4, 8),(7, 9)]
    print("\nSweep Line:", sweep_line(customers))


    print("\n" + "=" * 50)
    print("EJEMPLO VISUAL (lista pequeña)")
    print("=" * 50)

    test_list = np.random.randint(1, 50, 10).tolist()
    print("Lista original:", test_list)
    print()

    print("Bubble Sort:", bubble_sort(test_list))
    print("Selection Sort:", selection_sort(test_list))
    print("Counting Sort:", counting_sort(test_list))
    print("Quick Sort:", quick_sort(test_list))
    print("Merge Sort:", recursive_divide(test_list))