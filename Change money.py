#2022.5.20
#Change money

price = 1260
money = [500, 100, 50, 10]

count=0
for m in money:
  count += price//m
  price %=m

print(count) 