#Author: Emma Clarke
#Date: 3 July 2018

#This program generates matter power spectrum plots using CAMB
#for different sets of parameters

#this corresponds to camb_plots.py code for CMB plots

#N.B.: very inefficient code :)

from matplotlib import pyplot as plt

import numpy as np

import camb
from camb import model, initialpower
print('CAMB version: %s '%camb.__version__)


#plot0: original parameter values
#pars0 = camb.CAMBparams()
#pars0.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06)
#pars0.InitPower.set_params(ns=0.965, r=0)
#pars0.set_dark_energy() #addition?
#pars0.set_matter_power(redshifts=[0,0.8], kmax=2.0);

#from NOTEBOOK:
pars = camb.CAMBparams()
pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122)
pars.set_dark_energy() #re-set defaults
pars.InitPower.set_params(ns=0.965) #did not set As?)
pars.set_matter_power(redshifts=[0.], kmax=2.0) #w/o this line get_matter_power_spectrum doesn't work
pars.NonLinear = model.NonLinear_none
results = camb.get_results(pars)
kh, z, pk = results.get_matter_power_spectrum(minkh=1e-4, maxkh=1, npoints = 200)




#modify ombh2 to ombch2 ratio
#2: decrease
pars.set_cosmology(ombh2=0.002, omch2=0.142)
results2 = camb.get_results(pars)
kh2, z2, pk2 = results2.get_matter_power_spectrum(minkh=1e-4, maxkh=1, npoints = 200)
#3: double
pars.set_cosmology(ombh2=0.044, omch2=0.1)
results3 = camb.get_results(pars)
kh3, z3, pk3 = results3.get_matter_power_spectrum(minkh=1e-4, maxkh=1, npoints = 200)




#modify H_0
#2: small
pars.set_cosmology(H0=50, ombh2=0.022, omch2=0.122)
results22 = camb.get_results(pars)
kh22, z22, pk22 = results22.get_matter_power_spectrum(minkh=1e-4, maxkh=1, npoints = 200)
#3: large
pars.set_cosmology(H0=80, ombh2=0.022, omch2=0.122)
results23 = camb.get_results(pars)
kh23, z23, pk23 = results23.get_matter_power_spectrum(minkh=1e-4, maxkh=1, npoints = 200)




#modify total matter density
#2: double
pars.set_cosmology(H0=67.5, ombh2=0.044, omch2=0.244)
results32 = camb.get_results(pars)
kh32, z32, pk32 = results32.get_matter_power_spectrum(minkh=1e-4, maxkh=1, npoints = 200)
#3: halve
pars.set_cosmology(H0=67.5, ombh2=0.011, omch2=0.061)
results33 = camb.get_results(pars)
kh33, z33, pk33 = results33.get_matter_power_spectrum(minkh=1e-4, maxkh=1, npoints = 200)




#PLOTTING
plt.subplot(1,3,1)
#plotting baryon density changes
for i, (redshift, line) in enumerate(zip(z,['-','--'])):
    p1, = plt.loglog(kh, pk[i,:], color='k', ls = line)

for i, (redshift, line) in enumerate(zip(z,['-','--'])):
    p2, = plt.loglog(kh2, pk2[i,:], color='r', ls = line)

for i, (redshift, line) in enumerate(zip(z,['-','--'])):
    p3, = plt.loglog(kh3, pk3[i,:], color='b', ls = line)

plt.legend([p1,p2,p3],['original','$\omega_b=0.002$','$\omega_b=0.044$'])
plt.xlabel('k/h Mpc')
plt.ylabel('$P_k$')
plt.title('Varying $\omega_b$/$\omega_c$')


plt.subplot(1,3,2)
#plotting H_0 changes
for i, (redshift, line) in enumerate(zip(z,['-','--'])):
    p1, = plt.loglog(kh, pk[i,:], color='k', ls = line)

for i, (redshift, line) in enumerate(zip(z,['-','--'])):
    p22, = plt.loglog(kh22, pk22[i,:], color='r', ls = line)

for i, (redshift, line) in enumerate(zip(z,['-','--'])):
    p23, = plt.loglog(kh23, pk23[i,:], color='b', ls = line)

plt.legend([p1,p22,p23],['original','$H_0=50$','$H_0=80$'])
plt.xlabel('k/h Mpc')
plt.ylabel('$P_k$')
plt.title('Varying $H_0$')

plt.subplot(1,3,3)
#plotting total matter density changes
for i, (redshift, line) in enumerate(zip(z,['-','--'])):
    p1, = plt.loglog(kh, pk[i,:], color='k', ls = line)

for i, (redshift, line) in enumerate(zip(z,['-','--'])):
    p32, = plt.loglog(kh32, pk32[i,:], color='r', ls = line)

for i, (redshift, line) in enumerate(zip(z,['-','--'])):
    p33, = plt.loglog(kh33, pk33[i,:], color='b', ls = line)

plt.legend([p1,p32,p33],['original','doubled','halved'])
plt.xlabel('k/h Mpc')
plt.ylabel('$P_k$')
plt.title('Varying Total Matter Density')



plt.show()
