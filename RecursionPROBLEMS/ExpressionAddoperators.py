def dfs(index,path,cur_val,prev_val,target,num,ans):
    if index==len(num):
        if cur_val==target:
            ans.append(path)
        return 
    cur=""
    for i in range(index,len(num)):
        cur=num[index:i+1]
        cur_num=int(cur)
        if i>index and num[index]=="0":
            break
        if index==0:
            dfs(i+1,cur,cur_num,cur_num,target,num,ans)
        else:
            dfs(i+1,path+'+'+cur,cur_val+cur_num,cur_num,target,num,ans)
            dfs(i+1,path+'-'+cur,cur_val-cur_num,-cur_num,target,num,ans)
            newvalue=cur_val-prev_val+(prev_val*cur_num)
            dfs(i+1,path+'*'+cur,newvalue,prev_val*cur_num,target,num,ans)
            
num="123"
target=6
ans=[]
dfs(0,"",0,0,target,num,ans)
        
print(ans)