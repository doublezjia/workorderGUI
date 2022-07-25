# workorderGUI
工单记录工具

### 文件说明
通过python3.7+pyside2设计工单记录工具界面

>workorderMain.py 主程序

>WorkorderGUI Qtdesigner设计的界面

>json文件夹 保存界面部分下拉菜单的选项的json文件，如果没有几个文件，程序打不开

生成exe用`pyinstaller -F -w -i lion.icon workorderMain.py`

记录的文件保存到`csv_tables`文件夹中的csv表，如果没有这个会自动创建

打开时候会检查json文件夹中对应的几个json文件是否存在，不存在就不能打开