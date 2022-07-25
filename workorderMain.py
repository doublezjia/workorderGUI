#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : zealous (doublezjia@163.com)
# @Date    : 2022/7/20
# @Link    : https://github.com/doublezjia
# @File    ：workorderMain.py
# @Desc    :

import sys,os,json,csv,re,requests
from datetime import date
import workorderQRC_rc
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from WorkorderGUI_ui import *

# 使用QTdesigner设计UI界面
class workorderGUI(QWidget,Ui_workorderForm):
    # csv表的标题
    csv_Headers = ('name', 'problem', 'problem_category', 'method', 'problem_status', 'add_time')
    def __init__(self):
        super(workorderGUI,self).__init__()
        # 读取workOrder.json表，获取事件总类和分类的值
        try:
            with open('./json/workOrder.json', 'r') as f:
                self.woJson = json.load(f)
        except FileNotFoundError as f:
            QMessageBox.question(self, 'Tip', 'workOrder.json文件不存在，程序关闭', QMessageBox.Ok, QMessageBox.Ok)
            sys.exit()
        # 读取ename.json表，获取工程师名
        try:
            with open('./json/ename.json', 'r') as f:
                self.enameJson = json.load(f)
        except FileNotFoundError as f:
            QMessageBox.question(self, 'Tip', 'ename.json文件不存在，程序关闭', QMessageBox.Ok, QMessageBox.Ok)
            sys.exit()
        # 读取office.json表，获取工程师名
        try:
            with open('./json/office.json', 'r') as f:
                self.officeJson = json.load(f)
        except FileNotFoundError as f:
            QMessageBox.question(self, 'Tip', 'office.json文件不存在，程序关闭', QMessageBox.Ok, QMessageBox.Ok)
            sys.exit()
        # 判断文件夹是否存在，如果不存在就新建
        if not os.path.isdir('./csv_tables'):
            os.mkdir('./csv_tables')

        # 判断是否有csv文件，没有则创建，添加表头
        if not os.path.isfile('./csv_tables/workorder.csv'):
            with open('./csv_tables/workorder.csv', 'w', newline='') as datacsv:
                csvwriter = csv.writer(datacsv, dialect=('excel'))
                csvwriter.writerow(self.csv_Headers)

        self.setupUi(self)
        self.setWindowIcon(QIcon("lion.ico"))
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        # 限制窗口大小
        self.setFixedSize(self.width(),self.height())

        # 下拉菜单显示
        self.partComboBoxText()
        self.partComboBox.currentTextChanged.connect(self.partselectComboBox_TextChanged)
        self.enameComboBoxText()
        self.officeComboBoxText()

        self.submitButton.clicked.connect(self.submitButton_Click)
        self.resetButton.clicked.connect(self.resetButton_Click)

    # 事件总类下拉列表内容添加
    def partComboBoxText(self):
        # 添加事件总类的下拉栏内容
        for item in self.woJson:
            self.partComboBox.addItem(item['name'])

        # 添加默认显示事件子类下拉栏内容
        partIndex = self.partComboBox.currentIndex()
        self.partselectComboBox.clear()
        for partselectItem in self.woJson[partIndex]['selects']:
            self.partselectComboBox.addItem(partselectItem['select_name'])

    # 工程师下拉列表内容添加
    def enameComboBoxText(self):
        for item in self.enameJson:
            self.enameComboBox.addItem(item['ename'])

    # 工作区下拉列表内容添加
    def officeComboBoxText(self):
        for item in self.officeJson:
            self.officeComboBox.addItem(item['office'])

    # 事件总类的选择事件，选择对应的内容，事件子类下拉栏内容会变
    def partselectComboBox_TextChanged(self):
        # 获取总类下拉列表的index值
        partIndex = self.partComboBox.currentIndex()
        # 清空原来下拉列表
        self.partselectComboBox.clear()
        # 添加下拉列表内容
        for item in self.woJson[partIndex]['selects']:
            self.partselectComboBox.addItem(item['select_name'])

    # 提交按钮事件
    def submitButton_Click(self):
        # 获取事件总类的index
        partIndex = self.partComboBox.currentIndex()
        # 获取事件子类的index
        partselectIndex = self.partselectComboBox.currentIndex()
        # 获取json中对应的ID值和name
        partID = self.woJson[partIndex]['id']
        partText = self.woJson[partIndex]['name']
        partselectID = self.woJson[partIndex]['selects'][partselectIndex]['id']
        # 获取事件类型的值
        eventtype = self.eventtypeComboBox.currentText().strip()
        # 获取工程师名
        ename = self.enameComboBox.currentText().strip()
        # 获取报障来源的值
        datasource = self.datasourceComboBox.currentText().strip()
        # 当前状态值
        currentstatus = self.currentstatusComboBox.currentText().strip()
        # 获取紧急程度的值
        exigencies = self.exigenciesComboBox.currentText().strip()
        # 获取处理方式的值
        handle = self.handleComboBox.currentText().strip()
        # 获取办公区的值
        office = self.officeComboBox.currentText().strip()
        # 获取工单量的值
        evennumber = self.evennumberSpinBox.value()
        # 获取邮箱地址值
        email = self.emailLineEdit.text().strip()
        # 获取工位号的值
        siteno = self.sitenoLineEdit.text().strip()
        # 获取事件标题的值
        subject = self.subjectLineEdit.text().strip()
        # 获取详细内容的值
        falut = self.falutTextEdit.toPlainText().strip()

        """使用方法QMessageBox.question()来显示消息框"""
        """参数：处于哪个控件内,消息框标题,消息内容,按钮内容,默认选择按钮"""
        if evennumber < 1:
            QMessageBox.question(self,'Tip','工单量不能小于1',QMessageBox.Ok,QMessageBox.Ok)
            self.evennumberSpinBox.setValue(1)
        # 判断邮箱是否为空
        if email == '':
            QMessageBox.question(self,'Tip','邮箱不能为空',QMessageBox.Ok,QMessageBox.Ok)
            self.emailLineEdit.setFocus()
        else:
            # 判断邮箱格式是否正确
            if not re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',email):
                QMessageBox.question(self, 'Tip', '邮箱格式不对', QMessageBox.Ok, QMessageBox.Ok)
                self.emailLineEdit.setFocus()
        # 判断工位号是否为空
        if siteno == '':
            QMessageBox.question(self, 'Tip', '工位号不能为空', QMessageBox.Ok, QMessageBox.Ok)
            self.sitenoLineEdit.setFocus()
        # 判断事件标题是否为空
        if subject == '':
            QMessageBox.question(self, 'Tip', '事件标题不能为空', QMessageBox.Ok, QMessageBox.Ok)
            self.subjectLineEdit.setFocus()
        # 判断详细内容是否为空
        if falut == '':
            QMessageBox.question(self, 'Tip', '详细描述不能为空', QMessageBox.Ok, QMessageBox.Ok)
            self.falutTextEdit.setFocus()

        # 如果各项都不为空执行操作
        if partID and partselectID and eventtype and ename and datasource and \
                currentstatus and exigencies and handle and subject and \
                evennumber and  falut and \
                re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',email) and siteno:

            csv_status = self.save_csv(name=email,problem=subject,problem_category=partText,\
                                       method=handle,problem_status=currentstatus,add_time=date.today())
            if csv_status == 1:
                QMessageBox.question(self, 'Tip', '添加成功', QMessageBox.Ok, QMessageBox.Ok)

    # 重置界面输入
    def resetButton_Click(self):
        self.partComboBox.setCurrentIndex(0)
        self.partselectComboBox.setCurrentIndex(0)
        self.eventtypeComboBox.setCurrentIndex(0)
        self.enameComboBox.setCurrentIndex(0)
        self.datasourceComboBox.setCurrentIndex(0)
        self.currentstatusComboBox.setCurrentIndex(0)
        self.exigenciesComboBox.setCurrentIndex(0)
        self.handleComboBox.setCurrentIndex(0)
        self.officeComboBox.setCurrentIndex(0)
        self.evennumberSpinBox.setValue(1)
        self.emailLineEdit.setText("")
        self.sitenoLineEdit.setText("")
        self.subjectLineEdit.setText("")
        self.falutTextEdit.setText("")

    # 保存csv
    def save_csv(self,name, problem, problem_category, method, problem_status, add_time):
        try:
            csv_data = (name, problem, problem_category, method, problem_status, add_time)
            with open('./csv_tables/workorder.csv', 'a', newline='') as datacsv:
                csvwriter = csv.writer(datacsv, dialect=('excel'))
                csvwriter.writerow(csv_data)
            return 1
        except:
            return 0

if __name__ == '__main__':
    # 初始化
    app = QApplication(sys.argv)
    # 使用ui
    ui = workorderGUI()
    ui.show()
    sys.exit(app.exec_())