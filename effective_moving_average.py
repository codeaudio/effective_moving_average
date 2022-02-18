def effective_moving_average(lst: list, k: int):
    k = int(k)
    result = []
    s = 0
    for i in range(0, len(lst) + 1 - k):
        if len(result) == 0:
            s = sum(lst[i:k + i])
            result.append(s / k)
        else:
            s = s - lst[i - 1] + lst[k + i - 1]
            result.append(s / k)
    return result
    
