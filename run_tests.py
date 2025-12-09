import pytest
import sys

def main():
    """
    Script principal de ejecución.
    Detecta y ejecuta automáticamente todos los tests del proyecto.
    """
    print("🚀 Iniciando suite de pruebas automatizadas...")
    
    # Argumentos para Pytest (El plugin pytest-html crea la carpeta 'reports/' automáticamente)
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