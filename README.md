# Taller LLM
En este taler se aprenderá a usar Langchain 
librerias herramienta fundamental para crear
agentes que usen la técnica de Retrieval Augmented Generation, también 
llamada RAG.

## Instalando el proyecto
Para correr este proyecto en tu maquina local necesitarás:
- Git
- Python
- PyCharm

Primero, clonaremos este proyecto utilizando el siguiente comando en nuestra terminal:

    git clone https://github.com/isaeme23/TallerAI.git

Luego, abriremos el proyecto usando PyCharm e instalaremos las siguientes librerias:

- langchain
- openai version 0.27.8
- tiktoken
- requests
- pydantic
- pinecone-client

Antes de ejecutar el proyecto, es importante configurar las siguientes variables de entorno:

![Captura de Pantalla 2023-11-15 a la(s) 2 17 14 p m](https://github.com/isaeme23/TallerAI/assets/77862058/91047d6d-b0ff-4c43-a255-3ddbbbf656f4)

## Ejecutando el proyecto

En cuanto tengamos una llave valida y con suficientes creditos podremos ejecutar el archivo
main.py, que nos permitirá ver en nuestra consola de ejecución la respuesta a la consigna que
puede ser modificada. Esta pregunta se responderá teniendo como contexto los documentos
que se encuentran en la carpeta de 'docus'.

## Construcción

Para poder subir los documentos de la carpeta 'docus' a la plataforma de pinecone para ser
usados como contexto, utilizamos la funcion de 'load' para subir los documentos con ayuda de chunks,
asi se almacenarian en una base de datos de vectores en donde podriamos usarlos para nuestro RAG.

## Autores
Isabella Manrique 🎄

## Versión
1.0-SNAPSHOT

## Licencia
GNU - General Public License Family

## Agradecimientos
Profe Luis Daniel Benavides Navarro

David Esteban Useche, Lider Técnico de Sainapsis Inc.
