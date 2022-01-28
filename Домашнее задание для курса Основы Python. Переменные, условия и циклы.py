point_start = 0,2
point_1 = 2,5
point_2 = 5,2
point_3 = 6,6
point_4 = 8,3

i = point_start, point_1, point_2, point_3, point_4
b = point_start, point_1, point_2, point_3, point_4

m2 = []
check = point_start
name = []
data_1 = []
x = 0
finish = {}
def comparison ():
    global i, b, v, q, x, data_1, name, check
    if b[v] != i[q]:
        x = ((b[v][0] - i[q][0]) ** 2 + (b[v][1] - i[q][1]) ** 2) ** 0.5
        data_1.append(x)
        m = f'{b[v]} -> {i[q]}'
        m2.append(i[q])
        name.append(m)
                
time = 1
while(time <= 4):
    time =time+1
    
    if point_start == check:   
        for q in range (1, 5):
            v = 0
            comparison()
        data_min = (min(data_1))
        ind = data_1.index(min(data_1))
        finish[name[ind]] = data_min
        check = (m2[ind])

        
    elif point_1 == check:
        m2.clear()
        data_1.clear()
        name.clear()
        for q in range (1, 5):
            v = 1
            comparison()
        data_min = (min(data_1))
        ind = data_1.index(min(data_1))
        finish[name[ind]] = data_min
        check = (m2[ind])

    elif point_2 == check:
        m2.clear()
        data_1.clear()
        name.clear()
        for q in range (1, 5):
            v = 2
            comparison()
        data_min = (min(data_1))
        ind = data_1.index(min(data_1))
        finish[name[ind]] = data_min
        check = (m2[ind])
        
    elif point_3 == check:
        m2.clear()
        data_1.clear()
        name.clear()
        for q in range (1, 5):
            v = 3
            comparison()
        data_min = (min(data_1))
        ind = data_1.index(min(data_1))
        finish[name[ind]] = data_min
        check = (m2[ind])
        
    elif point_4 == check:
        m2.clear()
        data_1.clear()
        name.clear()
        for q in range (1, 5):
            v = 4
            comparison()
        data_min = (min(data_1))
        ind = data_1.index(min(data_1))
        finish[name[ind]] = data_min
        check = (m2[ind])

x = ((point_start[0] - check[0]) ** 2 + (point_start[1] - check[1]) ** 2) ** 0.5
y = f'{check} -> В исходную точку'
finish[y] = x
print(finish, ' = ', sum(finish.values()))








