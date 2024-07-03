# Generating Uniform Sampler from a Unifrom Random Number Generator

This is the fourth assignment submission for CS203: Mathematics for Computer Science III submitted by Aditi Khandelia and Kushagra Srivastava.

### Contents

- `inverse_cdf.py`
  - This is the main python file for the assignment.
  - It has functions to calculate the inverse CDF of a normal distribution and generate a normal sampler from a uniform random number generator.

### Build instructions

```
python3 inverse_cdf.py
```

### Formulae

Inverse CDF of a normal distribution is given by:
$$\Phi^{-1}\left(\mu, \sigma^2; x\right) =  \mu + \sigma \times \sqrt{2} \cdot \text{erf}^{-1}(2p - 1)$$
