Ripio Cryptocurrencies
=======================================================

Este repositorio tiene el objetivo de mostrar un proyecto 
personal donde se realiza el planteamiento de una plataforma
para el uso de monedas virtuales , donde cada usuario puede
realizar transacciones y obtener el balance de sus cuentas.

Pre-requisitos / Requerimientos
=====================
Python - Django - Postgresql - Django Rest Framework

Instalacion
=============================

Configuracion del entorno virtual - virtualenv (nombre de su entorno virtual) /

 pip install django/
 pip install django_rest_framework
 pip install psycopg2


Objetivos de Desarrollo
=============================
- Se debe poder crear una moneda (por ejemplo Peso, Dolar, Bitcoin, etc)
- Se debe poder enviar dinero entre usuarios (Juan le manda a Pedro 10 pesos)
- Se debe tener un un registro de las operaciones realizadas.
- Se debe consultar en cualquier momento el "balance" en una moneda que tiene cada
  usuario.
- Tener en cuenta que los usuarios sólo deben hacer operaciones sobre su cuenta.
- Tener en cuenta la validación de lo datos enviados a la API. (frontside / backside).
- Tener en cuenta un posible doble gasto u operación concurrente.


=======================================================

Desarrollo del proyecto
=======================================================
Se procedió a la creación del proyecto mediante la utilización de Django
 como plataforma de trabajo de desarollo
 backend.Realize la implementación de la lógica del proyecto y la creación de los modelos en la base de datos. Estos modelos son las estructuras fundamentales del proyecto, cuentan con validación en los formularios y a su vez con vistas.
 Todas las funciones estan protegidas por un login_required y a su vez cada usuario al generar un nuevo login recibe un email a su cuenta personal donde se comunica que alguien está siendo logeado con su cuenta.
Trabaje en la implementación de transferencias entre los usuarios, generando en ellas cierta lógica, donde cada usuario es capaz de transferir desde su propia cuenta, la cual posee un tipo de moneda especifico. En cada transferencia realizada, mediante un signal se procede al ajuste de la cantidad de dinero entre las cuentas de los usuarios involucrados en la transferencia, sumando a esto la implementación de una sumatoria de monedas, corroborando que el total que tienen todos los usuarios sea igual a la cantidad de monedas que está dando giros en el mercado. Se implemento el reenvío de emails automáticos para informar a los usuarios que se ha generado una transferencia con su cuenta (tanto el usuario que envía como el que recibe).
 Como en todas las monedas virtuales, uno de los pasos de seguridad es la capacidad de visualización publica de las transferencias realizadas. En este caso he implementado una vista donde cualquier usuario es capaz de ver las transferencias realizadas por todos los demás usuarios. En lo que respecta a las transferencias personales, realicé una vista donde detallo por medio de una tabla la cantidad de transferencias con la capacidad de visualizarlas en formato PDF y si es requerido por el usuario descargarlas.
 A su vez se genero la capacidad de compra de monedas a traves de la plataforma virtual de Paypal ,  utilize el codigo de la documentacion de este servicio y lo adjunte en una aplicacion con su nombre. La razon de implementarlo no es que sea funcional ya que este proyecto es solo a modo de prueba de tecnica, pero si no fuese asi , el sistema puede estar coordinado con Paypal para la adquisicion de las monedas departe del usuario que realiza la compra , y a su vez la implementacion de nuevas monedas en el sistema . 
 Para poder tener un control de la cantidad de monedas en el sistema , se implemento una funcion (la cual esta comentada en Transferences/forms.py ) que realiza la sumatoria de todas las monedas de las cuentas de los usuarios y las compara con el balance de monedas que el sistema tiene por cada transferencia que los usuarios realizan.

Agradezco a las personas de la empresa que me ha dado la oportunidad de tomar esta prueba desarrollarla y mostrarla.

<br>
<br>


<img src="Ripio/images/Untitled Diagram(1).png" width="800" height="500">
