from src.util.calculator import Calculator
from src.view.view import Viewer
from src.data.data import Data


class Controller:

    viewer = Viewer()
    data = Data()

    def __init__(self):
        pass

    def run(self):
        calc = Calculator()

        for i in self.data:
            self.viewer.print(f'Вычисляем: \'{i}\' = {calc.calculate(i)} - результат: {eval(i)}')