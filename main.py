#!/usr/bin/env python

import logging

def return_dollar(float dollar_value):
    return "$" + str(dollar_value)

if __name__ == "__main__":
    print(return_dollar(1.99))
