import numpy as np

def replica(matrix,N=2):
    x = np.repeat(matrix[:,],N,axis=1)
    return np.repeat(x,N,axis=0)
def lh_replicada(matrix):
    matrix[1::2,:] = matrix[1::2,:]*-1
    return matrix
def hl_replicada(matrix):
    matrix[:,1::2] = matrix[:,1::2]*-1
    return matrix
def hh_replicada(matrix):
    matrix[::2,1::2] = matrix[::2,1::2]*-1
    matrix[1::2,::2] = matrix[1::2,::2]*-1
    return matrix

def inversa(LL,LH,HL,HH):
    LLrep = replica(LL)
    print(LH.shape)
    LHrep = lh_replicada(replica(LH))
    print("lhrep",LHrep.shape)
    HLrep = hl_replicada(replica(HL))
    HHrep = hh_replicada(replica(HH))
    return LLrep + LHrep + HLrep + HHrep