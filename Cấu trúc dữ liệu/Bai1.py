import random
def sansinh(n):   
    mang = []
    for i in range(n):
        songaunhien = random.randint(-100, 100)
        mang.append(songaunhien)
    return mang
def timtuyentinh(mang, x):
    n = len(mang)
    for i in range(n):
        if mang[i] == x:
            return i
    return -1
def main():
    mang = sansinh(20)
    print('Mang ngau nhien la:', mang)
    x = int(input("Nhap vao gia tri can tim: "))
    vitri = timtuyentinh(mang, x)
    if vitri != -1:
        print("Phan tu x duoc tim thay tai vi tri", vitri)
    else:
        print("Khong tim thay phan tu x trong mang")
if __name__ == "__main__":
    main()