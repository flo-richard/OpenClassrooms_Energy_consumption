def diff_lists(L1,L2):
    """Returns the elements that are in a list L1 but not in another list L2, and vice versa"""
    
    diff_12 = list(set(L1) - set(L2))  #in L1 but not in L2
    diff_21 = list(set(L2) - set(L1))  #in L2 but not in L1
    
    return diff_12, diff_21


def transform_year_built(series):
    """splits the year built variable in 3 categories (old, median, recent)"""
    new_series = []
    for i in series:
        if i <= 1940:    new_series.append(1)
        elif i > 1940 and i <= 1995:    new_series.append(2)
        elif i > 1995:    new_series.append(3)
            
    return new_series


def transform_energy_type_use(series):
    
    new_series = []
    for i in series:
        if i <= 0:    new_series.append(0)   #if the building does not use this type of energy
        else:    new_series.append(1)
            
    return new_series


def get_first_row(df):
    
    return df.iloc[0,:]