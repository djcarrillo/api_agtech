## Fuentes

### Polygon

Polygon es un servicio que disponibiliza a sus usuarios los movimientos de acciones registrados en la bolsa de  New York, siendo esta una de las fuentes más usadas para este segmento de negocio en el mundo:  [more information here](https://polygon.io/)

### End Points from Polygon

El listado completo de endpoints de plataforma es listado [aquí](https://polygon.io/system).

Para este busineess case haremos uso de:

- /v2/snapshot/locale/global/markets/forex/tickers : Fuente en MVP de las compañías listadas.
- /v2/reference/news: Notias de la compañia consultada
- /v1/open-close/{stocksTicker}/{date}: Precio de la acción apertura / cierre en eun dia determinado:
    
    Ejemplo de uso:
    
    [Parametros del endpoint](https://www.notion.so/f8ccd35aeeca4f54b3e02499ded4d795)
    

### BD Dynamo

Estructura Base de Datos

{

user_id: Object(user_id  MD5):

favorite_companies: [

 {

name: string,

created_at: timestamp

},

{

name: string,

created_at: timestamp

},

{

name: string,

created_at: timestamp

}

],

discarded_companies:

[

{

name: string,

created_at: timestamp

},

{

name: string,

created_at: timestamp

}

], 

created_at: timestamp

}

# Lite Version

{

user_id_md5: 

{

favorite_companies: [string, string, string, string, string],

discarded_companies: [string, string, string, string, string],

created_at: timestamp

},

user_id_md5: 

{

favorite_companies: [string, string, string, string, string],

discarded_companies: [string, string, string, string, string],

created_at: timestamp

}

}

##