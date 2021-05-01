import os
from json import loads
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString #用来构建对象数据的模块部分

#构建数据结构对象，对照官方文档
def jsonToXml(json_path, xml_path):
    with open(json_path, 'r', encoding='gbk')as json_file:  #打开文件，用gbk方式编译
        load_dict = loads(json_file.read()) # load将字符串转换为字典
    print(load_dict)    #打印读取的字典
    my_item_func = lambda x: 'Annotation'
    xml = dicttoxml(load_dict, custom_root='Annotations', item_func=my_item_func, attr_type=False)
    dom = parseString(xml)  #借助parse string而调整数据结构
    with open(xml_path, 'w', encoding='UTF-8')as xml_file:  #xml_file是文件路径
        xml_file.write(dom.toprettyxml())   #doc.toprettyxml(indent, newl, encoding)方法可以优雅显示xml文档

#输出为转换为xml格式
def json_to_xml(json_dir, xml_dir):
    if (os.path.exists(xml_dir) == False):  #判断括号里的文件是否存在的意思，括号内的可以是文件路径。
        os.makedirs(xml_dir)    #用于递归创建目录
    dir = os.listdir(json_dir)  #返回输入路径下的文件和列表名称
    for file in dir:
        file_list = file.split("：") #通过：对字符串分割
        if (file_list[-1] == 'json'):       #对于json文件
            jsonToXml(os.path.join(json_dir, file), os.path.join(xml_dir, file_list[0] + '.xml'))   #调用函数，转为xml文档格式，os.path.join():拼接待操作对象

#调用函数，传参，保存为xml文档
if __name__ == '__main__':
    try:
        j_path = r"D:\code\python\jason转xml1\chords.json"
        x_path = r'D:\code\python\jason转xml1\chords.xml'
        jsonToXml(j_path, x_path)

        j_dir = r"D:\code\python\jason转xml1\chords.json"
        x_dir = r'D:\code\python\jason转xml1\chords.xml'
        json_to_xml(j_dir, x_dir)
    except:
        pass
