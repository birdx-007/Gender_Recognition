# This Python file uses the following encoding: utf-8
from dataloader import Loader
from sklearn.linear_model import LogisticRegression
from PIL import Image
import numpy as np
import re, random
import os, sys
import threading, time
import joblib
from ui_window import Ui_Form
from ui_traindlg import Ui_traindlg
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QGraphicsScene, QGraphicsPixmapItem
from PySide2.QtCore import Slot, QFile, QIODevice, QThread, Signal
from PySide2.QtGui import QPainter, QImage, QPixmap


class TrainDlg(QDialog):
    class BackendThread_Train(QThread):
        signal = Signal(int)

        def run(self):
            try:
                if not os.path.exists("BLR.model"):
                    self.signal.emit(-1)
                    # 加载数据
                    dataLoader = Loader()
                    dataLoader.LoadData()
                    # 获取训练、验证和测试数据并转换为与sklearn接口匹配的模式
                    train_images = []
                    train_labels = []
                    validation_images = []
                    validation_labels = []
                    test_images = []
                    test_labels = []
                    train_dataset=dataLoader.getTrainData()
                    validation_dataset=dataLoader.getValidationData()
                    test_dataset=dataLoader.getTestData()
                    ex="([a-z]*)_[0-9]*"
                    for key in train_dataset:
                        label=re.findall(ex,key)[0]# 'male'/'female'
                        image=train_dataset[key]
                        train_images.append(image)
                        train_labels.append(label)
                    for key in validation_dataset:
                        label=re.findall(ex,key)[0]# 'male'/'female'
                        image=validation_dataset[key]
                        validation_images.append(image)
                        validation_labels.append(label)
                    for key in test_dataset:
                        label=re.findall(ex,key)[0]# 'male'/'female'
                        image=test_dataset[key]
                        test_images.append(image)
                        test_labels.append(label)
                    c = 1000 # LogisticRegression的正则化参数
                    best_lr = None
                    error_rate_min = 1
                    counter = 0
                    self.signal.emit(counter)
                    while c > 0.01: # 通过循环尝试不同的超参数，自动找到较优的超参数
                        #参数详见 https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
                        lr = LogisticRegression(penalty='l1',C=c,multi_class='ovr', solver='liblinear')# 初始化逻辑回归类对象
                        lr.fit(train_images, train_labels)# 使用训练集训练
                        error_rate = 1 - lr.score(validation_images, validation_labels)# 使用验证集预测
                        # print('Validation error rate:', error_rate,' with c =',c)
                        if error_rate < error_rate_min:# 保存较优的模型
                            error_rate_min = error_rate
                            best_lr = lr
                        c = c / 2
                        counter += 1
                        self.signal.emit(counter)
                    joblib.dump(filename='BLR.model',value=best_lr)
                self.signal.emit(18)
            except IndexError:
                self.signal.emit(114514)

    def __init__(self):
        super(TrainDlg, self).__init__()
        self.ui = Ui_traindlg()
        self.ui.setupUi(self)
        self.ui.BeginButton.clicked.connect(self.getmodel)
        self.backend = self.BackendThread_Train()
        self.backend.signal.connect(self.handleDisplay)

    @Slot()
    def getmodel(self):
        self.backend.start()

    def handleDisplay(self,val):
        if val == -1:
            self.ui.BeginButton.setText('Training...')
            self.ui.BeginButton.setEnabled(False)
            self.ui.progresslabel.setText('Loading Data')
        if val >= 0 and val <= 17:
            text0 = 'Training ' + str(val) + '/17'
            self.ui.progresslabel.setText(text0)
        if val == 18:
            self.ui.progresslabel.setText('Complete')
            self.ui.BeginButton.setText('Begin!')
            self.ui.BeginButton.setEnabled(True)
            self.ui.BeginButton.clicked.connect(self.accept)
        if val == 114514:
            self.ui.progresslabel.setText('IndexError')
            self.ui.BeginButton.setText('Please Restart')


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.RandomButton.clicked.connect(self.randomphoto)
        self.ui.PredictButton.clicked.connect(self.predict)
        self.traindlg = TrainDlg()
        self.scene = QGraphicsScene()
        # self.scene.addText("Hello, world!")
        self.ui.graphicsView.setScene(self.scene)
        self.bestlr = None
        self.img = None

        male_label = open('./male_names.txt', 'r')
        female_label = open('./female_names.txt', 'r')
        self.male_list = male_label.read().splitlines()
        self.female_list = female_label.read().splitlines()
        self.ex = re.compile("([A-Za-z_-]*)_[0-9]*.jpg")
        self.size = len(self.male_list) + len(self.female_list)

        self.show()
        self.traindlg.show()

    def closeEvent(self, event):
        self.traindlg.done(0)

    @Slot()
    def randomphoto(self):
        index = random.randint(0,self.size-1)
        if index <= len(self.male_list)-1:
            self.imglabel = "male"
            self.imgname = self.male_list[index]
        else:
            self.imglabel = "female"
            self.imgname = self.female_list[index-len(self.male_list)]
        self.dirname = self.ex.findall(self.imgname)[0]
        self.picpath = './lfw image data/' + self.dirname + '/' + self.imgname
        self.img = Image.open(self.picpath)
        qimg = QImage(self.picpath)
        pixmap = QPixmap.fromImage(qimg)
        item = QGraphicsPixmapItem(pixmap)
        item.setScale(1.75)
        self.scene.addItem(item)
        # self.ui.label.setText(self.dirname)

    @Slot()
    def predict(self):
        if (not os.path.exists("BLR.model")) or self.img == None:
            self.ui.PredictButton.setText('x_x')
        else:
            self.ui.PredictButton.setText('Predict')
            if self.bestlr == None:
                self.bestlr = joblib.load(filename = "BLR.model")
            imggray = self.img.convert('L')
            smallimggray = imggray.resize((100,100))
            picarray = np.array(smallimggray).flatten() / 255.0
            self.predictlabel = self.bestlr.predict([picarray])[0]
            if self.predictlabel == self.imglabel:
                self.result = self.predictlabel + ' √'
            else:
                self.result = self.predictlabel + ' ×'
            self.ui.label.setText(self.result)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWidget()
    sys.exit(app.exec_())
