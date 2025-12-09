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

## 📂 Estructura del Proyecto

El proyecto sigue una arquitectura escalable y modular:

```text
├── data/                  # Datos de prueba (CSV, JSON)
├── logs/                  # Archivos de log generados (app.log)
├── pages/                 # Page Objects (Mapeo de elementos web)
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── reports/               # Reportes HTML y Capturas de pantalla
├── tests/                 # Scripts de prueba (UI y API)
│   ├── test_api.py        # Pruebas de API (CRUD)
│   ├── test_cart.py       # Flujos de carrito
│   ├── test_checkout_complete.py # Flujo E2E completo
│   ├── test_inventory.py  # Pruebas de catálogo
│   ├── test_login.py      # Login parametrizado
│   └── test_products_data.py # Validación de datos vs JSON
├── utils/                 # Utilidades (Logger, Lectores de datos)
├── conftest.py            # Configuración de Fixtures (Driver, Hooks)
└── requirements.txt       # Dependencias del proyecto
```markdown

## ⚙️ Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/proyecto-final-automation-testing.git](https://github.com/TU_USUARIO/proyecto-final-automation-testing.git)
    cd proyecto-final-automation-testing
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

## ▶️ Ejecución de Pruebas

### 1. Ejecutar todos los tests (UI + API)
Para correr la suite completa y ver los logs en vivo:
```bash
pytest -s


### 2. Generar Reporte HTML
Para generar el reporte visual con capturas de pantalla:
```bash
pytest --html=report.html --self-contained-html

