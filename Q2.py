# If start time is greater or equal to end time of recent activity, then we consider it


#======== without taking input===========
def activityselection(start ,end ):
	i = 0
	length_of_activities  = len(end)
	for j in range(length_of_activities):
		if start[j] >= end[i]:
			# print (j),
			i = j
start = [1 , 3 , 2 , 5]
end   = [2 , 4 , 3 , 6]
activityselection(start,end)







# ==================  with taking input ======================
# def activityselection(start ,end ):
# 	length_of_activities = len(end)
# 	i = 0
# 	for j in range(length_of_activities):
# 		if start[j] >= end[i]:
# 			print (j),
# 			i = j
# start=[]
# end=[]
# number_of_entries = int(input('enter no of entries : '))
# if number_of_entries > 1 and   number_of_entries<2102:
# 	for i in range(number_of_entries):
# 		a = int(input('enter values for start time : '))
# 		start.append(a)
# 	print("here is the data in start time", start)
# 	for i in range(number_of_entries):
# 		a = int(input('enter values for end time : '))
# 		end.append(a)
# 	print("here is the data in end time", end)
# 	activityselection(start, end)
# else:
# 	print("Number of entries  should be grater than 1  and less then 2102")


