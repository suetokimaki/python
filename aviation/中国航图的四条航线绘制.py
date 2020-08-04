import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap
import xlrd

ex = xlrd.open_workbook(r'D:\\university\\python\\data3.xlsx')
table = ex.sheet_by_index(0)
nrows = table.nrows

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文必备
plt.figure(1, dpi=100)
map = Basemap(llcrnrlon=115, llcrnrlat=36.3, urcrnrlon=119, urcrnrlat=40,
              projection='lcc', lat_1=33, lat_2=45, lon_0=100)
map.drawcoastlines()
map.drawcountries()

map.readshapefile('D:\\university\\python\\gadm36_CHN_shp\\gadm36_CHN_1',
                  'states', drawbounds=True)
map.readshapefile('D:\\university\\python\\gadm36_TWN_shp\\gadm36_TWN_1',
                  'taiwan', drawbounds=True)
parallels = np.linspace(3, 55, 40)
map.drawparallels(parallels, labels=[True, False, False, False])
meridians = np.linspace(70, 140, 40)
map.drawmeridians(meridians, labels=[False, False, False, True])

ax = plt.gca()
for nshape, seg in enumerate(map.states):
    poly = Polygon(seg, facecolor='g', alpha=0.5)
    ax.add_patch(poly)


def fun(s, e):
    for row in range(s, e):
        start_lon = table.cell_value(row, 2)
        start_lat = table.cell_value(row, 1)
        end_lon = table.cell_value(row, 4)
        end_lat = table.cell_value(row, 3)
        map.plot([start_lon, end_lon],[start_lat,end_lat],latlon=True,linewidth=2, color="#DF666A", markersize=10,marker='^',markerfacecolor='black')


fun(1, 3)  # 待改进部分
fun(3, 5)
fun(5, 7)
fun(7, nrows)

plt.title(r'中国航图的四条航线', fontsize=24)

plt.show()
