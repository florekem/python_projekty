import statistics as stat

numbers = [i.split() for i in open('statistics.txt')]
numbers_sorted = sorted(numbers)

mean = stat.mean(numbers)

#median = (numbers[int(noofval / 2)] + numbers[int(noofval / 2 - 1)]) / 2
median = statistics.median(numbers)


try:
    mode = statistics.mode(numbers)
except statistics.StatisticsError:
    error = True
finally:
    if error == True:
        mode = numbers_sorted[0]
    else:
        mode = statistics.mode(numbers)


print(mean)
print(median)
print(mode)
