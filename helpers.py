# libhelpers by Jack Anderson
# helper functions
import random
import time
import math
from os import system, name

# clear screen for both platforms, windows nt uses cls, unix uses clear
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")
# take a number as input, force it within range of f
# def floop(n, f):
#     if(f == 0): return 0
#     max = f
#     if n > f:
#         return floop(n-max, f)
#     else:
#         return n
def nfindex(ind, arr):
    if len(arr) == 0: return 0
    maxi = len(arr)-1
    
    if(ind < 0):
        return nfindex(ind+maxi+1, arr)
    elif(ind > 0):
        return findex(ind, arr)
# take a number as input, make sure it fits inside the index of arr given
def findex(ind, arr, ignore_negatives=False, cap=False, use_nfindex=False):
    if(len(arr) == 0): return 0
    maxi = len(arr)-1
    if ind > maxi:
        # cap: return max index and don't loop
        if(cap == True):
            return maxi
        else:
            return findex((ind-maxi)-1, arr)
    elif ind < 0:
        # ignore negatives: just return 0
        if(ignore_negatives == True):
            return 0
        elif(use_nfindex == True):
            return nfindex(ind, arr)
        else:
            return findex(abs(ind), arr)
    else:
        return ind


# safe indexof, find obj in arr
def indexOf(obj, arr):
    if obj in arr:
        return arr.index(obj)
    else:
        return -1     
      
# forced non empty string input
def sinput(prompt):
    i = str(input(prompt))
    if i == "":
        return sinput(prompt)
    return i

def flip(bit):
    if bit == 1:
        return 0
    else:
        return 1
# forced int input 
def fiinput(prompt, options):
    str_in = input(prompt)
    try:
        int_in = int(str_in)
        if not int_in in options:
            return fiinput(prompt, options)
        return int_in
    except:
        return fiinput(prompt, options)
        
# forced input takes a list of options that must match, or rerun input
def finput(prompt, options): 
    o = []
    for opt in options:
        o.append(opt.lower())
    options = o
    
    # get input and ensure is allowed
    i = str(input(prompt)).lower()
        
    if not i in options:
        return finput(prompt, options)
    else:
        return i
    
def log(text):
    print(f"[euchre] {text}")

def generate_id():
    return math.floor(time.time() * random.random())

# Ensure a unique random number within range, given an array, reps, of used numbers. 
# Return tuple of the number and reps array
def urand(low, high, reps):
    r = random.randint(low, high)
    if r in reps:
        return urand(low, high, reps)
    reps.append(r)
    return r, reps
