
# coding: utf-8

# In[18]:

import csv
import operator
import os


# In[19]:

# Limnology/csv-files
def get_attr_names_lc(_infolder):
    attributes_list_lc = []
    count_list_lc = []
    for file in os.listdir(_infolder):
        with open(os.path.join(_infolder,file), "r") as f:
            reader = csv.reader(f)
            i = next(reader)
            for each in i:
                if each.lower() in attributes_list_lc:
                    index = attributes_list_lc.index(each.lower())
                    count_list_lc[index]+=1
                    dict_lc[each.lower()]+=1
                else:
                    attributes_list_lc+=[each.lower()]
                    count_list_lc+=[1]
                    dict_lc[each.lower()]=1
    return dict_lc


# In[20]:

#lowerCaseFrequencyOrder.csv
def get_attr_names_frequency_order(_infolder,_outfile):
    # Obtain the dictionary of attribute names in lower case
    dict_lc = get_attr_names_lc(_infolder)
    
    # Sort them in the alphabetic order of the key values
    sorted_dict_lc = sorted(dict_lc.items(), key=operator.itemgetter(1),reverse=True)
    
    # Write the results to outfile
    with open(_outfile,'w',newline='') as f:
        w = csv.writer(f)
        w.writerows(sorted_dict_lc)


# In[21]:

#lowerCaseAlphabeticOrder.csv
def get_attr_names_alphabetic_order(_infolder,_outfile):
    # Obtain the dictionary of attribute names in lower case
    dict_lc = get_attr_names_lc(_infolder)
    
    # Initialize the dictionary sorted alphabetically in lower case
    dict_sorted_alphabeticOrder = {}

    # Create new dictionary
    for key in sorted(dict_lc):
        dict_sorted_alphabeticOrder[key] = dict_lc[key]
    
    # Write the results to outfile
    with open('lowerCaseAlphabeticOrder.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerows(dict_sorted_alphabeticOrder.items())


# In[23]:

# Examples

get_attr_names_frequency_order('Limnology/csv-files','lowerCaseFrequencyOrder.csv')
get_attr_names_alphabetic_order('Limnology/csv-files','lowerCaseAlphabeticOrder.csv')

