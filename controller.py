from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt
import database

class ControladorProductos:
    def __init__(self, vista):
        self.vista = vista
        
        database.inicializar_base_datos()
        
        self._conectar_eventos()
        
        self.actualizar_tabla()

    def _conectar_eventos(self):

        self.vista.btn_agregar.clicked.connect(self.registrar_producto)
        self.vista.btn_editar.clicked.connect(self.modificar_producto)
        self.vista.btn_eliminar.clicked.connect(self.remover_producto)
        self.vista.btn_limpiar.clicked.connect(self.limpiar_formulario)
        
        self.vista.tabla_productos.itemSelectionChanged.connect(self.cargar_producto_seleccionado)

    #             ***** LÓGICA DEL SISTEMA *****
  

    def actualizar_tabla(self):

        self.vista.tabla_productos.itemSelectionChanged.disconnect()
        
        self.vista.tabla_productos.setRowCount(0)
        
        lista_productos = database.leer_productos()
        
        for fila_index, datos in enumerate(lista_productos):
            self.vista.tabla_productos.insertRow(fila_index)
            id_p, nombre, precio, stock = datos
            
            item_id = QTableWidgetItem(str(id_p))
            item_id.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            item_nombre = QTableWidgetItem(nombre)
            
            item_precio = QTableWidgetItem(f"$ {precio:.2f}")
            item_precio.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter) 
            item_stock = QTableWidgetItem(str(stock))
            item_stock.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            self.vista.tabla_productos.setItem(fila_index, 0, item_id)
            self.vista.tabla_productos.setItem(fila_index, 1, item_nombre)
            self.vista.tabla_productos.setItem(fila_index, 2, item_precio)
            self.vista.tabla_productos.setItem(fila_index, 3, item_stock)
            
        self.vista.tabla_productos.itemSelectionChanged.connect(self.cargar_producto_seleccionado)

    def registrar_producto(self):
        nombre = self.vista.txt_nombre.text().strip()
        precio = self.vista.box_precio.value()
        stock = self.vista.box_stock.value()
        
        if not nombre:
            QMessageBox.warning(self.vista, "Campo Requerido", "El campo 'Nombre' no puede estar vacío.")
            return
            
        if precio <= 0:
            QMessageBox.warning(self.vista, "Validación de Datos", "El precio del producto debe ser mayor a cero.")
            return

        exito = database.crear_producto(nombre, precio, stock)
        if exito:
            QMessageBox.information(self.vista, "Éxito", "Producto agregado correctamente.")
            self.limpiar_formulario()
            self.actualizar_tabla()
        else:
            QMessageBox.critical(self.vista, "Error", "No se pudo registrar el producto en el sistema.")

    def cargar_producto_seleccionado(self):
        items_seleccionados = self.vista.tabla_productos.selectedItems()
        if not items_seleccionados:
            return
            
        id_p = items_seleccionados[0].text()
        nombre = items_seleccionados[1].text()
        precio_str = items_seleccionados[2].text().replace("$ ", "")
        stock = items_seleccionados[3].text()
        
        self.vista.txt_id.setText(id_p)
        self.vista.txt_nombre.setText(nombre)
        self.vista.box_precio.setValue(float(precio_str))
        self.vista.box_stock.setValue(int(stock))

    def modificar_producto(self):
        id_str = self.vista.txt_id.text()
        if not id_str:
            QMessageBox.warning(self.vista, "Selección Requerida", "Por favor, seleccione un producto de la tabla para modificar.")
            return
            
        id_producto = int(id_str)
        nombre = self.vista.txt_nombre.text().strip()
        precio = self.vista.box_precio.value()
        stock = self.vista.box_stock.value()
        
        if not nombre:
            QMessageBox.warning(self.vista, "Campo Requerido", "El campo 'Nombre' no puede quedarse vacío.")
            return
            
        if database.actualizar_producto(id_producto, nombre, precio, stock):
            QMessageBox.information(self.vista, "Éxito", "Producto modificado con éxito.")
            self.limpiar_formulario()
            self.actualizar_tabla()
        else:
            QMessageBox.critical(self.vista, "Error", "No se pudo actualizar el registro.")

    def remover_producto(self):
        id_str = self.vista.txt_id.text()
        if not id_str:
            QMessageBox.warning(self.vista, "Selección Requerida", "Debe seleccionar un producto de la tabla para eliminarlo.")
            return
            
        id_producto = int(id_str)
        nombre_producto = self.vista.txt_nombre.text()
        
        confirmacion = QMessageBox.question(
            self.vista, 
            "Confirmar Eliminación", 
            f"¿Está seguro de que desea eliminar permanentemente el producto:\n\"{nombre_producto}\"?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if confirmacion == QMessageBox.StandardButton.Yes:
            if database.eliminar_producto(id_producto):
                QMessageBox.information(self.vista, "Éxito", "Producto removido de la base de datos.")
                self.limpiar_formulario()
                self.actualizar_tabla()
            else:
                QMessageBox.critical(self.vista, "Error", "No se pudo completar la eliminación.")

    def limpiar_formulario(self):
        self.vista.txt_id.clear()
        self.vista.txt_nombre.clear()
        self.vista.box_precio.setValue(0.00)
        self.vista.box_stock.setValue(0)
        self.vista.tabla_productos.clearSelection()