# -*- mode: python -*-

block_cipher = None


a = Analysis(['T_Power_estimation.py'],
             pathex=['H:\\Buffer_zone\\quick_calculation\\BH_power_estimation\\TransientModel'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='T_Power_estimation',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
