import itertools
import numpy as np

from ..utilities import check_kwargs
from .problem import Problem
from .qubo import QUBO

class QuadraticKnapsack(Problem):
    """
    Creates an instance of the Quadratic Knapsack problem.

    Parameters
    ----------
    values: List[List[int]]
        The matrix values of the items that can be placed in the knapsack.
    weights: List[int]
        The weight of the items that can be placed in the knapsack.
    weight_capacity: int
        The maximum weight the knapsack can hold.
    penalty: float
        Penalty for the weight constraint.

    Returns
    -------
        An instance of the Knapsack problem.
    """

    __name__ = "quadratic_knapsack"

    def __init__(self, values, weights, weight_capacity, penalty):
        # Check whether the input is valid. Number of values should match the number of weights.
        if len(values) != len(weights):
            raise ValueError("Number of items does not match given value and weights")

        for v_i in values:
            if len(v_i) != len(weights):
                raise ValueError("Number of items does not match given value and weights")

        self.values = values
        self.weights = weights
        self.weight_capacity = weight_capacity
        self.penalty = penalty
        self.n_items = len(weights)


