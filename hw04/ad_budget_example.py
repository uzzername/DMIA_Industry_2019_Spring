#coding=utf-8

from sklearn.linear_model import LinearRegression 
from sklearn.ensemble import BaggingRegressor
from scipy.optimize import minimize
import numpy as np


# Ваш email, который вы укажете в форме для сдачи
AUTHOR_EMAIL = 'ivanov@gmail.com'


class Optimizer:
    def __init__(self):
        pass

    def optimize(self, origin_budget):
        default_target = self.model.predict([origin_budget])[0]
        random_gen = np.random.RandomState(42)
        best_budget = origin_budget

        for _ in range(2000):
            mask = (random_gen.randint(0, 3, size=len(origin_budget)) - 1) * 0.01 + 1
            new_budget = origin_budget * mask
            if self.model.predict([new_budget])[0] >= default_target and np.sum(best_budget) > np.sum(new_budget):
                best_budget = new_budget

        return best_budget

    def fit(self, X_data, y_data):
        #self.model = LinearRegression().fit(X_data, y_data)
        self.model = BaggingRegressor(LinearRegression(), n_estimators=10, max_samples=1.0, max_features=10, bootstrap=False).fit(X_data, y_data)
