import sys
from PyQt5 import QtWidgets
from Wd_Angbotsvorlage import Wd_Angbotsvorlage
from UI.UI_TestMainwindow import Ui_MainWindow


class RFFE_Vorlage_Schreiber(QtWidgets.QMainWindow):

    def Angebotsvorlage(self):
        if self.ui.tp_cbox.currentText() == "Angebot-Stundenpreis":
            self.Vorlage = Wd_Angbotsvorlage()
            self.Vorlage.show()

    def __init__(self):
        super(RFFE_Vorlage_Schreiber, self).__init__()
        self.Vorlage = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ok_btn.clicked.connect(self.Angebotsvorlage)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RFFE_Vorlage_Schreiber()
    window.show()
    sys.exit(app.exec_())
