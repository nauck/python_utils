from time import time

# start the timer
start = time()

public_key = int(input("enter any number as your public key: "))


# store the discovered factors in a list
factors = []

# Begin testing at 2
test_number = 2

# loop through all numbers from 2 up until the one below the you are testing
while test_number < public_key:

    # if the public key divides exactly into the test_number, it is a factor
    if public_key % test_number == 0:

        # add this factor to the list
        factors.append(test_number)

    # move on to the next test number
    test_number += 1
end = time()
total = end - start
print(str(total) + "seconds")
print(factors)
    
