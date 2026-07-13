from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QLineEdit, QSpinBox, 
    QDoubleSpinBox, QPushButton, QTableWidget, QTableWidgetItem, 
    QVBoxLayout, QHBoxLayout, QFormLayout, QHeaderView, QAbstractItemView
)
from PySide6.QtCore import Qt

class VistaProductos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión de Productos")
        self.resize(750, 500)
        self.setMinimumSize(650, 400)
        
        self._inicializar_ui()

    def _inicializar_ui(self):
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        
        layout_principal = QHBoxLayout(widget_central)
        layout_principal.setSpacing(15) 
        layout_principal.setContentsMargins(15, 15, 15, 15) 

    
        #    ***** ZONA IZQUIERDA: FORMULARIO Y ACCIONES *****

        layout_izquierda = QVBoxLayout()
        

        layout_formulario = QFormLayout()
        layout_formulario.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        

        self.txt_id = QLineEdit()
        self.txt_id.setPlaceholderText("Autoincrementable")
        self.txt_id.setEnabled(False) 
        
        self.txt_nombre = QLineEdit()
        self.txt_nombre.setPlaceholderText("Ej: Teclado Mecánico")
        

        self.box_precio = QDoubleSpinBox()
        self.box_precio.setRange(0.00, 10000.00)
        self.box_precio.setPrefix("$ ")
        self.box_precio.setDecimals(2)
        
        self.box_stock = QSpinBox()
        self.box_stock.setRange(0, 99999)
        
        layout_formulario.addRow(QLabel("ID Producto:"), self.txt_id)
        layout_formulario.addRow(QLabel("Nombre:"), self.txt_nombre)
        layout_formulario.addRow(QLabel("Precio Unitario:"), self.box_precio)
        layout_formulario.addRow(QLabel("Stock Disponible:"), self.box_stock)
        
        layout_izquierda.addLayout(layout_formulario)
        layout_izquierda.addSpacing(10)


        self.btn_agregar = QPushButton("Agregar Producto")
        self.btn_editar = QPushButton("Modificar Seleccionado")
        self.btn_eliminar = QPushButton("Eliminar Seleccionado")
        self.btn_limpiar = QPushButton("Limpiar Campos")
        
        for btn in [self.btn_agregar, self.btn_editar, self.btn_eliminar, self.btn_limpiar]:
            btn.setFixedHeight(30)
            layout_izquierda.addWidget(btn)
            
        layout_izquierda.addStretch() 
        layout_principal.addLayout(layout_izquierda, stretch=2)


        #     ***** ZONA DERECHA: TABLA DE VISUALIZACIÓN *****

        layout_derecha = QVBoxLayout()
        
        self.tabla_productos = QTableWidget()
        self.tabla_productos.setColumnCount(4)
        self.tabla_productos.setHorizontalHeaderLabels(["ID", "Nombre del Producto", "Precio", "Stock"])
        
        self.tabla_productos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows) 
        self.tabla_productos.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection) 
        self.tabla_productos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) 
        
        header = self.tabla_productos.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents) 
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)          
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents) 
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents) 
        
        layout_derecha.addWidget(self.tabla_productos)
        layout_principal.addLayout(layout_derecha, stretch=3)