import numpy as np

def calculate_percentile(data, percentile):
    return np.percentile(data, percentile)

data_set_1 = [10,15,20,25,30]
percentile_result_1 = calculate_percentile(data_set_1, 75)
print("75th percentile : ",percentile_result_1)

data_set_2 = [5,10,15,20,25,30,35]
percentile_result_2 = calculate_percentile(data_set_2, 50)
print("50th percentile : ",percentile_result_2)

#practice

"""import numpy as np

def calculate_percentile(data, percentile):
    return np.percentile(data, percentile)

data1 = [1,2,3,4,5]
result1 = calculate_percentile(data1, 50)
print("result1 : ",result1)

data2 = [5,6,7,8,9]
result2 = calculate_percentile(data2, 74)
print("result : ",result2)
"""
