#!/usr/bin/python
#challenge 243 easy

nums = [111, 112, 220, 69, 134, 85, 6, 28]
for num in nums:
	sum = 0
	for x in range(1, int(num**0.5) + 1):
		if num % x == 0:
			sum += x
			other_div = num / x
			if other_div != x:
				sum += other_div

	if sum > num * 2:
		print "%s is abundant by %s" %(str(num), str(sum - (num*2)))
	elif sum == num * 2:
		print "%s is a perfect number" % num
	else:
		print "%s is deficient" % str(num)