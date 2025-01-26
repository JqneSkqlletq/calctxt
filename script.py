def calculate_expression():
    try:

        with open("calc.txt", "r") as file:
            expression = file.read().strip()

        result = eval(expression)

        with open("calc.txt", "a") as file:
            file.write(f"={result}")

        print(f"Выражение вычислено: {expression} = {result}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    calculate_expression()
