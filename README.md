# Symmetric runs in Binary Sequences

Given a base $b$ sequence $s = (s_1, \dots, s_n)$, perform the following process. Find the largest $i$ so that $(s_1, s_2, \dots, s_i)$ is symmetric. Continue by finding the largest $j$ so that $(s_{i+1}, s_{i+2}, \dots, s_{j})$ is symmetric. Repeat until $s_n$ is part of a symmetric subsequence. 

For example, the binary sequence 
$$s = (1,1,0,1,0,0)$$
is of length $6$ and returns $3$, as the symmetric subsequences are $(1,1), (0,1,0), (0)$.

Let $m_{b,n}$ be the maximal number of symmetric subsequences for a base $b$ sequence of length $n$.It is not too hard to show that for $b>2$, we have $m_{b,n} = n$. Interestingly, for $b=2$ we have $m_{2,n} = \lfloor \frac{3n+10}{7} \rfloor.$ 

This project proves this claim and computes values of $m_{b,n}.$
