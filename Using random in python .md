### Python random randrange() and randint() to generate random integer number within a range

In this lesson, we will see how to use the randrange() and randint() functions of a Python random module to generate a random integer number.

Using randrange() and randint() functions of a random module, we can generate a random integer within a range. In this lesson, you’ll learn the following functions to generate random numbers in Python. We will see each one of them with examples.


| Function | Description |
| --- | --- |
| random.randint(0, 9) | Returns any random integer from 0 to 9 |
| random.randrange(20) | Returns a random integer from 0 to 19 |
| random.randrange(2, 20) | Returns a random integer from 2 to 19. |
| random.randrange(100, 1000, 3) | Returns any random integer from 100 to 999 with step 3. For example, any number from 100, 103, 106 … 994, 997. |
| random.randrange(-50, -5) | Returns a random negative integer between -50 to -6. |
| random.sample(range(0, 1000), 10) | Returns a list of random numbers |
| secrets.randbelow(10) | Returns a secure random number |
  
  
### How to use Python randint() and randrange() to get random integers

1. Import random module
Use Python’s random module to work with random data generation.
import it using a import random statement.

2. Use randint() Generate random integer
Use a random.randint() function to get a random integer number from the inclusive range. For example, random.randint(0, 10) will return a random number from [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10].

3. Use the randrnage() function to generate a random integer within a range
Use a random.randrange() function to get a random integer number from the given exclusive range by specifying the increment. For example, random.randrange(0, 10, 2) will return any random number between 0 and 20 (like 0, 2, 4, 6, 8).
