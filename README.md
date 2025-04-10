# 📘 Functions in Python

Functions in Python help you organize your code into reusable blocks. They allow you to avoid repetition, improve readability, and make your code more modular and manageable.

---

## 🧠 What is a Function?

A **function** is a block of code that performs a specific task and can be reused whenever needed. You define a function once and call it wherever required.

---

## 🧩 Syntax of a Function

```python
def function_name(parameters):
    # block of code
    return result
```

- `def`: Keyword to define a function.
- `function_name`: Any name you choose (follow naming rules).
- `parameters`: (Optional) Inputs passed to the function.
- `return`: (Optional) Used to return a value from the function.

---

## 🔹 Example: Simple Function

```python
def greet():
    print("Hello, Sathish!")
    
greet()  # Output: Hello, Sathish!
```

---

## 🔸 Example: Function with Parameters

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

---

## 🔁 Function with Default Parameters

```python
def greet(name="User"):
    print("Hello", name)

greet()          # Output: Hello User
greet("Sathish") # Output: Hello Sathish
```

---

## 🔁 Return Statement

- The `return` keyword sends a value back to where the function was called.
- Without `return`, the function returns `None`.

```python
def square(x):
    return x * x

print(square(4))  # Output: 16
```

---

## 🔍 Types of Functions

1. **Built-in Functions** – Predefined in Python (like `print()`, `len()`, `type()`)
2. **User-defined Functions** – Created by the programmer
3. **Lambda Functions** – Anonymous, short functions using `lambda` keyword

---

## ⚡ Lambda Function (One-liner functions)

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

## ✅ Best Practices

- Use meaningful function names.
- Keep functions short and do one specific task.
- Add comments/docstrings for documentation.

---

## 📚 Example: Docstring in a Function

```python
def multiply(a, b):
    """This function multiplies two numbers"""
    return a * b
```

You can access the docstring using:

```python
print(multiply.__doc__)
```
