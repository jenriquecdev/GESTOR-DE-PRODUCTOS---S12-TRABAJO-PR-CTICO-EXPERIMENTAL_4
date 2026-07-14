#S15-COMPONENTE PRACTICO_2 -- SISTEMA DE GESTIÓN DE PRODUCTOS
# Sistema de Gestión de Productos (Desktop App)

Aplicación de escritorio multiplataforma desarrollada en **Python** utilizando el framework gráfico **Qt (PySide6)** y el motor de base de datos relacional embebido **SQLite**. El sistema implementa una arquitectura modular con separación estricta de responsabilidades (GUI, Controlador y Persistencia) y seguridad integrada mediante consultas SQL parametrizadas.

---

## 🛠️ Requisitos Previos (Común para todos los OS)
Asegúrese de tener instalado **Python 3.10** o superior en el equipo antes de proceder. No se requiere instalar ningún motor de bases de datos externo (como MySQL o PostgreSQL), ya que SQLite se incluye de manera nativa en la librería estándar de Python.

---

## Instrucciones de Despliegue por Sistema Operativo

Siga los comandos correspondientes en la terminal o consola de comandos de su sistema operativo para inicializar el entorno virtual, instalar las dependencias locales y ejecutar la aplicación de forma aislada.

### 1. Cómo usar en macOS

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
```

### 2. Cómo usar en Windows

Abra la consola de comandos (Símbolo del sistema / CMD o PowerShell), navegue hasta la carpeta del proyecto y ejecute de forma secuencial:

```bash
:: 1. Crear el entorno virtual nativo
python -m venv env

:: 2. Activar el entorno virtual en Windows
env\Scripts\activate

:: 3. Instalar la dependencia oficial de Qt para Python
pip install PySide6

:: 4. Lanzar la aplicación gráfica
python main.py
```


### 3. Cómo usar en Linux (Ubuntu/Debian/Fedora)

Abra su terminal, posiciónese en el directorio del proyecto y ejecute de forma secuencial:

```bash
# 1. Crear el entorno virtual
python3 -m venv env

# 2. Activar el entorno virtual
source env/bin/activate

# 3. Instalar la dependencia oficial de Qt para Python
pip install PySide6

# 4. Lanzar la aplicación gráfica
python main.py
```
## Estructura Arquitectónica del Proyecto

El código fuente ha sido modularizado siguiendo buenas prácticas de ingeniería de software para evitar dependencias cruzadas y garantizar la mantenibilidad del sistema:

*   **`database.py` (Capa de Persistencia):** Gestiona de forma exclusiva la conexión e inicialización de la tabla en el motor SQLite. Implementa los métodos del ciclo CRUD empleando sentencias SQL parametrizadas, garantizando la seguridad del sistema al mitigar ataques por inyección de código.
*   **`views.py` (Capa de Interfaz Gráfica):** Declara la totalidad de los componentes visuales de Qt (`QLineEdit`, `QTableWidget`, `QSpinBox`) y los organiza mediante layouts dinámicos elásticos. Mantiene un diseño limpio libre de lógica de negocio o consultas de datos.
*   **`controller.py` (Capa Lógica / Mediador):** Actúa como el cerebro e intermediario de la aplicación. Intercepta los eventos de la interfaz gráfica a través del mecanismo de señales y slots, ejecuta las validaciones críticas de tipos de datos, interactúa con las funciones de persistencia y actualiza la pantalla dinámicamente.
*   **`main.py` (Punto de Entrada):** Inicializa la instancia principal de `QApplication`, vincula de forma segura los componentes del controlador con la vista y arranca el ciclo de ejecución de la aplicación de escritorio.



