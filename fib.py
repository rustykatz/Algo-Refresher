# Fib using Dynamic Programming 
def fibDP(n):
    x = 0
    y = 1

    if n == 0 or n==1:
        return n
    else:
        print(f'{x} {y}',end=' ')
        
        for i in range(n-1):
            temp = x +y
            x = y
            y= temp
            print(temp, end= ' ' )
    return temp

# Fib using Recursion 
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)




def main():
    cases = [5, 1, 2, 20]

    # 1, 1 ,2 ,3, 5
    #print('N = ', '5', '->', fibRec(5))
    arr=[]
    n=5
    # for i in range(n+1):
    #     print(fib(i), end=' ')
    # print('\n')

    a =fibDP(5)
    '''
    for case in cases: 
        # Fib w/ DP 
        # print('N = ', case, '->', fibDP(case))

        # Fib Recursive 
        print('N = ', case, '->', fibRec(case))
    '''

if __name__ == "__main__":
    main()