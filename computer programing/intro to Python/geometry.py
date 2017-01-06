# This program contains functions that evaluate formulas used in geometry.
#
# Grace Gumpert
# August 22,2014

import math

def triangle_area(b,h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r **2
    return a

# function calls
print (triangle_area (4,9))
print (circle_area (5))
print (circle_area (12))

def parallelogram_area (b,h):
    a = b * h
    return a

def trapezoid_area (a,b,h):
    a = (a + b) / 2 * h
    return a

def rectangular_prism_area (w,h,l):
    v = w * h * l
    return v

def sphere_surface_area (r):
    a = 4 * math.pi * r**2
    return a

def pythagoran_theorm ( a,b,c):
    c = math.sqrt *(a**2 + b**2) 
    return c

def herons_formula(a,b,c):
    s = (1/2)*( a + b +c)
    return s



def surface_area_cyclinder ( r,h):
    a = 2 * math.pi * r * h + 2 * math.pi ** r
    return a

print surface_area_cyclinder (4,10)


