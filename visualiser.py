from funcs import *

FASTA_PATH = "mut0.01.fasta"

ground_set = read_ground_set()

my_path = "exact_manual20.txt"
my_set = map(convert, set(open(my_path).readlines()[1:]))


def letter_map(x):
	return {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}[x]

def rev(s):
	return ''.join(map(letter_map, s))[::-1]


def print_solution(x):
	f = open(FASTA_PATH)
	a_string = None
	b_string = None
	while True:
		line1 = f.readline()
		line2 = f.readline()
		if not line2:
			break
		id = int(line1.strip()[1:])
		if id == x[0]:
			a_string = line2.strip()
		if id == x[1]:
			b_string = line2.strip()
		if a_string != None and b_string != None:
			break
	if a_string == None or b_string == None:
		print("OH NO COULDNT FIND STRINGS FOR ", x)
		quit()
	b_string = rev(b_string)
	print((' '*(-x[3]))+a_string)
	print((' '*(x[3]))+b_string)


def comparison(my_sols, her_sols):
	case1_count = 0
	case2_count = 0
	fp = 0
	for m in my_sols:
		case1 = m in her_sols
		case2 = special_case(m, her_sols)
		if not case1 and case2:
			print("My solution: ", m, '\ther solution: ', flip(m), '\nMINE')
			print_solution(m)
			print('\nHERS:')
			print_solution(flip(m))
			print('\n\n\n')
		if case1:
			case1_count += 1
		elif case2:
			case2_count += 1
		else:
			fp += 1

	missed = len(her_sols) - case1_count - case2_count
	tots = float(case1_count + case2_count + missed)


	case1_ratio = float(case1_count) / tots
	case2_ratio = float(case2_count) / tots
	missed_ratio = float(missed) / tots
	print('case1', case1_ratio, 'case2', case2_ratio, 'missed', missed_ratio)
	fn = len(her_sols) - fp # missing sols

	# print("RECALL IS ", float(tp) / (tp + fn))
comparison(my_sols=my_set, her_sols=ground_set)




#
# for x in ground_set:
# 	print_solution(x)