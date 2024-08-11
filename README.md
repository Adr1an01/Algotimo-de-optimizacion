# Descenso de gradiente



# Tamaños de paso
Para la implemetnación de los tamaños de pasos se consideró funciones de $3$ variables

## Búsquead de Armijo
Dados $s, \beta, \sigma$ con $0<\beta<1$, $0<\sigma<1$, definir: 

$$\lambda_k = s\beta^{m_k}, d^k = -\nabla f(x_k)$$

Donde $m_k$ es el menor entero no negativo en :

$$f(x_k)-f(x^k+s\beta^{m_k} d^k) \geq -\sigma \beta^{m_k} s \nabla f(x_k)^T d^k$$

- **Implementación de Búsqueda de Armijo**: [`armijo.py`](Adr1an01/Algotimo-de-optimizacion/Step%20Size/armijo.py).



## Búsqueda unidimensional
$$\lambda_k \in  \text{arg min}\{f(x^k-\lambda \nabla f(x^k)); \quad \lambda\geq 0\}$$


- **Implementación de Búsqueda unidimensional**: [`unidimensional.py`](Adr1an01/Algotimo-de-optimizacion/Step%20Size/unidimensional.py).

