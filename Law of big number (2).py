#2022.5.21
#Law of big number (2)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_num = data[n-1]
second_num = data[n-2]


count = (int)(m/(k+1) *k)
count += m%(k+1)

result = 0
result = (count) * first_num
result += (m-count) * second_num
print(result)
