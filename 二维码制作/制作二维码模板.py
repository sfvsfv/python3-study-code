from MyQR import myqr
# 带图片的艺术二维码：黑白
# myqr.run(
#   words='http://www.cnblogs.com/mayi0312',
#   picture='logo.jpg',
#   save_name='artistic.png'
# )
# 带图片的艺术二维码：彩色
myqr.run(
  words='https://yanghanwen.xyz/tu/',
  picture='s.jpg',
  colorized=True,
  save_name='ke.png'
)

# from MyQR import myqr
#
# # 动态二维码
# myqr.run(
#   words='http://www.cnblogs.com/mayi0312',
#   picture='Sources/gakki.gif',
#   colorized=True,
#   save_name='Animated.gif'
#