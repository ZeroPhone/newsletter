from collections import OrderedDict
from lxml import html as xhtml
import requests
import shutil
import sys
import os

posts_dir = "_posts"
images_dir = "images"

#From https://github.com/matthewwithanm/python-markdownify
from markdownify import MarkdownConverter
def md(html, **kwargs):
    class CustomMarkdownConverter(MarkdownConverter):
        def convert_hn(self, n, el, text):
            hashes = "#"*n
            ret =  "\n---\n\n{} {}\n\n".format(hashes, text.strip())
            return ret

    return CustomMarkdownConverter(**kwargs).convert(html)

print("Enter the URL for the newsletter page on MailChimp")
print("(the 'see in browser' URL from the email that MailChimp sent out)")
url = raw_input("URL: ")

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


#Getting article content
content_xpath = "/html/body/center/table/tr/td/table/tr[3]//tbody[@class='mcnTextBlockOuter']//td[@class='mcnTextContent']"
#TODO: shorten (XPATH: https://msdn.microsoft.com/en-us/library/ms256086(v=vs.110).aspx )
tree = xhtml.fromstring(html)
content_element = tree.xpath(content_xpath)[0]

#Asking newsletter date and number from user
print("Enter date in YYYY-MM-DD format")
date = raw_input("Date: ")
print("Enter newsletter number")
newsletter_number = int(raw_input("Number: "))

#Generating filename
post_filename = "{0}-ZeroPhone-Weekly-No.-{1}.md".format(date, newsletter_number)
print("Filename: {}".format(post_filename))

#Finding images
image_xpath_1 = "//img[@align='center']"
image_xpath_2 = "//img[@data-file-id]"
images = tree.xpath(image_xpath_1) + tree.xpath(image_xpath_2)
image_filenames = []
for i, image in enumerate(images):
    extension = image.get("src").rsplit('.', 1)[1]
    image_filename = "{0}_{1}_{2}.{3}".format(date, newsletter_number, i+1, extension)
    print(image_filename)
    image_filenames.append(image_filename)
first_image_filename = image_filenames[0]

#Downloading images
for i, image in enumerate(images):
    print("Downloading {}".format(image.get("src")))
    r = requests.get(image.get("src"), stream=True)
    if r.status_code == 200:
        img_path = os.path.join(images_dir, image_filenames[i])
        print("Done, writing into {}".format(img_path))
        with open(img_path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f) 
        image.set("src", os.path.join("..", img_path))
    else:
        print("Failed!")

#Getting title
title_xpath = "/html/head/title"
title = tree.xpath(title_xpath)[0].text

#Generating post header
post_header = """---
layout: post
title: {0}
img: {1}""".format(title, first_image_filename)

#Converting HTML into MD
content_html = xhtml.tostring(content_element)
unfiltered_md = md(content_html)

#Writing everything into a post file
post_path = os.path.join(posts_dir, post_filename)
with open(post_path, "w") as f:
    f.write(post_header.encode("utf8"))
    f.write(unfiltered_md.encode("utf8"))

#Done!
print("Article written to {}".format(post_path))
