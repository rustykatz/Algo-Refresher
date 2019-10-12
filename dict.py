'''
 dict.keys() 
 dict.values()
 dict.get(x) -> x = key and returns value of x 
'''

def dict(d):
    sol = {'[':']', '(':')', '{':'}'}
    opp = [']',')','}']
    s = [] 

    for i in range(len(d)):
        #print(len(d))
        current = d[i]
        
        # if current not in opp:
        if current in sol.keys():
            s.append(current) 
            print("Appending: ",s)

        if current not in sol.keys():
            if sol.get(s[-1]) == current:
                s.pop()
                print("Popping: ",s)
            else:
                print("Fail")
                break
    print(s)


def main():
    d = "[([{}[()]{}])]"
    dict(d)

if __name__ == "__main__":
    main()