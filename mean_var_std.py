import numpy as np

def calculate(lst):
    if len(lst) !=  9:
        raise ValueError("List must contain 9 numbers!!")
    
    matrix = np.array(lst).reshape(3,3)

    calculations = {
        'mean' : [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()],
        'variance' : [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()],
        'standard deviation' : [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.var(matrix).tolist()],
        'max' : [np.amax(matrix, axis=0).tolist(), np.amax(matrix, axis=1).tolist(), np.amax(matrix).tolist()],
        'min' : [np.amin(matrix, axis=0).tolist(), np.amin(matrix, axis=1).tolist(), np.amin(matrix).tolist()],
        'sum' : [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()],
    }
    
    return calculations


