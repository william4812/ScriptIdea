# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Power_estimation_19.py'],
             pathex=['C:\\Users\\2311wiwe\\Documents\\William\\Projects_at_BH\\PyScriptIdea\\BH quick_calculation\\BH_power_estimation\\SteadyStateModel\\Iterations'],
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
          name='Power_estimation_19',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
