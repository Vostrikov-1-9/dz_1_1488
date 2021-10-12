x = int(input())
y = int(input())
sum = 0
for i in range(x, y + 1):
    if i % 5 == 0:
        sum += i
print(sum)
