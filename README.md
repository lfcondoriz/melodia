# melodia
Plataforma de streaming de música · FastAPI · React Native · React

## Descripción
Melodia es una plataforma de streaming de música que permite a los usuarios escuchar sus canciones favoritas, crear listas de reproducción y descubrir nueva música. La aplicación está desarrollada utilizando FastAPI para el backend y React Native para el frontend móvil, con React para la interfaz web.

## Testing
Para ejecutar las pruebas, asegúrate de tener instalado `pytest` y ejecuta el siguiente comando en la raíz del proyecto:
```bash
docker compose exec api pytest
```
- `-v` para obtener una salida detallada de las pruebas.
- `--cov=app` para generar un informe de cobertura de código.