# Tarea de peticiones a servidor local a través de SSH

En esta tarea se nos pide utilizar el código del servidor hecho en JavaScript, ejecutándolo en un computador diferente, es decir, simulando que el servidor se encuentra alojado en una máquina distinta al cliente, para luego probar varios endpoints, en especial el endpoint __tasks__. Para conseguir esto, se siguieron los siguientes pasos (con los resultados correspondientes capturados en pantallazos):

1. Se utilizó una máquina virtual para simular el servidor alojado en otro pc, el sistema operativo de tal máquina es ubuntu versión 24.04.3. Luego se instaló node js y npm, aunque realmente solo fue necesario utilizar el comando de node para ejecutar server.js.

<img width="810" height="573" alt="image" src="https://github.com/user-attachments/assets/5508cce9-bc8c-4abd-9d1d-63bfb4c0132a" />

2. Después de ejecutar el servidor server.js, procedemos a conectar la máquina real y la máquina virtual a través de ssh.

<img width="1108" height="426" alt="image" src="https://github.com/user-attachments/assets/b6b717c1-fff9-4c49-9d8d-1fd46795b1a8" />

3. Puesto que en linux el powershell no va por defecto, es necesario instalar un paquete específico conocido como powershell, esto a través del gestor de paquetes snap, para luego ejecutar el powershell desde linux con el comando pwsh.


<img width="575" height="97" alt="image" src="https://github.com/user-attachments/assets/0e1cbc9d-b362-4177-9d81-7952d4237977" />

4. Creamos un usuario desde el endpoint register, en la imagen se puede ver que se trató de tomar el token directamente, lo que realmente es un error puesto que el token solo se brinda cuando se accede por un usuario, igualmente la línea del método POST se ejecuta y se crea el usuario, pero la variable $token queda vacía por lo que expliqué anteriormente.

<img width="1100" height="44" alt="image" src="https://github.com/user-attachments/assets/ae53cad8-8f96-4ddd-9244-10e00a4c8056" />

5. Ahora si obtenemos el token a partir del endpoint de login:

<img width="1097" height="94" alt="image" src="https://github.com/user-attachments/assets/f6d66d7d-3b93-4598-80f1-3df957a003ec" />

6. Generamos la tarea que hemos de probar.

<img width="1107" height="212" alt="image" src="https://github.com/user-attachments/assets/7443cbc3-c6eb-41ee-b28f-0a3f501b374d" />

7. Modificamos la tarea con un put en su status.

<img width="1111" height="184" alt="image" src="https://github.com/user-attachments/assets/a48f3141-7a4d-4df0-b205-4cb1e3bae079" />

8. Borramos la tarea y revisamos que ya no existe para el token almacenado.

<img width="1105" height="219" alt="image" src="https://github.com/user-attachments/assets/ed90c2d5-7c9b-4216-8f08-cbc711bb11b4" />

