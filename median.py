def calculate_median(data):
    data.sort()
    n = len(data)
    mid = n // 2

    if n%2 == 0:
        median = (data[mid - 1]+data[mid]) / 2

    else:
        median = data[mid]
    return median
    
data_set = [10,15,20,25,30,7]
median_result = calculate_median(data_set)
print("Median : ",median_result)



"""def calculate_median(data):
    data.sort()
    n = len(data)
    mid = n//2

    if n%2 ==0:
        median = data[mid-1]+data[mid]/2

    else:
        median = data[mid]

    return median

data=[4,17,2,23,76,1]
result = calculate_median(data)
print("Median is : ",result)"""