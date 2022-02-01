# Actividades a realizar:
Se solicita la creación de una API REST que permita interactuar de forma simple con el catálogo de EartExplorer (https://earthexplorer.usgs.gov/) en donde la búsqueda de datos, la recuperación de metadatos y la descarga imágenes satelitales de un área específica sea posible.
Puede apoyarse en las siguiente librería (  Landsatxplore: https://github.com/yannforget/landsatxplore  ) o directamente a través del API  ( Machine-to-Machine (M2M) API – USGS:   https://m2m.cr.usgs.gov/ )

## Especificaciones:
Usar el url base:   https://localhost/pruebaeos  para el desarrollo de la prueba.

Tanto las peticiones y respuestas del REST API aquí descritas a continuación son solo ejemplos, usted puede estructurar los verbos y los end-point como desee.

### 1)Debe retornar un objeto json que contenga el catálogo de escenas encontradas para el Dataset “Landsat 8 Collection 1 Level 1” para una coordenada y un periodo de tiempo especificado._

#### Request 

HTTP POST https://localhost/pruebaeos/catalogo

```sh
{
   "dataset":"landsat_8_c1",
   "lat":"1.8035",
   "lon":"-78.6298",
   "fecha_inicio":"2010-01-01",
   "fecha_fin":"2010-01-01",
   "nubosidad_max":"20"
}
```

#### Response (JSON)

```sh
{
	"escenas_encontradas": "3",
	"escenas": [{
			"fecha": "2021-10-17",
			"identificador": "LC08_L1GT_010059_20211017_20211026_01_T2"
		},
		{
			"fecha": "2017-01-23",
			"identificador": "LC08_L1TP_010059_20170123_20170311_01_T1"
		},
		{
			"fecha": "2015-06-11",
			"identificador": "LC08_L1TP_010059_20150611_20170408_01_T1"
		}
	]
}
```
### 2)	Debe descargar una escena en particular y descomprimirla en la carpeta indicada (output_dir) 

#### Request 

HTTP POST https://localhost/pruebaeos/descarga

```sh
{
   "escena":" LC08_L1GT_010059_20211017_20211026_01_T2",
   "output_dir":"./temporal",
   "accion":"descarga",
}
```

#### Response (JSON)

```sh
{
   "escena":" LC08_L1GT_010059_20211017_20211026_01_T2",
   "url" :    "https://localhost/pruebaeos/temporal/LC08_L1GT_010059_20211017_20211026_01_T2" 
}
```

### 3)	Se debe listar el contenido de la escena descomprimida en la carpeta indicada (output_dir) 


#### Request 

HTTP POST https://localhost/pruebaeos/descarga

```sh
{
   "escena":" LC08_L1GT_010059_20211017_20211026_01_T2",
   "output_dir":"./temporal",
   "accion":"listar",
}
```

#### Response (JSON)

```sh
{
   "escena":" LC08_L1GT_010059_20211017_20211026_01_T2",
   "url":"https://localhost/pruebaeos/temporal/LC08_L1GT_010059_20211017_20211026_01_T2",
   "archivos":[
      {
         "banda1":"LC08_L1GT_010059_20211017_20211026_01_T2_B1.TIF",
         "banda2":"LC08_L1GT_010059_20211017_20211026_01_T2_B2.TIF",
         "banda3":"LC08_L1GT_010059_20211017_20211026_01_T2_B3.TIF",
         "banda4":"LC08_L1GT_010059_20211017_20211026_01_T2_B4.TIF",
         "banda5":"LC08_L1GT_010059_20211017_20211026_01_T2_B5.TIF",
         "banda6":"LC08_L1GT_010059_20211017_20211026_01_T2_B6.TIF",
         "banda7":"LC08_L1GT_010059_20211017_20211026_01_T2_B7.TIF",
         "banda8":"LC08_L1GT_010059_20211017_20211026_01_T2_B8.TIF"
      }
   ]
}
```
> Nota: Si la escena no se encuentra descargada y descomprimida en la carpeta indicada responder de la siguiente forma:

#### Response (JSON)
```sh
{
   "escena":" LC08_L1GT_010059_20211017_20211026_01_T2",
   "mensaje" : "escena no encontrada" 
}
```

### 4) Cálculo de índice de vegetación 

#### Request 
HTTP POST https://localhost/pruebaeos/ndvi
```sh
{
   "escena":" LC08_L1GT_010059_20211017_20211026_01_T2",
   "lat":"1.8097",
   "lon":"-77.6141",
}
```

#### Response (JSON)
```sh
{
   "ndvi":" 0.22"
}
```


**El cálculo genérico del NDVI se muestra en esta fórmula:**

```javascript

(NIR - R) / (NIR + R)

En  Landsat 4-7, NDVI = (Band 4 – Band 3) / (Band 4 + Band 3).

En Landsat 8, NDVI = (Band 5 – Band 4) / (Band 5 + Band 4).


```






