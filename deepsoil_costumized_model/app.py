# A script to add a new model in a new layer.
# Soil Dynamics - Group 1

# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Rollings et al. (2020) model
def rollings_model(Cu, sigma0):
    
    # Define the strains of the model
    strain = np.array([1E-6, 3E-6, 1E-5, 3E-5, 0.0001, 0.0003 ,0.001, 0.003, 0.007, 0.01, 0.03, 0.07, 0.1])
    
    # Obtaining the damping vector
    damping = 26.05 * ((strain / (1 + strain)) ** 0.375) * (Cu ** 0.08) * (sigma0 ** -0.07)
    
    # Obtaining the modulus vector 
    modulus = 1 / (1 + ((strain / (0.0046 * (Cu ** -0.197) *  sigma0 ** 0.52)) ** 0.84))

    plt.plot(strain, damping, color = "red")
    plt.show()

    return 0

rollings_model(150, 100)



