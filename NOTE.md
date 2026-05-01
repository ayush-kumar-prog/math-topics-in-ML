### This file contains summary notes of double descent phenomenon
##### Created by Jacob


## Note
- 


## Double Descent
- ### Model-wise Double Descent
- ### Epoch-wise Double Descent
- ### Sample-wise Non-monotonicity
    - Number of training samples $n$ is varied
    - Increasing $n$ reduces the area under the curve in the graph of test error against model complexity
        - Area of the curve can be thought as the total test error of all model complexities
        - More data overall reduces model performance
    - Increasing $n$ shifts the curve to the right in the graph of test error against model complexity
        - There is a region where for the same model complexity, the models trained with more data have a worse performance
    - Conclusion: more data hurt
- ### Effective Model Complexity
    $$
    \text{EMC}_{D, \epsilon}(T) := \max \left\{ n \mid \mathbb{E}_{S \sim D^n} [\text{Error}_S(T(S))] \le \epsilon \right\}
    $$


## Resource
- [Main paper](https://iopscience.iop.org/article/10.1088/1742-5468/ac3a74/pdf)