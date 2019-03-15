import os
import numpy as np

def mysort(boxs,scores,idx):
    data=[(box,score) for box,score in zip(boxs,scores)]
    data2=sorted(data,key=lambda x:(x[0][idx]))
    boxs=[box for box, score in data2]
    scores=[score for box, score in data2]
    return boxs, scores
    
    
boxs=[[12,2],[18,3],[11,1],[20,7]]
scores=[0.9,0.7,0.6,0.5]
print(boxs)
print(scores)
boxs,scores=mysort(boxs,scores,0)

mean=(np.sum(boxs,axis=0) / len(boxs))[0]
num=np.sum(x[0]<mean for x in boxs)

boxfs=boxs[:num]
scorefs=scores[:num]

boxfs,scorefs=mysort(boxfs,scorefs,1)

boxbs=boxs[num:][:]
scorebs=scores[num:]
boxbs,scorebs=mysort(boxbs,scorebs,1)

boxfs.extend(boxbs)
scorefs.extend(scorebs)

print(boxfs)
print(scorefs)