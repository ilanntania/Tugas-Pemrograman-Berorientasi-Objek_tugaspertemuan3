class BangunDatar :
    SegitigaSamaKaki = None
    Jajargenjang = None

BD = BangunDatar()
SegitigaSamaKaki = None
Jajargenjang = None

round = 5
for i in range(round + 1, 0, -1):
    #nested reverse loop
    for j in range(0, i - 1):
        #display star
        print("*", end="")
    print("")

print ("Jajar Genjang")
n = int (input("Masukkan N: "))
i = 1
a = n
while (i<=n):
    print(" "*(n-1), "*" * a)
    n = n-1