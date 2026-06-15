# 🧪 SauceDemo – Automatización de Pruebas con Selenium + Pytest

Proyecto de testing automatizado sobre [SauceDemo](https://www.saucedemo.com/), una tienda web de práctica diseñada para testeo de aplicaciones. Cubre el flujo completo desde el login hasta la confirmación de compra, implementado con el patrón **Page Object Model (POM)**.

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
├── pages/
│   ├── __init__.py
│   ├── login_page.py        # Página de login
│   ├── inventory_page.py    # Catálogo de productos
│   ├── cart_page.py         # Carrito de compras
│   └── checkout_page.py     # Flujo de checkout
├── tests/
│   ├── test_login.py        # Tests de login
│   ├── test_inventory.py    # Tests de catálogo
│   ├── test_cart.py         # Tests de carrito
│   └── test_checkout.py     # Tests de checkout
├── utils/                   # Funciones auxiliares
├── assets/                  # Capturas u otros recursos
├── conftest.py              # Configuración de fixtures (driver)
├── requirements.txt         # Dependencias del proyecto
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
pytest tests/ -v
```

Correr un archivo específico:

```bash
pytest tests/test_checkout.py -v
```

Generar reporte HTML:

```bash
pytest tests/ -v --html=report.html --self-contained-html
```

---

## ✅ Casos de prueba

### Login
| Test | Descripción | Estado |
|---|---|---|
| `test_login` | Verifica inicio de sesión con credenciales válidas y redirección al inventario | ✅ PASSED |

### Inventario
| Test | Descripción | Estado |
|---|---|---|
| `test_titulo_inventario` | Verifica que el título de la página es "Products" | ✅ PASSED |
| `test_productos_visibles` | Verifica que el catálogo carga al menos un producto | ✅ PASSED |
| `test_segundo_producto_correcto` | Verifica que el segundo producto es "Sauce Labs Bike Light" | ✅ PASSED |
| `test_agregar_producto_al_carrito` | Verifica que el badge del carrito muestra 1 al agregar un producto | ✅ PASSED |
| `test_menu_lateral` | Verifica que el menú lateral contiene las opciones esperadas | ✅ PASSED |

### Carrito
| Test | Descripción | Estado |
|---|---|---|
| `test_producto_en_carrito` | Verifica que el producto agregado aparece en el carrito | ✅ PASSED |
| `test_nombre_producto_en_carrito` | Verifica que el nombre del producto en el carrito es el correcto | ✅ PASSED |
| `test_eliminar_producto_del_carrito` | Verifica que al eliminar un producto el carrito queda vacío | ✅ PASSED |
| `test_boton_remove_visible` | Verifica que el botón Remove es visible para el producto en el carrito | ✅ PASSED |
| `test_continuar_comprando` | Verifica que "Continue Shopping" redirige al inventario | ✅ PASSED |

### Checkout
| Test | Descripción | Estado |
|---|---|---|
| `test_checkout_campos_vacios` | Verifica que se muestra error al continuar sin completar datos | ✅ PASSED |
| `test_checkout_sin_apellido` | Verifica que se muestra error si falta el apellido | ✅ PASSED |
| `test_checkout_sin_codigo_postal` | Verifica que se muestra error si falta el código postal | ✅ PASSED |
| `test_checkout_resumen_producto` | Verifica que el producto aparece en el resumen de la orden | ✅ PASSED |
| `test_checkout_flujo_completo` | Verifica el flujo completo de compra hasta la confirmación | ✅ PASSED |

---

## 🏗️ Patrón Page Object Model (POM)

El proyecto está estructurado siguiendo el patrón **Page Object Model**, separando la lógica de interacción con el navegador de los casos de prueba.

Cada página de la aplicación tiene su propia clase en la carpeta `pages/`, con:
- **Locators** definidos como atributos de clase
- **Métodos** que encapsulan las acciones sobre la página
- **WebDriverWait** para esperas explícitas en cada interacción

Esto permite que si cambia un selector en la UI, el cambio se hace en un solo lugar y no en cada test.

---

## 🌐 Aplicación bajo prueba

- **URL:** https://www.saucedemo.com/
- **Usuario de prueba:** `standard_user`
- **Contraseña:** `secret_sauce`

---

## 📌 Notas

- Los reportes HTML generados por pytest están incluidos en `.gitignore` y no se versionan.
- Los archivos `__pycache__` están excluidos del repositorio via `.gitignore`.

---

## 👤 Autor

**Nicolás Sacco** – QA Tester 
[LinkedIn](https://linkedin.com/in/nicolas-sacco-35a0452a8) · [GitHub](https://github.com/NicolasSacco3)