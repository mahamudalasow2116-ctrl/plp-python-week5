# WEEK 5 PYTHON ASSIGNMENT
## Password Generator & Your Own Module

**Name:** Mahamud Abdi  
**Subject:** Python Programming  
**Repository:** `plp-python-week5`

---

## QUESTION 1: PASSWORD GENERATOR

**Filename: `password_generator.py`**

```python
import random
import string

def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


p1 = make_password()
p2 = make_password(12)

print("Password:", p1)
print("Length:", len(p1))
print("Password:", p2)
print("Length:", len(p2))
```

---

## QUESTION 2: YOUR OWN MODULE

### Part 1: Helpers Module

**Filename: `helpers.py`**

```python
import math

def tables_needed(people, seats):
    return math.ceil(people / seats)

def welcome(name):
    return f"Welcome to PLP, {name}!"

if __name__ == "__main__":
    print(tables_needed(10, 4))
```

### Part 2: Main Program

**Filename: `main.py`**

```python
import helpers

print(helpers.welcome("Amina"))
print(helpers.tables_needed(47, 6))
print(helpers.tables_needed(20, 5))
```

---

## EXPECTED PROGRAM OUTPUTS

### Output 1: password_generator.py

```text
Password: [random 8-character password]
Length: 8
Password: [random 12-character password]
Length: 12
```

### Output 2: main.py

```text
Welcome to PLP, Amina!
8
4
```

### Output 3: helpers.py

```text
3
```

---

## CONCLUSION

This assignment demonstrates how to:
1. Import and use Python built-in modules such as `random`, `string`, and `math`.
2. Create functions with default parameter values.
3. Generate random passwords of different lengths.
4. Create and import a custom Python module.
5. Use `if __name__ == "__main__":` to control code execution.

**Submission requirements:**
- `password_generator.py`
- `helpers.py`
- `main.py`
- Screenshots showing the required program outputs.

**GitHub repository:** `plp-python-week5`  
**Repository visibility:** Public
