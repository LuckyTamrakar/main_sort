from help import sort
print("Enter the five number : ")

arr = []
for i in range(0,5):
    a=int(input())
    arr.append(a)

b=sort(arr)
print(b)