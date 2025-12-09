import pytest
import sys

def main():
    """
    Script principal de ejecución.
    Detecta y ejecuta automáticamente todos los tests del proyecto.
    """
    print("🚀 Iniciando suite de pruebas automatizadas...")
    
    # Argumentos para Pytest:
    # -v: Verbose (detallado)
    # -s: Mostrar logs en consola
    # --html: Generar el reporte visual
    args = [
        "-v", 
        "-s", 
        "--html=report.html", 
        "--self-contained-html"
    ]
    
    # Ejecutar pytest (Automáticamente busca en la carpeta actual)
    codigo_salida = pytest.main(args)
    
    # Retornar el código de salida al sistema (0 = Éxito, 1 = Fallo)
    # Esto es útil cuando lo conectas a Jenkins o GitHub Actions
    sys.exit(codigo_salida)

if __name__ == "__main__":
    main()