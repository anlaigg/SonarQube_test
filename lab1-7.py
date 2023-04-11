import re

text = ''
while True:
    try:
        line = input()
        text += line
    except:
        break

pattern = r'singer="(.*?)">(.*?)</a>'
result = re.findall(pattern, text, re.S)
print(result)
