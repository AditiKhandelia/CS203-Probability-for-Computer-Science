import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from matplotlib.animation import FuncAnimation

fig, axes = plt.subplots(2, 2, figsize=(9, 9))

#Function to calculate the posterior distribution and plot it
def plot_posterior(prior_alpha, prior_beta, observed_heads, observed_tosses, plot_number):

    #Calculation of posterior parameters
    posterior_alpha = prior_alpha + observed_heads 
    posterior_beta = prior_beta + observed_tosses - observed_heads

    theta = np.linspace(0, 1, 100)

    #Plot the prior and posterior distributions
    axes[plot_number//2, plot_number%2].plot(theta, beta.pdf(theta, prior_alpha, prior_beta), label='Prior') 
    axes[plot_number//2, plot_number%2].plot(theta, beta.pdf(theta, posterior_alpha, posterior_beta), label='Posterior')
    axes[plot_number//2, plot_number%2].fill_between(theta, beta.pdf(theta, posterior_alpha, posterior_beta), alpha=0.2, color='orange')

    #Plot the MLE and MAP estimates
    mle = observed_heads / observed_tosses
    map_est = (posterior_alpha - 1) / (posterior_alpha + posterior_beta - 2)

    #Print the final results
    print("For alpha = ", prior_alpha, " beta = ", prior_beta, " heads = ", observed_heads, " tosses = ", observed_tosses)
    print(f"MLE: {mle}, MAP: {map_est}")
    axes[plot_number//2, plot_number%2].axvline(x=mle, color='r', linestyle='--', label='MLE', zorder=2, linewidth=1.4)
    axes[plot_number//2, plot_number%2].axvline(x=map_est, color='blue', linestyle='--', label='MAP', zorder=1, linewidth=1.5)
    axes[plot_number//2, plot_number%2].set_title('Beta Distribution (α={}, β={})'.format(prior_alpha, prior_beta) + f"\n with {observed_heads} heads and {observed_tosses-observed_heads} tails", size=8)
    axes[plot_number//2, plot_number%2].set_xlabel('θ (probability of heads)', fontsize=8)
    axes[plot_number//2, plot_number%2].set_ylabel('Probability Density', fontsize=8)
    axes[plot_number//2, plot_number%2].legend(fontsize=8)

# For alpha 2 and beta 5
plot_posterior(2, 5, 6, 10,0)

# For alpha 5 and beta 2
plot_posterior(5, 2, 6, 10,1)

# For alpha 1 and beta 1
plot_posterior(1, 1, 6, 10,2)

# For alpha 2 and beta 2
plot_posterior(2, 2, 6, 10,3)

# Save the plot
plt.subplots_adjust(left=0.1, bottom=0.2, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
plt.savefig('beta_distributions.png')
plt.show()
