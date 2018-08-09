import pickle
import os


def make_map(new_map, map_name):
    path = os.getcwd()
    dir = path + "\\Gamemap\\" + map_name + ".json"
    f = open(dir, "wb")
    width=len(new_map[0])
    height=len(new_map)
    pickle.dump(new_map,f)
    pickle.dump(width,f)
    pickle.dump(height,f)
    f.close()


def load_map(map_name):
    path = "..\\Gamemap\\" + map_name + ".json"
    f = open(path, "rb")
    game_map = pickle.load(f)
    width=pickle.load(f)
    height=pickle.load(f)
    f.close()
    return game_map,width,height

if __name__=="__main__":
   import numpy as np
   m=np.array([
       [0,0,0,0,0,0,0],
       [0,0,1,1,1,0,0],
       [0,1,0,0,0,1,0],
       [0,0,0,0,0,0,0]
   ])
   make_map(m,"map1")
