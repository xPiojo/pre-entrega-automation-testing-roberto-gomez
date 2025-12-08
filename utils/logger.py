import logging
import pathlib
import sys  # <--- Necesario para imprimir en consola

# Definir el directorio de logs
audit_dir = pathlib.Path("logs")
audit_dir.mkdir(exist_ok=True)
log_file = audit_dir / "app.log"

# Configurar el logger
logger = logging.getLogger("TalentoTech")
logger.setLevel(logging.INFO)

if not logger.handlers:
    # 1. Manejador de Archivo (Guarda en logs/app.log)
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 2. Manejador de Consola (Muestra en Terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)