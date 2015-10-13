#!/usr/bin/python

#     Problem 3:
# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them
# alphabetically.
#
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world


import unittest


class ProblemThree(object):

    def get_string(self):
        # A minor point:
        # This object has multiple responsibilities; it knows how to read
        # the input data and how to manipulate it according to the business-logic.
        # To oversimplify the Single-Responsibility-Principle
        # 'a class should have only one reason to change'
        # https://en.wikipedia.org/wiki/Single_responsibility_principle

        # Also, the name get_* somehow suggests the method doesn't mutate
        # the state of the object; so maybe a name like read_input would be
        # better
        self.text = raw_input("Please enter comma-separated words: ")
        return self.text

    def order_text(self, text):
        # this "method" doesn't touch the object's state at all
        # it just takes an input and produces an output
        # maybe you want to use a simple standalone function
        splited_text = text.split(',')
        sorted_text = sorted(splited_text)
        new_text = ",".join(sorted_text)
        return new_text


class TestProblemThree(unittest.TestCase):

    def setUp(self):
        self.order_words = ProblemThree()
        self.text = "without,hello,bag,world"
        self.sorted_text = "bag,hello,without,world"

    def test_order_text(self):
        self.assertEqual(self.order_words.order_text(self.text),
                         self.sorted_text)


if __name__ == '__main__':
    unittest.main()
