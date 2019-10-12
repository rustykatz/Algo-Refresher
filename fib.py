def fib(n):
    x = 0
    y = 1

    if n == 0 or n==1:
        return n
    else:
        for i in range(1,n):
            temp = x +y
            x = y
            y= temp
    return temp


def main():
    
    print('N = 5 -> ',fib(5))
    print('N = 1 -> ',fib(1))
    print('N = 2 -> ',fib(2))
    print('N = 20 -> ',fib(20))


if __name__ == "__main__":
    main()