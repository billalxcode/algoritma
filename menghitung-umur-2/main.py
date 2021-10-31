from datetime import date
hari_ini = str(date.today()).split("-")

jan = 0
feb = 31
mar = 59
apr = 90
mei = 120
jun = 151
jul = 181
agu = 212
sep = 243
okt = 273
nov = 304
des =  334

class Hari:
	def __init__(self, tanggal, bulan, tahun):
		self.tanggal = tanggal
		
		if bulan == 1:
			bulan = jan
		elif bulan == 2:
			bulan = feb
		elif bulan == 3:
			bulan = mar
		elif bulan == 4:
			bulan = apr
		elif bulan == 5:
			bulan = mei
		elif bulan == 6:
			bulan = jun
		elif bulan == 7:
			bulan = jul
		elif bulan == 8:
			bulan = agu
		elif bulan == 9:
			bulan = sep
		elif bulan == 10:
			bulan = okt
		elif bulan == 11:
			bulan = nov
		elif bulan == 12:
			bulan = des
			
			
		self.bulan = bulan
		self.tahun = tahun
	
	def hitung_hari(self):
		return self.bulan + self.tanggal
	
	def hitung_tahun(self):
		return int(hari_ini[0]) - self.tahun
	
print("[ Penghitung Umur ]")
print("[ Coded by: SalisM3 ]\n")
print("[+] Masukan Tanggal Lahir")
tanggal = int(input('[?] Tanggal: '))
if tanggal > 31 or tanggal == 0:
	exit('[!] Offside')
bulan = int(input('[?] Bulan (ex: 1): '))
if bulan > 12 or bulan == 0:
	exit('[!] Offiside')
tahun = int(input('[?] Tahun: '))
if tahun > int(hari_ini[0]) or tahun == 0:
	exit('[!] Offside')
a = Hari(tanggal, bulan, tahun)
b = Hari(int(hari_ini[2]),int(hari_ini[1]),int(hari_ini[0]))
jumlah = a.hitung_tahun() * 365 - a.hitung_hari() + b.hitung_hari()
jumlah += a.hitung_tahun() // 4
print()

print("[+] Umur Kamu:")
print("[+] Ukuran Tahun: " + str(a.hitung_tahun()) + " Tahun")
print("[+] Ukuran Hari: " + str(jumlah) + " Hari")
print("[+] Ukuran Jam: " + str(jumlah * 24) + " Jam")
print("[+] Ukuran Menit: " + str(jumlah * 24 * 60) + " Menit")
if a.hitung_hari() > b.hitung_hari():
	ultah = a.hitung_hari() - b.hitung_hari()
else:
	ultah = 365 - b.hitung_hari() + a.hitung_hari()
if b.hitung_hari() < 59 and int(hari_ini[0]) % 4 == 0:
	ultah += 1
else:
	pass

if int(hari_ini[1]) == bulan and int(hari_ini[2]) == tanggal:
	print("\n[!] Selamat Ulang Tahun ^_^")
else:
	print("\n[!] " + str(ultah) +" Hari Menuju Ulang Tahun")
print("[!] Gunakan Sisa Umurmu Sebaik Mungkin ^_^")