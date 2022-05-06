from time import time

def main():
    sum = 0
    number_list = [x for x in range(1,100000001)]
    start = time()
    for number in number_list:
        sum += number

    print(sum)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()