from operator import itemgetter, attrgetter
def get_ones_in_binary(task):
	count = 0
	bin_task = bin(task)
	for char in bin_task:
		if char == '1':
			count += 1
	return count
def order_tasks(tasks):
	tasks_arr = tasks.split(' ')
	tasks_based_on_ones = []
	for task in tasks_arr:
		tasks_based_on_ones.append((get_ones_in_binary(int(task)), int(task)))
	a = sorted(tasks_based_on_ones, key=itemgetter(0))
	#tasks_based_on_ones.sort()
	return a
		
test_cases = input()
for test_case in range(0, test_cases):
	days = input()
	tasks = raw_input()
	ordered_tasks_list = []
	for task in order_tasks(tasks):
		ones, t = task
		ordered_tasks_list.append(str(t))
	print ' '.join(ordered_tasks_list)