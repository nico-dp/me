# -*- coding: UTF-8 -*-

import requests

"""REFACTORING

Refactoring is the process of making your code better. You are usually looking 
to make it more readable or easier to maintain. Usually you'll do this by 
pulling out bits of code that encapsualte one idea, especially if that idea is 
used in several places.

We've talked already about 
    ↱red→green→refactor↴
    ↜←←←←←←←←←←←←←←←←←←↩

Where red means make sure the test fails if you haven't done anything, green 
means make the test pass, however you can, now this is the reafactor part.

The function below works fine, but it's long and hard to read. Identify the 
parts that are repeated, and pull them out into their own functions. I've made 
that easier for you by making the function stubs for the bits you need to do.

Modify this function, don't write a whole new one.
"""


def wordy_pyramid():
    """
    baseURL = (
        "https://us-central1-waldenpondpress.cloudfunctions.net/"
        "give_me_a_word?wordlength={length}"
    )
    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL.format(length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.text
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    for i in range(20, 3, -2):
        url = baseURL.format(length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.text
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    """

    up = list_of_words_with_lengths(3, 21, 2)
    down = list_of_words_with_lengths(20, 3, -2)

    pyramid_list = up + down

    return pyramid_list



def get_a_word_of_length_n(length):
    URL = f'https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}'
    
    response = requests.get(URL)

    if response.status_code == 200:
        word = response.text
    else:
        print("failed a request", response.status_code)
    
    return word


def list_of_words_with_lengths(start, end, step):
    list_of_words = []

    for i in range(start, end, step):
        word = get_a_word_of_length_n(i)
        list_of_words.append(word)

    return list_of_words


if __name__ == "__main__":
    pyramid = wordy_pyramid()
    for word in pyramid:
        print(word)
    
    list_of_words_with_lengths(3, 21, 2)