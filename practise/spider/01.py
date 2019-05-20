# def parse_newhouse(self, response):
#     print(response)
#     lis = response.xpath("//div[@class='nl_con clearfix']/ul/li")
#     print(len(lis))  # 输出21
#     for li in lis:
#         print(li)  # 实际输出6个 Selector
#         a_name = li.xpath(".//div[@class='nlcd_name']/a/text()").extract()[0]
#         name = a_name.strip()
#         print(name)  # 给出5个名字

import requests
from lxml import etree
base_url = "https://newhouse.fang.com/house/s/"
response = requests.get(base_url)
# print(response.)
html = response.text
print(response.text)
response = etree.HTML(response.text)
lis = response.xpath("//div[@class='nl_con clearfix']/ul/li")
print(len(lis))

# print(len(lis))  # 输出21
for c, li in enumerate(lis):
    a_name = li.xpath(".//div[@class='nlcd_name']/a/text()")
    a_name = a_name[0] if a_name else ""
    print(c + 1, a_name)

print(a_name)



