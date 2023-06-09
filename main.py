
import time

def measure_time(func):
    def wrapper(a, b):
        print(f'Function {func.__name__} started at {time.strftime("%H:%M:%S")}')
        print(f'Sides of the triangle: a={a}, b={b}')
        result = func(a, b)
        print(f'Result: {result}')
    return wrapper

@measure_time
def calculate_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c

if __name__ == '__main__':
    a = float(input("Введите первый катет a: "))
    b = float(input("Введите первый катет b: "))
    calculate_hypotenuse(a, b)


