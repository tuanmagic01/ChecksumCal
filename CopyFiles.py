import os
import shutil
File_List = open(r'C:\Users\Admin\Documents\PythonProject\ChecksumCal\Flist.txt','r')
configdesPath = r'C:\Users\Admin\Documents\PythonProject\ChecksumCal\Des'
for i in File_List:
    srcPath = r'C:\Users\Admin\Documents\PythonProject\ChecksumCal' + i.rstrip('\n')
    print(srcPath)
    startPos = srcPath.rfind('\\')
    FileName = srcPath[startPos+1:]
    desPath = configdesPath + i.rstrip(FileName + '\n')
    print(desPath)
    if not os.path.exists(desPath):
        os.makedirs(desPath)
    shutil.copy(srcPath,desPath)

