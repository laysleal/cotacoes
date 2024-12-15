#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from win10toast import ToastNotifier


# In[2]:


hoje = datetime.today()
ontem = hoje - timedelta(days = 1)
ontem = ontem.strftime('%Y-%m-%d')


# In[6]:


ativos = ['HGFF11.SA', 'HGLG11.SA', 'IVVB11.SA', 'SMAL11.SA']
cotacoes = {}

for ativo in ativos:
    cotacao = yf.download(ativo, ontem, hoje)
    cotacoes[ativo] = round(cotacao['Close'][ativo][0], 2)


# In[19]:


toaster = ToastNotifier()
if cotacoes['HGFF11.SA'] < 70:
    toaster.show_toast("ALERTA DE PREÇO", "HGFF11 está abaixo do preço alvo", duration=10)


# In[ ]:




