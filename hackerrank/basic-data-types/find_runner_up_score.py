#Task

#Given the participants' score sheet for your University Sports Day,
#you are required to find the runner-up score.
#You are given  scores. Store them in a list and find the score of the runner-up.

#Input Format

#The first line contains n. The second line contains an array A[] of integers
#each separated by a space.

#Constraints
#2 <= n <= 10
#-100 <= A[i] <= 100

#Output Format

#Print the runner-up score.

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

