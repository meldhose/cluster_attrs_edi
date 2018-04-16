
# coding: utf-8

# In[2]:

import csv
import os
import py_valuenormalization as vn


# In[3]:

# Function to remove any prefix string from the text
def remove_comment(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


# In[4]:

# Limnology/csv-files
def get_attr_names(_infolder):
    dict_lc={}
    attributes_list_lc = []
    count_list_lc = []

    for file in os.listdir(_infolder):
        with open(os.path.join(_infolder,file), "r") as f:
            reader = csv.reader(f)
            i = next(reader)
            for each in i:
                modified_each = remove_comment(each.lower().strip(),'#')
                if modified_each in attributes_list_lc:
                    index = attributes_list_lc.index(modified_each)
                    count_list_lc[index]+=1
                    dict_lc[modified_each]+=1
                else:
                    attributes_list_lc+=[modified_each]
                    count_list_lc+=[1]
                    dict_lc[modified_each]=1

    attributes_list_lc.remove('')
    vals = attributes_list_lc
    return vals


# In[19]:

# Limnology/Stage 3/clusteredAttributes.csv
# clusterAttributes_v4.csv
def cluster_attr_names(_infolder,_outfile):
    vals = get_attr_names(_infolder)
    hac = vn.HierarchicalClustering(vals)
    clusts = hac.cluster(sim_measure = '3gram Jaccard', linkage = 'single', thr = 0.7)


    #Sort the attribute names in the order of their size.
    clustered_Attributes = sorted(clusts, key=lambda k: len(clusts[k]), reverse=True)

    #Write the sorted clusters into csv file.
    with open(_outfile, "w",newline='') as outfile:
        writer = csv.writer(outfile, delimiter = ",")
        writer.writerow(["Cluster Name","Values","Size"])
        for key in clustered_Attributes:
            writer.writerow([key,clusts[key][0],len(clusts[key])])
            for i in range(1,len(clusts[key])):
                writer.writerow(['',clusts[key],''])
                
    return clusts


# In[21]:

# Limnology/Stage 3/clusteredAttributes.csv
# clusterAttributes_v4.csv
def print_cluster_attr_names(_infolder):
    vals = get_attr_names(_infolder)
    hac = vn.HierarchicalClustering(vals)
    clusts = hac.cluster(sim_measure = '3gram Jaccard', linkage = 'single', thr = 0.7)


    #Sort the attribute names in the order of their size.
    clustered_Attributes = sorted(clusts, key=lambda k: len(clusts[k]), reverse=True)

    #Print the sorted clusters
    for k in sorted(clusts, key=lambda k: len(clusts[k]), reverse=True):
            print(k+"  "+str(len(clusts[k])))
            print("\t%s"%("\n\t".join(clusts[k])))


# In[20]:

abc = cluster_attr_names('Limnology/csv-files','clusterAttributes_v4.csv')
abc


# In[22]:

print_cluster_attr_names('Limnology/csv-files')


# In[ ]:



