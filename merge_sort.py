def merge(left,right):
    i,j = 0,0
    arr = []
    while i < len(left) and j < len(right):
        if left[i]<= right[j]:
            arr.append(left[i])
            i +=1
    
        else:
            arr.append(right[j])
            j +=1
    arr +=left[i:]
    arr +=right[j:]
    return arr

def mergesort(data):
    if (len(data)<=1):
        return data
    
    

    mid = int(len(data) / 2)
    left = mergesort(data[:mid])
    right = mergesort(data[mid:])
    print("left",left)
    print("right",right)
    return merge(left, right)


data = [4,2,3]
data = mergesort(data)
print("data",data)



