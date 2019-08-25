from PyQt5 import QtWidgets,uic

import json

config = json.loads(open("store.json").read())

print(config)

app=QtWidgets.QApplication([])

dlg=uic.loadUi("firstuinew.ui")

dlg.show()

app.exec()