#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[10]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[45]:





# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[7]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[76]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return int(black_friday[(black_friday["Gender"] == "F") & (black_friday["Age"] == "26-35")].shape[0])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[78]:


def q3():
    return int(black_friday['User_ID'].nunique())


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    return black_friday.dtypes.nunique()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[70]:


def q5():
    return float(black_friday.isnull().sum().max()/black_friday.shape[0])


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[83]:


def q6():
    return int(black_friday.isnull().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[119]:


def q7():
    return float(black_friday['Product_Category_3'].value_counts(dropna=True).keys()[0])


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[155]:


def q8():
    norm = black_friday['Purchase']
    norm = (norm-norm.min()) / (norm.max()-norm.min())
    return float(norm.mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[25]:


def q9():
    standard = StandardScaler()
    purchase = standard.fit_transform(black_friday['Purchase'].values.reshape(-1, 1))
    return int(len(purchase[(purchase >= -1) & (purchase <= 1)]))


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[49]:


def q10():
    df_cat_2_null = black_friday[black_friday['Product_Category_2'].isnull()]
    df_cat_3_null = df_cat_2_null[df_cat_2_null['Product_Category_3'].isnull()]
    if (df_cat_2_null.shape[0] == df_cat_3_null.shape[0]):
        return True
    else:
        return False

