#meminta pengguna memasukkan suhu dalam derajat fahrenheit 
fahrenheit = float(input("masukkan suhu dalam fahrenheit :"))

#menghitung konversi suhu ke celcius
celcius = (fahrenheit - 32) * 5/9

#menampilkan hasil konversi
print("f{fahrenheit} derajat fahrenheit sama dengan{celcius} derajat celcius : " , celcius)
