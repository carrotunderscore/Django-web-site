import re

from django import template

register = template.Library()


@register.simple_tag
def markdown_heading(content):
    lineList = []
    cleaned_content = content.replace("<p>", "").replace("</p>", "")
    lines = cleaned_content.split("\n")
    for i in lines:
        lineList.append(i)

    headingList = []
    for line in lineList:
        count = 0
        for char in line:
            if char == "#":
                count += 1
        removedHashtag = line.replace("#", "")
        if count > 0:
            headingList.append("<h" + str(count) + ">" + removedHashtag + "</h" + str(count) + ">")
        else:
            headingList.append(removedHashtag + "<br>")
    headingString = ''.join(headingList)
    return '<div id="contentText">' + headingString + '</div>'





