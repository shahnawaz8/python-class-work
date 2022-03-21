import json
data={}
data['people']=[]
data['people'].append(
{
    'name':'Tiger',
    'website':'smat.com',
    'from':'Nebrsaka'
    
})
data['people'].append(
{
    'name':'larry',
    'website':'google.com',
    'from':'noida'
    
})
data['people'].append(
{
    'name':'lucky',
    'website':'mains.com',
    'from':'delhi'
    
})
with open('hs.json','w') as file:
    json.dump(data,file)