#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Du JunHao"
__pkuid__  = "180011833"
__email__  = "djh@pku.edu.cn"
"""


import re, sys, os
from collections import Counter
from urllib.request import urlopen


def wcount(lines, topn):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """

    punc = ["!", "?", ",", ".", ";", ":", '"', "(", ")", ]    # The common punctuations
    list_raw = lines.split()    # Converts text to a list
    list_new = []    # The finally processed list
    for a_word in list_raw:
        a_word = a_word.lower()    # Lowercase all letters
        new_word = []    # The word after delete the punctuations
        for a_letter in list(a_word):
            if a_letter not in punc:    # Get the word without punctuation
                new_word += a_letter
        list_new.append(''.join(new_word))    # Add the new words to the final list
    return Counter(list_new).most_common(int(topn))    # Get the maximum number of words


if __name__ == '__main__':
    """The main function of this program
    Confirm whether the network is connected
    Confirm whether the input format is correct
    Confirm whether the network connection is correct
    Then Run the wcount program
    """
    # Confirm whether the network is connected:
    state = os.system('ping www.baidu.com')
    print('-' * 25)
    if state == 0:
        print('网络连通正常')
    elif state == 1:
        print('无网络连接')
    # When detected incorrect input format：
    if (len(sys.argv) == 1) or (len(sys.argv) > 3):
        print('变量数量输入错误')
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    # len(sys.argv) == 2 or 3, This is the correct input format:
    else:
        # Make sure whether the url format entered is correct:
        if re.match(r'^https?:/{2}\w.+$', sys.argv[1]):
            print("网址格式正确")
        else:
            print("网址格式错误,请输入正确的网址格式如“http://xxx”。终止筛查")
            sys.exit(1)
        # Make sure whether the topn format entered is correct:
        if len(sys.argv) == 3:
            try:
                int(sys.argv[2])
                print('topn格式正确，开始筛查')
            except:
                print('topn格式错误，终止筛查')
                sys.exit(1)
        # Make sure whether the url visit is correct, then perform the wcount function:
        try:
            web_open = urlopen(sys.argv[1])    # Open the web
            if len(sys.argv) == 2:    # Didn't input 'topn', default 'topn' is 10
                topn = 10
            else:
                topn = sys.argv[2]
            ori_text = web_open.read()    # Read the content of the url
            web_open.close()    # Close the web
            text = bytes.decode(ori_text)    # Convert content format
            res = wcount(text, topn)    # Run the wcount program
            print('单词数量最多的前%s个为：' %str(topn))
            for i in res:
                print(i[0] + '   ' + str(i[1]))    # Print the result
            print('筛查结束')
        except:    # Url access error
            print('网址访问错误')
