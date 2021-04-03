import sys
from operator import itemgetter

nums = {}

for line in sys.stdin:
	line = line.strip()
	player,num = line.split('\t')
	try:
		num=int(num)
		nums[player]= nums.get(player,0) + num
	except ValueError:
		pass

sorted_count = sorted(nums.items(),key=itemgetter(0),reverse=True)
for player, count in sorted_count:
	
	print ('%s\t%s' % (player,count))
