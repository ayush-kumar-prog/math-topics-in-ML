### This file contains summary notes of double descent phenomenon
##### Created by Jacob


## Note
- Double descent is not the same as [Grokking](https://en.wikipedia.org/wiki/Grokking_(machine_learning))
    - There is only one descent in grokking


## Double Descent
- According to [this paper](https://iopscience.iop.org/article/10.1088/1742-5468/ac3a74/pdf)
- ### Model-wise Double Descent
    - Only model complexity/size is varied
    - Increasing model complexity first reduces test error, which then increases test error followed by another drop in test error (double descent)
    - Increasing model complexity always reduces training error
        - After the interpolation threshold, train error is approximately $0$
    - #### Intuition
        - For model sizes at the interpolation threshold, there is effectively only one model that fits the training data and this model is very sensitive to noise in training data
            - This model is barely able to fit the training data and thus, has a high test error
        - For model sizes beyond the interpolation threshold, there are many interpolating models that fit the training data and SGD is able to find one that both "memorises" the noise in the training data and performs well on the distribution (e.g. testing), giving a low test error
    - Fully understanding the mechanism behind model-wise double descent remains an open question though
- ### Epoch-wise Double Descent
    - Only number of training epochs is varied
    - Increasing epoch first reduces test error, which then increases test error (overfitting) followed by another drop in test error (double descent)
    - Increasing epoch always reduces training error
        - After the interpolation threshold, train error is approximately $0$
- ### Sample-wise Non-monotonicity
    - Number of training samples $n$ is varied
    - Increasing $n$ reduces the area under the curve in the graph of test error against model complexity
        - Area of the curve can be thought as the total test error of all model complexities
        - More data overall improves model performance
    - Increasing $n$ shifts the curve to the right in the graph of test error against model complexity
        - There is a region where for the same model complexity, the models trained with more data have a worse performance
    - Conclusion: more data hurt
- ### Impact of Noise
    - More noise makes the double-descent phenomenon more visible
- ### Effective Model Complexity
    $$
    \text{EMC}_{D, \epsilon}(T) := \max \left\{ n \mid \mathbb{E}_{S \sim D^n} [\text{Error}_S(T(S))] \le \epsilon \right\}
    $$
    - The maximum number of training samples such that the expected model's training error is approximately $0$ ($\mathbb{E}_{S \sim D^n} [\text{Error}_S(T(S))] \le \epsilon$)
    - Assume *more data hurt*
    - It is *maximum* because if you have more data, the model needs more epochs to achieve the same optimisation progress


## Resource
- [Main paper](https://iopscience.iop.org/article/10.1088/1742-5468/ac3a74/pdf)
- [Wikipedia on Double Descent](https://en.wikipedia.org/wiki/Double_descent)