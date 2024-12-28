







def calculate_mean(data):
    mean = sum(data)/len(data)
    return mean

data_set = {10,15,20,25,30}
mean_result = calculate_mean(data_set)
print("Mean: ", mean_result)