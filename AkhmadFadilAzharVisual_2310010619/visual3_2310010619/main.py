import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from users import users
from dzikirplaylist import dzikirplaylist
from zikircounter import zikircounter
from paymenttype import paymenttype
from shadaqahhistory import shadaqahhistory

class halamanUtama(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        fileformutama = QFile("main.ui")
        fileformutama.open(QFile.ReadOnly)
        formloader = QUiLoader()
        self.formutama = formloader.load(fileformutama,self)

        self.setMenuBar(self.formutama.menuBar())
        self.resize(self.formutama.size())

        self.formutama.actionUsers.triggered.connect(self.bukausers)
        self.formutama.actionDzikirPlaylist.triggered.connect(self.bukadzikirplaylist)
        self.formutama.actionZikirCounter.triggered.connect(self.bukazikircounter)
        self.formutama.actionPaymentType.triggered.connect(self.bukapaymenttype)
        self.formutama.actionShadaqahHistory.triggered.connect(self.bukashadaqahhistory)

    def bukausers(self):
        self.formusers = users()
        self.formusers.show()

    def bukadzikirplaylist(self):
        self.formdzikirplaylist = dzikirplaylist()
        self.formdzikirplaylist.show()

    def bukazikircounter(self):
        self.formzikircounter = zikircounter()
        self.formzikircounter.show()

    def bukapaymenttype(self):
        self.formpaymenttype = paymenttype()
        self.formpaymenttype.show()

    def bukashadaqahhistory(self):
        self.formshadaqahhistory = shadaqahhistory()
        self.formshadaqahhistory.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = halamanUtama()
    widget.show()
    sys.exit(app.exec())
