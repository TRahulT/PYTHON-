def fact(n):
	#smallest subproblem where we know the answer or the base case
	if n == 1:
		return(1)
	#recursive assumption
	else:
		subproblem = fact(n-1)
	#self work
		return n * subproblem
print(fact(5))
