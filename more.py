
## **Basic Function Problems**
### **1. Function to Print "Hello, World!"**

def hello():
    print("Hello, World!")

hello()


### **2. Function to Add Two Numbers**

def add(a, b):
    return a + b

print(add(5, 3))


### **3. Function to Find Maximum of Two Numbers**

def maximum(a, b):
    return a if a > b else b

print(maximum(10, 20))


### **4. Function to Find the Factorial of a Number**

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(factorial(5))


### **5. Function to Check if a Number is Even or Odd**

def is_even(n):
    return "Even" if n % 2 == 0 else "Odd"

print(is_even(7))




## **Intermediate Function Problems**
### **6. Function to Check if a Number is Prime**

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(13))


### **7. Function to Print Fibonacci Series Up to N Terms**

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)


### **8. Function to Find the Sum of Digits of a Number**

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(1234))


### **9. Function to Reverse a String**

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))


### **10. Function to Check if a String is a Palindrome**

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))




## **Advanced Function Problems**
### **11. Function to Find LCM of Two Numbers**

def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

print(lcm(12, 15))


### **12. Function to Count the Number of Vowels in a String**

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("Hello World"))


### **13. Function to Find the Sum of a List**

def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4, 5]))


### **14. Function to Find the Largest Number in a List**

def max_in_list(lst):
    return max(lst)

print(max_in_list([4, 9, 1, 7, 3]))


### **15. Function to Convert Celsius to Fahrenheit**

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(25))




## **Real-World Function Problems**
### **16. Function to Calculate Simple Interest**

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print(simple_interest(1000, 5, 2))


### **17. Function to Check If a Year is a Leap Year**

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(2024))


### **18. Function to Validate a Password (Min 8 Chars, Includes a Number)**

def validate_password(password):
    return len(password) >= 8 and any(char.isdigit() for char in password)

print(validate_password("mypassword1"))


### **19. Function to Count Words in a String**

def count_words(sentence):
    return len(sentence.split())

print(count_words("This is a simple sentence."))


### **20. Function to Generate a Random Password**

import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print(generate_password(10))


