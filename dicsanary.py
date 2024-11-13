 #Dictionary

# d={ 1:"monday","two":"tuesday","three":"wednsday"}
# print(d)
# print("\n")
# print(d["two"])
# ==========================================

# d={ 1:"monday","two":"tuesday","three":"wednsday"}
# print(d)
# d["four"]="thursday"
# d["five"]="friday"
# d["one"]="friday"
# print(d)
# =========(updete)============
# d={ 1:"monday","two":"tuesday","three":"wednsday"}
# print(d)
# d.update({"six":"saturday"})
# print(d)
# ===============================
# dic = {1:"mon",2:"tue",3:"wed"}
# dic.update({4:"thus"})
# dic[5]="fri"
# print(dic)
# ========================(21-oct)=====================================
# d ={1:["ayaj",23,"bhopal"],2:["jay",23,"ujjain"]}
# print(d)
# print(d[1])
# print(d[1][2])
# # ========================================
# dic = {1:["ayaj",23,"bhopal"],2:["jay",23,"ujjain"]}
# print(dic)
# dic[2][2]="indore"
# print(dic)
# ===================

# d1 = {101:{"name":"ajay","age":23,"city":"bhopal"},
#      102:{"name":"jay","age":23,"city":"ujjain"}}

# print(d1)
# print(d1[101])
# print(d1[101]["city"])
# d1[102]["city"]="indore"
# print(d1)
# d1[102].update({"city":"betul"})
# print(d1)
# =============================(method of dictonary)========================================
# d={1:"mon",2:"tue",3:"wed"}
# #kesys()
# keys=d.keys()
# print(keys)
# #valus()
# values=d.values()
# print(values)
# #items()
# items=d.items()
# print(items)
# ===============================(22/10)zip=================================================
# key = ["Ajay","vikash","Ankur","Shubham","Danish"]
# value = [23,23,45,24,26]
# result = tuple(zip(key,value))
# print(result)
# result =dict(zip(key,value))
# print(result)
# ===========================(get function)=====================================
# data = {'Ajay':23,'Vikash':23,'Danish':45}
# a=data.get('Shivam')
# print(a)
# =================(setdefault)================================
#key available--->return existing value,
#key not avalible-->key-value pair add
                    #return added value
# data = {'1':2390, '2':2387,'3':4533}
# data.setdefault('1',9999)
# print(data)
# Value = data.setdefault('11',5654)
# print(data)
# print(Value)
# ==========================pop(),popitem()===============================================

# data = {'1':2390, '2':2387,'3':4533}
# print(data)
# value = data.pop('2')
# print(data)
# print(value)

# /==========(popitem)===============
# data = {'1':2390, '2':2387,'3':4533}
# print(data)
# value = data.popitem()
# print(data)
# print(value)
# =================================================

# data = {'1':2390, '2':2387,'3':4533,
#         '4':{'11':3523,'22':63634,'44':4574}}
# print(data)
# value = data.popitem()
# print(value)
# print(data)
#===============================================
# data = {'1':2390, '2':2387,'3':4533,
#         '4':{'11':3523,'22':63634,'44':4574}}

# print(type(data['1']))
# print(type(data['4']))
# data['4'].popitem()
# print(data)
# ===================================================================




