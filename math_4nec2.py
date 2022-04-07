import math

def SIN(a):
    return math.sin(math.radians(a))

def COS(a):
    return math.cos(math.radians(a))

def TAN(a):
    return math.tan(math.radians(a))

def ATN(a):
    return mat.degrees(math.atan(a))

def SQR(a):
    return math.sqrt(a)

def LOG(a):
    return math.log(a)

def LOG10(a):
    return math.log10(a)

def EXP(a):
    return math.exp(a)

def ABS(a):
    return math.fabs(a)

def SGN(a):
    return bool(a>0) - bool(a<0)

def MAX(a,b):
    return max(a,b)

def MIN(a,b):
    return min(a,b)

def INT(a):
    return int(a)

PI = math.pi
CM = 1.E-2
MM = 1.E-3
IN = 2.54E-2
FT = 0.3048
PF = 1.E-12
NF = 1.E-9
UF = 1.E-6
NH = 1.E-9
UH = 1.E-6

# AWG radii in mm

(
    AWG_0,
    AWG_1,
    AWG_2,
    AWG_3,
    AWG_4,
    AWG_5,
    AWG_6,
    AWG_7,
    AWG_8,
    AWG_9,
    AWG_10,
    AWG_11,
    AWG_12,
    AWG_13,
    AWG_14,
    AWG_15,
    AWG_16,
    AWG_17,
    AWG_18,
    AWG_19,
    AWG_20,
) = (
    0.00412623,
    0.00367411,
    0.00327152,
    0.00291338,
    0.00259461,
    0.00231013,
    0.0020574,
    0.00183261,
    0.00163195,
    0.00145288,
    0.00129413,
    0.00115189,
    0.00102616,
    0.0009144,
    0.00081407,
    0.00072517,
    0.00064516,
    0.00057531,
    0.00051181,
    0.00045593,
    0.0004064,
)

