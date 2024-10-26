# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['coderdecoder.py'],
    pathex=['D:\Projekti\cipher-coder-decoder'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries + [('Typewriter.ico', 'D:\Projekti\cipher-coder-decoder\Typewriter.ico', 'DATA')],
    a.zipfiles,
    a.datas,
    [],
    name='coderdecoder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Typewriter.ico'],
)
