import logging
logging.basicConfig(filename="log_test.log", level=logging.DEBUG, 
                    format="%(levelname)s:%(asctime)s:%(filename)s:%(message)s")

def mutiply(n, x):
    return n * x
num1 = 3
num2 = 8
logging.debug(f"mul {num1}, {num2} = {mutiply(num1, num2)}")