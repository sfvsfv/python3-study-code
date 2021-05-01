import requests
from lxml import etree

html = '''<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="a-inactive"><a href="link3.html" class="yao">third item1</a></li>
         <li class="b-inactive"><a href="link4.html">third item2</a></li>
         <li class="c-inactive"><a href="link5.html">third item3</a></li>
         <li class="d-inactive"><a href="link6.html">third item4</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>'''

html_tree = etree.HTML(html)
# print(html_tree)
#看一下html_tree里面的数据
# print(etree.tostring(html_tree).decode('utf-8'))

#获取文件中所有的标签li
#xpath返回数据是列表, [Element li 内存地址]
li = html_tree.xpath('//li')
# print(li)

li2 = html_tree.xpath('//li[@class="item-1"]')
#获取第二个item-1文本,li2[1]返回的是Element,继续使用xpath
# print(li2[0].xpath('.//a/text()'))

#查询li标签class包含inactive字符串
li4 = html_tree.xpath('//li[contains(@class,"inactive")]')
print(li4)