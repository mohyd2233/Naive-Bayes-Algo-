import pandas as pd

class Naive:

    def __init__(self,X,y):

        self.X = X
        self.y = y

    def Probability(self,colname,colvalue):

        gt = pd.concat([self.X,self.y],axis=1)
        dt = gt[gt[colname]==colvalue]
        yes = len(dt[dt[dt.columns[-1]]=="Yes"])
        no = len(dt[dt[dt.columns[-1]]=="No"])
        p_yes = (yes) / (yes+no)
        p_no = (no) / (yes+no)

        return [p_yes]

    def predict(self,pred):

        self.pred = pred

        for i in range(len(self.pred)):
            
            var = self.Probability(self.pred.columns[i],pred[i])

            return var




