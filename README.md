# RoadSearchingAlgorithm
Road Searching Algorithm Programed In Python

## 介绍

该项目目前提供了游戏中常用的4中寻路算法：广度优先搜索算法（BFS），迪杰斯特拉算法（Dijkstra），贪婪最优优先搜索算法（Greedy Best-First Search）以及A星路径搜索算法。

项目提供了地图存储和加载模块MapMaker。模块提供了存储地图的make_map(new_map,map_name)方法，以及加载地图的load_map(map_name)方法。
make_map(new_map,map_name)的第一个参数new_map为代表地图逻辑数据的二维数组，map_name为地图名称，调用该方法可将地图数据以及地图尺寸（宽、高）以json文件的形势保存在GameMap目录下。
调用load_map(map_name)方法，输入地图名称，即可从地图目录GameMap中加载相应的地图数据

目前，四种寻路算法核心封装在类内，对外开放find_path()接口和path[],actions[]两个属性，加载地图数据后，输入起点、终点坐标以及地图数据创建算法对象，调用find_path()方法，计算路径，返回Bool值，True表示路径存在，False表示路径不存在。访问path[]和actions[]属性，即可获得路径序列（坐标），或者动作序列（上下左右）

## Example:

```python
from AStart.A_Star_Algorithm import AStarAlgorithm
import Map_Maker as MapMaker

my_map,width,height = MapMaker.load_map("map1")


star = AStarAlgorithm(0, 0, 6, 3, width, height, my_map)


if star.find_path():
    print(star.path)
    print(star.actions)
