from PySide2.QtWidgets import QApplication, QMessageBox, QPushButton
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QProcess
import subprocess
import autoinsertmysql

class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        qtstats = QFile("ui/main.ui")
        qtstats.open(QFile.ReadOnly)
        qtstats.close()
        self.ui=QUiLoader().load(qtstats)
        self.ui.me1.triggered.connect(lambda: self.openf("loadziduan.txt"))
        self.ui.me2.triggered.connect(lambda: self.openf("archive.txt"))
        self.ui.me3.triggered.connect(lambda: self.openf("connection_info.txt"))
        self.ui.me4.triggered.connect(lambda: self.openf("loadmain.txt"))
        self.ui.me5.triggered.connect(lambda: self.openf("automysql.txt"))
        self.ui.me6.triggered.connect(lambda: self.openf("txtt/success.txt"))
        self.ui.me7.triggered.connect(lambda: self.openf("txtt/failu.txt"))
        self.ui.dbbutton.clicked.connect(self.condb)
        self.ui.clear.clicked.connect(lambda: self.clearfi("automysql.txt"))
        self.ui.clear2.clicked.connect(lambda: self.clearfi("txtt/success.txt"))
        self.ui.clear3.clicked.connect(lambda: self.clearfi("txtt/failu.txt"))
        #开始生成1
        self.ui.sc1.clicked.connect(self.btc)
        #单选
        self.ui.xuanze1.clicked.connect(lambda: self.set_xuanze(1))
        self.ui.xuanze2.clicked.connect(lambda: self.set_xuanze(2))
        self.ui.xuanze3.clicked.connect(lambda: self.set_xuanze(3))

    xuanze=0
    succ_num=0
    faliu_nun=0
    cnt = 0
    facnt=0
    def btc(self):
        geshu=int(self.ui.n1.toPlainText())
        geshu2=int(self.ui.n2.toPlainText())+1
        self.cnt=autoinsertmysql.insert(self.xuanze, 1, geshu,geshu2,autoinsertmysql.conn)
        self.facnt=geshu2-geshu-self.cnt
        cg11="成功插入到数据库："+str(self.cnt)+"条"
        cg22="失败："+str(self.facnt)+"条"
        self.ui.cg1.setText(cg11)
        self.ui.cg2.setText(cg22)
        pass
    def set_xuanze(self, value):
        self.xuanze = value
    def clearfi(self,file_path):
        try:
            with open(file_path,"w",encoding="utf-8") as f:
                f.write("")
                QMessageBox.information(
                    self.ui,
                    '操作成功',
                    '清空成功')
        except:
            QMessageBox.critical(
                self.ui,
                '错误',
                '清空失败')
    def condb(self):
        if autoinsertmysql.code==-1:
            QMessageBox.critical(
                self.ui,
                '错误',
                '数据库连接错误，检查用户密码')
        if autoinsertmysql.code==-2:
            QMessageBox.critical(
                self.ui,
                '错误',
                '数据库选择出错！')
        if autoinsertmysql.code==2:
            self.conn = autoinsertmysql.conn
            QMessageBox.information(
                self.ui,
                '操作成功',
                '数据库选择成功')
        pass
    def openf(self, file_path):
        subprocess.run(["start", file_path], shell=True)  # 适用于 Windows

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()


