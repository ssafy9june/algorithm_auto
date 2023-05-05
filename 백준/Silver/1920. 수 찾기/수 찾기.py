def binary_search(arr, lo, hi, key):
    if arr[lo] <= key <= arr[hi]:
        while lo <= hi:
            mid = (lo + hi) // 2
            if key == arr[mid]:
                return 1
            elif key < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return 0
    return 0


N = int(input())
N_lst = list(map(int, input().split()))

M = int(input())
M_lst = list(map(int, input().split()))

N_lst.sort()
for num in M_lst:
    print(binary_search(N_lst, 0, N-1, num))
