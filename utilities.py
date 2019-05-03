import numpy as np

def LowRow(image):
    lowRowImage = np.zeros(shape=(image.shape[0],image.shape[1]//2))
    contt = 0
    for i in range(0,image.shape[1],2):
        lowRowImage[:,contt:contt+1] = (image[:,i:i+1] + image[:,i+1:i+2])/2
        contt += 1
    
    """for i in range(0,image.shape[0]):    
        cont = 0
        for j in range(0, image.shape[1],2):
            lowRowImage[i][cont] = ((image[i][j] + image[i][j+1]) / 2)
            if(lowRowImage[i][cont] < 0.9):
                lowRowImage[i][cont] = 0;
            cont += 1"""
    return np.clip(lowRowImage,1,255)

def LowCol(image):
    lowColImage = np.zeros(shape=(image.shape[0]//2,image.shape[1]))
    contt = 0
    for i in range(0,image.shape[0],2):
        lowColImage[contt:contt+1,:] = (image[i:i+1,:] + image[i+1:i+2,:])/2
        contt += 1
    
    
    """for j in range(0,image.shape[1]):
        cont = 0
        for i in range(0, image.shape[0], 2):
            lowColImage[cont][j] = ((image[i][j] + image[i+1][j]) / 2)
            if(lowColImage[cont][j] < 0.9):
                lowColImage[cont][j] = 0;
            cont += 1"""
    return np.clip(lowColImage,1,255)

def HighRow(image):
    lowRowImage = LowRow(image)
    highRowImage = np.zeros(shape=lowRowImage.shape)
    for i in range(0,lowRowImage.shape[1]):
        highRowImage[:,i:i+1] = image[:,2*i:(2*i)+1] - lowRowImage[:,i:i+1]
        
    """for i in range(0,image.shape[0]):
        cont = 0
        for j in range(0,lowRowImage.shape[1]):
            highRowImage[i][cont] = image[i][2*j] - lowRowImage[i][j]
            if(highRowImage[i][cont] < 0.9):
                highRowImage[i][cont] = 0;
            cont += 1"""
    return np.clip(highRowImage,1,255)

def HighCol(image):
    lowColImage = LowCol(image)
    highColImage = np.zeros(shape=lowColImage.shape)
    for i in range(0,lowColImage.shape[0]):
        highColImage[i:i+1,:] = image[2*i:(2*i)+1,:] - lowColImage[i:i+1,:]
        
    """for j in range(0,image.shape[1]):
        cont = 0
        for i in range(0,lowColImage.shape[0]):
            highColImage[cont][j] = image[i*2][j] - lowColImage[i][j]
            if(highColImage[cont][j] < 0.9):
                highColImage[cont][j] = 0;
            cont += 1"""
    return np.clip(highColImage,1,255)

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
    #print(LH.shape)
    LHrep = lh_replicada(replica(LH))
    #print("lhrep",LHrep.shape)
    HLrep = hl_replicada(replica(HL))
    HHrep = hh_replicada(replica(HH))
    return LLrep + LHrep + HLrep + HHrep


def wavelet(frame):
    lRow = LowRow(frame)
    hRow = HighRow(frame)
    
    LL = LowCol(lRow)
    LH = HighCol(lRow)
    HL = LowCol(hRow)
    HH = HighCol(hRow)
    
    wave_sup = np.hstack((LL,LH))
    wave_inf = np.hstack((HL,HH))
    
    wave = np.vstack((wave_sup,wave_inf))
    
    return wave

def dewavelet(frame):
    
    alto = frame.shape[0]
    ancho = frame.shape[1]
    LL = frame[:alto//2,:ancho//2]
    HL = frame[:alto//2,ancho//2:ancho]
    LH = frame[alto//2:alto,:ancho//2]
    HH = frame[alto//2:alto,ancho//2:ancho]
    return inversa(LL,LH,HL,HH)