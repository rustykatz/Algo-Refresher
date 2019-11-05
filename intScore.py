'''
Excerpt: Given some integer I, determine what a score based on the values in the integer.
If the number contains:
1) 5                -> score + 5
2) 4                -> score / 4
3) even             -> score + 2
4) divisible by 3   -> score - 3
5) consecutive 2    -> score - 2
6) decreasing seq   -> score + seq ** 2
Time: 
1) 3:28
'''


def score(inputData):
    d = str(inputData)
    s = 0
    seq = 0
    for i in range(0,len(d)):
        if d[i] == '5':
            s += 5
        elif d[i] == '4':
            s /= 4
        elif d[i] == '2' and i != len(d) -1 and d[i+1] =='2':
            s -=2

        if i > 0:
            if d[i] < d[i-1]: 
                if seq == 0:
                    seq += 2 
                else:
                    seq += 1
            else:
                s += seq * 2
                seq = 0
            


    if inputData %3 ==0:
        s -= 3
    if inputData % 2 ==0:
        s += 2
    return s


def main():
    i = [12345678, 2263845, 589822, 66]
    a = [4.0, 6.5, 11.0,-1.0]
    
    res = [score(k) for k in i]
    print('RES: ', res)
    total = 0

    for k in range(0,len(a)):
        if a[k] == res[k]:
            print("PASS TEST #", k)
            total += 1
        else:
            print("FAIL TEST# ", k)
            print("RES: ", res[k], "-> ANS: ", a[k])

    print("TOTAL: ", total,'/',len(i)) 


if __name__ == "__main__":
    main()