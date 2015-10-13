#!/usr/bin/python 

# Problem 1:
# Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a 
# single line.


# to nitpick: min and max are builtin functions, and you should avoid using these names for variables
def numbers(min, max):
    # result = []
    # for number in xrange(min, max):
    # you want to go to max+1, xrange(1, 3) gives you [1, 2]
    for number in xrange(min, max + 1):
        if number % 7 == 0 and number % 5 is not 0:
            # result.append(number)
            yield number  # if you use yield you get a generator, and we don't need to build
            # up the list in memory; think of it as a sort of lazy list
            # yield is like having a function "return" a value then continue to execute
    # return result


# printed_result = ""
# for number in  numbers(2000, 3200):
#     printed_result = "{} {},".format(printed_result, number)
# print printed_result[:-1]

# just use the join method of the string type, pass it a list of strings and no
# more trailing comma to handle
print ",".join(
    [str(num) for num in numbers(2000, 3200)]
)
