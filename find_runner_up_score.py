if __name__ == '__main__':
    n = int(input())
    while n < 2 or n >10:
        n = int(input())

    arr = map(int, input().split())
    arr = list(arr)

    for i in range(len(arr)):
        while arr[i] < -100 or arr[i] > 100:
            arr = map(int, input().split())
            arr = list(arr)

    sorted_arr = list(set(sorted(arr, reverse=True)))
    print(sorted_arr[1])