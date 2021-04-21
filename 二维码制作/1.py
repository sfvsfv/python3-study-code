from MyQR import myqr

# 动态二维码
myqr.run(
  words='https://yanghanwen.xyz/bainian/',
  picture='qie.gif',
  colorized=True,
  save_name='bainian.gif',
  version=40
)