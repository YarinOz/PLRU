# PLRU binary-tree Simulator

PLRU(Pseudo-Least-Recently-Used) binary tree simulator for 8-way associative cache in modern CPU's.
PLRU is a cache replacement policy used in modern CPU's as an applicable way as opposed to LRU.
In most cases PLRU is the true LRU block.

This simulator is meant to show the state of the binary tree used to keep track of the PLRU block when a cache miss occurs.

TO RUN SIMULATOR:

1. run 
    python3 plru_tree.py
    
2. Input line sequence from {A,B,C,D,D,E,H,G,X,Y,Z} in the format "line1 line2 ..."

3. PLRU_DT.png contain the current tree state.

Knowledge of the PLRU block state can be abused to create intentional misses in the cache using certain load sequences:
The following sequence is part of a framework from ShowTime's paper [purnal et. al.].

run
  ./abuse.sh 
  
This specific sequence results in an abuse with 0.25 hit ratio and can be changed using ShowTime's paper [purnal et. al.] or manually using the SIM.
