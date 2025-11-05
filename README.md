# 🧰 PiPfast — Gestor rápido de paquetes Python

**PiPfast** es una herramienta de línea de comandos (CLI) hecha en **Python + Colorama**, diseñada para **gestionar paquetes pip** de forma rápida, amigable y colorida.  
Permite instalar, desinstalar, mostrar información y actualizar paquetes, además de detectar entornos virtuales y versiones de Python disponibles.

---

## 🚀 Características

- 📦 **Instalación múltiple** de paquetes con un solo comando (usando comas).  
- 🔍 **Visualización de información** de paquetes (`pip show`).  
- ❌ **Desinstalación rápida** con confirmación automática (`-y`).  
- ♻️ **Actualización de pip** a la última versión.  
- 🧠 **Detección automática** de:
  - Intérprete de Python real (aun si la app está compilada en `.exe`)
  - Versión de Python instalada
  - Entorno virtual activo o no  
- 🎨 **Colores dinámicos** con `colorama` para resaltar errores, avisos y éxito.  
- 📊 **Barra de progreso** durante las operaciones de pip.  
- 🪶 Compatible con entornos **Windows, Linux y macOS**.  
- 💾 Se puede ejecutar como script `.py` o como `.exe` compilado (usando `cx_Freeze`, `PyInstaller` o `Nuitka`).

---

## ⚙️ Requisitos

- **Python 3.8 o superior**
- Paquetes:
  ```bash
  pip install colorama tqdm
