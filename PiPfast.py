import subprocess
import colorama
import os
import sys
import shutil

colorama.init(autoreset=True)

# Colores
TITLE = colorama.Fore.GREEN
COMMANDS = colorama.Fore.CYAN
USER = colorama.Fore.BLUE
ERROR = colorama.Fore.RED
PIP = colorama.Fore.YELLOW
SUCCESS = colorama.Fore.LIGHTGREEN_EX

titulo = (r"""
 ____ ___ ____    _____ _    ____ _____ 
|  _ \_ _|  _ \  |  ___/ \  / ___|_   _|
| |_) | || |_) | | |_ / _ \ \___ \ | |
|  __/| ||  __/  |  _/ ___ \ ___) || |
|_|  |___|_|     |_|/_/   \_\____/ |_|
""")


def python_path():
    exe = sys.executable

    # Si no es un ejecutable Python (por ejemplo, un .exe compilado)
    if exe.endswith(".exe") and "python" not in exe.lower():
        posibles = [
            shutil.which("python"),
            shutil.which("python3"),
            r"C:\Python312\python.exe",
            r"C:\Python311\python.exe",
            r"C:\Python310\python.exe",
            r"C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe",
        ]
        for p in posibles:
            if p and os.path.exists(os.path.expandvars(p)):
                return os.path.expandvars(p)
        return "python"
    return exe

def detectar_entorno():
    print(PIP + "\n=== ESTADO DEL ENTORNO ===")

    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print(SUCCESS + f"Estás dentro de un entorno virtual: {sys.prefix}")
    else:
        print(ERROR + "No estás dentro de un entorno virtual.")

    python_exec = python_path()

    try:
        version = subprocess.run([python_exec, "--version"], capture_output=True, text=True)
        print(PIP + f"\nPython detectado: {version.stdout.strip()}")
    except Exception:
        print(ERROR + "No se pudo detectar la versión de Python.")

    print(PIP + f"Ruta del intérprete: {python_exec}\n")

#Comandos base


def comandos():
    print(COMMANDS + "\n=== OPCIONES ===")
    print(COMMANDS + "1. install (instalar paquetes)")
    print(COMMANDS + "2. show (mostrar información de paquetes)")
    print(COMMANDS + "3. uninstall (desinstalar paquetes)")
    print(COMMANDS + "4. update (actualizar pip)")
    print(COMMANDS + "5. info (detectar Python y entornos)")
    print(COMMANDS + "6. exit (salir)")

def colorear_salida(texto):
    if not texto.strip():
        print(ERROR + "No se recibió salida del comando.")
        return

    for linea in texto.splitlines():
        if "ERROR" in linea or "Exception" in linea:
            print(ERROR + linea)
        elif "WARNING" in linea or "Deprecation" in linea:
            print(colorama.Fore.MAGENTA + linea)
        elif "Successfully" in linea or "installed" in linea or "uninstalled" in linea:
            print(SUCCESS + linea)
        else:
            print(PIP + linea)

def run_command(command):
    print(PIP + f"\n>>> Ejecutando comando: {command}\n")
    try:
        process = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        colorear_salida(process.stdout)
    except Exception as e:
        print(ERROR + f"ERROR: {e}")

def limpiar():
    input(USER + "\nPresiona ENTER para limpiar la consola...")
    os.system("cls" if os.name == "nt" else "clear")


def procesar_paquetes(accion):
    paquetes = input(PIP + f"Ingrese los paquetes a {accion} (separa con comas): ").strip()
    lista = [pkg.strip() for pkg in paquetes.split(",") if pkg.strip()]

    if not lista:
        print(ERROR + "No ingresaste ningún paquete.")
        limpiar()
        return

    python_exec = python_path()
    for pkg in lista:
        print(PIP + f"\nProcesando: pip {accion} {pkg}")
        if accion == "uninstall":
            run_command(f'"{python_exec}" -m pip uninstall -y {pkg}')
        else:
            run_command(f'"{python_exec}" -m pip {accion} {pkg}')

def actualizar_pip():
    print(SUCCESS + "\nActualizando pip a la última versión...\n")
    run_command(f'"{python_path()}" -m pip install --upgrade pip')


#menu

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(TITLE + titulo)
        detectar_entorno()
        comandos()

        user = input(USER + "\nOpción: ").strip().lower()

        if user == '1':
            procesar_paquetes("install")
            limpiar()

        elif user == '2':
            procesar_paquetes("show")
            limpiar()

        elif user == '3':
            procesar_paquetes("uninstall")
            limpiar()

        elif user == '4' or user == 'update':
            actualizar_pip()
            limpiar()

        elif user == '5' or user == 'info':
            detectar_entorno()
            limpiar()

        elif user == '6' or user == 'exit':
            print(PIP + "Ejecución detenida.")
            input(TITLE + "Presiona ENTER para salir...")
            break

        else:
            print(ERROR + "Ingresa una opción válida.")
            limpiar()

if __name__ == "__main__":
    main()
