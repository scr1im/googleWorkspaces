# googleWorkspaces
 
Programa para Eliminar cuentas de correo gmail by Scr1im

Realizado en python3 version 3.11

Requiere las siguientes librerias para poder ejecutarse:
pip install -U selenium, pip install pandas y pip install webdriver-manager

Tener presente la actaulización del navegador de selenium.
Si requiere usar el navegador de selenium manager tener presente las lineas comentariadas

Utiliza un CSV con la lista de los correos a eliminar.
Modificar el path para el archivo .csv

Recomendaciones de uso:
1. Este programa es de uso personal y no debe usarse para motivos maliciosos.
2. Debe estar monitoreando el programa debido a tiempos de respuesta por parte de google.
3. Si el monitor es de menos de 20 pulgadas tener en cuenta que la ventana de selenium debe realizar zoom -(80%)

Por último y más importante debe tener en cuenta que el path de la linea 82 cambia cada semana por politicas de google, por lo que debe verificar el campo del valor antes de ejecutar el programa.

Para verificar el campo debe realizar los siguientes pasos:
1. Iniciar sesion en admin.google.com
2. Dirigirse a campo de busqueda de cuentas de correo electronico (ubicado en la parte superior de la página)
3. Click derecho inspeccionar código fuente
![image](https://github.com/scr1im/googleWorkspaces/assets/89859500/64c7652b-eb07-48c9-9c3c-55747a14e609)
4. Realizar alguna busqueda y verificar el campo HTML que cambia (el path de button class = 'gb_Le gb_Ne')
![image](https://github.com/scr1im/googleWorkspaces/assets/89859500/7a9609ff-8332-4b10-bd9a-745262886a7c)
5. Confirmar el nombre de la clase y modificarlo en el código para que este pueda borrar la busqueda

Les deseo muchos exitos..!!
