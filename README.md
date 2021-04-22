Ripio Cryptocurrencies
=======================================================
<img src="Ripio/images/Untitled Diagram(1).png" width="800" height="500">

<br>
<br>

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

- pip install -r requirements.txt

Objetivos de Desarrollo
=============================
- Se debe poder crear una moneda (por ejemplo Peso, Dolar, Bitcoin, etc)
- Se debe poder enviar dinero entre usuarios (Juan le manda a Pedro 10 pesos)
- Se debe tener un un registro de las operaciones realizadas.
- Se debe consultar en cualquier momento el "balance" en una moneda que tiene cada
  usuario.
- Tener en cuenta que los usuarios sólo deben hacer operaciones sobre su cuenta.
- Tener en cuenta la validación de lo datos enviados a la . (frontside / backside).
- Tener en cuenta un posible doble gasto u operación concurrente.


=======================================================

Desarrollo del proyecto
=======================================================
Este proyecto se desarrollo utilizando Django. 
Los modelos plasmados en la base de datos son estructuras fundamentales del proyecto, que cuentan con validación en los formularios y las vistas filtrando elementos de la base de datos. 
Todas las funciones están protegidas por un login_required y por cada nuevo login el usuario es notificado por email. 

- Transferencias:

    Los usuarios pueden transferir desde su propia cuenta, las cuales tienen  un tipo de moneda especifico. 
               En cada transferencia realizada, se envían emails automáticamente a los usuarios (de la cuenta origin y destino), notificando la operacion realizada.Tambien mediante un Signal se ajusta la cantidad de dinero entre las cuentas de los usuarios involucrados en la transferencia. Adicionalmente, se corrobora que el total en tenencia por los usuarios sea igual a la cantidad en circulación de cada moneda. La funcion que registra la cantidad de  monedas esta comentada , ya que el proyecto es de prueba, pero esto seria una forma de controlar la seguridad del sitema , mediante el control monetario.
               Como en todas las monedas virtuales, se intenta garantizar la seguridad mediante la publicación de las transferencias realizadas. Para ello, creé una vista donde las transferencias realizadas se muestren publicamente.
               Respecto a las transferencias personales, se pueden ver en "Mis transfencias" y descargar en formato PDF si asi se fuese requerido.

- Paypal:

   El sistema cuenta con la capacidad de comprar monedas por medio de Paypal, utilice el código de la documentación de este servicio y lo adjunte en una aplicación con su nombre. 
        A futuro, el proyecto podría ser configurado con Paypal para la adquisición de las monedas por parte del usuario, y a su vez la implementación de nuevas monedas en el sistema. 

Conclusion
=======================================================
En lo que respecta al proyecto , se intento realizar la mayor cantidad de sobre escrituras evitando la utilizacion de las herramientas que Django provee por defecto. Esto ha generado un plus de esfuerzo ya que las validaciones y los detalles fueron el principal objetivo a tener en cuenta. Se procedió a la creacion de la API rest con Django rest framework , ofreciendo en formato Json elementos de la base de datos. Este paso podria ser util en el caso que se proceda con el proyecto , para que mediante tecnologias , se comunique el Backend con el Frontend .
En lo personal agradezco a las personas de la empresa que me ha dado la oportunidad de tomar esta prueba desarrollarla y mostrarla.





