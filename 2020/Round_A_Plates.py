
#Compute a running sum of beauty values in each input stack
def running_sum(l_in):

	#Running sum starts with 0 on index 0. 
	#This represents the beauty value when picking 0 plate from this stack.
	
	l_out = [0]
	cur = 0
	for i in range(len(l_in)):
		cur += l_in[i]
		l_out.append(cur)

	return l_out


def solver(dp):
	#Corresponding to N,K,P
	count_lines, length, num_plates_needed = map(int, input().split())
	#print(count_lines)
	#print(length)
	#print(num_plates_needed)

	#Stores stacks of plates
	stacks = []

	for j in range(count_lines):
		new_line = input()
		stack = [int(x) for x in new_line.split()]

		#running sum stack
		rs_stack = running_sum(stack)

		stacks.append(rs_stack)

	#print(stacks)

	#reset DP
	for i in range(count_lines+1):
		for j in range(num_plates_needed+1):
			dp[i][j] = 0


	#print(dp)

	#Iterate through the stacks
	for i in range(count_lines):
		#Iterate through picking j plates, j = [0, number of plates needed] 
		for j in range(0, num_plates_needed+1):
			#X is a 'splitting' variable, taking x plates from the new stack, and j-x best plates from the previous stacks
			for x in range(0, min(j, length)+1):
				#print("i={};j={};x={}".format(i,j,x))
				try:
					prev_best = dp[i-1][j-x]
				except IndexError:
					prev_best = 0
				new_sum_stack = stacks[i][x]
				#print("prev_best = {}, new_sum_stack = {}, dpij = {}".format(prev_best, new_sum_stack, dp[i][j]))

				dp[i][j] = max(dp[i][j], new_sum_stack + prev_best)
				#print(dp)
				#print("\n")

	return dp[count_lines-1][num_plates_needed]


def main():

	num_cases = int(input())

	#Construct the solution table
	'''
	The solution table dp[i][j] stores the best beauty value possible from
	using the first i stacks, picking j plates in total across stacks. j starts
	from zero to take into consideration of not picking any plate from a
	particular stack
	'''
	dp = [[0 for x in range(1500+1)] for y in range(1000)]

	for i in range(num_cases):
		ans = solver(dp)
		print("Case #{}: {}".format(i+1, ans))

		

if __name__ == "__main__":

	main()




'''
Problem
Dr. Patel has N stacks of plates. Each stack contains K plates. Each plate has a positive beauty value, describing how beautiful it looks.

Dr. Patel would like to take exactly P plates to use for dinner tonight. If he would like to take a plate in a stack, he must also take all of the plates above it in that stack as well.

Help Dr. Patel pick the P plates that would maximize the total sum of beauty values.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the three integers N, K and P. Then, N lines follow. The i-th line contains K integers, describing the beauty values of each stack of plates from top to bottom.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum total sum of beauty values that Dr. Patel could pick.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ K ≤ 30.
1 ≤ P ≤ N * K.
The beauty values are between 1 and 100, inclusive.

Test set 1
1 ≤ N ≤ 3.

Test set 2
1 ≤ N ≤ 50.

Sample

Input
 	
Output
 
2
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10

  
Case #1: 250
Case #2: 180

  
In Sample Case #1, Dr. Patel needs to pick P = 5 plates:
He can pick the top 3 plates from the first stack (10 + 10 + 100 = 120).
He can pick the top 2 plates from the second stack (80 + 50 = 130) .
In total, the sum of beauty values is 250.

In Sample Case #2, Dr. Patel needs to pick P = 3 plates:
He can pick the top 2 plates from the first stack (80 + 80 = 160).
He can pick no plates from the second stack.
He can pick the top plate from the third stack (20).
In total, the sum of beauty values is 180.

Note: Unlike previous editions, in Kick Start 2020, all test sets are visible verdict test sets, meaning you receive instant feedback upon submission.
'''
