def max_consec_sum(numbers, n):
    window_sum = sum(numbers[:n])
    best_sum = window_sum

    for i in range(n, len(numbers)):
        window_sum += numbers[i] - numbers[i - n]
        best_sum = max(best_sum, window_sum)

    return best_sum