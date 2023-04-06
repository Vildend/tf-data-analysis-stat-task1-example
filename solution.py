import pandas as pd
import numpy as np
import scipy.special

chat_id = 897901830

def solution(x: np.array) -> float:
    t = 22
    l = x.mean()
    return (np.power(l * t, len(x)) * np.exp(-(l * t))) / scipy.special.factorial(len(x))
