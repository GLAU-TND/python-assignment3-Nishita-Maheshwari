def pal(str1,str2,m,n):
    if not m:
        return n
    if not n:
        return m
    if str1[m-1]==str2[m-2]:
        return Pal(str1, str2, m-1, n-1) 
    res = 1 + min(isKPalRec(str1, str2, m-1, n),(isKPalRec(str1, str2, m, n-1)))
    return res
def isKPal(string, k): 
    revStr = string[::-1] 
    l = len(string) 

    return (isKPalRec(string, revStr, l, l) <= k * 2) 
string = str(input("enter a string"))
k = int(input("enter no"))
print("Yes" if isKPal(string, k) else "No") 

     
