import pandas as pd
import numpy as np

from scipy.stats import norm, chi


chat_id = 415542660 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    n = len(x)
    scale = ( x * x ).sum() / n
    return scale * (n - 1) / chi.ppf(alpha, n - 1), \
           nscale * (n - 1) / chi.ppf(alpha /2, n - 1)
