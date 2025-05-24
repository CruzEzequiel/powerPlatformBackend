# API de Cargadores Eléctricos

Esta API permite interactuar con un sistema de monitoreo de estaciones de carga para vehículos eléctricos. La API está construida en Python utilizando FastAPI y Firebase Admin SDK para autenticación y manejo de datos.

## Funcionalidades

* **Autenticación con Firebase**: Utiliza Firebase Admin SDK para la verificación de tokens JWT, asegurando que solo los usuarios autenticados puedan acceder a las rutas protegidas.
* **Generación de datos de muestra**: La API genera datos de muestra relacionados con estaciones de carga a través de la ruta `/data/chargers`.

## Rutas

### 1. **GET /data/chargers**

* **Descripción**: Esta ruta genera datos de muestra para estaciones de carga de vehículos eléctricos.
* **Método**: `GET`
* **Autenticación**: Requiere un token JWT de Firebase. El token debe enviarse en el encabezado `Authorization` como un `Bearer token`.
* **Respuesta**:

  * Retorna un JSON con los datos de muestra de las estaciones de carga.

## Requisitos

* **Python 3.x**
* **FastAPI**: Para la creación de las rutas de la API.
* **firebase-admin**: Para la integración con Firebase y la validación de tokens.
* **Uvicorn**: Para correr el servidor de desarrollo.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <directorio_del_repositorio>
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Asegúrate de tener configuradas las credenciales de Firebase en tu entorno. Crea un archivo `.env` con las variables necesarias para la autenticación de Firebase.

## Ejecución

Para ejecutar la API en desarrollo:

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.

## Ejemplo de Uso

### Autenticación

Para acceder a las rutas protegidas, debes incluir un token JWT válido en el encabezado de la solicitud:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/data/chargers' \
  -H 'Authorization: Bearer <tu_token_jwt>'
```
