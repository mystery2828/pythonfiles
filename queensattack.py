queen_pos = list(map(int, input('Enter the queen\'s position: ').strip()))
obs_pos = []
for i in range(7):
    obs_pos.append(list(map(int, input('Enter the obstackle position: ').strip(''))))

dimension = int(input('Enter the dimenson of the board: '))
matrix = [[0 for i in range(dimension)] for j in range(dimension)]
for ele in obs_pos:
    matrix[ele[0]][ele[1]] = 1
print(matrix)

def attack(queen_pos, obs_pos, dimension,matrix):
    
    n = 0
    
    #computing row_left
    for i in range(queen_pos[1]):
        if matrix[queen_pos[0]][i] is not 1:
            n=n+1
        else:
            break
    
    #computing row_right
    for j in range(queen_pos[1],dimension):
        if matrix[j][queen_pos[0]] is not 1:
            n=n+1
        else:
            break
    
    #computing column_up
    for k in range(queen_pos[0]):
        if matrix[queen_pos[1]][k] is not 1:
            n+=1
        else:
            break

    #computing column_down
    for l in range(queen_pos[0],dimension):
        if matrix[l][queen_pos[0]] is not 1:
            n+=1
        else:
            break
            
    #computing left_up 
    x,y=queen_pos[0]-1,queen_pos[1]-1
    while x>=0 and y>=0:
        if matrix[x][y] is not 1:
            n+=1
            x-=1
            y-=1
        else:
            break

    #computing right_down
    x,y=queen_pos[0]+1,queen_pos[1]+1
    while x<dimension and y<dimension:
        if matrix[x][y] is not 1:
            n+=1
            x+=1
            y+=1
        else:
            break
    
    #computing right_up
    x,y=queen_pos[0]-1,queen_pos[1]+1
    while x>=0 and y<dimension:
        if matrix[x][y] is not 1:
            n+=1
            x-=1
            y+=1
        else:
            break

    #computing left_down
    x,y=queen_pos[0]+1,queen_pos[1]-1
    while x<dimension and y>=0:
        if matrix[x][y] is not 1:
            n+=1
            x+=1
            y-=1
        else:
            break

    return n

print(attack(queen_pos,obs_pos,dimension,matrix))