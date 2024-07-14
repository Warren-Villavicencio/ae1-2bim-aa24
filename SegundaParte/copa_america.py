from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class CopaAmericaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('copaamerica.ui', self)  
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        anio = self.lineEdit.text()
        sede = self.lineEdit_2.text()
        campeon = self.lineEdit_3.text()
        subcampeon = self.lineEdit_4.text()
        goleador = self.lineEdit_5.text()
        partidos_jugados = self.lineEdit_6.text()
        goles_marcados = self.lineEdit_7.text()

        print(f'Año: {anio}, Sede: {sede}, Campeón: {campeon}, Subcampeón: {subcampeon}, '
              f'Goleador: {goleador}, Partidos Jugados: {partidos_jugados}, Goles Marcados: {goles_marcados}')

if __name__ == '__main__':
    app = QApplication([])
    ex = CopaAmericaApp()
    ex.show()
    app.exec()
