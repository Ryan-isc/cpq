#!/usr/bin/env python3

############################################################################################################################################################
################ ISC code for calculating the cyclical polygonal quotient (Gallacher et al., in prep) for a list of Event Station Azimuths #################
################ Created 03/10/2024 by Ryan Gallacher Seismologist/Developer at the International Seismological Centre - ryan@isc.ac.uk    #################
################                                                                                                                           #################
################ When using this code please cite:                                                                                         #################
################ Gallacher et al. (2025) Revising the Seismic Ground Truth Reference Event Identification Criteria. Seismica               #################
############################################################################################################################################################

############################################################################################################################################################
################ This work is licensed under Creative Commons Attribution 4.0 International. To view a copy of this license, visit         ################# 
################ https://creativecommons.org/licenses/by/4.0/                                                                              #################
############################################################################################################################################################

############################################################################################################################################################
################ Expected input is Event Station Azimuths from 0 - 360 degrees                                                             #################
################ How to run: ./cpq.py 2,100,150,160,170,200,250,300,359                                                                    #################
################ Expected output: 0.8029686796937914                                                                                       #################
############################################################################################################################################################

import sys
import math
import numpy as np

import time

############################################################################################################################################################
################################################################## Functions ###############################################################################
############################################################################################################################################################

def calc_cpq(esaz):

    ### Create Cartesian Coordinate Arrays

    x = []
    y = []

    ### Convert list of Event Station Azimuth strings to floats

    try:

        esaz_list = [float(i) for i in list(esaz.split(','))]

    ### If Event Station Azimuth input cannot be converted to float then quit

    except:

        print("Failure to convert event station azimuths to floats, please check that the input is correctly formatted i.e. ./cpq.py 2,100,150,160,170,200,250,300,359")

        sys.exit()

    if max(esaz_list) > 360 or min (esaz_list) < 0:

        print("Event Station Azimuths must be between 0 and 360 degrees")

        sys.exit()

    ### Sort list of Event Station Azimuths

    esaz_list.sort()

    ### Loop over Event Station Azimuths and append Cartesian coordinates to Cartesian Coordinate Arrays 

    for ii in esaz_list:
        x.append(math.cos(math.radians(float(ii))))
        y.append(math.sin(math.radians(float(ii))))

    ### Calculate area of polygon (Surveyor's Area Formula: Bart Braden, The College Mathematics Journal, 1986)

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    cpq = (0.5*np.absolute(S1 - S2))/math.pi

    return cpq

############################################################################################################################################################
############################################################### Main Code Start ############################################################################
############################################################################################################################################################

def main():

    ### Get list of Event Station Azimuths from input to code

    try:

        esaz = sys.argv[1]

    ### If no Event Station Azimuths provided then quit

    except:

        print("Failure to run, invalid input arguments, please check that the input is correctly formatted i.e. ./cpq.py 2,100,150,160,170,200,250,300,359")

        sys.exit()

    ### If no commas then quit

    if (',') not in esaz:

        print("Failure to run, invalid input arguments, please check that the input is correctly formatted i.e. ./cpq.py 2,100,150,160,170,200,250,300,359")

        sys.exit()

    ### If less than three Event Station Azimuths provided then quit

    if len(esaz.split(',')) < 3:

        print("Failure to run, insufficient input arguments, a minimum of three event station azimuths are required to calculate CPQ") 

        sys.exit()

    ### Call calc_cpq function

    cpq = calc_cpq(esaz)

    ### Print value of CPQ

    print(cpq)

    sys.exit()


############################################################################################################################################################
################################################################## Execution ###############################################################################
############################################################################################################################################################

if __name__ == "__main__":
    main()
