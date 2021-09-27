# Extract digits from Tuple list
from itertools import chain

test_list = [(12, 34), (3, 91), (4, 10), (8, 2)]


print("The original list is : " + str(test_list))


temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
res = set()
for sub in temp:
	for ele in sub:
		res.add(ele)


print ("The extracted digits : " + str(res))