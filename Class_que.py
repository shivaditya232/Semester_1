list=["gopal","ravo"]
tuple=[("gopal",2006),"ravi",2007]
dict={"gopal":"Inactive","ravi":"active"}
activities={"football","cricket"}
"""N=int(input("enter the number of students"))"""


"""def add_student(list,tuple,dict):
    for i in range(N):
        name=input('Enter name')
        year=int(input('Enter yr'))
        list.append(name)
        tuple.append((name,year))
        dict[name]='Active' 
    return list,tuple,dict
print(add_student(list,tuple,dict))"""

"""def update_activities(activities,new_activity):
    y=set({new_activity})
    if new_activity not in activities:
        activities.update(y)
        print(activities)


new_activity=input("enter the new activity")
update_activities(activities,new_activity)"""

def check_membership(dict,name):
    x=dict[name]
    count=0
    for i in dict:
        if dict[i]=="active":
            count+=1
    print((x,count))


name=input("enter the name")
check_membership(dict,name)
