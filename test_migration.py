#!/usr/bin/env python3
"""
Test that migration was successful and research workflow works
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from ase import Atoms
import uncertainties as unc

print("=== RESEARCH WORKFLOW TEST ===")
print()

# 1. Basic numerical calculations
print("1. Numerical calculations:")
x = np.linspace(0, 10, 100)
y = np.sin(x)
print(f"   Array operations: {x.shape}, {y.mean():.3f}")

# 2. Data handling
print("\n2. Data handling:")
data = pd.DataFrame({
    'Temperature': [300, 400, 500, 600],
    'Conductivity': [150, 145, 140, 135]
})
print(f"   DataFrame shape: {data.shape}")
print(f"   Mean conductivity: {data['Conductivity'].mean():.1f}")

# 3. Physics calculations
print("\n3. Physics calculations:")
# Lattice parameter calculation
wavelength = 1.5406  # Cu Kα in Å
two_theta = 31.5  # degrees
theta_rad = np.radians(two_theta / 2)
d_spacing = wavelength / (2 * np.sin(theta_rad))
a = d_spacing * np.sqrt(1**2 + 0**2 + 0**2)  # for (100)
print(f"   Lattice parameter: {a:.4f} Å")

# 4. Uncertainty propagation
print("\n4. Uncertainty propagation:")
u_temp = unc.ufloat(300.0, 0.5)  # 300 ± 0.5 K
u_resistance = unc.ufloat(100.0, 1.0)  # 100 ± 1 Ω
u_power = u_temp * u_resistance
print(f"   Power = {u_power}")

# 5. Materials simulation (ASE)
print("\n5. Materials simulation:")
si_atoms = Atoms('Si2', positions=[[0, 0, 0], [0.25, 0.25, 0.25]], 
                 cell=[5.43, 5.43, 5.43], pbc=True)
print(f"   Created {len(si_atoms)} silicon atoms")
print(f"   Cell volume: {si_atoms.get_volume():.2f} Å³")

# 6. Plotting
print("\n6. Plotting test...")
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, 'b-', linewidth=2)
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('sin(X)', fontsize=12)
ax.set_title('Test Plot - Migration Successful', fontsize=14)
ax.grid(True, alpha=0.3)
plt.savefig('migration_test_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"   Plot saved as 'migration_test_plot.png'")

print("\n" + "="*50)
print("✅ ALL TESTS PASSED!")
print("Your research environment is fully functional.")
print("="*50)
