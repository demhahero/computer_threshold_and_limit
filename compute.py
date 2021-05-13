import sys


def output_func(arr, threshold, limit):

    sum_val = 0
    for i, element in enumerate(arr):
        #Subtract the threshold
        val = max(0, element - threshold)

        #If we reached the limit, only print zeros
        if (sum_val == limit):
            print(0)
        elif sum_val + val < limit: #If not, and the new value is still less than limit, add it to sum
            sum_val += val
            print(val)
        else: #Else if greater or equals to limit, only print the differece which is the last portion and make sum_val = limit
            print(limit - sum_val)
            sum_val = limit

    print(sum_val)

def isfloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    arr = []
    if isfloat(sys.argv[1]) and isfloat(sys.argv[2]):
        threshold = float(sys.argv[1])
        limit = float(sys.argv[2])
    else:
        exit()

    #Check threshold and limit within the specified ranges.
    if not ( 0 <= threshold <= 1000000000.0 and 0 <= limit <= 1000000000.0):
        exit()

    #Read form the file line by line
    for line in iter(sys.stdin.readline, ''):
        line = line.replace("\n", "")
        if isfloat(line):
            line = float(line)
            if 0 <= line <= 1000000000.0:
                arr.append(line)
            else:
                exit()
        else:
            exit()

    #Make sure that the input does not exceed 100
    if len(arr) > 100:
        exit()

    output_func(arr, threshold, limit)
