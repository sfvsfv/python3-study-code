import sys
from you_get import common as you_get#  导入you-get库

#  设置下载目录
directory=r'E:/'
#  要下载的视频地址
url='http://www.kuwo.cn/play_detail/167677601'
#  传参数
sys.argv=['you-get','-o',directory,'--format=flv',url]

you_get.main()
