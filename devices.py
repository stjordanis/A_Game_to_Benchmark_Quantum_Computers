def supportedDevices ():

	# Returns the list of all supported devices

	return ["ibmqx4","ibmqx5"]

def getLayout (device):

	# Input:
	# 
	# * *device* - A string which specifies the device to be used.
	# 
	# Process:
	# 
	# * Look up the details of that device.
	# 
	# Output:
	# 
	# * *num* - The number of qubits in the device.
	# * *area* - A list with two entries specifying the width and height for the plot of the device. These should be in units of qubits (i.e. *area=[8,2]* for an *8x2* grid of qubits).
	# * *entangleType* - Type of entangling gate ("CX" or "CZ").
	# * *pairs* - A dictionary of pairs of qubits for which an entagling gate is possible. The key is a string which serves as the name of the pair. The value is a two element list with the qubit numbers of the two qubits in the pair. For controlled-NOTs, the control qubit is listed first.
	# * *pos* - A dictionary of positions for the qubits in the plot. Keys are qubit numbers and values are a two element list of coordinates.
	# * *example* - An example set of noisy entanglement results for use in the tutorial.
	# * *sdk* - The SDK to be used when running jobs on this device.
    # * *runs* - Data that has been obtained. As a dictionary with values of *sim* as keys.
    
    if device=="ibmqx5":
    
        # the positions of qubits on the device (numbers), and names of pairs (letters) for ibmqx5
        #    [1]---(A)---[2]---(B)---[3]---(C)---[4]---(D)---[5]---(E)---[6]---(F)---[7]---(G)---[8]
        #     |           |           |           |           |           |           |           |
        #    (H)         (I)         (J)         (K)         (L)         (M)         (N)         (O)
        #     |           |           |           |           |           |           |           |
        #    [0]---(P)--[15]---(Q)--[14]---(R)--[13]---(S)--[12]---(T)--[11]---(U)--[10]---(V)---[9]

        num = 16
        area = [8,2]
        entangleType = "CX"
        pairs = { 'A': [1,2], 'B': [2,3], 'C': [3,4], 'D': [5,4], 'E': [6,5], 'F': [6,7], 'G': [8,7],
                 'H': [1,0], 'I': [15,2], 'J': [3,14], 'K': [13,4], 'L': [12,5], 'M': [6,11], 'N': [7,10], 'O': [9,8],
                 'P': [15,0], 'Q': [15,14], 'R': [13,14], 'S': [12,13], 'T': [12,11], 'U': [11,10], 'V': [9,10]}
        pos = { 0: [0,0], 1: [0,1],  2: [1,1],  3: [2,1],  4: [3,1],  5: [4,1],  6: [5,1],  7: [6,1],
               8: [7,1], 9: [7,0], 10: [6,0],  11: [5,0],  12: [4,0],  13: [3,0],  14: [2,0],  15: [1,0] }
        example = [0.11, 0.09, 0.49, 0.52, 0.31, 0.89, 0.15, 0.18, 0.47, 0.43, 0.67, 0.62, 0.93, 0.29, 0.77, 0.73]
        sdk = "QISKit"
        runs = {True:{'shots':[100,1000,10000],'move':['C','R'],'maxScore':20,'samples':100},False:{'shots':[8192],'move':['C'],'maxScore':3,'samples':20}}
    
    elif device=="ibmqx4":
    
        # the positions of qubits on the device (numbers), and names of pairs (letters) for ibmqx3
        #    [4]         [0]
        #     | \       / |
        #     | (D)   (B) | 
        #     |   \   /   |
        #    (F)   [2]   (A)
        #     |   /  \    |
        #     | (E)  (C)  |
        #     | /       \ |
        #    [3]         [1]
    
        num = 5
        area = [3,3]
        entangleType = "CX"
        pairs = { 'A': [1,0], 'B': [2,0], 'C': [2,1], 'D': [2,4], 'E': [3,2], 'F': [3,4] }
        pos = { 0: [1,1], 1: [1,0],  2: [0.5,0.5],  3: [0,0],  4: [0,1] }
        example = [0.11,0.09,0.49,0.52,0.31]
        sdk = "QISKit"
        runs = {True:{'shots':[100,1000,10000],'move':['C','R'],'maxScore':20,'samples':100},False:{'shots':[8192],'move':['C'],'maxScore':5,'samples':20}}
        
    else:
        
        print("\nWarning: This is not a known device.\n")
    
    return num, area, entangleType, pairs, pos, example, sdk, runs
