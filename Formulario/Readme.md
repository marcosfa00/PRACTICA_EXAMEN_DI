# EXPLIACIÓN FORMULARIO

## myModel & Window

Bien, como el propio subtítulo indica, para hacer un formulario, debemos crear una **clase myModel**. Aquí definiremos:

1. **Imports**: Se han importado varios módulos necesarios de PyQt6 para la interfaz gráfica.

2. **Clase myModel(QAbstractListModel)**: Esta clase es un modelo de datos personalizado que hereda de `QAbstractListModel`. Se utiliza para manejar la lógica de los datos en el formulario.

   - **Constructor (`__init__`)**: Inicializa la clase, esperando una lista de tareas. Si no se proporciona, se crea una lista vacía.

   - **Método `data`**: Se utiliza para obtener los datos asociados con un índice y un rol específicos. Devuelve el texto o el ícono asociado según el rol solicitado.

   - **Método `rowCount`**: Devuelve el número de filas en el modelo, que es igual a la longitud de la lista de tareas.

3. **Uso de la clase `myModel` en el formulario (a completar)**: A continuación, se implementará la ventana (`Window`) que utilizará este modelo para mostrar datos en un formulario. 

## de Window no dimos nada nuevo

Asique simplemente vamos a repetir la ventana del primer examen para practicar
