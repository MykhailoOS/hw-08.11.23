import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# file = logging.FileHandler("logger.log")
# file.setLevel(logging.INFO)
# file.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

# logger.addHandler(file)
logger.addHandler(console)

#
def resources(file):
    def next_step(func):
        def inner(text):
            x = func(text)
            with open(file, "a") as f:
                logger.info("run resource decorator")
                f.write(f"{text}")
                logger.info(f"write into {file} file")
            logger.info("return func")
            return x

        return inner

    return next_step


@resources("sys.txt")
def tested(*args):
    logger.info("return *args from func")
    return f">>>> {args}"


res = tested("simple test string")
print(res)



def handle_exceptions(func):
    def error(a, b):
        try:
            func(a, b)
        except ZeroDivisionError as e:
            return f"Не можна ділити на нуль! {e}"

    return error


@handle_exceptions
def divide(a, b):
    return a / b


res = divide(5, 0)
print(res)


# Task4
import time

def measure_time(func):
    def inner():
        measure = time.time()
        return measure

    return inner


@measure_time
def some_function():
    time.sleep(2)


a = some_function()
print(a)



#Task 5
def log_arguments_results(func):
    logger.info("working with decorator")
    def next_func(a, b):
        res = func(a, b)
        logger.info(f"return a + b = {res}")
        return res
    return next_func   

@log_arguments_results
def add_numbers(a, b):
    return a + b

add_numbers(3, 4)

