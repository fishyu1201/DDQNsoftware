import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QMessageBox
from mainwindow import Ui_MainWindow


class run_window(Ui_MainWindow):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi(mainWindow)
        self.initUI()

    def initUI(self):
        # 函数功能与组件绑定
        self.pushButton.clicked.connect(self.direct_submit)
        self.pushButton_2.clicked.connect(self.path_submit)
        self.pushButton_3.clicked.connect(self.import_path)
        self.pushButton_4.clicked.connect(self.save_path)
        self.pushButton_5.clicked.connect(self.calculate)
        self.pushButton_6.clicked.connect(self.exit_software)

    def direct_submit(self):
        # 获取软件所在目录
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # 拼接文件路径
        file_path = os.path.join(current_directory, "input.txt")
        # 判断文件是否存在
        if os.path.exists(file_path):
            # 返回文件的绝对路径
            self.lineEdit.setText(os.path.abspath(file_path))
            QMessageBox.information(mainWindow, "提交成功", "文件已导入", QMessageBox.Yes)
        else:
            # 返回错误提示
            QMessageBox.information(mainWindow, "提交失败", "请确认文件是否存在", QMessageBox.Yes)

    def path_submit(self):
        if self.lineEdit.text() and os.path.basename(self.lineEdit.text()) == "input.txt":
            QMessageBox.information(mainWindow, "提交成功", "文件已导入", QMessageBox.Yes)
        else:
            QMessageBox.information(mainWindow, "提交失败", "请重新提交", QMessageBox.Yes)

    def import_path(self):
        # 获取导入文件路径
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Text Files (*.txt)")  # 文件类型特定为.txt
        if file_dialog.exec_():
            filenames = file_dialog.selectedFiles()
            # print(filenames[0])
            self.lineEdit.setText(filenames[0])

    def save_path(self):
        # 获取保存文件路径
        file_dialog = QFileDialog()

        # 设置对话框标题和默认目录
        file_dialog.setWindowTitle("选择文件夹")
        file_dialog.setDirectory("/path/to/default/directory")

        # 打开文件夹选择对话框并获取用户选择的文件夹路径
        folder_path = file_dialog.getExistingDirectory()
        self.lineEdit_2.setText(folder_path)
        app.exec_()

    def calculate(self):
        # 判断文件读取、保存路径是否正常，传入参数进行计算
        if not self.lineEdit.text():
            QMessageBox.information(mainWindow, "错误", "请传入初始参数文件", QMessageBox.Yes)
        elif not self.lineEdit_2.text():
            QMessageBox.information(mainWindow, "错误", "未选择路径文件存储地址", QMessageBox.Yes)
        else:
            QMessageBox.information(mainWindow, "成功", "提交成功，正在计算结果", QMessageBox.Yes)
            # 以下为需要传入的参数
            # self.checkBox.isChecked()
            # self.checkBox_2.isChecked()
            # self.checkBox_3.isChecked()
            # self.checkBox_4.isChecked()
            # self.checkBox_5.isChecked()
            # self.lineEdit.text()
            # self.lineEdit_2.text()
            pass  # 此处应为传参至算法 暂时省略

    @staticmethod
    def exit_software():
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    form = run_window(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
