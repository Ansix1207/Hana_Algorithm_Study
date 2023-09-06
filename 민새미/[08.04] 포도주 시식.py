n = int(input())
array = [0] * 10000
for i in range(n):
    array[i] = int(input())

# 근데 왜 런타임 에러가 날까?????????????
d = [0] * 10000
d[0] = array[0]
d[1] = array[0] + array[1]
d[2] = max(array[2] + array[0], array[2] + array[1], d[1])
for i in range(3, n):
    d[i] = max(array[i] + d[i - 2], array[i] + array[i - 1] + d[i - 3], d[i - 1])

print(max(d))

# n = int(input())
# arr = list()
# for i in range(n):
#     arr.append(int(input()))


# if n == 1:
#     print(arr[0])
# elif n == 2:
#     print(arr[0] + arr[1])
# else:
#     dp.append(arr[0])
#     dp.append(arr[0] + arr[1])
#     dp.append(max(arr[0] + arr[2], arr[1] + arr[2], dp[1]))
#     for i in range(3, n):
#         # 2칸 + 띄고 1칸 / 1칸 + 다음+다음 / 안가고 바로 이전
#         dp.append(max(dp[i - 2] + arr[i], dp[i - 3] + arr[i] + arr[i - 1], dp[i - 1]))

#     print(max(dp))
