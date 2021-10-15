num_1 = 1
num_2 = 1
fib_no = [1, 1]
jmlderet = int(input("Masukkan jumlah deret Fibonacci: "))
update = 0
flag = 0
while update < jmlderet:
	if flag == 0:
		num_1 += num_2
		fib_no.append(num_1)
		flag = 1
	elif flag == 1:
		num_2 += num_1
		fib_no.append(num_2)
		flag = 0
	update += 1
print("Deret Fibonnaci :")
print(fib_no)
quo_list = []
for ind in range(0, len(fib_no)-1):
	quo = fib_no[ind+1]/fib_no[ind]
	quo_list.append(quo)
print("Hasil bagi dari suku-suku berturut-turutnya :")
print(quo_list)
