import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Lecture du fichier
df = pd.read_csv('medical_examination.csv')

# 2 - Calculer l'obésité
df['overweight'] = (df['weight'] / ((df['height']/100) ** 2) > 25).astype(int)

# 3 - Normaliser
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    
    # 6
    df_cat = df_cat.groupby(['variable', 'value', 'cardio']).size().reset_index(name='total')
    
    # 7
    g = sns.catplot(x='variable', y='total', hue='value', col='cardio', 
                    data=df_cat, kind='bar')
    
    # CORRECTION CRITIQUE - minuscules exactes
    g.set_axis_labels('variable', 'total')
    
    # 8
    fig = g.fig
    
    # 9 Sauvegarder
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11 - Nettoyer
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # 12 - Corrélation
    corr = df_heat.corr()
    
    # 13 - Masque triangulaire
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # 14 - Figure
    fig, ax = plt.subplots(figsize=(11, 9))
    
    # 15 - Heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', 
                center=0, square=True, linewidths=0.5, 
                cbar_kws={'shrink': 0.8})
    
    # 16 - Sauvegarder
    fig.savefig('heatmap.png')
    return fig
