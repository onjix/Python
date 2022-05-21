#2022.5.21
#Law of big number (1)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_num = data[n-1]
second_num = data[n-2]

result = 0

while True:
  for i in range(0, k):
    if m == 0:
      break;
    result +=first_num
    m-=1
  
  if m == 0:
    break
  result +=second_num
  m -=1

print(result)