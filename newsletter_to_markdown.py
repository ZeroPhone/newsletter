from collections import OrderedDict
from lxml import html as xhtml
import requests
import sys
import os

posts_dir = "_posts"
images_dir = "images"

#From https://github.com/matthewwithanm/python-markdownify
from markdownify import markdownify as md

print("Enter the URL for the newsletter page on MailChimp")
print("(the 'see in browser' URL from the email that MailChimp sent out)")
#url = raw_input("URL: ")
url = "http://mailchi.mp/1e519fe20bdb/call-for-contributors-first-batch-of-zerophones-and-zerophone-wiki?e=4681421369"

if len(url) < 10:
    print("Do you have a filename to read from?")
    filename = raw_input("Enter filename: ")
    with open(filename, 'r') as f:
        html = f.read()
else:
    req = requests.get(url)
    if req.status_code != 200:
        print("Can't get the newsletter HTML!")
        sys.exit(1)
    html = req.text


#TODO: shorten (XPATH reference: https://msdn.microsoft.com/en-us/library/ms256086(v=vs.110).aspx )
content_xpath = "/html/body/center/table/tr/td/table/tr[3]//tbody[@class='mcnTextBlockOuter']//td[@class='mcnTextContent']"

tree = xhtml.fromstring(html)

content_element = tree.xpath(content_xpath)[0]
content_html = xhtml.tostring(content_element)

#Asking newsletter date and number from user
#print("Enter date in YYYY-MM-DD format")
#date = raw_input("Date: ")
date = "2017-00-00"
#print("Enter newsletter number")
#newsletter_number = int(raw_input("Number: "))
newsletter_number = 9

#Generating filename
filename = "{0}-ZeroPhone-Weekly-No.-{1}.md".format(date, newsletter_number)
print("Filename: {}".format(filename))

import pdb; pdb.set_trace()

#image_xpath = None
#found_images = None

#images = OrderedDict()
#first_image_filename = images[images.keys()[0]]
first_image_filename = "ZeroPhone-x.jpg"

#Getting title
title_xpath = "/html/head/title"
title = tree.xpath(title_xpath)[0].text

post_header = """---
layout: post
title: {0}
img: {1}
---


""".format(title, first_image_filename)


unfiltered_md = md(content_html)

with open(os.path.join(posts_dir, filename), "w") as f:
    f.write(post_header.encode("utf8"))
    f.write(unfiltered_md.encode("utf8"))


print("Article written to ")
#Done!
