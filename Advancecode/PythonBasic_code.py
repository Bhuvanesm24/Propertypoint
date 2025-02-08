# To remove dublicate values
list1 = ["apple", "banana", "littee"]
list2 = ["apple", "staberry", "love", "banana"]
list3= set(list1+list2)
print(list3)

# Remove dublicate and get unique value
list4 = ["apple", "banana", "littee"]
list5 = ["apple", "staberry", "love", "banana"]

set3=set(list4)
set4=set(list5)
list6= set3.symmetric_difference(set4)
print(list6)

