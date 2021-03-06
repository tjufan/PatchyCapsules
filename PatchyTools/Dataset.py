import pandas as pd
import os


names = ['emails','ENZYMES','DD','NCI1','Flickr','YouTube']

edge_urls = {}
edge_urls[names[0]]="https://github.com/meltzerpete/Embedding-Vis/raw/master/emails/emails.edgelist"
edge_urls[names[1]]="https://raw.githubusercontent.com/koyamabraintree/dataset/master/ENZYMES/edges"
edge_urls[names[2]]="https://raw.githubusercontent.com/koyamabraintree/dataset/master/DD/edges"
edge_urls[names[3]]="https://raw.githubusercontent.com/koyamabraintree/dataset/master/NCI1/edges"
edge_urls[names[4]]="https://raw.githubusercontent.com/koyamabraintree/dataset/master/Flickr/edges"
edge_urls[names[5]]="https://raw.githubusercontent.com/koyamabraintree/dataset/master/YouTube/edges"

labels_urls = {}
labels_urls[names[0]]="https://github.com/meltzerpete/Embedding-Vis/raw/master/emails/emails.labels"
labels_urls[names[1]]="https://raw.githubusercontent.com/koyamabraintree/dataset/master/ENZYMES/node_labels"
labels_urls[names[2]]="https://raw.githubusercontent.com/koyamabraintree/dataset/master/DD/node_labels"
labels_urls[names[3]]="https://raw.githubusercontent.com/koyamabraintree/dataset/master/NCI1/node_labels"
labels_urls[names[4]]="https://raw.githubusercontent.com/koyamabraintree/dataset/master/Flickr/node_labels"
labels_urls[names[5]]="https://raw.githubusercontent.com/koyamabraintree/dataset/master/YouTube/node_labels"



##### insert here your DropboxData ########


## look at here https://wiki.braintree.com/GAMMA/GAMMA
#data_path = os.environ['GAMMA_DATA_ROOT']
#DropboxDataRoot = str(data_path)+ 'Samples/'
data_path = '~/.gamma_data_root/'
DropboxDataRoot = str(data_path)+ 'Samples/'

class Dropbox:
    '''#Node id is made to start from 0 due to nauty package requirement, even if it starts from 1 in the original file
    
    '''
    
    def __init__(self,datasetname):
        self.node_label_filename =  '{0}/{0}_node_labels.txt'.format(datasetname)
        self.edge_label_filename = '{0}/{0}_edge_labels.txt'.format(datasetname)
        self.adj_filename = '{0}/{0}_A.txt'.format(datasetname)
        self.graph_ind_filename = '{0}/{0}_graph_indicator.txt'.format(datasetname)
        self.graph_label_filename = '{0}/{0}_graph_labels.txt'.format(datasetname)

    def get_node_label(self):
        df_node_label = pd.read_csv(os.path.join(DropboxDataRoot,self.node_label_filename), delimiter=' ',header=None)
        df_node_label.columns =['label']
        df_node_label['node'] = df_node_label.index.values
        return df_node_label
    
    def get_edge_label(self):
        df_edge_label = pd.read_csv(os.path.join(DropboxDataRoot,self.edge_label_filename), delimiter=' ',header=None)
        df_edge_label.columns =['edge_label']
        df_edge_label['edge_id'] = df_edge_label.index.values
        return df_edge_label

    def get_graph_ind(self): 
        df_graph_ind = pd.read_csv(os.path.join(DropboxDataRoot,self.graph_ind_filename), delimiter=' ',header=None)
        df_graph_ind.columns =['graph_ind']
        df_graph_ind['node'] = df_graph_ind.index.values
        return df_graph_ind

    def get_graph_label(self): 
        df_graph_ind = pd.read_csv(os.path.join(DropboxDataRoot,self.graph_label_filename), delimiter=' ',header=None)
        df_graph_ind.columns =['graph_label']
        df_graph_ind['node'] = df_graph_ind.index.values
        return df_graph_ind
    
    def get_adj(self):
        df_adj = pd.read_csv(os.path.join(DropboxDataRoot,self.adj_filename), delimiter=',',header=None)
        df_adj.columns =['from', 'to']
        df_adj['from'] = df_adj['from'].values - 1
        df_adj['to'] = df_adj['to'].values - 1
        return df_adj
    


    

'''
class githublink:
    def __init__(self,datasetname):
        self.node_label_filename =  
        self.edge_label_filename = 
        self.adj_filename = 
        self.graph_ind_filename = 
        self.graph_label_filename = 
'''

    

