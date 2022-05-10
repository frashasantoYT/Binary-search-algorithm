elements = []
n = int(input("Enter total elements? "))
for i in range(0, n):
    ele = int(input())
    elements.append(ele)


item = float(input("Enter element to be searched? "))
l = elements[0]
r = len(elements) - 1

while(l <= r):
    mid = (l + r) // 2
    if item == elements[mid]:
        print("element found at index ", mid , " and position ", mid + 1)
        break
    elif elements[mid] < item:
        r = mid - 1
    else:
        l = mid + 1
print(elements[0])