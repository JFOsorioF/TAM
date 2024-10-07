# Ejercicios

### Varianza:

$$
\begin{align*}

\mathbb{E}\left\{ (x-\mu_{x})^{2} \right\} &= \int (x-\mu_{x})^{2} p(x) \, dx  \\
 & = \int (x^{2}-2x\mu_{x} + \mu_{x}^{2})p(x)  \, dx  \\
 & = \int x^{2}p(x) \, dx -2 \mu_{x}\int xp(x)   \, dx +\int \mu_{x}^{2}p(x) \, dx \\
 & = \mathbb{E}\left\{ x^{2} \right\} - 2\mathbb{E}\left\{ x \right\} \mathbb{E}\left\{ x \right\} +\mathbb{E}\left\{ \mathbb{E}^{2}\left\{ x \right\}  \right\}  \\
 & = \mathbb{E}\left\{ x^{2} \right\} - 2\mathbb{E}^{2}\left\{ x \right\}  +\mathbb{E}\left\{ \mathbb{E}^{2}\left\{ x \right\}  \right\}  \\
 & = \mathbb{E}\left\{ x^{2} \right\} - 2\mathbb{E}^{2}\left\{ x \right\}  + \mathbb{E}^{2}\left\{ x \right\}   \\
 & =\mathbb{E}\left\{ x^{2} \right\} -\mathbb{E}^{2} \left\{ x \right\}  
\end{align*}
$$

### Covarianza:

$$
\begin{align*}

\text{Cov}\left\{  x, y \right\}&=\mathbb{E}\left\{ (x-\mu_{x})(y-\mu_{y}) \right\} \\
 & = \mathbb{E}\left\{ xy-x\mu_{y}-y\mu_{x} +\mu_{y}\mu_{x} \right\}  \\
 & = \mathbb{E}\left\{ xy \right\} - \mathbb{E}\left\{ x\mu_{y} \right\} -\mathbb{E}\left\{ y\mu_{x} \right\} +\mathbb{E}\left\{ \mu_{y}\mu_{x} \right\}  \\
 & = \mathbb{E}\left\{ xy \right\} - \mu_{y}\mathbb{E}\left\{ x \right\} -\mu_{x}\mathbb{E}\left\{ y \right\} +\mu_{x}\mu_{y} \\
 & = \mathbb{E}\left\{ xy \right\} - 2\mathbb{E}\left\{ x \right\} \mathbb{E} \left\{ y \right\}  +\mathbb{E}\left\{ x \right\} \mathbb{E} \left\{ y \right\}\\
 & = \mathbb{E}\left\{ xy \right\} - \mathbb{E}\left\{ x \right\} \mathbb{E} \left\{ y \right\}  
\end{align*}
$$

### Covarianza Vectorial:

$$
\begin{align*}
\text{Cov}(\mathbf{X}, \mathbf{Y}) &= \mathbb{E}[(\mathbf{X} - \mathbb{E}[\mathbf{X}])(\mathbf{Y} - \mathbb{E}[\mathbf{Y}])^\top] \\
&= \mathbb{E}[\mathbf{X} \mathbf{Y}^\top - \mathbf{X} \mathbb{E}[\mathbf{Y}]^\top - \mathbb{E}[\mathbf{X}] \mathbf{Y}^\top + \mathbb{E}[\mathbf{X}] \mathbb{E}[\mathbf{Y}]^\top] \\
&= \mathbb{E}[\mathbf{X} \mathbf{Y}^\top] - \mathbb{E}[\mathbf{X}] \mathbb{E}[\mathbf{Y}]^\top
\end{align*}
$$

### Deravacion de la media $\mu$ de la Gaussiana:

La media $\mu$ de la distribución gaussiana es el valor esperado $\mathbb{E}[x]$:

$$
\mathbb{E}[x] = \int_{-\infty}^{\infty} x \, p(x) \, dx
$$

Sustituyendo la función de densidad de probabilidad (PDF) de la distribución gaussiana:

$$
\mathbb{E}[x] = \int_{-\infty}^{\infty} x \, \frac{1}{\sqrt{2 \pi \sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right) dx
$$

Para evaluar esta integral:

   Cambio de variable: Sea $y = x - \mu$ (por lo tanto $dy = dx$). Esto centra la gaussiana en 0.

$$
\mathbb{E}[x] = \int_{-\infty}^{\infty} (y + \mu) \, \frac{1}{\sqrt{2 \pi \sigma^2}} \exp\left(-\frac{y^2}{2\sigma^2}\right) dy
$$

Dividimos la integral:

$$
\mathbb{E}[x]  = \frac{1}{\sqrt{2 \pi \sigma^2}} \int_{-\infty}^{\infty} y \, \exp\left(-\frac{y^2}{2\sigma^2}\right) dy + \frac{\mu}{\sqrt{2 \pi \sigma^2}} \int_{-\infty}^{\infty} \exp\left(-\frac{y^2}{2\sigma^2}\right) dy
$$

La primera integral (la que involucra $y$) es cero porque es la integral de una función impar sobre un intervalo simétrico:

$$
\int_{-\infty}^{\infty} y \, \exp\left(-\frac{y^2}{2\sigma^2}\right) dy = 0
$$

La segunda integral es simplemente la normalización de la distribución gaussiana, que es igual a $1$:

$$
\frac{\mu}{\sqrt{2 \pi \sigma^2}} \int_{-\infty}^{\infty} \exp\left(-\frac{y^2}{2\sigma^2}\right) dy = \mu
$$

Por lo tanto:

$$
\mathbb{E}[x]  = \mu
$$

### Deravacion de la varianza $\sigma^{2}$ de la Gaussiana:

La varianza de $X$ se define como:

$$
\text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2]
$$

Dado que $\mathbb{E}[X] = \mu$, esto se simplifica a:

$$
\text{Var}(X) = \mathbb{E}[(X - \mu)^2]
$$

Expandiendo el cuadrado:

$$
\text{Var}(X) = \mathbb{E}[(X - \mu)^2] = \mathbb{E}[X^2 - 2\mu X + \mu^2]
$$

Usando la linealidad de la esperanza:

$$
\text{Var}(X) = \mathbb{E}[X^2] - 2\mu \mathbb{E}[X] + \mathbb{E}[\mu^2]
$$

Dado que $\mathbb{E}[X] = \mu$ y $\mu^2$ es una constante, tenemos:

$$
\text{Var}(X) = \mathbb{E}[X^2] - 2\mu^2 + \mu^2
$$

Esto se simplifica a:

$$
\text{Var}(X) = \mathbb{E}[X^2] - \mu^2
$$

Como se discutió anteriormente, para una distribución gaussiana $X$, el segundo momento es:

$$
\mathbb{E}[X^2] = \sigma^2 + \mu^2
$$

Sustituye esto en la ecuación de la varianza:

$$
\text{Var}(X) = (\sigma^2 + \mu^2) - \mu^2
$$

Simplificando:

$$
\text{Var}(X) = \sigma^2
$$

### Distribuciones Condicionales Gaussianas:

Dado:

$$
\mathbf{x} = \begin{bmatrix}
\mathbf{x}_{a}  \\
\mathbf{x}_{b}
\end{bmatrix}, \quad \boldsymbol{\mu}=\begin{bmatrix}
\boldsymbol{\mu}_{a} \\
\boldsymbol{\mu}_{b} 
\end{bmatrix}, \quad \boldsymbol{\Sigma}=\begin{bmatrix}
\boldsymbol{\Sigma}_{aa} & \boldsymbol{\Sigma}_{ab} \\
\boldsymbol{\Sigma}_{ba} & \boldsymbol{\Sigma}_{bb}
\end{bmatrix}, \quad \boldsymbol{\Sigma}_{ab}=\boldsymbol{\Sigma}_{ba}^\top
$$

Queremos encontrar $p(\mathbf{x}_{b}|\mathbf{x}_{a})$ dado que $p(\mathbf{x})=p([\mathbf{x}_{a}, \mathbf{x}_{b}])$

$$
p(\mathbf{x}_{b}|\mathbf{x}_{a})=\mathcal{N}(\mathbf{x}_{b}|\boldsymbol{\mu}_{b|a}, \boldsymbol{\Sigma}_{b|a})
$$

Sabemos que:

$$
-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu} )^\top \boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})  = -\frac{1}{2}\mathbf{x}^\top \boldsymbol{\Sigma}^{-1}\mathbf{x} + \frac{1}{2} \mathbf{x}^\top \boldsymbol{\Sigma}^{-1}\boldsymbol{\mu} + \text{cte}
$$

Por lo tanto podemos dividir la expresion en una parte cuadratica, una parte lineal y una parte constante. Expandiendo obtenemos:

$$
\begin{align*}
=& -\frac{1}{2}\mathbf{x}_{a}^\top \boldsymbol{\Lambda}_{aa}\mathbf{x}_{a}+\mathbf{x}_{a}^\top\boldsymbol{\Lambda}_{aa}\boldsymbol{\mu}_{a}-\frac{1}{2}\boldsymbol{\mu}_{a}^\top\boldsymbol{\Lambda}_{aa}\boldsymbol{\mu}_{a} \\
 & -\frac{1}{2}\mathbf{x}_{b}^\top \boldsymbol{\Lambda}_{ba}\mathbf{x}_{a}+\mathbf{x}_{b}^\top\boldsymbol{\Lambda}_{ba}\boldsymbol{\mu}_{a}+\frac{1}{2}\boldsymbol{\mu}_{b}^\top\boldsymbol{\Lambda}_{ba}\mathbf{x}_{a}-\frac{1}{2}\boldsymbol{\mu}_{b}^\top\boldsymbol{\Lambda}_{ba}\boldsymbol{\mu}_{a} \\
 & -\frac{1}{2}\mathbf{x}_{a}^\top \boldsymbol{\Lambda}_{ab}\mathbf{x}_{b}+\mathbf{x}_{a}^\top\boldsymbol{\Lambda}_{ab}\boldsymbol{\mu}_{b}+\frac{1}{2}\boldsymbol{\mu}_{a}^\top\boldsymbol{\Lambda}_{ab}\mathbf{x}_{b}-\frac{1}{2}\boldsymbol{\mu}_{a}^\top\boldsymbol{\Lambda}_{ab}\boldsymbol{\mu}_{b} \\
& -\frac{1}{2}\mathbf{x}_{b}^\top \boldsymbol{\Lambda}_{bb}\mathbf{x}_{b}+\mathbf{x}_{b}^\top\boldsymbol{\Lambda}_{bb}\boldsymbol{\mu}_{b}-\frac{1}{2}\boldsymbol{\mu}_{b}^\top\boldsymbol{\Lambda}_{bb}\boldsymbol{\mu}_{b} 
\end{align*}
$$

Queremos encontrar los parametros $\boldsymbol{\mu}_{b|a}$ y $\boldsymbol{\Sigma}_{b|a}$ que definen $p(\mathbf{x}_{b}|\mathbf{x}_{a})$ cuando $\mathbf{x}_{a}$ es una constante, por lo tanto no tomamos en cuanta los terminos que dependen de $\mathbf{x}_{b}$

$$
\begin{align*}
=& \cancel{ -\frac{1}{2}\mathbf{x}_{a}^\top \boldsymbol{\Lambda}_{aa}\mathbf{x}_{a} }+\cancel{ \mathbf{x}_{a}^\top\boldsymbol{\Lambda}_{aa}\boldsymbol{\mu}_{a} }-\cancel{ \frac{1}{2}\boldsymbol{\mu}_{a}^\top\boldsymbol{\Lambda}_{aa}\boldsymbol{\mu}_{a} } \\
 & -\frac{1}{2}\mathbf{x}_{b}^\top \boldsymbol{\Lambda}_{ba}\mathbf{x}_{a}+\frac{1}{2} \mathbf{x}_{b}^\top\boldsymbol{\Lambda}_{ba}\boldsymbol{\mu}_{a}+\cancel{ \frac{1}{2}\boldsymbol{\mu}_{b}^\top\boldsymbol{\Lambda}_{ba}\mathbf{x}_{a} }-\cancel{ \frac{1}{2}\boldsymbol{\mu}_{b}^\top\boldsymbol{\Lambda}_{ba}\boldsymbol{\mu}_{a}  }\\
 & -\frac{1}{2}\mathbf{x}_{a}^\top \boldsymbol{\Lambda}_{ab}\mathbf{x}_{b} + \frac{1}{2}\cancel{ \mathbf{x}_{a}^\top\boldsymbol{\Lambda}_{ab}\boldsymbol{\mu}_{b} }+\frac{1}{2}\boldsymbol{\mu}_{a}^\top\boldsymbol{\Lambda}_{ab}\mathbf{x}_{b}-\cancel{ \frac{1}{2}\boldsymbol{\mu}_{a}^\top\boldsymbol{\Lambda}_{ab}\boldsymbol{\mu}_{b} } \\
& -\frac{1}{2}\mathbf{x}_{b}^\top \boldsymbol{\Lambda}_{bb}\mathbf{x}_{b}+\mathbf{x}_{b}^\top\boldsymbol{\Lambda}_{bb}\boldsymbol{\mu}_{b}-\cancel{ \frac{1}{2}\boldsymbol{\mu}_{b}^\top\boldsymbol{\Lambda}_{bb}\boldsymbol{\mu}_{b} } 
\end{align*}
$$

Sabemos que las partes cuadraticas deben ser iguales, esto nos permite hayar la matriz de covarianzas:

$$
\begin{align*}

-\frac{1}{2}\mathbf{x}^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}&=-\frac{1}{2}\mathbf{x}_{b}^\top\boldsymbol{\Lambda}_{bb}\mathbf{x}_{b} \\
\boldsymbol{\Sigma}_{b|a}^{-1}&=\boldsymbol{\Lambda}_{bb}
\end{align*}
$$

Escribiendo los terminos lineales:

$$
\begin{align*}
-\frac{1}{2}\mathbf{x}_{b}^\top \boldsymbol{\Lambda}_{ba}\mathbf{x}_{a}+ \frac{1}{2}\mathbf{x}_{b}^\top\boldsymbol{\Lambda}_{ba}\boldsymbol{\mu}_{a} -\frac{1}{2}\mathbf{x}_{a}^\top \boldsymbol{\Lambda}_{ab}\mathbf{x}_{b} + \frac{1}{2}\boldsymbol{\mu}_{a}^\top\boldsymbol{\Lambda}_{ab}\mathbf{x}_{b}+\mathbf{x}_{b}^\top\boldsymbol{\Lambda}_{bb}\boldsymbol{\mu}_{b}
\end{align*}
$$

Simplificando obtenemos:

$$
\begin{align*}

\mathbf{x}^\top_{b}\boldsymbol{\Lambda}_{ba}\boldsymbol{\mu}_{a}-\mathbf{x}^\top_{b}\boldsymbol{\Lambda}_{ba}\mathbf{x}_{a} +\mathbf{x}^\top_{b}\boldsymbol{\Lambda}_{bb}\boldsymbol{\mu}_{b} &= \mathbf{x}_{b}^\top(\boldsymbol{\Lambda}_{bb}\boldsymbol{\mu}_{b}-\boldsymbol{\Lambda}_{ba}\mathbf{x}_{a}+\boldsymbol{\Lambda}_{ba}\boldsymbol{\mu}_{a}) \\
 & =\mathbf{x}_{b}^\top(\boldsymbol{\Lambda}_{bb}\boldsymbol{\mu}_{b}+\boldsymbol{\Lambda}_{ba}(\boldsymbol{\mu}_{a}-\mathbf{x}_{a}))
\end{align*}
$$

Igualando con el termino lineal podemos despejar $\boldsymbol{\mu}_{b|a}$:

$$
\begin{align*}
\mathbf{x}_{b}^\top\boldsymbol{\Sigma}_{b|a}^{-1}\boldsymbol{\mu}_{b|a} &= \mathbf{x}_{b}^\top(\boldsymbol{\Lambda}_{bb}\boldsymbol{\mu}_{b}+\boldsymbol{\Lambda}_{ba}(\boldsymbol{\mu}_{a-}\mathbf{x}_{a})) \\
 \boldsymbol{\mu}_{b|a}& = \boldsymbol{\Sigma}_{b|a}(\boldsymbol{\Lambda}_{bb}\boldsymbol{\mu}_{b}+\boldsymbol{\Lambda}_{ba}(\boldsymbol{\mu}_{a-}\mathbf{x}_{a})) \\
 & = \boldsymbol{\Sigma}_{b|a}\boldsymbol{\Sigma}_{b|a}^{-1} \boldsymbol{\mu}_{b}+\boldsymbol{\Sigma}_{b|a}\boldsymbol{\Sigma}_{ba}^{-1}(\boldsymbol{\mu}_{a}-\mathbf{x}_{a}) \\ \\

 \boldsymbol{\mu}_{b|a}& = \boldsymbol{\mu}_{b}+\boldsymbol{\Lambda}_{bb}^{-1}\boldsymbol{\Lambda}_{ba}(\boldsymbol{\mu}_{a}-\mathbf{x}_{a})
\end{align*}
$$

Ahora queremos tener $\boldsymbol{\mu}_{b|a}$ y $\boldsymbol{\Sigma}_{b|a}$ en terminos de la matriz de covarianza $\boldsymbol{\Sigma}$, para esto podemos utilizar la siguiente igualdad:

$$
\begin{bmatrix}
\mathbf{A} & \mathbf{B}  \\
\mathbf{C} & \mathbf{D} 
\end{bmatrix}^{-1}=\begin{bmatrix}
\mathbf{M} & -\mathbf{M}\mathbf{B}\mathbf{D}^{-1} \\
-\mathbf{D}^{-1}\mathbf{C}\mathbf{M} & \mathbf{D}^{-1}+\mathbf{D}^{-1}\mathbf{C}\mathbf{M}\mathbf{B}\mathbf{D}^{-1}
\end{bmatrix}
$$

Donde:

$$
\mathbf{M} = (\mathbf{A}-\mathbf{B}\mathbf{D}^{-1}\mathbf{C})^{-1}, \quad \mathbf{M}\mathbf{M}^{-1}=\mathbf{I}=\mathbf{M}^{-1}\mathbf{M}
$$

Para la covarianza:

$$
\begin{align*}

\boldsymbol{\Sigma}_{b|a}&=\boldsymbol{\Lambda}_{bb}^{-1} \\ \\
 \boldsymbol{\Sigma}_{b|a}^{-1}& =\boldsymbol{\Lambda}_{bb} =\boldsymbol{\Sigma}_{bb}^{-1}+\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba}\mathbf{M} \boldsymbol{\Sigma}_{ab }\boldsymbol{\Sigma}_{bb}^{-1} \\
 & =\boldsymbol{\Sigma}_{bb}^{-1}+\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba}(\boldsymbol{\Sigma}_{aa}-\boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba})^{-1}\boldsymbol{\Sigma}_{ab }\boldsymbol{\Sigma}_{bb}^{-1} \\
 & =\boldsymbol{\Sigma}_{bb}^{-1}+(\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb})^{-1}(\boldsymbol{\Sigma}_{aa}-\boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba})^{-1}\boldsymbol{\Sigma}_{ab }\boldsymbol{\Sigma}_{bb}^{-1} \\
 & =\boldsymbol{\Sigma}_{bb}^{-1}+(\boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\boldsymbol{\Sigma}_{ab}\cancel{ \boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb} })^{-1}\boldsymbol{\Sigma}_{ab }\boldsymbol{\Sigma}_{bb}^{-1}\\
 & =\boldsymbol{\Sigma}_{bb}^{-1}+(\boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\boldsymbol{\Sigma}_{ab})^{-1}\boldsymbol{\Sigma}_{ab }\boldsymbol{\Sigma}_{bb}^{-1} \\
 & =\boldsymbol{\Sigma}_{bb}^{-1}+(\boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\boldsymbol{\Sigma}_{ab})^{-1}(\boldsymbol{\Sigma}_{bb }\boldsymbol{\Sigma}_{ab}^{-1})^{-1}\\
 & =\boldsymbol{\Sigma}_{bb}^{-1}+(\boldsymbol{\Sigma}_{bb}\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\boldsymbol{\Sigma}_{bb}\cancel{ \boldsymbol{\Sigma}_{ab}^{-1} \boldsymbol{\Sigma}_{ab} })^{-1}\\
 & =\boldsymbol{\Sigma}_{bb}^{-1}+(\boldsymbol{\Sigma}_{bb}\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\boldsymbol{\Sigma}_{bb})^{-1} \\
 & =\boldsymbol{\Sigma}_{bb}^{-1}+(\boldsymbol{\Sigma}_{bb}(\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\mathbf{I}))^{-1}\\
 & =\boldsymbol{\Sigma}_{bb}^{-1}+(\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\mathbf{I})^{-1}\boldsymbol{\Sigma}_{bb}^{-1}\\
 & =(\mathbf{I}+(\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\mathbf{I})^{-1})\boldsymbol{\Sigma}_{bb}^{-1} \\
 \boldsymbol{\Sigma}_{b|a}^{-1}& =(\boldsymbol{\Sigma}_{bb}(\mathbf{I}+(\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\mathbf{I})^{-1}))^{-1}\\ \\
 \boldsymbol{\Sigma}_{b|a}& =\boldsymbol{\Sigma}_{bb}(\mathbf{I}+(\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\mathbf{I})^{-1}) \\
& =\boldsymbol{\Sigma}_{bb}+\boldsymbol{\Sigma}_{bb}(\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\mathbf{I})^{-1} \\
& =\boldsymbol{\Sigma}_{bb}+((\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}\boldsymbol{\Sigma}_{bb}-\mathbf{I}) \boldsymbol{\Sigma}_{bb}^{-1})^{-1}\\
& =\boldsymbol{\Sigma}_{bb}+(\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}- \boldsymbol{\Sigma}_{bb}^{-1})^{-1}\\
\end{align*}
$$

De esta manera finalmente obtenemos que:

$$
\boldsymbol{\Sigma}_{b|a} =\boldsymbol{\Sigma}_{bb}+(\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}- \boldsymbol{\Sigma}_{bb}^{-1})^{-1}
$$

Para $\boldsymbol{\mu}_{b|a}$ observamos que:

$$
\begin{align*}
\boldsymbol{\mu}_{b|a} & =\boldsymbol{\mu}_{b}+\boldsymbol{\Sigma}_{b|a}\boldsymbol{\Sigma}_{ba}^{-1}(\boldsymbol{\mu}_{a}-\mathbf{x}_{a}) \\ 
 &   =\boldsymbol{\mu}_{b}+[\boldsymbol{\Sigma}_{bb}+(\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}- \boldsymbol{\Sigma}_{bb}^{-1})^{-1}]\boldsymbol{\Sigma}_{ba}^{-1}(\boldsymbol{\mu}_{a}-\mathbf{x}_{a})\\
 &   =\boldsymbol{\mu}_{b}+[\boldsymbol{\Sigma}_{bb}\boldsymbol{\Sigma}_{ba}^{-1}+(\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}- \boldsymbol{\Sigma}_{bb}^{-1})^{-1}\boldsymbol{\Sigma}_{ba}^{-1}](\boldsymbol{\mu}_{a}-\mathbf{x}_{a})\\
 &   =\boldsymbol{\mu}_{b}+[\boldsymbol{\Sigma}_{bb}\boldsymbol{\Sigma}_{ba}^{-1}+(\boldsymbol{\Sigma}_{ba}(\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}- \boldsymbol{\Sigma}_{bb}^{-1}))^{-1}](\boldsymbol{\mu}_{a}-\mathbf{x}_{a})\\ \\

 \boldsymbol{\mu}_{b|a}&   =\boldsymbol{\mu}_{b}+[\boldsymbol{\Sigma}_{bb}\boldsymbol{\Sigma}_{ba}^{-1}+(\boldsymbol{\Sigma}_{ba}\boldsymbol{\Sigma}_{ab}^{-1}  \boldsymbol{\Sigma}_{aa}\boldsymbol{\Sigma}_{ba}^{-1}- \boldsymbol{\Sigma}_{ba}\boldsymbol{\Sigma}_{bb}^{-1})^{-1}](\boldsymbol{\mu}_{a}-\mathbf{x}_{a})
\end{align*}
$$
