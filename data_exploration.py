
# strategy 1.0
# 1. Select all the columns of the dataframe by dtype with .select_dtypes
# 2. Create a figure to match the number of plots per page, equal to the total number of columns per group.
# 3. Add each group of columns to a plot figure, and save the figure.

def data_explorer(df):
    # get object and float data
    dobj = df.select_dtypes(include=['object'])
    dflo = df.select_dtypes(include=['float'])
    
    # create a figure with two plots for each pair in dobj
    fig, axes = plt.subplots(2, 2, figsize=(20, 30))
    for col, ax in zip(dobj.columns, axes.flat):
        sns.countplot(data=dobj[[col]], x=col, ax=ax)
    fig.savefig(f'EDA_{"_".join(dobj.columns)}.pdf')
        
    # create a figure with two plots for each pair in dflo
    fig, axes = plt.subplots(2, 2, figsize=(20, 30))
    for col, ax in zip(dflo.columns, axes.flat):
        sns.boxplot(data=dflo[[col]], x=col, ax=ax)
    fig.savefig(f'EDA_{"_".join(dflo.columns)}.pdf')


data_explorer(df)

####################################################################################################################################################################
# strategy 2.0  4 figures with 2 plots per page
# 1. Select all the columns of the dataframe by dtype with .select_dtypes
# 2. Separate the columns into chunks based on the number of plots per page using a list comprehension. Adjust the chunk size n as needed.
# 3. Iterate through each group of columns
# 4. Create a figure with a number of rows equal to the number of plots per page
# 5. Add the plots to the figure and save the figure


def data_explorer(df):
    # get object and float data
    dobj = df.select_dtypes(include=['object'])
    dflo = df.select_dtypes(include=['float'])
    
    # split columns into groups of two; two being the plots per page
    n = 2
    cols_obj = [dobj.columns[i:i+n] for i in range(0, len(dobj.columns), n)]
    cols_flo = [dflo.columns[i:i+n] for i in range(0, len(dflo.columns), n)]
    
    # create a figure with two plots for each pair in dobj
    for cols in cols_obj:  # iterate through each group
        fig, axes = plt.subplots(n, 1, figsize=(15, 30))
        for col, ax in zip(cols, axes):
            sns.countplot(data=dobj[[col]], x=col, ax=ax)
        fig.savefig(f'EDA_{"_".join(cols)}.pdf')
        
    # create a figure with two plots for each pair in dflo
    for cols in cols_flo:  # iterate through each group
        fig, axes = plt.subplots(n, 1, figsize=(15, 30))
        for col, ax in zip(cols, axes):
            sns.boxplot(data=dflo[[col]], x=col, ax=ax)
        fig.savefig(f'EDA_{"_".join(cols)}.pdf')


data_explorer(df)
