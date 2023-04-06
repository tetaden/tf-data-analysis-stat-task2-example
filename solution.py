import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 415542660 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    n = len(x)
    s2 = ((x - x.mean()) ** 2).sum() / n
    return np.sqrt(s2 / (26 * chi.ppf( (1 + alpha) / 2, 2))) , np.sqrt(s2 / (26 *  chi.ppf((1 - alpha) /2, 2)))
