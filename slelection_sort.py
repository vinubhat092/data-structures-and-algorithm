def selection_sort(data):
    for swap in range(len(data)):
        min_size = swap
        for j in range(swap+1,len(data)):
            
            if data[j] < data[min_size]:
                min_size = j

        data[swap],data[min_size] = data[min_size],data[swap]


data = [7,5,2,4]
selection_sort(data)
print("data",data)