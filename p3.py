#!/usr/bin/python 

#     Problem 3:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# 
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world


class ProblemThree:

    def getString(self):
        self.text = raw_input("Please enter comma-separated words: ")
        return self.text

    def orderText(self, text):
        splited_text = self.text.split(',')
        sorted_text = sorted(splited_text)
        new_text = ','.join(sorted_text)
        print new_text


x = ProblemThree()
text = x.getString()
x.orderText(text)

