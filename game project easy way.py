#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def start_game():
    
    mat =[]
    for i in range(4):
        mat.append([0]*4)
    return mat
def add_new(mat): #at random positions add 2
    r= random.randint(0,3)
    c= random.randint(0,3)
    while(mat[r][c]!=0):
        r= random.randint(0,3)
        c= random.randint(0,3)     
    mat[r][c] = 2
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])      
    return new_mat
def transpose(mat):
    new_mat =[]
    
    for i in range(4):
        new_mat.append([])  #ith row in matrix
        for j in range(4):
            new_mat[i].append(mat[j][i])          #particular we are appending the element at ma[i][j] t jth position         
    return new_mat
def merge(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j]!=0:
                mat[i][j] = mat[i][j]*2
                mat[i][j+1] = 0 
                changed = True
               
    return mat,changed            

def compress(mat):
    changed = False
    
    new_mat =[]
    for i in range(4):
        new_mat.append([0]*4)
        
        
        
        
    for i in range(4):
        pos = 0                    
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos+=1
                if j!= pos:
                    changed = True
                




def move_left(grid):
    
    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp =  compress(new_grid)
    return new_grid,changed
    
def move_right(grid):
    
    reversed_grid = reverse(grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid =  compress(new_grid)
    final_grid =reverse(new_grid)
    return final_grid,changed
 
    
    pass
def move_up(grid):
    
    
    transposed_grid = transpose(grid)
    new_grid,changed1 = compress(transposed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid =  compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid,changed
    pass

def move_down(grid):
    transposed_grid = transpose(grid)
    reverse_grid = reverse(transposed_grid)
    new_grid,changed1 = compress(reverse_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid =  compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid,changed

    pass
                                                                
def curr_state(mat):
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048):
                return 'WON'
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0):
                return 'GAME NOT OVER'
    for i in range(3):
        
        for j in range(3):
            
            if (mat[i][j]== mat[i+1][j] or mat[i][j]== mat[i][j+1]):
                
                
                
                return 'GAME NOT OVER'
        for j in range(3):
                if (mat[3][j])==mat[3][j+1]:   #for row lastt
                    
                    return 'GAME NOT OVER'
                
                
        for i in range(3):
                if mat[i][3]==mat[i+1][j] : #for last column
                    
                    
                    return 'GAME NOT OVER'
                      
        


# In[2]:


mat = start_game()
print(mat)


# In[3]:


add_new(mat)
print(mat)


# In[4]:


add_new(mat)
print(mat)


# In[ ]:





# In[5]:


mat = move_up(mat)
print(mat)


# In[6]:


mat = move_down(mat)
print(mat)


# In[7]:


add_new(mat)
print(mat)


# In[8]:


mat = move_left(mat)
print(mat)


# In[9]:


mat = move_right(mat)
print(mat)


# In[ ]:





# In[ ]:




