def AND_gate(x1, x2):
    w1=0.5
    w2=0.5
    b=-0.7
    result = x1*w1 + x2*w2 + b
    if result <=0:
        return 0
    else :
        return 1

print( 'AND(x1,x2) = (0, 0) => {0}' .format(AND_gate(0, 0)) )
print( "AND(x1,x2) = (1, 0) => {0}" .format(AND_gate(1, 0)) )
print( "AND(x1,x2) = (0, 1) => {0}" .format(AND_gate(0, 1)) )
print( "AND(x1,x2) = (1, 1) => {0}" .format(AND_gate(1, 1)) )

def NAND_gate(x1, x2):
    w1=-0.5
    w2=-0.5
    b=0.7
    result = x1*w1 + x2*w2 + b
    if result <= 0:
        return 0
    else:
        return 1

print( 'NAND(x1,x2) = (0, 0) => {0}' .format(NAND_gate(0, 0)) )
print( "NAND(x1,x2) = (1, 0) => {0}" .format(NAND_gate(1, 0)) )
print( "NAND(x1,x2) = (0, 1) => {0}" .format(NAND_gate(0, 1)) )
print( "NAND(x1,x2) = (1, 1) => {0}" .format(NAND_gate(1, 1)) )

def OR_gate(x1, x2):
    w1=0.6
    w2=0.6
    b=-0.5
    result = x1*w1 + x2*w2 + b
    if result <= 0:
        return 0
    else:
        return 1

print( 'OR(x1,x2) = (0, 0) => {0}' .format(OR_gate(0, 0)) )
print( "OR(x1,x2) = (1, 0) => {0}" .format(OR_gate(1, 0)) )
print( "OR(x1,x2) = (0, 1) => {0}" .format(OR_gate(0, 1)) )
print( "OR(x1,x2) = (1, 1) => {0}" .format(OR_gate(1, 1)) )

def XOR_gate(x1, x2):
    s1=NAND_gate(x1,x2)
    s2=OR_gate(x1,x2)
    y=AND_gate(s1,s2)
    return y

print( 'XOR(x1,x2) = (0, 0) => {0}' .format(XOR_gate(0, 0)) )
print( "XOR(x1,x2) = (1, 0) => {0}" .format(XOR_gate(1, 0)) )
print( "XOR(x1,x2) = (0, 1) => {0}" .format(XOR_gate(0, 1)) )
print( "XOR(x1,x2) = (1, 1) => {0}" .format(XOR_gate(1, 1)) )