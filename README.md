# PRUEBA TÉCNICA
____________________________________________________________________________________________________________________________________________________________________________________

Lo que he desarrollado como prueba técnica es un monolito con una subarquitectura en donde el modelo o lo que maneja la lógica y los datos se encuentra en los archivos de _capa_persistencia.py_ y _capa_seguridad_API.py_ mientras que la parte de vista y controlador se encuentran amalgamados en la _capa_presentacion.py_, realmente en este modelo no existe una vista como tal porque no existe una interfaz gráfica real.

Antes de empezar la prueba técnica y por lo que se pedía el consumo de varios endpoints recurrí a realizar la validación de las respuestas de las peticiones que necesitaba hacer en Postman, solo una de ellas (la petición para obtener las tablas) resulto estar fuera del alcance de la petición puesto que arroja un código 401, es decir, que no se encuentra autorizada la petición para acceder al endpoint. Cada una de las peticiones está en las siguientes imagenes;

<img width="1866" height="334" alt="image" src="https://github.com/user-attachments/assets/c8917331-d60b-4996-9279-a16d094a2d1b" />

<img width="1865" height="439" alt="image" src="https://github.com/user-attachments/assets/f61187cd-14d8-4154-b7d1-7fcd9c7601d9" />

<img width="1872" height="299" alt="image" src="https://github.com/user-attachments/assets/071d809c-edc3-48e4-8169-ba01597e28b7" />

<img width="1857" height="333" alt="image" src="https://github.com/user-attachments/assets/8ac95bf2-30c9-4247-b3ff-cdebc721caa1" />

Junto con el ambiente utilizado en Postman:

<img width="1873" height="616" alt="image" src="https://github.com/user-attachments/assets/0301d954-6e56-4e70-885d-1b61b3511d78" />

Ahora si después de hacer las validaciones se procede a hacer el código de estas peticiones utilizando la librería requests de python:

<img width="1075" height="828" alt="image" src="https://github.com/user-attachments/assets/9a08227a-9fa9-4c29-ba1a-2ab542ea46c9" />

 __*capa_seguridad_API.py*__

Este archivo contiene tres funciones que validan cada uno de los endpoits que se pedían en la prueba técnica, la primera se refiere a la verificación de las versiones, la segunda refereida al login y la "descarga" de las tablas que se encuentran en el API pero que no pueden ser accedidas como se vió en el Postman. Por último está la función que obtiene todas las localidades:

<img width="928" height="362" alt="image" src="https://github.com/user-attachments/assets/a2f46dab-4b8b-4373-b6cf-2d8548180e6d" />

<img width="689" height="716" alt="image" src="https://github.com/user-attachments/assets/4f59564e-36a6-4bb9-839a-c93ce1c87fa6" />

<img width="642" height="269" alt="image" src="https://github.com/user-attachments/assets/35605598-744d-403f-85f5-d7af622179bb" />

 __*capa_persistencia.py*__

 En esta capa se procede con lo pedido para almacenar los datos del usuario y las tablas que no se pueden acceder, todo esto a través de una base de datos local de SQLite con la librería de python SQLite3. En este archivo se encuentran las funciones pra inicializar la base de datos, guardar y acceder a los datos del usuario que ha iniciado sesión y el guardado de las tablas en la base de datos local:

 <img width="665" height="581" alt="image" src="https://github.com/user-attachments/assets/4dab49b9-ed51-450e-ad93-b1f5c685b4cd" />
 
<img width="674" height="251" alt="image" src="https://github.com/user-attachments/assets/34fbfedd-5439-4028-8265-e6daeb9ea49a" />

<img width="802" height="301" alt="image" src="https://github.com/user-attachments/assets/8c780027-e9e4-43b6-a717-ae47f54521a6" />

<img width="728" height="194" alt="image" src="https://github.com/user-attachments/assets/532395e4-7da2-4889-b4e9-7463899a52b0" />

<img width="491" height="168" alt="image" src="https://github.com/user-attachments/assets/3c3c57e8-1023-48bb-a131-33889070703a" />

 __*capa_presentacion.py*__

 En esta capa se encuentran las impreisones y el flujo de interacción del usuario por consola, además de la función main en donde se define la interacción del usuario con la "aplicación" están otras 3 funciones que representan cada una de las vistas o pantallas, una para el inicio o HOME, otra para las localidades y una última para las tablas que obviamente no funcionará pues el API de nuevo no puede ser accedida en ese endpoint. 

 <img width="644" height="441" alt="image" src="https://github.com/user-attachments/assets/134891c2-417c-4a7e-be55-6221174e53e4" />

 <img width="644" height="441" alt="image" src="https://github.com/user-attachments/assets/12821b09-100a-44ca-8ce5-317c65ecfa97" />

 <img width="464" height="194" alt="image" src="https://github.com/user-attachments/assets/d8afda2d-6d77-410e-86a3-e01042e2cc20" />

 <img width="640" height="292" alt="image" src="https://github.com/user-attachments/assets/50e4327b-0e8b-400e-af71-954bd4262a7a" />

 __Evidentemente entre los archivos se imporatan entre ellos, la parte de persistencia es llamada por la parte de consumo de API y ambos archivos de capa de Modelo van a ser llamados por la capa de Presentación__

 __*Tests.py*__

En este último archivo residen los tests que se le hacen al archivo de modelo de consumo de API, los test se hacen a través de los mocks para no estar generando peticiones al API real, se hacen 6 test, realmente son 3 unitarios puesto que son dos test por cada una de las funciones que hacen peticiones al API. La primera función prueba el caso en que la verificación de versión es exitosa (código HTTP 200) y otra en donde la conexión con el API es fallida. Para el login se hacen dos test, el primero cuando se logra hacer un Login exitoso y otro cuando por el cointrario el Login no logra efectuarse. Así también para la parte de localidades.

<img width="864" height="564" alt="image" src="https://github.com/user-attachments/assets/ec6f0fa4-dd92-476e-b075-9658c4300f39" />

<img width="711" height="429" alt="image" src="https://github.com/user-attachments/assets/6b66aec8-2619-4970-afab-1d8dfa35fe3e" />

<img width="738" height="605" alt="image" src="https://github.com/user-attachments/assets/0b745a71-6bde-4be1-9615-738f386cfac1" />


Los resultados de los test son exitosos:

<img width="822" height="261" alt="image" src="https://github.com/user-attachments/assets/d63c16b5-c2d7-488f-99a5-86fbf71412d7" />





