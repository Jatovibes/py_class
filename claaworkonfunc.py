def find_common_elements(list1,list2):
    list3 = []
    for element in list1:
        if element in list2 and element not in list3:
            list3.append(element
                         )
    return list3
list1= [2,3,4,5,6]
list2= [3,4,5,6,7] 
list3= find_common_elements(list1,list2)
print(list3)