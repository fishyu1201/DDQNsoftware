import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QMessageBox
from mainwindow import Ui_MainWindow


class run_window(Ui_MainWindow):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi(mainWindow)
        self.initUI()

    def initUI(self):
        self.pushButton_1.clicked.connect(self.direct_submit)
        self.pushButton_2.clicked.connect(self.path_submit)
        self.pushButton_3.clicked.connect(self.getPath_1)
        self.pushButton_4.clicked.connect(self.getPath_2)
        self.pushButton_5.clicked.connect(self.calculate)
        self.pushButton_6.clicked.connect(self._exit)

    def direct_submit(self):
        QMessageBox.information(mainWindow, "提交成功", "成功", QMessageBox.Yes)

    def path_submit(self):
        print(self.lineEdit.text())
        if not self.lineEdit.text():
            QMessageBox.information(mainWindow, "提交失败", "请重新提交", QMessageBox.Yes)
        else:
            QMessageBox.information(mainWindow, "提交成功", "成功", QMessageBox.Yes)

    def getPath_1(self):
        dig = QFileDialog()
        dig.setFileMode(QFileDialog.AnyFile)
        dig.setNameFilter("Text Files (*.txt)")
        if dig.exec_():
            filenames = dig.selectedFiles()
            # print(filenames[0])
            self.lineEdit.setText(filenames[0])

    def getPath_2(self):
        dig = QFileDialog()
        dig.setFileMode(QFileDialog.AnyFile)
        dig.setNameFilter("Text Files (*.txt)")
        if dig.exec_():
            filenames = dig.selectedFiles()
            # print(filenames[0])
            self.lineEdit_2.setText(filenames[0])

    def calculate(self):
        if not self.lineEdit.text():
            QMessageBox.information(mainWindow, "错误", "请输入任务数据文件地址或直接提交", QMessageBox.Yes)
        elif not self.lineEdit_2.text():
            QMessageBox.information(mainWindow, "错误", "未选择路径文件存储地址", QMessageBox.Yes)
        else:
            QMessageBox.information(mainWindow, "成功", "提交成功，正在计算结果", QMessageBox.Yes)
            pass   # 此处应为提交计算，省略

    # 退出软件
    def _exit(self):
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    form = run_window(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
