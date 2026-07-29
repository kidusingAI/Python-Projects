# doubles = [x*3 for x in range(1,11)]
# triples = [x*3 for x in range(1,11)]
# squares = [x**2 for x in range(1,11)]
#fruits = ["apple","banana","orange","pear","pineapple"]
#fruits = [fruit.upper() for fruit in fruits]
#fruits = [
#         fruit[0] for fruit in fruits
#         ]

#numbers = [
#          -5,-4,-3,-2,-1,0,1,2,3,4,5
#          ]
#          
#          
#positive_nums = [
#                num * -1 for num in numbers if num < 0
#                ]
#even_nums = [
#            num for num in numbers if num%2 == 0
#            ]
#odd_nums = [
#           num for num in numbers if num%2 != 0
#           ]
grades = [
         85,42,78,64,59,76,46,100,90,89,56,37,29,0,15
         ]
passing_grades = [grade for grade in grades if grade >= 60]
            
print(passing_grades)
