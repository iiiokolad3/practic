import re

from urllib import request
import re
import ssl
import urllib.request


ssl._create_default_https_context = ssl._create_unverified_context

link = ' https://msk.spravker.ru/avtoservisy-avtotehcentry'
# pattern_link = r'(?:<a href=\")([^<+]+)(?:\" title)(?:.*)'
pattern_name = r'(?<=(?:class=\"org-widget-header__title-link\">)([^<+]+)(?:</a>))'
pattern_adders = r'(?:<span class=\"org-widget-header__meta org-widget-header__meta--location\">)([^<+]+)(?:</span>)'
pattern_number = r'(\+\d \(\d{3}\) \d{3}-\d{2}-\d{2})'
pattern_timework = r'(?:<dd class=\"spec__value\">)([^<+]+)(?:</dd>)'
pattern_rewiews = r'(?:class=\"org-widget-feedback__comment\">)(?:\s+<p>)([^<+]+)(?:</p>)'
pattern = r'(?:class=\"org-widget\-header__title-link\">[^\w]*|<span class=\"org-widget\-header__meta ' \
r'org-widget\-header__meta\--location\">[^\w]*|<dt class=\"spec__index\"><span ' \
r'class=\"spec__index-inner\">Телефон</span></dt>\n*\s*<dd class=\"spec__value\">[^\w]*|<dt ' \
r'class=\"spec__index\"><span class=\"spec__index-inner\">Часы работы</span></dt>\n*\s*<dd ' \
r'class=\"spec__value\"[^\w]*>|<p>[^\w]*)([^<]*\b)'
content = request.urlopen(link).read().decode()
match = re.findall(pattern, content)
rez = [match[i: i+5] for i in range(0, len(match), 5)]
for i in range(len(rez)):
    print(rez[i], '\n')