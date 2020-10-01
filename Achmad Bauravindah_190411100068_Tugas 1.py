# No. 1 (Cari rata2)
print("No. 1 (Cari rata2)")
A = 1
B = 2
C = 3
D = 4
E = A
Rata2 = (A+B+C+D+E)/5.0
print(Rata2)
print("#"*10)

# No. 2 (Luas dan keliling)
print("No. 2 (Luas dan keliling)")
panjang = int(input("Masukan Panjang Segi Empat (cm) = "))
lebar = int(input("Masukan Lebar Segi Empat (cm)= "))
keliling = 2 * (panjang+lebar)
luas = panjang*lebar
print("Keliling = " + str(keliling) + "cm")
print("Luas = " + str(luas) + " cm2")
print("#"*10)

# No. 3 (Program BMI)
print("No. 3 (Program BMI)")
bb = int(input("Masukan Berat Badan (kg) = "))
tb = float(input("Masukan Tinggi Badan (m) = "))
bmi = bb/(tb*tb)
print("BMI Anda " + str(bmi))
if bmi < 18.5:
    print("Berat badan kurang")
elif bmi >= 18.5 and bmi <= 22.9:
    print("Berat badan normal")
elif bmi >= 23 and bmi <= 29.9:
    print(" Berat badan berlebih (kecenderungan obesitas)")
else:
    print("Obesitas")
print("#"*10)

# No. 4 (Nilai Maks dan Min)
print("No. 4 (Nilai Maks dan Min)")
x = 1
N = 5
List = []
while x < N:
    Masukan = int(input("Masukan Nilai Ke - " + str(x) + " = "))
    List.append(Masukan)
    x += 1
print("Nilai Maksimal = " + str(max(List)))
print("Nilai Minimal = " + str(min(List)))
print("#"*10)

# No. 5 (Validasi Login)
print("No. 5 (Validasi Login)")
userValid = "admin"
passValid = "admin"
for i in range(3):
    username = input("Masukan Username : ")
    password = input("Masukan Password : ")
    if username == userValid and password == passValid:
        print("anda berhasil masuk")
        break
    else:
        print("maaf user name dan password anda salah")
