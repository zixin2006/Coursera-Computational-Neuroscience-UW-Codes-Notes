<font face = 'Palatino'>

1. **Likelihood ratio test with asymmetric costs**
Given two univariate distribution functions for $s_1$ and $s_2$
$$\begin{align*}
p_1(s)&=\frac{1}{\sqrt{2\pi \cdot 0.5^2}}\exp(\frac{-(s-5)^2}{2\times 0.5^2}) \\ 
p_2(s)&=\frac{1}{\sqrt{2\pi \cdot 1^2}}\exp(\frac{-(s-7)^2}{2\times 1^2})
\end{align*}$$
By finding the value of $z$ that minimizes loss functon below:
$$\begin{align} L(z)&=L_-p(r\geq z|-)+L_+p(r<z|+)
\\ &=2\int_z^{+\infty}p_1(s)ds + \int_{-\infty}^z p_2(s)ds\end{align}$$
We've determined the best threshold that results in the smallest actual loss of choice. By iteration (using computer), $z=0.978$.

2 & 3 & 4. **ML Inference and MAP Inference**

Let $p(+)$ denote the prbability of being tested positive ($p(+)=1/100$ million), $p(-)$ the probability of being tested negative, and $r_+$, $r_-$ representing the results of illness tests, we have
$$p(+|r_+)=\frac{p(r_+|+)p(+)}{p(r_+)}$$
Looking at likelihood $p(r_+|+)$, since it equals 0.99. we will almost certainly deduce that this patient is positive. However, when considering a posteriori, we multiply this 0.99 by $p(+)$, which is a very small value, 1 divided by 1 million. Based on this consideration, we'd best not to diagnose this patient as positive. We see a difference between the two criteria because MAP incorporates prior distribution, which is very low in our case.

Therefore, the answers are 2. positive, 3. negative, 4. prior distribution.