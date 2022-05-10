elements = [10,20,32,30,51,16,78,100,89,90,56,80,90,111,8,9,0]
item = 0
l = 0
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
