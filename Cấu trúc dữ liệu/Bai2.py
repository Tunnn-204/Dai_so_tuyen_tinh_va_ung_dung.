import random
def sansinhtangdan(n):
    mang =[]
    mang.append(random.randint(-100, 100))
    for i in range(1, n):
        tang = random.randint(1, 10)
        so = mang [i -1] + tang
        mang.append(so)
    return mang
def timnhiphan(mang, x):
    trai = 0
    phai = len(mang) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] == x:
            return giua
        if x < mang[giua]:
            phai = giua - 1
        else:
            trai = giua + 1
    return -1
def main():
    mang = sansinhtangdan(20)
    print(mang)
    x = int(input("Nhap vao gia tri can tim: "))
    vitri = timnhiphan(mang, x)
    if vitri != -1:
        print("Phan tu x duoc tim thay tai vi tri", vitri)
    else:
        print("Khong tim thay phan tu x trong mang")
if __name__ == "__main__":
    main()