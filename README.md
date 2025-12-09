# 🧪 Framework de Automatización de Pruebas (QA)

Este proyecto es el Trabajo Final Integrador para el curso de QA Automation. Consiste en un framework robusto construido con **Python**, **Selenium** y **Pytest** para automatizar pruebas de UI (Frontend) y API (Backend).

## 🚀 Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Framework de Test:** Pytest
* **Web Automation:** Selenium WebDriver
* **API Automation:** Requests
* **Reportes:** Pytest-HTML
* **Patrón de Diseño:** Page Object Model (POM)
* **Logging:** Sistema de logs personalizado
* **Data Driven Testing:** CSV y JSON

---

## 📂 Estructura del Proyecto

El proyecto sigue una arquitectura escalable y modular:

```text
├── data/                  # Datos de prueba (CSV, JSON)
├── logs/                  # Archivos de log generados (app.log)
├── pages/                 # Page Objects (Mapeo de elementos web)
│   ├── __init__.py        # Inicializador de paquete Python
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── reports/               # Reportes HTML y Capturas de pantalla
│   └── screenshots/       # Subcarpeta para capturas de tests fallidos
├── tests/                 # Scripts de prueba (UI y API)
│   ├── __init__.py        # Inicializador de paquete Python
│   ├── test_api.py        # Pruebas de API (CRUD)
│   ├── test_cart.py       # Flujos de carrito
│   ├── test_checkout_complete.py # Flujo E2E completo
│   ├── test_inventory.py  # Pruebas de catálogo
│   ├── test_login.py      # Login parametrizado
│   └── test_products_data.py # Validación de datos vs JSON
├── utils/                 # Utilidades (Logger, Lectores de datos)
│   ├── __init__.py        # Inicializador de paquete Python
│   ├── data_login_loader.py # Lector de datos de login CSV
│   ├── lector_json.py     # Lector de datos de productos JSON
│   └── logger.py          # Configuración del Logger personalizado
├── conftest.py            # Configuración de Fixtures (Driver, Hooks)
├── run_tests.py           # Script principal de ejecución
└── requirements.txt       # Dependencias del proyecto
```

## ⚙️ Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/xPiojo/pre-entrega-automation-testing-roberto-gomez.git](https://github.com/xPiojo/pre-entrega-automation-testing-roberto-gomez.git)
    cd pre-entrega-automation-testing-roberto-gomez
    ```

2.  **Crear entorno virtual (Opcional pero recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Mac/Linux
    venv\Scripts\activate     # En Windows
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```


## ▶️ Ejecución de Pruebas (Runner Principal)

### 1. Ejecutar la Suite Completa (Método Recomendado)
Usar el script `run_tests.py` es el método principal para ejecutar todos los tests, generar el reporte HTML y mostrar los logs en tiempo real.

```bash
python run_tests.py
```
(Este comando ejecuta todos los tests UI/API y genera automáticamente el archivo report.html)

### 2. Ejecución Manual (Pytest)
Para correr solo una parte específica o un comando diferente:
```bash
pytest tests/test_login.py  # Solo tests de login
```


## 📊 Características del Framework

1.  **Page Object Model:** La lógica de interacción con la web está separada de los tests, facilitando el mantenimiento.
2.  **Capturas Automáticas:** Si un test falla, se guarda una captura de pantalla en la carpeta `reports/`.
3.  **Enlace en Reporte:** El reporte HTML incluye un enlace directo a la captura de pantalla cuando un test falla.
4.  **Logs Detallados:** Cada paso de la prueba se registra en consola y en `logs/app.log` para facilitar la depuración.
5.  **Validación de Datos:** Se comparan los precios de la web contra un archivo maestro `productos.json`.

---
**Autor:** Roberto Gomez
**Curso:** QA Automation Testing - Talento Tech