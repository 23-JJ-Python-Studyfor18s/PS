# 하나씩 다 더하면 n^2아닌가? -> 다른 방식으로 풀어야함

n = int(input())
numbers = list(map(int, input().split()))

for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i]+numbers[i-1])

print(max(numbers))