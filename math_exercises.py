import random


def generate_addition(max_digits=4):
    max_value = 10**max_digits - 1
    a = random.randint(0, max_value)
    b = random.randint(0, max_value)
    return a, b, a + b


def generate_subtraction(max_digits=4):
    max_value = 10**max_digits - 1
    a = random.randint(0, max_value)
    b = random.randint(0, a)  # ensure non-negative result
    return a, b, a - b


OPERATIONS = {
    '+': generate_addition,
    '-': generate_subtraction,
}


def main():
    print("Bienvenido al juego de matemáticas!")
    while True:
        op = random.choice(list(OPERATIONS.keys()))
        a, b, result = OPERATIONS[op]()
        user_input = input(f"Cuánto es {a} {op} {b}? (o escribe 'salir' para terminar) ")
        if user_input.strip().lower() == 'salir':
            print("Gracias por jugar!")
            break
        try:
            user_answer = int(user_input)
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        if user_answer == result:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es {result}.")


if __name__ == '__main__':
    main()
