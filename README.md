# 🧮 Calculadora Mejorada

Una calculadora interactiva en Python que opera desde la consola y permite realizar operaciones matemáticas básicas ( suma y multiplicación) y validaciones numéricas. 
Este proyecto promueve buenas prácticas de programación, pruebas automatizadas así como herramientas de calidad de código.

## 📦 Contenido del Proyecto

- `main.py`: Lógica principal de la calculadora y menú interactivo.
- `test_.py`: Pruebas unitarias para validar el comportamiento de las funciones.
- Documentación técnica y guía de instalación de herramientas.

## 🚀 Funcionalidades

La calculadora incluye las siguientes funciones:

| Función                       | Descripción                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `addmultiplenumbers(lista)`   | Suma todos los números de una lista. Devuelve 0 si está vacía.              |
| `multiplymultiplenumbers(lista)` | Multiplica todos los números de una lista. Devuelve 1 si está vacía.        |
| `isiteven(numero)`            | Verifica si un número es par (y entero).                                   |
| `isitaninteger(numero)`       | Verifica si un número es entero, incluyendo flotantes sin decimales (ej. 3.0). |


## Instalar dependencias 
```
pip install pytest pytest-cov black flake8 isort mypy
```
## Ejecutar el programa 
```
python main.py
```
## 🧪 Pruebas
Las pruebas están definidas en test_.py y cubren todos los casos relevantes
```
pytest
```
Para ver la covertura del codigo
```
pytest --cov
```
## 🛠️ Herramientas de Calidad

| Herramienta  | Uso                                                             |
|--------------|------------------------------------------------------------------|
| `black`      | Formato automático del código: `black .`                         |
| `flake8`     | Revisión de estilo y sintaxis: `flake8`                          |
| `isort`      | Ordenamiento de imports: `isort main.py test_.py`               |
| `mypy`       | Verificación de tipos estáticos: `mypy main.py test_.py`        |
| `pytest`     | Ejecución de pruebas: `pytest`                                   |
| `pytest-cov` | Medición de cobertura: `pytest --cov`                            |

## 📋 Buenas Prácticas
- Validación de entradas (listas vacías, números decimales).
- Mensajes claros para el usuario.
- Cobertura de pruebas del 100% en test_.py.

## 🤖 Uso de IA
Se utilizó IA para investigar el uso de herramientas como pytest, black y para estructurar la documentación técnica, facilitando la automatización y estandarización del proyecto.

Desarrollado con 💡 por Fernando.

