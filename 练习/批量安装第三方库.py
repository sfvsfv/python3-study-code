import os # 导入os库
libs = {"re"} # 将需要安装的库名称放到列表中
for lib in libs:
        os.system("pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple "+lib) # 遍历并安装库,注意了：simple后面有一个空格！



# web = "https://pypi.tuna.tsinghua.edu.cn/simple "  # 清华大学镜像源。
# web = "http://mirrors.aliyun.com/pypi/simple "  # 阿里云镜像源。
# web = "https://pypi.mirrors.ustc.edu.cn/simple "  # 中国科技大学镜像源。
# web = "http://pypi.douban.com/simple "  # 豆瓣镜像源。
