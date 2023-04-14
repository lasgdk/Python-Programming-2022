import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from sklearn.preprocessing import LabelEncoder
#import graphviz
from sklearn import tree
from IPython.core.display import display

class KMeansCustom:
    
    def __init__(self, X, clusters = 2):
        self.X = X
        self.clusters = clusters
        
    def initialize(self):
        self.alloc = np.random.randint(0, self.clusters, self.X.shape[0])
        self.centroids = np.zeros((self.clusters, self.X.shape[1]))
        self._update_centroids()
              
    def _calc_dist(self):
        # Calculate distances
        self.dist_mat = np.zeros((self.X.shape[0], self.clusters))
        for i in range(self.clusters):
            self.dist_mat[:, i] = np.sqrt(np.sum((self.X - self.centroids[i, :])**2, axis = 1))
    
    def _update_alloc(self):
        # Update alloc
        self.alloc = np.argmin(self.dist_mat, axis = 1)
        
    def _update_centroids(self):
        # Update centroids
        for i in range(self.clusters):
            self.centroids[i, :] = np.mean(self.X[self.alloc == i, :], axis = 0)
        
    def iterate(self, itr = 1):
        for i in range(itr):
            self._iterate()
            
    def _iterate(self):
        self._calc_dist()
        self._update_alloc()
        self._update_centroids()

    def plot_iterations(self, itr = 1):
        if self.X.shape[1] == 2:
            
            if not hasattr(self, 'alloc'):
                self.initialize()

            for ii in range(itr):
                self._iterate()
                plt.scatter(self.X[:, 0], self.X[:, 1], c = self.alloc)
                plt.scatter(self.centroids[:,0], self.centroids[:,1])
                plt.show()

        else:
            raise ValueError("Cannot plot data of dimention {}, only 2-dimensional data can be plotted".format(self.X.shape[1]))

def plot_tree(clf, feature_names = None, unique_label_names = None):
    '''
    A function to plot decision trees.
    
    Input:
    clf: A fitted DecisionTreeClassifier
    feature_names: A list of the column names e.g. from `df.columns`
    unique_label_names: A list/array of the unique label values e.g. from np.unique(df['target'])
    '''
    
    if feature_names is not None and unique_label_names is not None:
        dot_data = tree.export_graphviz(clf,
                                        out_file=None, 
                                        feature_names=feature_names,  
                                        class_names=unique_label_names,  
                                        filled=True, 
                                        rounded=True,  
                                        special_characters=True)  
    elif feature_names is not None:
        dot_data = tree.export_graphviz(clf,
                                        out_file=None, 
                                        feature_names=feature_names,  
                                        filled=True, 
                                        rounded=True,  
                                        special_characters=True)
    elif unique_label_names is not None:
        dot_data = tree.export_graphviz(clf,
                                        out_file=None, 
                                        class_names=unique_label_names,
                                        filled=True, 
                                        rounded=True,  
                                        special_characters=True)
    else:
        dot_data = tree.export_graphviz(clf,
                                        out_file=None, 
                                        filled=True, 
                                        rounded=True,  
                                        special_characters=True)
    graph = graphviz.Source(dot_data)  
    display(graph)

def plot_decision_boundary(clf, df, features, target):
    '''
    Function to plot a trained classification model. It allows
    up to 3 outcomes, and they can be encoded as strings.
    
    Arguments:
    clf: A trained sklearn classifier
    df: The dataframe used for training
    features: List of strings, with feature names, should have
        two elements, e.g. ['a', 'b'].
    target: String, name of target variable in df
    '''
    
    # Validate arguments
    if len(features) != 2:
        raise ValueError("The argument 'features' must be of length 2!")
    if features[0] not in df.columns or features[1] not in df.columns:
        raise ValueError("The values of 'features' must be names of columns in 'df'!")
    if target not in df.columns:
        raise ValueError("The value of 'target' must be the name of a column in 'df'!")
    
    # Number of classes
    classes = df[target].unique()

    # Create figure
    fig, ax = plt.subplots(dpi = 400, figsize=(5,3))
    
    # Find number of colors
    base_colors = ['tab:blue', 'tab:orange', 'tab:green']
    chosen_colors = base_colors[:len(classes)]
    
    cm = colors.ListedColormap(chosen_colors)
    for cidx, class_ in enumerate(classes):
        
        idx = df[target] == class_
        
        label = class_
        
        # Make plot
        ax.scatter(
            df.loc[idx, features[0]],
            df.loc[idx, features[1]],
            c=chosen_colors[cidx],
            alpha=0.8,
            label=label,
            marker='o',
            edgecolors='black'
        )
    
    # Set labels
    ax.set_xlabel(features[0])
    ax.set_ylabel(features[1])
    
    # Set title and legend
    ax.set_title("Decision boundary of classifier")
    ax.legend()
    
    # Get size of plotting canvas
    x_min, x_max = ax.get_xlim() #(-2.9589217371230414, 6.841078262876966)
    y_min, y_max = ax.get_ylim() #(-3.0752964709347888, 5.3379911387481949)

    # Create grid
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),np.arange(y_min, y_max, 0.1))
    
    # Check if the target variable is a string
    is_string = np.dtype('O') == df[target].dtype
    
    if is_string:
        # If the target variables is a string use a label
        # encoding
        le = LabelEncoder()

        # Fit labelencoder
        le.fit(df[target])

        # Encode train
        df['encoded_target'] = le.transform(df[target])

    else:
        # Determine number of classes:
        classes = df[target].unique()
        
    # Predict on grid
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    
    if is_string:
        # If the targets is a string, transform to number for plotting
        Z = le.transform(Z)
        
    Z = Z.reshape(xx.shape)

    ax.contourf(xx, yy, Z, alpha=0.4, cmap = cm, zorder=0)
    
    # Show plot
    plt.show()

def plot_regression_tree(clf, df, feature, target, step=0.01):
    '''
    Function to plot a trained regression model. It plots
    both the labels and the predictions for a given model.
    
    Arguments:
    clf: A trained sklearn classifier
    df: The dataframe used for training
    feature: String, the name of the feature used to train
        clf. Should be a column name in df.
    target: String, name of target variable in df
    '''
    # Extract min max value for feature
    min_val = df[feature].min()
    max_val = df[feature].max()

    # Predict
    X_test = np.arange(min_val, max_val, step)
    n_test_obs = X_test.shape[0]
    X_test = X_test.reshape((n_test_obs, 1))
    pred = clf.predict(X_test)
    
    # Plot the results
    plt.figure(dpi=200)
    plt.scatter(
        df[feature], 
        df[target],
        s=20,
        edgecolor="black",
        c="darkorange",
        label="labels"
    )
    plt.plot(
        X_test,
        pred,
        color="cornflowerblue",
        label="prediction",
        linewidth=2
    )
    plt.xlabel(feature)
    plt.ylabel(target)
    plt.title("Decision Tree Regression")
    plt.legend()
    plt.show()