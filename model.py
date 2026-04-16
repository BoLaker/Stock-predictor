import numpy as np

class linearRegressionGD:
    
    def __init__(self):
        self.theta = None
        self.cost_history = []
    
    def fit(self, x, y , lr=0.01, epochs=1000):
        m,n = x.shape
        
        #Add column with ones for the intercept
        x_b = np.c_[np.ones(m), x]
        
        self.theta = np.random.randn(n+1, 1)*0.01
        
        y = y.reshape(-1,1)
        
        for i in range(epochs):
            y_hat = x_b @ self.theta
            
            error = y_hat-y
         
            gradient = (1/m) * x_b.T @ error
            
            self.theta -= lr * gradient
            
            cost = (1/(2*m)) * np.sum(error**2)
            self.cost_history.append(cost)
            

    def predict(self, x):
        x_b = np.c_[np.ones(x.shape[0]),x]
        return x_b @ self.theta
        
        
        