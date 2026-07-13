import sys
from PySide6.QtWidgets import QApplication
from views import VistaProductos
from controller import ControladorProductos

def ejecutar_aplicacion():
    app = QApplication(sys.argv)
    
    vista = VistaProductos()
    
    controlador = ControladorProductos(vista)
    
    vista.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    ejecutar_aplicacion()