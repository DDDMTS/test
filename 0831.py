# coding:utf-8
def suan(a, b):
    na = getn(a)
    nb = getn(b)
    rd = []
    for i in na.keys():
        if i in nb.keys():
            if(na[i] > nb[i]):
                for a in  range(nb[i]):
                    rd.append(i)
            else:
                for a in range(na[i]):
                     rd.append(i)
    return rd
def getn(a):
    temp = {}
    for i in a:
        if i in temp.keys():
            temp[i] += 1
        else:
            temp[i] = 1
    return temp
if __name__ == '__main__':
    a=[4,9,5]
    b=[9,4,8,4]
    data = suan(a, b)
    for i in data:
        print(str(i)+" ")
# 如果已经给定顺序可以按顺序比较，从第一位开始，a比b小的时候，a向后移一位，b小的时候，则b向后移一位，ab相等的时候，输出且ab同时向后移一位
# 用num2的每一位和num1比较，相同的时候num1对应位删除，同时输出
# 每次取出Num2的一部分和num1比较，遇到相同的数字输出，并删除num1中对应的数字（如果num2是有序的，可以每次取出一部分并按第一条方法排序）