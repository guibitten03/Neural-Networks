import numpy as np


def bipolar_step(input):
    output = 1 if input >= 0 else -1
    return output