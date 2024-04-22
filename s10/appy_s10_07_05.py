#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/22 20:39:40 (UT+8) daisuke>
#

# import astropy module
import astropy.cosmology

# making your own cosmology model
#  Hubble constant         = 70.0 km / Mpc / sec
#  matter density          = 0.30
#  baryonic matter density = 0.04
#  flat universe
cosmo = astropy.cosmology.FlatLambdaCDM (H0=70.0, Om0=0.30, Ob0=0.04)

# Hubble constant and density parameters
H0      = cosmo.H0
Ode0    = cosmo.Ode0
Om0     = cosmo.Om0
Odm0    = cosmo.Odm0
Ob0     = cosmo.Ob0
Onu0    = cosmo.Onu0
Ogamma0 = cosmo.Ogamma0
Ok0     = cosmo.Ok0
Ot0     = Ode0 + Odm0 + Ob0 + Ogamma0 + Onu0 + Ok0

# Hubble time
hubble_time = cosmo.hubble_time

# printing parameters
print (f'Parameters from Planck 2018 model')
print (f'  H0          = {H0:20s} # Hubble constant at z=0')
print (f'  Ode0        = {Ode0:8.6f}             # dark energy density at z=0')
print (f'  Om0         = {Om0:8.6f}             # matter density at z=0')
print (f'  Odm0        = {Odm0:8.6f}             # dark matter density at z=0')
print (f'  Ob0         = {Ob0:8.6f}             # baryonic matter density at z=0')
print (f'  Onu0        = {Onu0:8.6f}             # neutrino density at z=0')
print (f'  Ogamma0     = {Ogamma0:8.6f}             # photon density at z=0')
print (f'  Ok0         = {Ok0:8.6f}             # curvature density at z=0')
print (f'  Ot0         = {Ot0:8.6f}             # Ode0+Odm0+Ob0+Ogamma0+Onu0+Ok0 at z=0')
print (f'  Hubble time = {hubble_time}')
