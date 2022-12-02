def membuathuruf(str):
    panjang=len(str)
    if panjang % 2 == 0 :
        return str[0]+str[1]+str[2]+ 'dan' +str[-3]+str[-2]+str[-1]
    else:
        mid=int(panjang/2)
        return str[mid-1]+str[mid]+str[mid+1]

a=input("Masukan kata : ")
b=membuathuruf(a)
print("Huruf yang diambil pada ", a , 'adalah', b)