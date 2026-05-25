# 🧪 SauceDemo – Automatización de Pruebas con Selenium + Pytest

Proyecto de testing automatizado sobre [SauceDemo](https://www.saucedemo.com/), una tienda web de práctica diseñada para testeo de aplicaciones. Cubre el flujo completo desde el login hasta la gestión del carrito de compras.

---

## 🛠️ Tecnologías utilizadas

| Herramienta | Descripción |
|---|---|
| Python 3.x | Lenguaje base |
| Selenium WebDriver | Automatización del navegador |
| pytest | Framework de testing |
| pytest-html | Generación de reportes HTML |

---

## 📁 Estructura del proyecto

```
saucedemo-selenium-tests/
├── tests/
│   └── test_saucedemo.py   # Casos de prueba automatizados
├── utils/                  # Funciones auxiliares (helpers)
├── assets/                 # Capturas u otros recursos
├── conftest.py             # Configuración de fixtures (driver)
├── requirements.txt        # Dependencias del proyecto
└── README.md
```

---

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/NicolasSacco3/saucedemo-selenium-tests.git
cd saucedemo-selenium-tests
```

### 2. Crear un entorno virtual (recomendado)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Requiere tener **Google Chrome** instalado. Selenium gestiona el ChromeDriver automáticamente.

---

## ▶️ Ejecución de los tests

Correr todos los tests con salida detallada:

```bash
pytest tests/test_saucedemo.py -v
```

Generar reporte HTML:

```bash
pytest tests/test_saucedemo.py -v --html=report.html --self-contained-html
```

---

## ✅ Casos de prueba

| Test | Descripción | Estado |
|---|---|---|
| `test_login` | Verifica el inicio de sesión con credenciales válidas y redirección al inventario | ✅ PASSED |
| `test_catalogo_productos` | Valida que el catálogo carga productos y que el segundo ítem es el esperado | ✅ PASSED |
| `test_verificar_barra_menu` | Comprueba que la barra lateral se abre y contiene las opciones correctas | ✅ PASSED |
| `test_agregar_al_carrito` | Verifica que se agrega un producto al carrito y que el nombre coincide | ✅ PASSED |
| `test_verificar_boton_remove_de_un_producto` | Comprueba que el botón "Remove" aparece luego de agregar un producto | ✅ PASSED |

---

## 🌐 Aplicación bajo prueba

- **URL:** https://www.saucedemo.com/
- **Usuario de prueba:** `standard_user`
- **Contraseña:** `secret_sauce`

---

## 📌 Notas

- Los reportes HTML generados por pytest están incluidos en `.gitignore` y no se versionan.
- El proyecto no implementa Page Object Model (POM); los tests interactúan directamente con el DOM. Una próxima mejora planificada es refactorizar aplicando POM para mayor mantenibilidad.

---

## 👤 Autor

**Nicolás Sacco** – QA Tester en 
[LinkedIn](https://www.linkedin.com/in/nicol%C3%A1s-sacco-35a0452a8/) · [GitHub](https://github.com/NicolasSacco3)