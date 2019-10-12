
def isEqual(s1,s2):
    return bool(s1==s2)

def isEqualNotCaseSens(s1,s2):
    return bool(s1.upper() == s2.upper())

def isEqualSpace(s1,s2):
    s1 = s1.replace(' ',"")
    s2 = s2.replace(' ',"")
    return bool(s1==s2)

def isPalindrome(s):
    
    for i in range(0,len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False

    return True

def isPNCS(s):
    for i in range(len(s)//2):
        if s[i].upper() != s[len(s)-i-1].upper():
            return False 
    return True

def isPS(s):
    s = s.replace(" ","")
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

# Done in place without using replace 
def isPS2(s):
    left = 0
    right = len(s)-1

    for i in range(len(s)):
        while s[left] == " ":
            left +=1

        while s[right] == " ":
            right += 1
        
        if s[left] != s[right-left]:
            return False 

    return True
        


def main():
    str1 = "ABCDCBA"
    str2 = "abcdcba"
    str3 = "ABCDcba"
    str4 = "ABCD C BA"
    str5 = "ABC123"
    str6 = "abc123"

    '''
    s = no spaces
    ncs = not case sens
    '''
    print("Equal? S1 and S2: " ,isEqual(str1,str2))
    print("Equal NCS? S1 and S2: " ,isEqualNotCaseSens(str1,str2))
    print("Equal NCS? S5 and S6: " ,isEqualNotCaseSens(str5,str6))
    print("Equal S? S1 and S4: " ,isEqualSpace(str1,str4))

    print("Palindrome? S1: ",isPalindrome(str1))
    print("Palindrome? S4: ",isPalindrome(str4))
    print("Palindrome NCS? S3: ",isPNCS(str3))
    print("Palindrome S? S4: ",isPS(str4))
    print("Palindrome S2? S4: ",isPS(str4)) # Not using replace fxn

if __name__ == "__main__":
    main()