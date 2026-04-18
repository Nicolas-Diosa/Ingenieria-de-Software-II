# Tarea API’s
**Nicolás Alejandro Diosa Benavides**

**Ingeniería de Software II**

Docente: Sergio Vargas Pedraza

**Resumen:**
1.
API ELEGIDA: Joke API — Chistes
https://v2.jokeapi.dev/joke

2.

* Esta API no tiene una estructura específica de petición para traer todas las bromas (por ejemplo) y tampoco se puede armar puesto que el número máximo de chistes en una petición es de 10, pero lo que sí podríamos hacer es ir a algún endpoint y traer toda la información específica de ese endpoint, en este caso voy al endpoint de los endpoints (valga la redundancia), además también voy a mostrar que está limitado a diez la cantidad de chistes

<img width="1066" height="879" alt="image" src="https://github.com/user-attachments/assets/09e9817c-28b7-44d5-abfe-7dcc259a1ade" />

<img width="1059" height="867" alt="image" src="https://github.com/user-attachments/assets/c903ee1b-c948-406e-835e-5900eeb42299" />

(Sé que son 1368 chistes porque en el endpoint de info se puede ver cuántos chistes existen en total)

<img width="305" height="310" alt="image" src="https://github.com/user-attachments/assets/99e3c907-242b-4bbe-8f9d-0407bdccf797" />

* En este punto haré una petición para traer el primer chiste, para ello utilizaré la categoría any puesto que no sé de qué categoría es, y 0 como id pues el conteo de chistes empieza por el id 0.

<img width="1066" height="748" alt="image" src="https://github.com/user-attachments/assets/fd199d0b-1aa5-4d94-9293-2d6857b44943" />


* Esta API tiene post para enviar un chiste tentativo que podría llegar a ser incluido, para ello existe el endpoint submit, este endpoint solo recibe datos en formato JSON por lo tanto el post lo haremos así:

<img width="1045" height="656" alt="image" src="https://github.com/user-attachments/assets/9164fff9-717b-4cf9-abd8-e5a4d0f1e8e7" />


Lamentablemente está deshabilitado el envío de nuevos chistes.

* En la primera petición se utilizó un query param.

* Para hacer los test debemos generar scripts que verifiquen algo dentro de nuestra petición, lo primero que me recomendó postman y que se vio en clase fue el siguiente test para la primera petición:

<img width="1055" height="623" alt="image" src="https://github.com/user-attachments/assets/b9fceae5-0bf3-4e92-9940-0bb6a8aa2e76" />


Para el segundo test la idea es hacer algo un poco más elaborado, quiero por ejemplo que el id que pida en la petición del primer chiste sea verificado:

<img width="1065" height="522" alt="image" src="https://github.com/user-attachments/assets/8573bf34-a216-4686-8485-0e4e0717a688" />

3. En el repositorio se encuentra el archivo .json

4.
   → ¿Qué API elegiste y por qué?
   
Elegí el API de chistes porque la verdad es que estoy viejito y me pareció que podía llegar a dar gracia.

   → ¿Qué datos devuelve?
   
Chistes.

   → ¿Usa token o no? ¿Qué tipo?
   
No usa token, pero curiosamente este API ha sido atacado a través de DoS. Por ello han limitado las respuestas y peticiones por minuto.

   → ¿Qué código de estado recibiste en cada request?
   
En casi todos los casos fue recibido un código 200, en la única petición que no pasó fue en la de POST, pues fue deshabilitado por los creadores tal endpoint. en ella salió un código 500.

   → ¿Qué aprendiste diferente a JSONPlaceholder?
   
La verdad me llamó la atención que en esta API no se pudieran obtener todos los chistes con un endpoint o parámetro específico.

**Las variables de entorno utilizadas fueron las siguientes:**

<img width="1059" height="242" alt="image" src="https://github.com/user-attachments/assets/b2c090e4-be0a-4b61-a3d4-406e7a411fcc" />

_____________________________________________________________________

PARTE GRAPHQL:

**Resumen:**


1.
<img width="1060" height="352" alt="image" src="https://github.com/user-attachments/assets/5cd5de28-12a4-4269-91fe-a8352e1fb263" />

2.
2.1. Lo primero es traer todos los idiomas:

 <img width="1057" height="876" alt="image" src="https://github.com/user-attachments/assets/50697c3c-4d13-49e1-bf14-7814ebc87657" />


2.2. Los estados de China:

<img width="1057" height="871" alt="image" src="https://github.com/user-attachments/assets/8087ae6c-83ec-4756-bbe8-0f99acca5c9b" />

2.3. Monedas por continente

<img width="1056" height="857" alt="image" src="https://github.com/user-attachments/assets/4ca68a33-6d8e-47ef-ab96-a3d1979e3e55" />

2.4. Filtrar al país por su moneda (Colombia)

<img width="1064" height="691" alt="image" src="https://github.com/user-attachments/assets/456b0645-8435-433f-8093-3ccc9d7f5e65" />


2.5. Filtrar a colombia por su moneda y luego ver todos los países del mismo continente con su moneda:

<img width="1061" height="882" alt="image" src="https://github.com/user-attachments/assets/dbe40612-13ef-4a5d-bc7b-557b97a890a6" />


3. Los queries anidados pueden verse en el 2.2. 2.3. y 2.5.
4. Los queries con filtros son  2.2. 2.4. y 2.5.


5.
<img width="1068" height="665" alt="image" src="https://github.com/user-attachments/assets/95361056-c872-4926-8e0a-2d73b6be28b2" />

<img width="1059" height="569" alt="image" src="https://github.com/user-attachments/assets/b258be82-8925-4165-bb6b-1dca1e4d51e3" />

<img width="972" height="572" alt="image" src="https://github.com/user-attachments/assets/f0e39161-7130-4bb7-8000-2249cd7b2a9f" />

<img width="973" height="567" alt="image" src="https://github.com/user-attachments/assets/7180a1e6-6b40-4fe9-8634-e748e74bcbe1" />

<img width="960" height="585" alt="image" src="https://github.com/user-attachments/assets/598e604a-531a-468f-9cfd-59ad7aad3763" />

 → ¿Qué diferencia encontraste vs REST?
 
La estructura de las peticiones se vuelve muy diferentes, se manejan casi como directorios, y también es posible anidar queries, cosa que en REST no parece tan fácil, evidente o posible de hacer.

→ ¿Cuántos requests REST necesitarías para reemplazar tu query más compleja?

En mis queries la más compleja de las estructuras es la de ConsultaAnidada, creo que necesitaría alrededor de 3 peticiones que luego extrapolaría para hallar el mismo resultado.

-Encontrar a colombia por su moneda

-Encontrar el continente en el que está Colombia

-Traer a todos los países del continente.

→ ¿En qué proyecto real usarías GraphQL?

En proyectos que necesitaran traer información muy puntual del servidor, para evitar consultar información innecesaria o evitar traer menos información de la que necesite, además en proyectos en los que se necesiten usar API’s con un límite de request, sería más viable utilizar Graphql que REST.
