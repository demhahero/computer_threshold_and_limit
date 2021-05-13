import sys


def output_func(arr, threshold, limit):

    sum_val = 0
    for i, element in enumerate(arr):
        val = max(0, element - threshold)

        if (sum_val == limit):
            print(0)
        elif sum_val + val < limit:
            sum_val += val
            print(val)
        else:
            print(limit - sum_val)
            sum_val = limit

    print(sum_val)



if __name__ == "__main__":
    arr = []
    threshold = float(sys.argv[1])
    limit = float(sys.argv[2])

    #You can change this value

    if not ( 0 <= threshold <= 1000000000.0 and 0 <= limit <= 1000000000.0):
        exit()

    for line in iter(sys.stdin.readline, ''):
        line = line.replace("\n", "")
        if line.isnumeric():

            line = float(line)
            if 0 <= line <= 1000000000.0:
                arr.append(line)
            else:
                exit()
        else:
            exit()


    if len(arr) > 100:
        exit()

    output_func(arr, threshold, limit)
