### This file contains summary notes of double descent phenomenon
##### Created by Jacob


## Note
- 


## Double Descent
- According to [this paper](https://iopscience.iop.org/article/10.1088/1742-5468/ac3a74/pdf)
- ### Model-wise Double Descent
    - Model complexity/size is varied
    - Increasing model complexity first reduces test error, which then increases (overfitting) followed by a drop (double descent)
    - Increasing model complexity always reduces training error
        - After the interpolation threshold, train error is approximately $0$
    - #### Intuition
        - For model sizes at the interpolation threshold, there is effectively only one model that fits the training data and this model is very sensitive to noise in training data
            - This model is barely able to fit the training data and thus, has a high test error
        - For model sizes beyond the interpolation threshold, there are many interpolating models that fit the training data and SGD is able to find one that both "memorises" the noise in the training data and performs well on the distribution (e.g. testing), giving a low test error
    - Fully understanding the mechanism behind model-wise double descent remains an open question though
- ### Epoch-wise Double Descent
- ### Sample-wise Non-monotonicity
    - Number of training samples $n$ is varied
    - Increasing $n$ reduces the area under the curve in the graph of test error against model complexity
        - Area of the curve can be thought as the total test error of all model complexities
        - More data overall reduces model performance
    - Increasing $n$ shifts the curve to the right in the graph of test error against model complexity
        - There is a region where for the same model complexity, the models trained with more data have a worse performance
    - Conclusion: more data hurt
- ### Impact of Noise
    - More noise makes the double-descent phenomenon more visible
- ### Effective Model Complexity
    $$
    \text{EMC}_{D, \epsilon}(T) := \max \left\{ n \mid \mathbb{E}_{S \sim D^n} [\text{Error}_S(T(S))] \le \epsilon \right\}
    $$


## Resource
- [Main paper](https://iopscience.iop.org/article/10.1088/1742-5468/ac3a74/pdf)