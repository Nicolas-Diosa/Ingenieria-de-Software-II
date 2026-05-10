# PATRONES DE DISEÑO

__SINGLETON__

Dentro del ejercicio de singleton se me ocurrió hacer un ejemplo abstracto sobre el singleton, normalmente en la industria del transporte existen varios conductores para una mula que está en servicio, en este caso cuando un conductor entra en su turno no puede haber otro conductor simultáneamente en la misma mula manejando por lo tanto el singleton será orientado a crear un único conductor en turno para la mula en cuestión. Por último se hace la prueba de que el conductor que entro en turno por primera vez es el único que puede manejar la mula:

<img width="1300" height="876" alt="image" src="https://github.com/user-attachments/assets/ade8aae2-a6a8-4e75-adf9-3466545af94f" />

La salida es entonces:

<img width="1700" height="139" alt="image" src="https://github.com/user-attachments/assets/5afd819d-81b4-4c7c-b491-f2fa482bd969" />

__PROTOTYPE__

Ahora para aplicar otro patrón creacional me remití a la idea de una empresa del sector de transporte que transporta diferentes tipos de cargas, en este caso en específico llevaría por ejemplo materiales de construcción, alimentos y animales, como todas al final son flotas de transporte pero de diferentes tipos lo que se hace es crear una clase flota, luego un objeto que sea prototipo o carro pesado y copiarlo o clonarlo a través del deep.copy (código que permite clonar un objeto incluso con las listas que tenga por dentro e información interna al detalle). Al final el código resultante es el siguiente:

<img width="955" height="681" alt="image" src="https://github.com/user-attachments/assets/9717c0a1-34c8-4f6f-b037-e32a111ed264" />

<img width="1000" height="658" alt="image" src="https://github.com/user-attachments/assets/3ba61e4b-97f0-4560-81f2-528b7acf8980" />

A raíz de todas estas copias imprimimos que quedó dentro de cada uno de los objetos, cabe resaltar que la función que se define como __str__ arriba es útil para modificar lo que se imprimirá al definir el print del objeto por defecto.

El resultado de la impresión es la siguiente:

<img width="1543" height="113" alt="image" src="https://github.com/user-attachments/assets/9ee5d8a9-f745-44de-bab9-61eab17c5256" />

__PROTOTYPE+BRIDGE__

Complementado el código anterior supongamos ahora que existen diferentes logísticas, es decir, puede llevarse la carga no solamente en carretera sino en vías ferroviarias también, por lo que no haría sentido también añadir otro atributo que lo definiera por temas de escalamiento, para ello entonces definimos una clase general que a través de implementaciones concretas especificará que tipo de logística sería necesaria, lo que estamos haciendo quí es dividir nuestra clase de transportes principal en dos clases que encapsulen las funcionalidades necesarias, tanto de definición de logística como de otros temas, al final el bridge nos está permitiendo evitar añadir atributos o generar más clases para solucionar el problema del tipo de logística.

Dentro del código lo ideal es ahora ver que cada uno de los clones que creamos antes tengan por supuesto su tipo de logística, en este caso creamos nada más dos clones:

<img width="692" height="626" alt="image" src="https://github.com/user-attachments/assets/6f28e080-4879-4342-ac7c-05729522b0ac" />

<img width="846" height="431" alt="image" src="https://github.com/user-attachments/assets/5166e6eb-496e-446a-8db1-1498dd833d4a" />

<img width="775" height="525" alt="image" src="https://github.com/user-attachments/assets/a30754b2-4f37-4dbc-ac4b-4fc6c34dd850" />

El resultado final es el siguiente:

<img width="1596" height="87" alt="image" src="https://github.com/user-attachments/assets/6832bf98-a570-4293-88da-0d423340188e" />

__PROTOTYPE+BRIDGE+CHAIN OF RESPONSABILITY__

Ahora complejicemos el problema, ¿si se va a enviar una carga por cuál de las logísticas se debería hacer?, digamos en este caso que más que por costo lo queremos hacer por una logística que pueda llevar tal cantidad de elementos. Para ello utilizamos los manejadores propios del patrón de chain of responsability, y de menor a mayor evaluamos cuál de todas nuestras logísticas es la primera en ser capaz de llevar la carga a su destino. Para ello entonces definimos una clase general de manejadores y creamos un manejador para cada tipo de logística. Al final definimos cuál logística usar para cada uno de los tipos de flota.

<img width="732" height="597" alt="image" src="https://github.com/user-attachments/assets/36011dc9-ebe6-407a-a995-db4d1cb1b2b8" />

<img width="913" height="600" alt="image" src="https://github.com/user-attachments/assets/a1758a81-606a-4a2d-a99b-e8c5fded881f" />

Los resultados son los siguientes:

<img width="1560" height="123" alt="image" src="https://github.com/user-attachments/assets/35313a32-0fdd-4d63-9a7a-0b32a3bcdd41" />





