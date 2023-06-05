"""
Identifique qué paquetes se descargan automáticamente. Investigue la utilidad que tienen estos
paquetes.
Los paquetes que se descargan  automáticamente al momento de crear el servidor Django son:
django: El propio paquete de Django.
    __init__.py: Es un archivo vacío que se utiliza para indicar a Python que un directorio debe ser considerado un paquete. Su presencia en un directorio indica que el directorio es un paquete de Python y puede contener otros módulos o subpaquetes.

    asgi.py: Este archivo es el punto de entrada para la configuración del servidor web utilizando ASGI (Asynchronous Server Gateway Interface). ASGI es una especificación para construir aplicaciones web en Python que pueden manejar conexiones asíncronas. El archivo asgi.py define la aplicación ASGI para ejecutar el proyecto Django.

    settings.py: Este archivo contiene la configuración principal del proyecto Django. Aquí se definen diversas opciones de configuración, como la base de datos a utilizar, la configuración de internacionalización y la configuración de aplicaciones instaladas. Es un archivo importante donde se especifican las variables y ajustes clave para el proyecto.

    urls.py: define las rutas (URLs) disponibles en el proyecto Django. Contiene un mapeo entre las URLs y las vistas que manejan esas URLs. Aquí se define cómo se debe manejar cada solicitud entrante en la aplicación web, y se asigna a una vista específica que generará la respuesta correspondiente.

    wsgi.py: es el punto de entrada para la configuración del servidor web utilizando WSGI (Web Server Gateway Interface). WSGI es una especificación que define cómo los servidores web pueden comunicarse con aplicaciones web escritas en Python. El archivo wsgi.py define la aplicación WSGI para ejecutar el proyecto Django.

Estos archivos son parte integral de un proyecto Django y se utilizan para estructurar y configurar la aplicación web.    
   Además nos encontramos con:

   * pytz: Biblioteca para el manejo de zonas horarias en Python.
   * sqlparse: Herramienta para analizar y formatear consultas SQL en Python.
   * setuptools: Biblioteca que facilita la distribución de paquetes Python.
   * wheel: Herramienta para construir y distribuir paquetes Python precompilados.
   * asgiref: Biblioteca de referencia para la capa ASGI (Asynchronous Server Gateway Interface).
   * pytzdata: Datos actualizados de zonas horarias utilizados por pytz.
   * typing-extensions: Extensiones de tipado para Python.
   * sqlparse: Analizador de consultas SQL en Python.

¿Qué facilidades nos proporciona Django?

Django proporciona una amplia gama de facilidades y características que hacen que el desarrollo de aplicaciones web 
sea más rápido, eficiente y seguro. Algunas de las principales facilidades que Django ofrece son:

1. Administrador de Django: Django incluye un administrador web preconstruido y altamente personalizable que 
proporciona una interfaz de administración para gestionar fácilmente los modelos de datos de la aplicación. 
Esto permite crear, leer, actualizar y eliminar registros de la base de datos sin tener que escribir código adicional.

2. Mapeo Objeto-Relacional (ORM): Django utiliza su ORM incorporado para manejar la interacción con la base de datos.
   Proporciona una abstracción de alto nivel que permite a los desarrolladores trabajar con la base de datos 
   utilizando objetos y métodos en lugar de escribir consultas SQL directamente. El ORM de Django maneja la 
   generación de consultas SQL y el mapeo entre los modelos de datos y las tablas de la base de datos.
   
3. Rutas y vistas: Django proporciona un sistema de enrutamiento fácil de usar que mapea las URL de la aplicación 
a las vistas correspondientes. Esto permite definir patrones de URL y asociarlos con funciones o clases de vista que
generan la respuesta HTTP adecuada. Además, Django incluye utilidades para procesar parámetros de URL y generar 
enlaces inversos.

4. Plantillas: Django cuenta con un poderoso motor de plantillas que permite separar la lógica de presentación del 
código. Las plantillas de Django permiten incrustar lógica dinámica en HTML y generar contenido dinámico de manera 
sencilla. Además, ofrecen características avanzadas como herencia de plantillas, etiquetas y filtros personalizados,
y procesamiento de formularios.

5. Seguridad: Django se preocupa por la seguridad y proporciona muchas facilidades para ayudar a los desarrolladores 
a proteger sus aplicaciones web. Incluye funciones de protección contra ataques comunes como Cross-Site Scripting 
(XSS), Cross-Site Request Forgery (CSRF) y SQL injection. Además, ofrece mecanismos para autenticación de usuarios, 
autorización basada en roles y gestión de contraseñas seguras.

6. Internacionalización y localización: Django proporciona soporte completo para la internacionalización y localización 
de aplicaciones web. Permite traducir automáticamente los textos de la interfaz de usuario, formatear fechas y 
números según las preferencias locales, y manejar diferentes zonas horarias.

7. Testing y depuración: Django facilita la realización de pruebas unitarias y funcionales para garantizar la 
calidad del código. Proporciona herramientas para escribir pruebas y realizar pruebas automatizadas. Además, ofrece 
capacidades de depuración, registro de eventos y seguimiento de errores para facilitar la identificación y solución 
de problemas.

Esto entre otras muchas facilidades que Django ofrece a los desarrolladores.

Con relación al levantamiento de un servidor. ¿Existe una forma de realizarlo con Python y sin Django?

Sí existe una forma de levantar un servidor utilizando Python y sin usar Django.Ya que Python proporciona varias
bibliotecas y herramientas que permiten crear y gestionar servidores web.

¿Qué desventajas nos trae este tipo de proyectos sin Django?
Entre las desventajas que nos trae este tipo de proyectos sin Django, están:
1. Complejidad y trabajo adicional: es necesario realizar más trabajo manual para configurar y gestionar el servidor.
Implemenetar rutamiento, manejo de formularios, autenticación y autorización, entre otros. 
Esto puede llevar más tiempo y requerir un conocimiento más profundo de los detalles técnicos y las mejores 
prácticas de desarrollo web.

2. Reinvención de la rueda: Django proporciona una amplia gama de características y herramientas listas para usar 
que han sido probadas y optimizadas por la comunidad. Al desarrollar sin Django, es posible que se deba implementar 
manualmente funcionalidades que Django ya proporciona, lo que implica más tiempo y esfuerzo. 
Además, es posible que no se obtenga todas las ventajas de seguridad y rendimiento que Django ofrece de manera 
predeterminada.

3. Escalabilidad y mantenimiento: Django se ha diseñado para ser escalable y mantener aplicaciones web a largo plazo. 
Proporciona estructuras y patrones bien establecidos para el desarrollo y la organización del código. Sin Django, es 
posible que se deba enfrentar desafíos adicionales al escalar una aplicación o al mantenerla a medida que crece y 
evoluciona con el tiempo.

A continuación se creará un servidor con Python denominado server.py
"""
"""
django-admin startproject es una herramienta esencial para crear un nuevo proyecto Django de manera rápida y 
eficiente. Proporciona la estructura y los archivos necesarios para comenzar a desarrollar una aplicación web 
con Django, lo que facilita el proceso de configuración inicial y asegura una base sólida y consistente para el 
proyecto.
"""

