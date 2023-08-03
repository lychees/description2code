def get_count_divisors(input_arr):
	count = 0
	for num in range(int(input_arr[0]), int(input_arr[1]) + 1):
		if (num % int(input_arr[2]) == 0):
			count += 1
	return count
input_num = raw_input()
input_num_arr = input_num.split(' ')
print get_count_divisors(input_num_arr)