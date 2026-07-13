#--S12-TRABAJO-PR-CTICO-EXPERIMENTAL_4 -- SISTEMA DE GESTIÓN DE PRODUCTOS
# Sistema de Gestión de Productos (Desktop App)

Aplicación de escritorio multiplataforma desarrollada en **Python** utilizando el framework gráfico **Qt (PySide6)** y el motor de base de datos relacional embebido **SQLite**. El sistema implementa una arquitectura modular con separación estricta de responsabilidades (GUI, Controlador y Persistencia) y seguridad integrada mediante consultas SQL parametrizadas.

---

## 🛠️ Requisitos Previos (Común para todos los OS)
Asegúrese de tener instalado **Python 3.10** o superior en el equipo antes de proceder. No se requiere instalar ningún motor de bases de datos externo (como MySQL o PostgreSQL), ya que SQLite se incluye de manera nativa en la librería estándar de Python.

---

## 🚀 Instrucciones de Despliegue por Sistema Operativo

Siga los comandos correspondientes en la terminal o consola de comandos de su sistema operativo para inicializar el entorno virtual, instalar las dependencias locales y ejecutar la aplicación de forma aislada.

### 🍏 1. Cómo usar en macOS

Abra la aplicación **Terminal**, navegue hasta la raíz de la carpeta del proyecto y ejecute de forma secuencial:

```bash
# 1. Crear el entorno virtual aislado
python3 -m venv env

# 2. Activar el entorno virtual en macOS
source env/bin/activate

# 3. Instalar la dependencia oficial de Qt para Python
pip install PySide6

# 4. Lanzar la aplicación gráfica
python main.py
