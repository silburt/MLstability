#This script migrates planets with small and large masses into MMR so that I can measure the libration amplitude. This will ultimately constrain what the minimum sampling frequency can be for my FFT features for the MLStability project. I want to capture these libration amplitudes as they will be important for measuring any instability.

import multiprocessing as mp
import os
import sys
import random
import numpy as np
import pandas as pd
import glob

def make_runs(N_runs):
    #draw masses from the posterior
    m1 = 1e-4
    m2 = 1e-4
    #make N_runs for simulation
    random.seed()
    runs = []
    mig_rate = random.sample(np.round(np.logspace(3,6,10*N_runs)), N_runs)
    K1 = random.sample(np.logspace(-1,3,10*N_runs), N_runs)
    K2 = random.sample(np.logspace(-1,3,10*N_runs), N_runs)
    path = 'output/'
    for i in xrange(0,N_runs):
        seed = int(10000*random.random())
        name = path+'m%.1e_tau%.1e_Kin%.1e_Kout%.1e_sd%d'%(m1,mig_rate[i],K1[i],K2[i],seed)
        runs.append((m1,m2,mig_rate[i],K1[i],K2[i],seed,name))
    return runs

#each pool worker executes this
def execute(pars):
    os.system('./rebound %f %f %f %f %f %d %s'%pars)

#Main multiprocess execution - Give sysname and letters of outer planets close to resonance
#############Main Code##############################
if __name__== '__main__':
    os.system('make')
    N_runs = 300
    runs = make_runs(N_runs)
    
    pool = mp.Pool(processes=np.min([N_runs, 10]))
    pool.map(execute, runs)
    pool.close()
    pool.join()

