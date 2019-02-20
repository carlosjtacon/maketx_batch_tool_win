# MakeTX Batch Convert Tool - for Windows
Really simple but useful tool to batch convert all the images inside a folder to .tx inside the windows explorer. [MakeTX MAN Page](https://www.mankier.com/1/maketx).

## How to
1. _Stop working on windows. If you won't then go to step 2_
2. You will need to install the maketx.exe command line tool from [OpenImageIO](https://github.com/OpenImageIO/oiio/).
3. Replace needed paths to your own:
   - maketx_tool.py L5: MAKETX_PATH = "PATH TO maketx.exe"
   - maketx_tool.bat: "PATH TO python.exe" [Your python 2.7 installation path]
   - maketx_tool.bat: "PATH TO maketx_tool.py" [Wherever you placed this tool]
4. Right click maketx_tool.bat and create shortcut, then rename it to MakeTX [or whatever you prefer].
5. Go to %APPDATA%\Microsoft\Windows\SendTo (Copy+Paste in Windows Explorer Address Bar)
6. Paste "MakeTX" Shorcut in that folder.
7. Now you can right click on any folder -> Send To -> MakeTX.
8. It will convert all images inside the folder to .tx.