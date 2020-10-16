import json

#读取json格式的数据
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    '''
       引入模块json，json.load()可以将数据转换为python能处理的格式，此时为一个列表
    '''
    all_eq_data = json.load(f)   #类似于一个很大的对象，一个map集合

#每个元素都是一个字典，包含很多键值对
all_eq_dicts = all_eq_data['features']
# a = all_eq_data['type']
# print(',,,,,,,,',a)

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#显示列表中0-10序号的数，不包含10
print(mags[:10])
#显示列表中0-5序号的数，不包含5
print(lons[:5])
#显示列表中0-5序号的数，不包含5
print(lats[:5])
