### Instalar lldb
```
sudo apt install lldb
```
### Compilar con información de depuración
```
gcc -g3 programa.c -o programa
```
### Breakpoint en main
```
lldb ./programa
(lldb) breakpoint set --name main
(lldb) run
```
### Ejecución paso a paso
```
next      # siguiente línea (no entra en funciones)
step      # entra en la función
finish    # salir de función
continue  # continuar
quit      # salir
```
### Inspeccionar variables
```
frame variable # variables locales
expr x         # imprime el valor de x
```
### Breakpoints estratégicos
```
breakpoint set --file programa.c --line 42
```
### Condiciones para encontrar errores lógicos
- Ejemplo : Supón que esperabas que i nunca fuese negativo. Puedes hacer:
```
breakpoint set --file programa.c --line 60 --condition "i < 0"
```


# Code Sanatizer

- AddressSanitizer
```-fsanitize=address```
- LeakSanitizer
```-fsanitize=leak ```
- UndefinedBehavior
```-fsanitize=undefined```
- ThreadSanitizer
```-fsanitize=thread```

<https://en.wikipedia.org/wiki/Code_sanitizer>


# Uso básico de Valgrind

| Propósito                         | Comando básico                                                    | Descripción                                                                |
|-----------------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------|
| Análisis general de memoria       | `valgrind ./programa`                                             | Detecta errores comunes de memoria (lecturas/escrituras inválidas, fugas)  |
| Detectar fugas de memoria         | `valgrind --leak-check=full ./programa`                           | Reporta fugas de memoria con información detallada                         |
| Mostrar trazas de pila completas  | `valgrind --leak-check=full --show-leak-kinds=all ./programa`     | Muestra todos los tipos de fugas, incluyendo trazas de pila detalladas     |
| Ignorar errores de ciertas libs   | `valgrind --leak-check=full --gen-suppressions=all ./programa`    | Genera reglas para ignorar errores conocidos (falsos positivos)            |
| Guardar salida a archivo          | `valgrind --log-file=valgrind.log ./programa`                     | Guarda la salida de Valgrind en un archivo en lugar de la consola          |
| Ver memoria no inicializada       | `valgrind --track-origins=yes ./programa`                         | Muestra el origen de la memoria no inicializada usada                      |
| Comprobar uso de memoria por función | `valgrind --tool=massif ./programa`                            | Analiza el uso de memoria dinámica a lo largo del tiempo con **Massif**    |
| Visualizar output de Massif       | `ms_print massif.out.pid`                                         | Muestra el reporte generado por Massif en formato legible                  |
| Comprobar condiciones de carrera  | `valgrind --tool=helgrind ./programa`                             | Detecta errores de sincronización y condiciones de carrera entre hilos     |

