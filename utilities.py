import numpy as np
class Operation:

    def replica(self,matrix,N=2):
        x= np.repeat(matrix,N,axis=1)
        return np.repeat(x,N,axis=0)
    def lh_replicada(self,matrix):
        matrix[1::2,:] = matrix[1::2,:]*-1
        return matrix
    def hl_replicada(self,matrix):
        matrix[:,1::2] = matrix[:,1::2]*-1
        return matrix
    def hh_replicada(self,matrix):
        matrix[::2,1::2] = matrix[::2,1::2]*-1
        matrix[1::2,::2] = matrix[1::2,::2]*-1
        return matrix
    def inversa(self,LL,LH,HL,HH):
        LLrep = self.replica(LL)
        LHrep = self.lh_replicada(self.replica(LH))
        HLrep = self.hl_replicada(self.replica(HL))
        HHrep = self.hh_replicada(self.replica(HH))
        return LLrep + LHrep + HLrep + HHrep
if __name__=='__main__':
    r=Operation()
    y = r.replica(np.matrix([[2,3],[2,1]]))
    print(y)
    y1 = r.hh_replicada(y)
    print(y1)