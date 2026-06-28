# quest_27_fizzbuzz_test.py

for i in range(1, 101):
    # check both 3 and 5 first, otherwise it'll print Fizz or Buzz and never get to FizzBuzz
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
