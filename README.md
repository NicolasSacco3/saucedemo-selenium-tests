🧪 SauceDemo - Automatización de Pruebas con Selenium
Proyecto de testing automatizado para la web SauceDemo, cubriendo el flujo completo desde el login hasta la gestión del carrito de compras.

🛠️ Tecnologías utilizadas
HerramientaDescripciónpytestFramework de testing para PythonseleniumAutomatización del navegadorpytest-htmlGeneración de reportes HTML

📁 Estructura del proyecto
├── tests/
│   └── test_saucedemo.py
├── requirements.txt
└── README.md

⚙️ Instalación

Clonar el repositorio:

bashgit clone <url-del-repositorio>
cd <nombre-del-proyecto>

Crear un entorno virtual (opcional pero recomendado):

bashpython -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

Instalar las dependencias:

bashpip install -r requirements.txt

▶️ Ejecución de los tests
Correr todos los tests:
bashpytest tests/test_saucedemo.py -v
Generar reporte HTML:
bashpytest tests/test_saucedemo.py -v --html=report.html --self-contained-html

✅ Casos de prueba
TestDescripciónEstadotest_loginVerifica el inicio de sesión con credenciales válidas✅ PASSEDtest_catalogo_productosValida que el catálogo de productos carga correctamente✅ PASSEDtest_verificar_barra_menuComprueba la presencia y funcionamiento de la barra de menú✅ PASSEDtest_agregar_al_carritoVerifica que se pueden agregar productos al carrito✅ PASSEDtest_verificar_boton_remove_de_un_productoComprueba que el botón de eliminar un producto del carrito funciona✅ PASSED

🌐 Aplicación bajo prueba
SauceDemo es una tienda web de práctica diseñada para el testing de aplicaciones.

URL: https://www.saucedemo.com/
Usuario de prueba: standard_user
Contraseña: secret_sauce


📄 requirements.txt
pytest
selenium
pytest-html