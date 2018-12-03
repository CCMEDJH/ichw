# Assign2.py
# Du JunHao (CCMEDJH)
# December 2, 2018
"""Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange."""

from urllib.request import urlopen   # Access the URL in Python3


def get_from(source, target, amt):
    """Open the URL and extract the list, in order to get the value
    you need"""
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?' \
                  + 'from='+ source + '&to=' + target + '&amt='\
                  + amt)   # Open the URL you wanted
    docstr = doc.read()    # output the text
    doc.close()    # Close the URL
    jstr = docstr.decode('ascii')    # Translate 'docstr' into list
    return jstr


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.
    Parameter currency_from: the currency on hand.
    Parameter currency_to: the currency to convert to.
    Parameter amount_from: amount of currency to convert."""

    jstr = get_from(currency_from, currency_to, amount_from)
    median_1 = jstr.split(",")    # Extract output value
    median_2 = median_1[1].split(" ")    # Extract output value
    amount = median_2[3].replace('"','')     # Get the output value
    guide = median_1[-1]    # Introduces a function that determines whether the input is correct
    return amount, median_2, guide


def test_get_from():
    """test the function'get_from'"""
    assert('{ "from" : "1 United States Dollar", "to" : "6.8521 Chinese Yuan", "success" : true, "error" : "" }' \
           == get_from('USD', 'CNY', '1'))


def test_exchange():
    """test the function'exchange'"""
    string_output2 = ('6.8521', ['', '"to"', ':', '"6.8521', 'Chinese', 'Yuan"'], ' "error" : "" }')
        # standard output of 'exchange'
    assert(string_output2 == exchange('USD', 'CNY', '1'))


def test_all():
    """test all cases"""
    test_get_from()
    test_exchange()
    print("All tests passed")


def main():
    '''main function.
    Determine whether to enter normal mode or test mode.

    Determine the type of error the user entered:
        1.Currency code error
        2.Currency amount error'''
    judge = input('请输入“N”进入正常模式，输入“T”进入测试模式------', )
    if judge == 'N':    # Enter the normal mode
        source = input('您的原有货币代码：',)    # Enter currency code and amount
        target = input('您的兑换货币代码：',)
        amt = input('您的兑换量：',)
        amount, median_2, guide = exchange(source, target, amt)
        if guide == ' "error" : "Source currency code is invalid." }':
                # Determines whether the source currency code was entered incorrectly
            print('原有货币代码输入错误，请重新输入')
            main()
        elif guide == ' "error" : "Exchange currency code is invalid." }':
                # Determines whether the exchange currency code was entered incorrectly
            print('兑换货币代码输入错误，请重新输入')
            main()
        elif guide == ' "error" : "Currency amount is invalid." }':
                # Determines whether the amount was entered incorrectly
            print('兑换量输入错误，请重新输入')
            main()
        elif guide == ' "error" : "" }':
                # Determines whether the input is correct and outputs the result
            print('兑换后得到 ' + amount + ' ' + median_2[-1].replace('"',''))
                # Output converted values and units
    elif judge == 'T':    # Enter the test mode
        test_all()    # Run the test function
        main()    # Run the main function again after testing
    else:
        main()    # The input is neither N nor T, rerun the main function


if __name__ == '__main__':
    main()
