import logging
import pathlib

# Definir el directorio de logs
audit_dir = pathlib.Path("logs")

# Crear el directorio de logs si no existe
audit_dir.mkdir(exist_ok=True)

# Definir la ruta del archivo de log
log_file = audit_dir / "app.log"

# Configurar el manejador de archivo para el logger
logger = logging.getLogger("TalentoTech")
logger.setLevel(logging.INFO)

if not logger.handlers:
    # Configurar el manejador de archivo para el logger
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)