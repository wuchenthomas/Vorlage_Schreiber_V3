import datetime
import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyPDF2 import PdfFileMerger
from py_sub_class.LaTeX_LB import LaTeX_LB
from py_sub_class.AngStdPreis import LaTeXAng_Stdpr
from UI.UI_angbotsvorlage import Ui_AngWindow
from DB_viewer import DB_viewer


def get_delayed_date(start_date, delay_day):
    try:
        start_date = datetime.datetime.strptime(start_date, "%d.%m.%Y")
        end_date = (start_date + datetime.timedelta(days=delay_day)).strftime("%d.%m.%Y")
        return end_date
    except ValueError:
        print("ValueError")


class Wd_Angbotsvorlage(Ui_AngWindow):
    def generate_AngPDF(self):
        AngInfo = {
            'Nr': self.ui.Nr_le.text(),
            'Bez': self.ui.Bez_te.toPlainText(),
            'Dat': self.ui.AnlD_de.text(),
            'StdPr': self.ui.StdPr_le.text(),
            'GesStd': self.ui.gesStd_le.text(),
            'AblDat': get_delayed_date(self.ui.AnlD_de.text(), int(self.ui.Gd_cbox.currentText()))
        }
        KdInfo = {
            'Titel': self.ui.titel_cbox.currentText(),
            'VN': self.ui.KdVN_le.text(),
            'NN': self.ui.KdNN_le.text(),
            'Geschl': self.ui.KdGeschl_cbox.currentText(),
            'FaN': self.ui.FaN_le.text(),
            'FaNErg': self.ui.FaNErg_le.text(),
            'PLZ': self.ui.PLZ_le.text(),
            'St': self.ui.St_le.text(),
            'Anschr': self.ui.Anschr_le.text()
        }
        Absender = self.ui.Abs_le.text()
        LBloc = self.ui.LBpath_le.text()
        main_dir = os.path.dirname(os.path.abspath(__file__))
        outdir = os.path.join(self.ui.out_dic_le.text(), AngInfo['Nr'])
        # outdir = os.path.join('/home/chen/PycharmProjects/Vorlage_Schreiber_V3/testfolder', AngInfo['Nr'])
        Angebot = LaTeXAng_Stdpr(root_dir=main_dir, out_dir=outdir, AngInfo=AngInfo, KdInfo=KdInfo, Absender=Absender)

        LB = LaTeX_LB(root_dir=main_dir, out_dir=outdir, AngInfo=AngInfo, LBloc=LBloc)
        try:
            Angebot.compile_PDF()
            LB.compile_PDF()
            # print(Angebot.get_pdf_loc())
            # print(LB.get_pdf_loc())
            if self.ui.onePDF_cb.isChecked():
                pdf_merge = PdfFileMerger()
                pdf_merge.append(Angebot.get_pdf_loc())
                pdf_merge.append(LB.get_pdf_loc())
                merged_pdf_loc = os.path.abspath(os.path.join(os.path.dirname(Angebot.get_pdf_loc()), "."))
                pdf_merge.write(os.path.join(merged_pdf_loc, "{}.pdf".format(AngInfo['Nr'])))
                pdf_merge.close()
            QtWidgets.QMessageBox.about(self, "Done", "PDF_Generated")

        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def select_LB(self):
        dlg = QtWidgets.QFileDialog()
        fileName = dlg.getOpenFileName(self, str("Select Leistungsbeschreibung"), "", "*")
        self.ui.LBpath_le.setText(fileName[0])

    def connect_to_DB(self):
        self.DB.show()

    def clear_all(self):
        self.ui.Nr_le.clear()
        self.ui.Bez_te.clear()
        self.ui.StdPr_le.clear()
        self.ui.Abs_le.clear()
        self.ui.KdVN_le.clear()
        self.ui.KdNN_le.clear()
        self.ui.FaN_le.clear()
        self.ui.FaNErg_le.clear()
        self.ui.Anschr_le.clear()
        self.ui.PLZ_le.clear()
        self.ui.St_le.clear()

    def test(self):
        print(self.ui.onePDF_cb.isChecked())

    def __init__(self):
        super(Wd_Angbotsvorlage, self).__init__()
        self.ui = Ui_AngWindow()
        self.ui.setupUi(self)
        self.setMouseTracking(True)
        self.DB = DB_viewer()
        self.ui.out_dic_le.setText(os.path.abspath('testfolder'))
        self.ui.PDFG_btn.clicked.connect(self.generate_AngPDF)
        self.ui.LBpathbw_btn.clicked.connect(self.select_LB)
        self.ui.AnlD_de.setDateTime(QtCore.QDateTime(
            QtCore.QDate(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day),
            QtCore.QTime(0, 0, 0)))
        self.ui.clear_btn.clicked.connect(self.clear_all)
        self.ui.DB_btn.clicked.connect(self.connect_to_DB)
        self.ui.test_btn.clicked.connect(self.test)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Wd_Angbotsvorlage()
    ui.show()
    sys.exit(app.exec_())
