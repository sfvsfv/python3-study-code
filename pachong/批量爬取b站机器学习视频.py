# -*- coding: utf-8 -*-
import os


def test_cmd():
    radio_list = ["https://www.bilibili.com/video/BV1Yp411d7uq",
                  "https://www.bilibili.com/video/BV1xp411d7Bu",
                  "https://www.bilibili.com/video/BV16p411R7nJ",
                  "https://www.bilibili.com/video/BV1Cp411R7gB",
                  "https://www.bilibili.com/video/BV1fW411A7Gs",
                  "https://www.bilibili.com/video/BV1AW411P7YB",
                  "https://www.bilibili.com/video/BV1uW411P7mg",
                  "https://www.bilibili.com/video/BV1uW411P7JM",
                  "https://www.bilibili.com/video/BV1gW411P7nG",
                  "https://www.bilibili.com/video/BV13W411P7Ba",
                  "https://www.bilibili.com/video/BV1AW411A7wa",
                  "https://www.bilibili.com/video/BV1Ws411771n",
                  "https://www.bilibili.com/video/BV1ss41177zv",
                  "https://www.bilibili.com/video/BV1Ts41157z2",
                  "https://www.bilibili.com/video/BV1Ts411572q",
                  "https://www.bilibili.com/video/BV1us41157WL",
                  "https://www.bilibili.com/video/BV1Es411n7u9",
                  "https://www.bilibili.com/video/BV1os411T7w2",
                  "https://www.bilibili.com/video/BV1ab411F7Hs",
                  "https://www.bilibili.com/video/BV1ct411o7ui",
                  "https://www.bilibili.com/video/BV1wt411o742",
                  "https://www.bilibili.com/video/BV1ct411o7QU",
                  "https://www.bilibili.com/video/BV1pt411X74k",
                  "https://www.bilibili.com/video/BV114411c7xD", ]

    for i in range(len(radio_list)):
        try:
            show_cmd = "you-get -i " + radio_list[i]
            print(show_cmd)
            os.system(show_cmd)
            print("开始下载：" + radio_list[i])

            download_cmd = "you-get --format=flv " + radio_list[i]
            print(download_cmd)
            res = os.system(download_cmd)
            print(res)
            print(radio_list[i] + "下载完成")
        except Exception:
            print("第" + str(i) + "个视频下载出现了错误")
            print("名字是：" + radio_list[i])


if __name__ == '__main__':
    test_cmd()

