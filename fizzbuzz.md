# FizzBuzz 

## Problem Statement 
Write a program that prints the numbers from 1 to n. But for multiples of 3, print 
```"Fizz"``` instead of the number, and for the multiples of 5, print ```"Buzz"```.

For numbers which are multiples of ```both 3 and 5```, print ```"FizzBuzz"```. 

# Example
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz


# Implementation
```
def fizzBuzz(n: int) -> None:
  for i in range(1, n+1):
    output = ""
    if i%3 == 0:
      output += "Fizz"
    if i%5 == 0:
      output += "Buzz"
    if output == "":
      output = str(i)
    print(output)

  // Example:
  fizzBuzz(15)
```
