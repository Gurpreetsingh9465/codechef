# https://www.codechef.com/JULY19B/problems/MMAX

T = int(input())
while T:
    N = int(input())
    K = int(input())
    arr = [K//N]*N
    x = K%N
    for i in range(0,x):
        arr[-(i+1)] += 1
    sum = 0
    i=0
    j=N-1
    sum=0
    sum += abs(arr[0] - arr[1])
    sum += abs(arr[N-1] - arr[N-2])
    for i in range(1,N-1):
        sum += max(abs(arr[i] - arr[i-1]), abs(arr[i] - arr[i+1])); 
    print(sum)
    T-=1
