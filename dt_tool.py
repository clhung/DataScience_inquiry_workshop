import numpy as np

def dt_ig(df,feature):
    n=len(df)
    im=0
    for target in df[feature].unique():
        data=df.iloc[:,-1][df[feature]==target]
        im += len(data)/n*dt_entropy(data)
    ig=dt_entropy(df.iloc[:,-1])-im
    return ig

def dt_entropy(data):
    n=len(data)
    ent=0
    for target in data.unique():
        p=len(data[data==target])/n
        ent += p*np.log2(p)

    return -1*ent
