

block_cipher = None


a = Analysis(['main.py','game.py','window.py','ai.py','corner_widget.py'],
             pathex=['D:\\code\\python\\wuziqi'],
             binaries=[],
             datas=[('D:\code\python\wuziqi\imgs','imgs')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['window','PyQt5','numpy ','copy','time'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
