# exeggecutor-katas

Mantiene alas pruebas, soluciones y comandos de disntitos problemas.
Inicialmente contiene 2 katas:
 - FizzBuzz
 - RSA.

Este repositorio mantiene compatibilidad con python 2 y 3.

## Instalación

Clona el repositorio y crea un virtualenv para poder instalar las despendencias.

```
git clone https://github.com/zoek1/exeggecutor-katas.git
```

```console
cd eggecutor-katas
pip install -r requirements.txt
```

## Uso

Puedes hacer uso del comando `exeggutor` el vual se encuentra en la carpeta `bin`.
Sus funciones principales son listas, ejecutar y testear las katas del repositorio
que cumple con un determinado formato.


### Listado, Ejecución y Pruebas

Muestra las katas disponibles a ejecutar y testear.

```console
bin/exeggutor l
```

La kata que se ejecuta por defecto es fizzbuzz, pero puedes indicar el nombre de la
carta despues del typo comando `test|t` or `run|r`.

```console
bin/exeggutor test # ejecuta por defecto  fizzbuzz
bin/exeggutor t rsa
```

La ejecución es similar a la interfaz de pruebas.
