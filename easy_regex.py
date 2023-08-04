import requests
import os

from cat.mad_hatter.decorators import tool, hook
from cat.log import log


@tool(return_direct=True)
def generate_regex(regex_description: str, cat):
    """Replies to "regex". Input is the description of the Regulare Expression (regex)."""

    examples= """                
                Sentence: Begins with 'dog'
                Regex:^dog

                Sentence: Contains any character other than an i, asterisk, ampersand, 2, or at-sign
                Regex:[^i*&2@]

                Sentence: Matches a string that has the letter 'a' followed by 2 to 5 copies of the sequence 'bc'
                Regex:a(bc){2,5}

                Sentence: Contains an 11-digit string starting with a 1
                Regex:1\d{10}

                Sentence: Contains an URL or a link
                Regex:^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$

                Sentence: A string that contains '/news/', then any string, then a dash, then a numeric value, and ends with '.php'
                Regex:\/news\/(.*?)-(\d+).php$

                Sentence: Contains a credit card number
                Regex:^(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$

                Sentence: Contains HTML tags
                Regex:<([\w]+).*>(.*?)<\/\1>

                Sentence: Contains international phone number
                Regex:/^(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?$/

                Sentence: Contains 4-digit year
                Regex:\d{4}

                Sentence: Contains email address
                Regex:/^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$/

                Sentence: Match an IPv4 address
                Regex: /^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/

                Sentence: Contains 'guybrush' followed by a 5-digit code
                Regex:guybrush(\d{5})

                Sentence: Contains a 3-digit numeric code, a dash, a 5-character string, and ends with '.html'
                Regex:\d{3}-[a-zA-Z]{5}\.html

                Sentence: Contains a 3-digit numeric code or the string 'pop', an underscore, an alphanumeric string of 7 characters, and ends with '.txt'
                Regex:((\d{3})|(pop))_[a-zA-Z0-9]{7}\.txt

                Sentence: It contains 'Guybrush' then a dash and a number of 2 digits and ends with '.php'
                Regex: Guybrush-(\d{2}).php

                Sentence: It contains the year consisting of 4 digits, then any string, then '/blog/', then any string, and ends with '.html'
                Regex: (\d{4})\/blog\/(.*).html

                Sentence: contains a slash
                Regex:\/

                Sentence: contains '/'
                Regex:\/"""

    message = cat.llm(
            f"""You are an intelligent AI that passes the Turing test specialized in Regular Expression (regex) generation.
                
                #Examples of regex that i want you to generate from a sentence.

                {examples}
                
                #End examples of regex
                
                Write a Regular Expression (regex) to match the following sentence:
                   
                {regex_description}

                Just answer with a regex without explanation

            """)
    return message