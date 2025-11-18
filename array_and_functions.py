#1
"""import array as arr
def find_duplicate_packets(list1):
    a=arr.array('i')
    set1=set(list1)
    dict={}
    for i in set1:
        dict[i]=list1.count(i)
    print(dict)
        



list1=eval(input("enter a list"))
find_duplicate_packets(list1)
"""
#2

"""def identify_intruders(login_attempts,authorized_users):
    set1=set(login_attempts)
    set2=set()
    for i in set1:
        if i not in authorized_users:
            set2.add(i)
    print(set2)





    
login_attempts=eval(input("enter the login attempts"))
authorized_users=eval(input("authorized users"))
identify_intruders(login_attempts,authorized_users)
"""
#3
"""def find_first_error(L):
    for i in L:
        if i[1]=="ERROR":
            print(i[0])
            break
        
    else:
        print("None")
L=[]
N=int(input("enter the number of data you want to append"))
for i in range(N):
    timestamp=input("enter the time")
    log_level=input("enter info warn or error")
    message=input("enter the message")


    tuple1=(timestamp,log_level,message)
    L.append(tuple1)
find_first_error(L)
"""

#4
"""def scale_resolutions(resolutions,factor):
    L=[]
    T=tuple()
    for i in resolutions:
        for j in i:
            T=T+tuple(j*factor)
            L.append(T)
    print(L)



resolutions=eval(input("enter the resolutions"))
factor=float(input("enter the factor"))
scale_resolutions(resolutions,factor)
"""




#5
"""def update_visited_links(visited,new_links):
    y=set(new_links)
    y.update(visited)
    x=y-visited
    print((y,len(x)))
    


visited={'http://example.com','http://google.com','http://test.com'}
new_links=['http://google.com','http://python.org','http://example.com/about','http://test.com']
update_visited_links(visited,new_links)"""

#6
"""def distribute_tasks(server_loads,new_tasks):
    for i in range(new_tasks):
        x=min(server_loads)
        y=server_loads.index(x)
        server_loads[y]=x+1
    print(server_loads)
server_loads=[10,5,2,8]
new_tasks=5
distribute_tasks(server_loads,new_tasks)"""
#7
"""def simulate_movement(size,moves):
    index=0
    for i in moves:
        if size-1>i+index>0:
            index=index+i
        elif i+index>=size-1 and i+index>0:
            index=size-1
        elif i+index<0:
            index=0
        index=index
    print(index)
        
    
size=10
moves=[3,2,-1,5,-8,2]
simulate_movement(size,moves)
"""



#8
"""def group_by_extension(files):
    dict={}
    h=[]
    for i in files:
        x=i.split('.')
        L=[]
        y=x[1]
        for j in files:
            if y in j and j not in h:
                L.append(j)
                h.append(j)
        if L!=[]:
            print(L)
        dict[y]=L
    print(dict)
files=["script.py","notes.txt","data.csv","main.py","image.png","list.txt","shiva.mass"]
group_by_extension(files)"""

#9
def build_gradebook(entries):
    dict={}
    
    for i in entries:
        L=[]
        x=i["name"]
        for j in entries:
            if x==j.get("name"):
                y=j.get("score")
                L.append(y)
        dict[x]=L
    print(dict)


            
entries=[{"name":'Alice',"score":85},{"name":'Bob',"score":90},{"name":'Alice',"score":92},{"name":'Charlie',"score":78},{"name":'Bob',"score":88},{"name":'Alice',"score":81}]
build_gradebook(entries)