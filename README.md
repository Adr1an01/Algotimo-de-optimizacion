# Descenso de gradiente



# Tamaños de paso
Para la implemetnación de los tamaños de pasos se consideró función de $3$ variables

## Búsquead de Armijo
Dados $s, \beta, \sigma$ con $0<\beta<1$, $0<\sigma<1$, definir: 

$$\lambda_k = s\beta^{m_k}, d^k = -\nabla f(x_k)$$

Donde $m_k$ es el menor entero no negativo en :

$$f(x_k)-f(x^k+s\beta^{m_k} d^k) \geq -\sigma \beta^{m_k} s \nabla f(x_k)^T d^k$$

- **Implementación de Búsqueda de Armijo**: [`armijo.py`](StepSize/armijo.py).



## Búsqueda unidimensional
$$\lambda_k \in  \text{arg min}\{f(x^k-\lambda \nabla f(x^k)); \quad \lambda\geq 0\}$$

Para el uso de este tipo de paso es necesario hacer :

```
        g=np.array(x0)+l*f_
        l_min=b_unidimensional(g,str(f))
```

Donde :
- f : Es la función objetivo
- f : Gradiente de la función en un punto ($\nabla$ f($x_k$))
- x0 : Es el punto $x_k$
- **Implementación de Búsqueda unidimensional**: [`unidimensional.py`](StepSize/unidimensional.py).

