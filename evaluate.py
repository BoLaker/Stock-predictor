import matplotlib.pyplot as plt

def plot_data(y_data_list,labels, title, x_label, y_label):
    
    plt.figure(figsize=(12,6))
    for data,label in zip(y_data_list, labels):
       plt.plot(data, label=label) 
    
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend
    plt.grid(True, alpha=0.3)
    
    plt.show()
    