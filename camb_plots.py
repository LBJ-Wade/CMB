#Author: Emma Clarke
#Date: 2 July 2018

#This program generates CMB temperature power spectrum plots using CAMB
#for different sets of parameters

#N.B.: very inefficient code :)

from matplotlib import pyplot as plt

import numpy as np

import camb
from camb import model, initialpower
print('CAMB version: %s '%camb.__version__)


#plot0: original parameter values
pars0 = camb.CAMBparams()
pars0.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06)
pars0.InitPower.set_params(ns=0.965, r=0)
pars0.set_for_lmax(2500, lens_potential_accuracy=0);
results0 = camb.get_results(pars0)
powers0 =results0.get_cmb_power_spectra(pars0, CMB_unit='muK')
unlensedCL0=powers0['unlensed_scalar']




#Varying baryon to cdm density
#plot2: omega_b = 0.002, omega_c adjusts
pars02 = camb.CAMBparams()
pars02.set_cosmology(H0=67.5, ombh2=0.002, omch2=0.142, mnu=0.06, omk=0, tau=0.06)
pars02.InitPower.set_params(ns=0.965, r=0)
pars02.set_for_lmax(2500, lens_potential_accuracy=0);
results02 = camb.get_results(pars02)
powers02 = results02.get_cmb_power_spectra(pars02, CMB_unit='muK')
unlensedCL02=powers02['unlensed_scalar']

#plot3: omega_b = 0.044, omega_c adjusts
pars03 = camb.CAMBparams()
pars03.set_cosmology(H0=67.5, ombh2=0.044, omch2=0.1, mnu=0.06, omk=0, tau=0.06)
pars03.InitPower.set_params(ns=0.965, r=0)
pars03.set_for_lmax(2500, lens_potential_accuracy=0);
results03 = camb.get_results(pars03)
powers03 = results03.get_cmb_power_spectra(pars03, CMB_unit='muK')
unlensedCL03=powers03['unlensed_scalar']




#Varying H_0
#H_0 = 0.1
pars12 = camb.CAMBparams()
pars12.set_cosmology(H0=0.1, ombh2=0.002, omch2=0.142, mnu=0.06, omk=0, tau=0.06)
pars12.InitPower.set_params(ns=0.965, r=0)
pars12.set_for_lmax(2500, lens_potential_accuracy=0);
results12 = camb.get_results(pars12)
powers12 = results12.get_cmb_power_spectra(pars12, CMB_unit='muK')
unlensedCL12=powers12['unlensed_scalar']
#H_0 = 200
pars13 = camb.CAMBparams()
pars13.set_cosmology(H0=200, ombh2=0.002, omch2=0.142, mnu=0.06, omk=0, tau=0.06)
pars13.InitPower.set_params(ns=0.965, r=0)
pars13.set_for_lmax(2500, lens_potential_accuracy=0);
results13 = camb.get_results(pars13)
powers13 = results13.get_cmb_power_spectra(pars13, CMB_unit='muK')
unlensedCL13=powers13['unlensed_scalar']




#Varying total matter density
#double both baryon and cdm (so ratio same)
pars21 = camb.CAMBparams()
pars21.set_cosmology(H0=67.5, ombh2=0.044, omch2=0.244, mnu=0.06, omk=0, tau=0.06)
pars21.InitPower.set_params(ns=0.965, r=0)
pars21.set_for_lmax(2500, lens_potential_accuracy=0);
results21 = camb.get_results(pars21)
powers21 =results21.get_cmb_power_spectra(pars21, CMB_unit='muK')
unlensedCL21=powers21['unlensed_scalar']

#halve both baryon and cdm (so ratio same)
pars22 = camb.CAMBparams()
pars22.set_cosmology(H0=67.5, ombh2=0.011, omch2=0.061, mnu=0.06, omk=0, tau=0.06)
pars22.InitPower.set_params(ns=0.965, r=0)
pars22.set_for_lmax(2500, lens_potential_accuracy=0);
results22 = camb.get_results(pars22)
powers22 =results22.get_cmb_power_spectra(pars22, CMB_unit='muK')
unlensedCL22=powers22['unlensed_scalar']




#general portion
totCL=powers0['total']
ls = np.arange(totCL.shape[0])




#plotting portion: all on one figure
plt.figure()

#matter ratio varying
plt.subplot(1,3,1)
p0, = plt.semilogx(ls,unlensedCL0[:,0])
p02, = plt.semilogx(ls,unlensedCL02[:,0])
p03, = plt.semilogx(ls,unlensedCL03[:,0])
plt.title('Varying $\omega_b$/$\omega_c$')
plt.xlabel('l')
plt.legend([p0,p02,p03],['original','$\omega_b = 0.002$','$\omega_b = 0.044$'])

#Hubble constant varying
plt.subplot(1,3,2)
p0, = plt.semilogx(ls,unlensedCL0[:,0])
p12, = plt.semilogx(ls,unlensedCL12[:,0])
p13, = plt.semilogx(ls,unlensedCL13[:,0])
plt.title('Varying $H_0$')
plt.xlabel('l')
plt.legend([p0,p12,p13],['original','$H_0$ = 0.1','$H_0$ = 200'])

#total matter varying
plt.subplot(1,3,3)
p0, = plt.semilogx(ls,unlensedCL0[:,0])
p21, = plt.semilogx(ls,unlensedCL21[:,0])
p22, = plt.semilogx(ls,unlensedCL22[:,0])
plt.title('Varying Total Matter Density')
plt.xlabel('l')
plt.legend([p0,p21,p22],['original','doubled','halved'])


plt.show()
