import pytest
import sys
import os

def main():
    """
    Script principal de ejecución.
    Detecta y ejecuta automáticamente todos los tests del proyecto.
    """
    print("🚀 Iniciando suite de pruebas automatizadas...")

    # asegurar que existe la carpeta reports/ (pytest-html no siempre crea carpetas anidadas)
    os.makedirs("reports", exist_ok=True)
    
    # Argumentos para Pytest
    args = [
        "-v", 
        "-s", 
        "--html=reports/report.html", 
        "--self-contained-html"
    ]
    
    # Ejecutar pytest
    codigo_salida = pytest.main(args)
    
    # Retornar el código de salida al sistema (0 = Éxito, 1 = Fallo)
    sys.exit(codigo_salida)

if __name__ == "__main__":
    main()
