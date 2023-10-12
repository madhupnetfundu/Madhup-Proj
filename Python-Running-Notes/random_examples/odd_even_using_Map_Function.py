def odd_or_even(num):
	if num%2==0:
		print('The number {} is even'.format(num))
	else:
		print('The number {} is odd'.format(num))

the_numbers=[1,2,3,8,99,100]
# the_numbers=[]
final_result = list(map(odd_or_even, the_numbers))
print(final_result)