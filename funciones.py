def graficar_features(DataFrame):
    import matplotlib.pyplot as plt
    import seaborn as sns

    for n, i in enumerate(DataFrame):
        plt.subplot((len(list(DataFrame.columns))/4)+1,4,n+1)
        if DataFrame[i].dtypes == float:
            sns.distplot(DataFrame[i])
            plt.title(i)
            plt.xlabel("")
        elif DataFrame[i].dtypes == "object":
            sns.countplot(DataFrame[i])
            plt.title(i)
            plt.xlabel("")
            plt.xticks(rotation = 45, horizontalalignment = 'right', fontweight ='light',fontsize = '5')
        else:
            sns.distplot(DataFrame[i], kde = True)
            plt.title(i)
            plt.xlabel("")

    plt.tight_layout()