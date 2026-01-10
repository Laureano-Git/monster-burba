🍔MonsterBurga - Fullstack Delivery System
¡Bienvenido a MonsterBurga! Una aplicación web de delivery de hamburguesas diseñada para optimizar la toma de pedidos a través de WhatsApp. Este proyecto fue construido con un enfoque en la reactividad, el diseño moderno (Estética Neón) y la eficiencia en la comunicación entre Backend y Frontend.

🚀Características principales
Menú Dinámico: Gestión completa de productos (hamburguesas y complementos) desde un panel administrativo.

Personalización de Pedidos: Selección de tamaños (Simple, Doble, Triple), ingredientes y adicionales en tiempo real.

Checkout Reactivo: Validación instantánea de datos de envío (Nombre, Dirección) antes de habilitar la compra.

Integración con WhatsApp: Generación automática de mensajes formateados y codificados para una recepción de pedidos sin errores.

Arquitectura Limpia: Uso de variables de entorno para seguridad y modelos de datos unificados.

🛠️Tech Stack
Django	Backend y API REST (Python)
SvelteKit	Frontend Reactivo (JavaScript)
SQLite	Base de datos (Desarrollo)
CSS Custom Properties	Diseño Neón / UI / UX
dotenv	Gestión de variables de entorno y seguridad

📦 Instalación y Configuración
1. Backend (Django - en consola)
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

2. Frontend (SvelteKit - en consola)
cd frontend
npm install
npm run dev

⚙️ Variables de Entorno (.env)
Para que el proyecto funcione correctamente, debés configurar los siguientes archivos .env:

En /backend/.env:

SECRET_KEY: Tu clave secreta de Django.

DEBUG: True para desarrollo.

En /frontend/.env:

PUBLIC_API_URL: URL de tu backend (ej. http://127.0.0.1:8000/api).

PUBLIC_WHATSAPP_PHONE: El número donde se recibirán los pedidos.

👤 Autor
Massa Laureano - Desarrollador Fullstack Junior

LinkedIn - https://www.linkedin.com/in/laureanomassa/

## 🧠 Retos Técnicos y Aprendizajes

Durante el desarrollo de MonsterBurga, me enfrenté a varios desafíos que me permitieron profundizar en el stack Fullstack:

1. **Unificación de Modelos (Refactorización):** Inicialmente, el sistema separaba "Extras" y "Bebidas" en tablas distintas. Refactoricé la lógica hacia un modelo unificado de `Products` vinculado a `Categories`, lo que redujo la redundancia de código en un 40% y facilitó la escalabilidad del catálogo.
2. **Reactividad en el Pedido:** Implementé el uso de variables reactivas en SvelteKit (`$:`) para que el precio total y el mensaje de WhatsApp se actualicen instantáneamente según las opciones del usuario, mejorando la experiencia de usuario (UX).
3. **Seguridad de Datos:** Migré toda la configuración sensible (claves de API, configuración de base de datos) a variables de entorno utilizando `python-dotenv` y `$env/static/public`, asegurando que la información privada no sea expuesta en el repositorio público.
