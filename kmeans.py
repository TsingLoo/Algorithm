
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
file_name ='gaochengzuobiao.csv'
arr = genfromtxt(file_name, delimiter=',')
#print(type(my_data))
#print(my_data.__len__)

def distance(e1, e2):
    return np.sqrt((e1[0]-e2[0])**2+(e1[1]-e2[1])**2)

# 集合中心
def means(arr):
    return np.array([np.mean([e[0] for e in arr]), np.mean([e[1] for e in arr])])

# arr中距离a最远的元素，用于初始化聚类中心
def farthest(k_arr, arr):
    f = [0, 0]
    max_d = 0
    for e in arr:
        d = 0
        for i in range(k_arr.__len__()):
            d = d + np.sqrt(distance(k_arr[i], e))
        if d > max_d:
            max_d = d
            f = e
    return f

# arr中距离a最近的元素，用于聚类
def closest(a, arr):
    c = arr[1]
    min_d = distance(a, arr[1])
    arr = arr[1:]
    for e in arr:
        d = distance(a, e)
        if d < min_d:
            min_d = d
            c = e
    return c


if __name__=="__main__":
    ## 生成二维随机坐标，手上有数据集的朋友注意，理解arr改起来就很容易了
    ## arr是一个数组，每个元素都是一个二元组，代表着一个坐标
    ## arr形如：[ (x1, y1), (x2, y2), (x3, y3) ... ]
    #arr = np.random.randint(100, size=(100, 1, 2))[:, 0, :]
    #print(type(arr))
    #print(arr.__len__)
    ## 初始化聚类中心和聚类容器
    m = 5
    r = np.random.randint(arr.__len__() - 1)
    print("--------------------------------")
    print("Read " + file_name + " successfully")
    print("--------------------------------")
    k_arr = np.array([arr[r]])
    cla_arr = [[]]
    for i in range(m-1):
        print("Initializing... " + str(i) +"/" + str(m-1) + " Done")
        k = farthest(k_arr, arr)
        k_arr = np.concatenate([k_arr, np.array([k])])
        cla_arr.append([])

    print("Initializing... Done")
    print("--------------------------------")

    ## 迭代聚类
    n = 20
    cla_temp = cla_arr
    for i in range(n):    # 迭代n次
        print("Calculating... " + str(i) + "/" +str(n) + " Done")
        for e in arr:    # 把集合里每一个元素聚到最近的类
            ki = 0        # 假定距离第一个中心最近
            min_d = distance(e, k_arr[ki])
            for j in range(1, k_arr.__len__()):
                if distance(e, k_arr[j]) < min_d:    # 找到更近的聚类中心
                    min_d = distance(e, k_arr[j])
                    ki = j
            cla_temp[ki].append(e)
        # 迭代更新聚类中心
        for k in range(k_arr.__len__()):
            if n - 1 == i:
                break
            k_arr[k] = means(cla_temp[k])
            cla_temp[k] = []

    print("Calculating... Done")

    print("--------The Results are---------")


    ## 可视化展示
    col = ['HotPink', 'Aqua', 'Chartreuse', 'yellow', 'LightSalmon']


    for i in range(m):

        print("Cluster center (" + str(k_arr[i][0]) + "," + str(k_arr[i][1]) + ") for color " + col[i])

        print("Leftmost : " + str(min([e[0] for e in cla_temp[i]])))

        #for e in cla_temp[i]:

        #    if e[0] == min([e[0] for e in cla_temp[i]]):
        #        print("Leftmost : (" + str(min([e[0] for e in cla_temp[i]])) + "," + str([e[1]] ) + ")")
        #    else:
        #        if e[0] == max([e[0] for e in cla_temp[i]]):
        #            print("Rightmost : (" + str(max([e[0] for e in cla_temp[i]])) + "," + str(e[1])+  ")")

        print("--------------------")
        plt.scatter(k_arr[i][0], k_arr[i][1], linewidth=12, color=col[i])
        plt.scatter([e[0] for e in cla_temp[i]], [e[1] for e in cla_temp[i]], color=col[i])
    print("--------------END---------------")
    plt.show()
