html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import Comment
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
for string in soup.strings:
    print(repr(string))
    #prints the strings
for tag in soup.find_all([True]):
    print(tag.name)
    #prints the tags in the page
for string in soup.stripped_strings:
    print(repr(string))
    #removes the whitespaces between strings
new_comment = Comment("Nice to see you.")
tag.append(new_comment)
tag
# <b>Hello there<!--Nice to see you.--></b>
tag.contents
markup = "<p>I want <b>pizza</b> and more <b>pizza</b>!</p>"
soup = BeautifulSoup(markup, 'html.parser')
first_b, second_b = soup.find_all('b')
print(first_b == second_b)
# True

print(first_b.previous_element == second_b.previous_element)
import copy
p_copy = copy.copy(soup.p)
print(p_copy)