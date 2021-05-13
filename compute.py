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
    n = 2

    if not ( 0 <= threshold <= 1000000000.0 and 0 <= limit <= 1000000000.0 and 0 < n <= 100 ):
        exit()

    while len(arr) < n:
        val = input()
        if val.isnumeric():
            val = float(val)
            if 0 <= val <= 1000000000.0:
                arr.append(val)
            else:
                exit()
        else:
            exit()
    print("\n")
    output_func(arr, threshold, limit)
