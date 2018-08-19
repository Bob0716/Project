# -*- coding: utf-8 -*-
import subprocess
import os

def getAllFile_name(folder):
    assert os.path.exists(folder)
    assert os.path.isdir(folder)
    FileList = os.listdir(folder)
    # for i in range(len(FileList)):
    FileList.sort()
    return FileList
    # print(FileList)
        # FileList[i] = FileList[i].split('.')
        # print(FileList[i])#['1204095924', 'PDF']
        # FileList[i][0]=int(FileList[i][0])
        # print(FileList[i][0])#<class 'int'> 1204014661
    # for j in range(len(FileList)):
    #     FileList[j][0] = str(FileList[j][0])
    #     FileList[j] = FileList[j][0] + '.' + FileList[j][1]
    # return FileList
def get_allfile_route(FileList):
    all_route = []
    for i in range(len(FileList)):
        t = 'C:\example\\' + FileList[i]
        # print(t)
        all_route.append(t)
    return all_route
def main():
    folder='C:\example'
    FileList = getAllFile_name(folder)
    # print FileList
    all_route = get_allfile_route(FileList)
    # print all_route
    for route in all_route:
        subprocess.Popen(r"D:\pdf2htmlEX-win32-0.14.6-with-poppler-data\pdf2htmlEX.exe "+route+" --dest-dir htmlfile",shell=True)  #无阻塞并行 .call 为等待子程序结束再进行

if __name__ == "__main__":
    main()