languages =  ["Python", "Java", "C++", "JavaScript"]

reversed_list=[]

for i in range(len(languages)-1,-1,-1):
    reversed_list.append(languages[i])
print("Reversed List: ", reversed_list)