#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#*--Honeywell Hackathon--*


# In[280]:


import numpy as np
import os
import queue as Q
import time
from IPython.display import clear_output


# In[281]:


MALL_SIZE = 12


# In[327]:


# Random Mall Scenario

def display(mall_size,route,shops,final=None,initial=None,End=None,Shopping_list=None):
        for r in range(-1,mall_size+1):
            for c in range(-1,mall_size+1):
                if End!=None and  r == End[0] and c==End[1]:
                    print( 'E',end =" "),
                elif final!=None and  r == final[0] and c==final[1]:
                    print( 'T',end =" "),
                elif initial!=None and  r == initial[0] and c==initial[1]:
                    print( 'I',end =" "),
                elif Shopping_list!=None and [r,c] in Shopping_list:
                    print( 'U',end =" "),
                elif [r,c] in route:
                    print( '-',end =" "),
                elif [r,c] in shops:
                    print( 'S',end =" "),
                elif r == -1 or r == mall_size:
                    print( 'X',end =" "),
                elif c == -1 or c == mall_size:
                    print( 'X',end =" "),
                else:
                    print( ' ',end =" "),
            print()
        print()


def create_random_mall(n):
    shops = []
    path = []
    for i in range(0,n,2):
        for j in range(0,n-1):
            shops.append([j,i])
        path.append([n-1,i])
#         path.append([i,0])
    for i in range(1,n,2):
        for j in range(0,n):
            path.append([j,i])
    return shops, path


Shops,Paths = create_random_mall(MALL_SIZE)
display(MALL_SIZE,Paths,Shops)


# In[328]:


No_Shops = len(Shops)
pick = np.random.randint(No_Shops,size = int(0.2*No_Shops))
S = np.array(Shops)
shopping_list = S[pick].tolist()
# print(shopping_list)
S_L = shopping_list.copy()
display(MALL_SIZE,Paths,Shops,Shopping_list = shopping_list)
Source = [np.random.randint(1,MALL_SIZE,1)[0], MALL_SIZE-1]


# In[330]:


#Entry to MAll is at any point on the right alley - picked randomly:


shopping_list = S_L.copy()

Source_o = Source
End = Source
MALL = np.zeros([MALL_SIZE,MALL_SIZE])
for i in Shops:
    MALL[i[0]][i[1]]=1
    
    
    


#Dijkstras Shortes Path Algo to find nearest Shop:

while(len(shopping_list)>=0):
    pq = Q.PriorityQueue()
    dist = np.full([MALL_SIZE,MALL_SIZE],np.inf)
    parent = np.zeros([MALL_SIZE,MALL_SIZE,2])
    pq.put([0,Source])
    dist[Source[0]][Source[1]] = 0

    direction = [[1,0],[-1,0],[0,1],[0,-1]]
    parent[Source[0]][Source[1]] = [-1,-1]
#     parent[Source[0]][Source[1]][1] = -1
    while not pq.empty():
        n = pq.get()[1];
        for d in direction:
            x = n[0] + d[0]
            y = n[1] + d[1]

            if(x>=0 and y>=0 and x<MALL_SIZE and y<MALL_SIZE and dist[x][y] > dist[n[0]][n[1]] + 1):
                dist[x][y] = dist[n[0]][n[1]] + 1
                parent[x][y] = n
                if(MALL[x][y]==0):
                    pq.put([dist[x][y],[x,y]])

    if(len(shopping_list)==0):
        Source = End
        m = dist[End[0]][End[1]]
        Route = []
        n_s = Source
        n_s = parent[int(n_s[0])][int(n_s[1])]
        while(parent[int(n_s[0])][int(n_s[1])][0]!=-1 or parent[int(n_s[0])][int(n_s[1])][1]!=-1 ):
            Route.append(n_s)
            n_s = parent[int(n_s[0])][int(n_s[1])]
        Route.append(n_s)

        for i in range(0,len(Route)):
            Route[i] = Route[i].tolist()

        time.sleep(2)
        clear_output(wait=True)

        display(MALL_SIZE,Route,Shops,Source,Source_o,End)
        print("Distance - ", m)
        break;
        


    # print(parent)

    m = np.inf
    # print(shopping_list)
    for s in shopping_list:
        if(m>dist[s[0]][s[1]]):
            m = dist[s[0]][s[1]]
            Source = s

    Route = []
    n_s = Source
    n_s = parent[int(n_s[0])][int(n_s[1])]
    if(n_s[0]!=-1 or n_s[1]!=-1):
        while(parent[int(n_s[0])][int(n_s[1])][0]!=-1 or parent[int(n_s[0])][int(n_s[1])][1]!=-1 ):
            Route.append(n_s)
            n_s = parent[int(n_s[0])][int(n_s[1])]
        Route.append(n_s)

    for i in range(0,len(Route)):
        Route[i] = Route[i].tolist()
    
    time.sleep(2)
    clear_output(wait=True)
    
    display(MALL_SIZE,Route,Shops,Source,Source_o,Shopping_list=shopping_list)
    shopping_list.remove(Source)
    Source_o = Source
    print("Distance - ", m)


# In[ ]:





# In[ ]:





# 
