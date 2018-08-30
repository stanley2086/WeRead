#coding: utf-8
import subprocess


def status():
	process = subprocess.Popen('cd F:\\Git\\WeRead\\',shell=True)
    archiveCmd = 'git status'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("查看工作区状态错误")
    else:
        print('add')
        add()

def add():
    archiveCmd = 'git add --all'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print( "添加到缓存区错误")
    else:
        print('commit')
        commit()

#提交本地版本库

def commit():
    inputNote = input("请输入提交内容:").decode('utf-8')
    archiveCmd = "git commit -m ' " + inputNote + "'"
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("提交失败")
    else:
        print("提交成功",inputNote)
        pull()

#拉取

def pull():
    archiveCmd = 'git pull'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("拉取远程代码失败")
    else:
        push()

#推送

def push():
    archiveCmd = 'git push'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("上传远程git服务器失败")
    else:
        print("上传成功")

#执行一哈

def main():
    status()

if __name__ == '__main__':
    main()

