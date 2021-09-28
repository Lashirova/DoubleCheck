doubleWords=['homework', 'assignment', 'quiz', 'discussion', 'quiz', 'program']
doubleWords1=[];
for i in doubleWords:
    if i not in doubleWords1:
        doubleWords1.append(i)
    else:
        print(i,end=' ')

#         Explanation
# The list (l) with duplicate elements is taken to find the duplicates.

# An empty list (l1) is taken to store the values of non-duplicate elements from the given list.

# The for loop is used to access the values in the list (l), and the if condition is used to check if the elements in the given list (l) are present in the empty list (l1).

# If the elements are not present, those values are appended to the list (l1); else, they are printed.

# Here, the list (l1) has no duplicates. The values printed are the duplicates from list (l).


# def Find_Repeated(x):
#     x2=sorted(x)
#     List_Of_Repeated=[]
#     for i in x2:
#         if x2.count(i)>1:
#             List_Of_Repeated.append([i,x2.count(i)])
#             for c in range(x2.count(i)):
#                 for j in x2:
#                     if i==j and x2.count(i)>1:
#                         x2.remove(i)
#     List_Of_Repeated.sort()
#     return List_Of_Repeated
#     List=['homework', 'assignment', 'quiz', 'discussion', 'quiz', 'program'] 
#     print(Find_Repeated(List),"\n")

def bubble_sort(doubleWords):
    n = len(doubleWords)
    for i in range(n):
        for j in range(n - i - 1):
            if doubleWords[j] > doubleWords[j + 1]:
                # sorting by using simultaneous assignment in python
                doubleWords[j], doubleWords[j + 1] = doubleWords[j + 1], doubleWords[j]
doubleWords=['homework', 'assignment', 'quiz', 'discussion', 'quiz', 'program'] 
print('Before sorting an String Array: {}'.format(doubleWords))
bubble_sort(doubleWords)
print('After sorting an String Array: {}'.format(doubleWords))