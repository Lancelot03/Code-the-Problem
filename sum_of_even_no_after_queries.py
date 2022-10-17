nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
final=[]

even_sum=0
for i in nums:
	if i%2==0:
		even_sum+=i

for i in range(len(queries)):
	
	flag=0
	val,index=queries[i]
	# print(queries[i])
	# print(val)
	# print(index)
	if nums[index]%2 == 0:
		flag=nums[index]
	nums[index]=nums[index]+val
	even=0
	temp2=0
	if nums[index]%2==0:
		temp2=nums[index]
	even=even_sum-flag+temp2
	even_sum=even
	final.append(even)
	# print(nums)
	
print(final)
	
	