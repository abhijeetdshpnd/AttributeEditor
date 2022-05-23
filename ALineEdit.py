
from Qt import QtWidgets , QtCore , QtGui 
import sys
test_dict = {"test":"test01", "test02": "test", "test03":50 , "test04":[1,2,3,4]}
class ALineEdit(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ALineEdit, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout()
        self.name = QtWidgets.QLabel("name")
        self.value = QtWidgets.QLineEdit()
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.value)
        self.setLayout(self.layout)
    
    def set_name(self, name):
        self.name.setText(name)
    
    def set_value(self, value):
        self.value.setText(value)
        
    def get_value(self):
        return self.value.text()
    
    def get_name(self):
        return self.name.text()

class AttrWidget(QtWidgets.QWidget):
    def __init__(self):
        super(AttrWidget, self).__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        self.attr_widget = {}
        # self.create_attrs(test_dict)

    def create_attrs(self, attr_dict):
        for key, value in attr_dict.items():
            print(key, value)
            self.attr_widget['key']  = ALineEdit()
            self.attr_widget['key'].set_name(key)
            self.attr_widget['key'].set_value(str(value))
            self.layout.addWidget(self.attr_widget['key'])

class MainUi(QtWidgets.QMainWindow):
  def __init__(self):
    super(MainUi, self).__init__()
    self.setWindowTitle("Attr Widget")
    self.attr_widget = AttrWidget()
    self.setCentralWidget(self.attr_widget)
    self.attr_widget.create_attrs(test_dict)


def main():
  app = QtWidgets.QApplication(sys.argv)
  win = MainUi()
  win.show()
  app.exec_()

main()