#VD1
danhsach1 = [1.,3.]
danhsach2 = [5.,7.]
danhsach = danhsach1 + danhsach2
print(danhsach)
danhsachgapdoi = 2*danhsach
print(danhsachgapdoi)
danhsachchiadoi = danhsach/2
print(danhsachchiadoi)
#VD2
monhoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thutu = [2, 3, 4, 1]
diemso = [10, 9, 8, 7]
anhxa = zip(thutu, monhoc, diemso)
print(anhxa)
taphop = set(anhxa) 
print(taphop)
lay_TT, lay_monhoc , lay_diem = zip(*anhxa)
lay_monhoc
#VD3
import itertools
tapsinh = list(itertools.chain(range(4), range(5,10), range(15,20)))
print(tapsinh)
#VD5
list(zip(range(4), range(7, 12), reversed(range(11))))
