import csv
class Empleado:
    def __init__(self, nombre, apellido, edad, salario, deducciones, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario
        self.deducciones = deducciones
        self.genero = genero

    def get_edad(self):
        return self.edad

    def get_salario(self):
        return self.salario

    def get_deducciones(self):
        return self.deducciones

    def get_genero(self):
        return self.genero


def read_file(archivo):
    with open(archivo, "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader, None)  # Omitir la cabecera
        return [Empleado(*row) for row in reader]


def persona_mayor_edad(empleados):
    return max(empleados, key=lambda empleado: empleado.edad)


def persona_menor_edad(empleados):
    return min(empleados, key=lambda empleado: empleado.edad)


def cantidad_hombres(empleados):
    return sum(1 for empleado in empleados if empleado.genero == "Masculino")


def cantidad_mujeres(empleados):
    return len(empleados) - cantidad_hombres(empleados)


def promedio_salario(empleados):
    salarios = [float(empleado.salario) for empleado in empleados]
    return sum(salarios) / len(salarios)



def persona_mas_deducciones(empleados):
    return max(empleados, key=lambda empleado: empleado.deducciones)


def persona_mas_ganadora(empleados):
    # Convierte salario y deducciones a números
    empleados_numericos = [
        Empleado(
            empleado.nombre,
            empleado.apellido,
            empleado.edad,
            float(empleado.salario),
            float(empleado.deducciones),
            empleado.genero
        )
        for empleado in empleados
    ]

    # Encuentra la persona con mayor salario - deducciones
    return max(empleados_numericos, key=lambda empleado: empleado.salario - empleado.deducciones)


if __name__ == "__main__":
    empleados = read_file("empleados.csv")

    persona_mayor_edad_result = persona_mayor_edad(empleados)
    print("Persona con mayor edad:", persona_mayor_edad_result.nombre, persona_mayor_edad_result.apellido, persona_mayor_edad_result.edad)

    persona_menor_edad_result = persona_menor_edad(empleados)
    print("Persona con menor edad:", persona_menor_edad_result.nombre, persona_menor_edad_result.apellido, persona_menor_edad_result.edad)

    cantidad_hombres_result = cantidad_hombres(empleados)
    print("Cantidad de hombres:", cantidad_hombres_result)

    cantidad_mujeres_result = cantidad_mujeres(empleados)
    print("Cantidad de mujeres:", cantidad_mujeres_result)

    promedio_salario_result = promedio_salario(empleados)
    print("Promedio de salario:", promedio_salario_result)

    persona_mas_deducciones_result = persona_mas_deducciones(empleados)
    print("Persona con más deducciones:", persona_mas_deducciones_result.nombre, persona_mas_deducciones_result.apellido, persona_mas_deducciones_result.deducciones)

    persona_mas_ganadora_result = persona_mas_ganadora(empleados)
    print("Persona que gana más:", persona_mas_ganadora_result.nombre, persona_mas_ganadora_result.apellido, persona_mas_ganadora_result.salario)

