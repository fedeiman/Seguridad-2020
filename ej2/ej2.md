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
