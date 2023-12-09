<div align="center">
<table>
    <theader>
        <tr>
            <td style="width:25%;"><img src="https://github.com/rescobedoulasalle/iw-23b/blob/main/proyecto/logo_ulasalle_2017.png?raw=true" alt="ULASALLE" style="width:20%; height:auto"/></td>
            <td>
                <span style="font-weight:bold;">UNIVERSIDAD LA SALLE</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE MATEMÁTICAS E INGENIERÍAS</span><br />
                <span style="font-weight:bold;">CARRERA PROFESIONAL DE INGENIERÍA DE SOFTWARE</span>
            </td>            
        </tr>
    </theader>
    <tbody>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Proyecto web</span>: Desarrollo de una red social (Crazy Challenge)</td>
        </tr>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Fecha</span>:  07/12/2023</td>
        </tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">PROYECTO WEB</span><br />
</div>


<table>
<theader>
<tr><th>INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td>Ingeniería Web</td>
    </tr>
    <tr>
        <td>SEMESTRE:</td><td>VIII</td>
    </tr>
    <tr>
        <td>FECHA INICIO:</td> <td>01-Agosto-2023</td> 
        <td>FECHA FIN:</td> <td>07-Dic-2023</td>
    </tr>
    <tr>
        <td colspan="13">DOCENTE:
        <ul>
        <li>Richart Smith Escobedo Quispe - r.escobedo@ulasalle.edu.pe</li>
        </ul>
        </td>
    </<tr>
    <tr>
        <td colspan="11">GRUPO:
        <ul>
          <li>Juliana Berrios Butron</li>
          <li>Jose Grados Chuquitaype</li>
          <li>Daria Lopez Franco</li>
          <li>Bradlhy Machado Medina</li>
          <li>Jean Mamani Mota</li>
        </ul>
        </td>
    </<tr>
</tdbody>
</table>

#   WebApp con Django

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

##  Tipo de Sistema
    La aplicación "Crazy Challenge" es un emocionante y vibrante plataforma diseñada para brindar a los usuarios una 
    experiencia única de desafío, diversión y creatividad. Este documento describe los módulos de la aplicación y sus 
    interacciones, estableciendo las bases para un entendimiento más profundo de su arquitectura y funcionamiento.

##  Requisitos del sistema
    El sistema debe satisfacer los siguientes requisitos funcionales y no funcionales:

    REQUISITOS FUNCIONALES (RQF)
    - RQF01 : Registro y Autenticación
      • Los usuarios deben poder registrarse en la plataforma utilizando la autenticación del sistema.
      
    - RQF02 : Perfil de Usuario
      • El usuario podrá completar y/o editar la biografía de su perfil además de su avatar, preferencias e información personal.
      
    - RQF03 : Recopilación de Preferencias en el Perfil de Usuario
      • Debe haber una sección de preferencias donde los usuarios puedan seleccionar categorías, temas o etiquetas. Los usuarios 
        al iniciar sesión deben especificar sus preferencias e intereses en su perfil (mínimo 3 preferencias).
    
    - RGF04 : Chat entre Usuarios
      • Los usuarios pueden chatear de forma privada con otros usuarios que siguen.
      
    - RQF04 : Publicación de Videos y Contenido de Retos
      • Los usuarios deben poder cargar videos y fotos para mostrar cómo completaron un reto asociándolo al reto correspondiente.
      
    - RQF05 : Interacción Social
      • Los usuarios pueden postear, subir videos o desafíos.
      • Los usuarios pueden seguir a otros usuarios y ser seguidos.
      • Los usuarios pueden reaccionar a los videos de los retos con una variedad de reacciones (por ejemplo, “Cumplió”, 
        “No cumplió”, “Incompleto” ).
      • Los usuarios pueden comentar en los videos de los retos.
      
    REQUISITOS NO FUNCIONALES (RQNF)
    - RQNF01 : Seguridad
        • Deben poder iniciar sesión de manera segura.
        • Debe implementarse un sistema de seguridad robusto para proteger los datos de los usuarios y prevenir contenido peligroso.
    
    - RQNF02 : Rendimiento
        • La plataforma debe ser altamente receptiva para mantener la satisfacción del usuario.
        • Los tiempos de respuesta deben ser cortos para mantener la atención del usuario.
        
    - RQNF03 : Escalabilidad
        • La plataforma debe ser escalable para acomodar un crecimiento futuro en términos de usuarios y contenido.
    
    - RQNF04 : Almacenamiento de Contenido Multimedia
        • Debe existir un sistema eficiente de almacenamiento y gestión de contenido multimedia, como videos y fotos.
    
    - RQNF04 : Privacidad de Datos
        • Los datos recopilados del usuario deben manejarse con alta seguridad y respetar la privacidad de ellos.

    - RQNF05 : Usabilidad
        • La interfaz de usuario debe ser intuitiva y fácil de usar para proporcionar una experiencia agradable al usuario.
        
    - RQNF06 : Cumplimiento Legal
        • La plataforma debe cumplir con las regulaciones de privacidad de datos y derechos de autor aplicables.
        • Deben existir políticas claras para el contenido que no cumple con las normas de la comunidad.
        
##  Modelo de datos
    El modelo de datos esta conformado por las siguientes entidades.

    -  Users : Esta es la entidad principal, ya que será el que usa el sistema desde su registro hasta las acciones que se realice.
    -  Preferences : Entidad relacionada con usuarios, preferencias o gustos de cada usuario.
    -  Followers : Esta es una entidad que contendrá los usuarios seguidores de otros usuarios.
    -  Posts : Entidad que contendrá cada publicación que realicen los usuarios.
    -  Reactions : Es la entidad que contiene las reacciones a las publicaciones de cada usuario.
    -  Comments : Entidad útil para el almacenamiento de los comentarios que habrá entre usuarios.
    -  Notifications : Es una entidad para las notificaciones que recibirán los usuarios.
    -  Challenges : Es la entidad donde se alojarán los retos de los post que realice cada usuario.
    -  Participations : Entidad para almacenar y gestionar las participaciones de los usuarios en los retos.
    -  GroupChats: Es la table que contiene los Grupos de chats entre usuarios.
    -  Members: Es la lista de usuarios que pertenecen a un chat.
    -  Messages : Entidad de los mensajes que tienen los chats.
    -  ChallengesCategory : Entidad donde están las categorias de los retos.
    -  Categories : Es la entidad que contendrá las categorias que se creen para los retos.

##  Diccionario de datos

    Para el acceso al diccionario de datos, se debe clonar el proyecto, ingresar a la carpeta "Diccionario de Datos" y ejecutar el archivo "index.html".
    Este archivo contiene el diccionario detallado, estilizado y categorizado con todos los elementos útiles y necesarios usados en la Base de Datos.

##  Diagrama Entidad-Relación
![alt text](https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Ffeb49bee-9cd1-4bcb-a0dd-c7dca6a650ae%2Fd6aae043-343e-4d6b-95aa-c58fffddd7c0%2FUntitled.png?table=block&id=3d388a59-af5b-4ea6-aa9d-2a90a5e05c08&spaceId=feb49bee-9cd1-4bcb-a0dd-c7dca6a650ae&width=2000&userId=0aa2e18a-586b-40e8-b6c6-1959f35888d8&cache=v2)
    

##  Administración con Django
#### Paso 1: Crear y ejecutar un entorno virtual 
        $ python -m venv my_env
        $ .\my_env\Scripts\activate
        
#### Paso 2: Crear un nuevo proyecto Django
        $ django-admin startproject nombre_del_proyecto
        $ cd nombre_del_proyecto

#### Paso 3: Crear una aplicacion Django
        $ mkdir MyWebApps
        $ cd MyWebApps
        $ django-admin startapp MyFirstApplication
    
#### Paso 4: Definir los modelos
Ya sea modificar el archivo models.py o crear una carpeta models y dentro de ella establecer un modelo para cada entidad.
    
#### Paso 5 Crear migraciones
        $ python manage.py makemigrations
        $ python manage.py migrate

#### Paso 6 Crear un superusuario para el panel de administración
        $ python manage.py createsuperuser

#### Paso 7  Registrar los modelo en el panel de administración
Edita el archivo "admin.py" en la aplicación y registrar el modelo:
        
 ```python
        from django.contrib import admin
        from .models import MiModelo
        
        admin.site.register(MiModelo)
```
#### Paso 8 Levatar el proyecto
        $ python manage.py runserver
        
    
##  Plantillas Bootstrap
Para la aplicación desarrolada no se usó plantillas gráficas, se inició desde cero.

Se usó "React" con Material-UI, la documentación y componente están es este [link](https://mui.com/material-ui/).


##  CRUD - Core Business - Clientes finales
    El núcleo de negocio del sistema de inscripciones tiene valor de aceptación para los cliente finales (alumnos) radica en realizar el proceso de inscripción propiamente, que empieza desde que:
    1. El usuario se registra en el sistema.
    2. El usuario inicia sesión.
    3. El alumno selecciona todas sus preferencias con respecto a los retos.
    4. El usuario puede administrar, editar o modificar los datos con respecto a él.
    5. El usuario puede ver distintos post de retos en una pasarela de retos.
    6. El usuario puede comentar los post.
    7. El usuario puede inscribirse a retos elegidos.
    8. El usuario puede reaccionar a los retos posteados.
    9. El usuario cierra sesión.

Cada una de estas pantallas funciona y se estableció en la parte gráfica de la aplicación.
A continuación se muestran las actividades realizadas para su construcción:

#### Paso 1 : Maquetado
Se maqueto las imagenes en un maquetador de GUI's (Figma), este es el enlace del  [maquetado](https://www.figma.com/file/T53LCMNa6UUuoYUMtFYTT8/Dashboard-design---Figma-variants---Light-mode-to-Dark-mode-(Community)?type=design&node-id=2%3A2&mode=design&t=V8p6c1wwip1fZZ6C-1).
   
#### Paso 2 : Framework
Se eligió un framework para la programación e implementación de estas maquetas en pantallas interactivas y funcionales.
    
#### Paso 3 : Programación e implementación
Posteriormente se procedió a implementar cada pantalla modelada con el framework.

#### Paso 4 : Pruebas
Finalmente luego de programar e implementar todas las vistas se realizó las pruebas de fluidez y correcto funcionamiento.
    

##  Servicios mediante una API RESTful
    Se ha creado una aplicación que pondra a disposición cierta información para ser consumida por otros clientes HTTP.
    1. GET : Con el método get se devolverá la lista de los elementos de la base de datos, ya sea por un listado general o solo obtener un registro por id, este modelo se sequirá para todas las entidades presentes en el proyecto. 
    2. POST : Con este método se realizará la creación de entidades en el backend, además de el login y registro en el sistema.
    3. DELETE : Este método es para la eliminación de registros de entidades  

Ejemplo método post para creación de publicaciones:
```python
    @api_view(['POST'])
    @token_required
    def create_post(request):
        token = request.COOKIES.get('token')
    
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')
    
            user = User.objects.get(pk=user_id)
    
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
```
Se especifican los pasos para crear el servicio RestFul

#### Paso 1: Instalación de Django REST Framework
    pip install djangorestframework

#### Paso 2: Agregar 'rest_framework' a INSTALLED_APPS
En el archivo settings.py del proyecto, debemos asegurarnos de tener 'rest_framework' en la lista INSTALLED_APPS.
```python
    # En archivo settings.py
    INSTALLED_APPS = [
        # ...
        'rest_framework',
        # ...
    ]
```

#### Paso 3: Crear un serializador
Un serializador en DRF define cómo los modelos y las consultas deben ser convertidos a JSON y viceversa. 
Crear un archivo serializers.py o carpeta donde dentro se pongan serializadores para cada modelo
```python
    class PostSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('__all__')
```
#### Paso 4: Crear vistas utilizando ViewSets
Crear un archivo views.py o carpeta donde dentro se pongan view y se defina un ModelViewSet que utilizará el serializador.
```python
    from ..models import User, Post
    from ..serializers import PostSerializer
    import jwt
    from datetime import datetime, timedelta
    from django.conf import settings
    from ..decorators import token_required

    @api_view(['POST'])
    @token_required
    def create_post(request):
        token = request.COOKIES.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')
            user = User.objects.get(pk=user_id)
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
```

#### Paso 5: Configurar las URLs
En el archivo urls.py de la aplicación, configurar las URLs utilizando un Router.
```python
    from django.urls import path, include, re_path
    from rest_framework import routers
    from .views.User_view import UserView
    from .views import login_view, post_view
    
    router = routers.DefaultRouter()
    router.register(r'users', UserView)
    
    urlpatterns = [
        re_path('signup', login_view.signup),
        re_path('login', login_view.login),
        re_path('test_token', login_view.test_token),
        re_path('post', post_view.create_post),
        re_path('all', post_view.get_all_posts),
        path("users/", include(router.urls)),
    ]
```

#### Paso 6: Actualizar y ejecutar el proyecto
Realizar las migraciones y levantar el proyecto
        
        $ python manage.py makemigrations
        $ python manage.py migrate

```
    $ python manage.py runserver
```

##  Operaciones asíncronas AXIOS
Para las operaciones asíncronas, realizar solicitudes HTTP en la aplicación y conección con el backend se usó AXIOS para así evitar la recarga excesiva de la pantalla y porque su sintaxis y complejidad suele ser muy sencilla y facil de entender.


#### Paso 1:  Crear un archivo "axios.js"
Se creó el archivo mencionado ya que contendrá la importación que suele ser genérica para las peticiones
```javascript
    import axios from "axios";
    import { PORTBACKEND } from "../config";

    const instance = axios.create({
        baseURL: PORTBACKEND,
        withCredentials: true,
    });

    export default instance;
```

#### Paso 2: Crear un archivo "auth.js"
Crear el archivo donde se contendrá las solicitudes a realizar.
```javascript
    import axios from './axios';
    
    export const loginRequest = (user) => {
        axios.post('/api/user/login')
    }
```

#### Paso 3: Manejar las respuestas y errores en cada componente
Crear el archivo donde se contendrá las solicitudes a realizar.
```javascript
    useEffect(() => {
        const fetchData = async () => {
            try {
                await axios.get(PORTBACKEND + '/api/user/verify');
            } catch (err) {
                navigate('/');
            }
        };

    fetchData();
```

##  Investigación: Front-End.
En este proyecto, se optó por utilizar React como el framework de Front-End para consumir la API proporcionada por Django Rest Framework (DRF). React es una biblioteca de JavaScript desarrollada por Facebook y ampliamente utilizada en el desarrollo web moderno. Se eligió React debido a sus numerosos beneficios y características que hacen que sea una elección sólida para construir interfaces de usuario interactivas y eficientes.

#### Beneficios:
1. Componentización: React sigue un enfoque basado en componentes, permitiendo la creación de interfaces de usuario modularizadas. Cada componente puede ser desarrollado, probado y mantenido de forma independiente, facilitando la reutilización del código y la escalabilidad del proyecto.

2. Virtual DOM: React utiliza un Virtual DOM para realizar actualizaciones eficientes en la interfaz de usuario. Esto significa que en lugar de actualizar directamente el DOM cada vez que cambia el estado de la aplicación, React realiza comparaciones en un DOM virtual y solo actualiza los elementos que han cambiado, lo que mejora significativamente el rendimiento.

3. React Hooks: Los Hooks de React permiten el uso de estado y otras características de React en componentes de función, eliminando la necesidad de clases en muchos casos. Esto simplifica la sintaxis y facilita la gestión del estado y del ciclo de vida de los componentes.

4. Librería Activa y Comunidad Activa: React es una librería activamente mantenida con una gran comunidad de desarrolladores. Esto significa que hay una abundancia de recursos, bibliotecas y soluciones disponibles, así como actualizaciones regulares y mejoras de rendimiento.

5. React Router: Facilita la navegación y el enrutamiento en la aplicación, permitiendo la creación de aplicaciones de una sola página (SPA) de manera sencilla y organizada.

6. React es Declarativo: La programación declarativa de React hace que sea más fácil comprender cómo funcionan los componentes y facilita el mantenimiento del código a lo largo del tiempo.

7. Gran Ecosistema: React cuenta con un amplio ecosistema de bibliotecas y herramientas que se integran fácilmente. Además, al ser parte de la biblioteca de JavaScript, puede combinarse con otras tecnologías y herramientas según las necesidades del proyecto.
    

##  Sobre el proyecto
- Github BackEnd: https://github.com/jeanusll/Django-Web.git
- Github FrontEnd: https://github.com/l0stKitten/CrazyChallengeFrontend.git

- URL Playlist YouTube: 

    - Video 01 - Sistema - Requisitos. 
    - Video 02 - Modelo de datos - DD - DER.
    - Video 03 - Back
    - Video 04  - Front
    - Video 05 - Funcional


## REFERENCIAS
-   https://mui.com/material-ui/
-   https://www.djangoproject.com/
-   https://www.django-rest-framework.org/
-   https://www.solbyte.com/blog/react-js-ventajas-e-inconvenientes/
-   https://axios-http.com/docs/intro

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
