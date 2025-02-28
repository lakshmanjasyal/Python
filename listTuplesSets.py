# courses_1=['History','Math','Physics','CompSci']
# # courses_2=['Art','Education']
# # print(courses_1  + courses_2)
# # print(len(courses_1+courses_2))
# # print(courses_1[0])
# # print(courses_1[0:3])
# # courses_1.append('Art')
# # courses_1.insert(0,'King')
# # print(courses_1)
# # # courses_1.extend(courses_2)
# # courses_1.remove('Math')
# # print(courses_1)
# # # courses_1.pop()

# # # Reversing the list
# # courses_1.reverse()
# # print(courses_1)
# # Sorting the list
# nums=[1,5,2,4,3]
# nums.sort()
# print(nums)
# # Sorting in reverse
# nums.sort(reverse=True)
# print(nums)

# sorted_courses=sorted(courses_1)
# print(sorted_courses)
# print(min(nums))
# print(max(nums))
# print(sum(nums))
# print(courses_1.index('Physics'))

# print('Art' in courses_1)
# print('Math' in courses_1)

# # for item in courses_1:
# #     print(item)

# # for index,course in enumerate(courses_1,start=1):
# #     print(index,course)

# course_str=' - '.join(courses_1)
# # print(course_str)
# new_list=course_str.split(' - ')
# print(course_str)
# print(new_list)


# Tuples are immutable and lists are mutable
            # list_1=['History','Math','Physics','CompSci']
            # list_2=list_1

            # print(list_1)
            # print(list_2)
            
            # list_1[0]='Art'
            # print(list_1)
            # print(list_2)


# tuple_1=('History','Math','Physics','CompSci')
# tuple_2=tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0]='Art'    # This will throw an error because tuples are immutable
# print(tuple_1)
# print(tuple_2)

# Sets
# Sets are unordered and have no duplicates
cs_courses={'History','Math','Physics','CompSci','Design'}
art_courses={'History','Math','Art','Design'}
# print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))

# Empty lists
empty_list=[]
empty_list=list()

# Empty tuples
empty_tuple=()
empty_tuple=tuple()

# Empty sets
empty_set={} # This is wrong because it is a dictionary
empty_set=set()