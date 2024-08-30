# Print a first 10 natural number by using recursive function

# def a_funtion(n):
#     if n >= 0: 
#         s= a_funtion(n-1)
#         print(n)
#         return s
# r = a_funtion(10)

# Write a recursive function to print first N natural number in rever order

# def reverse(n):
#     if n >=0:
#         print(n,end=" ")
#         reverse(n-1)
# r= reverse(10)  

# Write a recursive function to print first N odd number

# def odd(n):
#     if n >0:
#         odd(n-1)
#         print(n*2-1,end=" ")

# r= odd(10)  

# Write a recursive function to print first N Even number
# def Even(n):
#     if n >0:
#         Even(n-1)
#         print(n*2,end=" ")

# r= Even(10)  

# Write a recursive function to print first N odd number in reverse order

# def odd_reverse(n):
#     if n >0:
#         print(n*2-1,end=" ")
#         odd_reverse(n-1)
    
# r= odd_reverse(10)  

# Write a recursive function to print first N Even number in reverse order

# def Even_reverse(n):
#     if n >0:
#         print(n*2,end=" ")
#         Even_reverse(n-1)
    
# r= Even_reverse(10)  

# Write a recursive function to clculate the the sum of first 10 natural number

# def sum_even(n):
#     if n==0:
#         return 0
#     return n + sum_even(n-1)
# r= sum_even(10)
# print(r)

# Write a recurse function to add N odd number

# def odd_sum(n):
#     if n == 0:
#         return 0
#     s= n*2 -1 + odd_sum(n-1)
#     return s 
# print(odd_sum(3))
# 
#write a recursive function to find the sum of N Even number
# def even_sum(n):
#     if n == 0:
#         return 0
#     sum  = n*2 +even_sum(n-1)
#     return sum
# print(even_sum(10))
    
# Write a recursve function to fincd the factorial of a N number
# def factorial(n):
#     if n == 1:
#         return 1
#     fact = n * factorial(n-1)
#     return fact
# print(factorial(4))

#Write a recursive function to calculate the sum of squre of first n natural numbers
def sum_squre(n):
    if n == 0:
        return 0 
    s = n*n + sum_squre(n-1)
    
    return s
print(sum_squre(5))