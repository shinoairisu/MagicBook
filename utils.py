# -*- coding: utf-8 -*-
import os
from ruamel import yaml
import glob

#测试git

def getConfig():
    """
    获取config.yaml
    只有config.yaml中为true的tag文件才会被读取
    """
    ymlContents = None
    with open("config.yml", "r", encoding="utf-8") as f:
        ymlContents = yaml.load(f.read(), Loader=yaml.Loader)
    return ymlContents


def setConfig(name,able): #哪个数据库，是否启用
    ymlContents = None
    with open("config.yml", "r", encoding="utf-8") as f:
        ymlContents = yaml.load(f.read(), Loader=yaml.Loader)
    ymlContents[name] = able
    with open("config.yml", "w", encoding="utf-8") as f:
        yaml.dump(ymlContents, f, Dumper=yaml.RoundTripDumper)


def getTagConfig():
    """
    获取所有的tag文件名
    """
    content = getConfig()
    


def getTagContent():
    """
    获取tag内容
    """
    pass


def refreshConfig():
    """
    设置config.yaml
    扫描所有 tagdbs 新文件,删除没有的文件,默认新文件配置false
    """
    ymlFiles = glob.glob("./tagdbs/*.yml")
    ymlContents = None
    names = list(
        map(lambda x: os.path.basename(x).replace(".yml", ""), ymlFiles))
    with open("config.yml", "r", encoding="utf-8") as f:
        ymlContents = yaml.load(f.read(), Loader=yaml.Loader)
    for i in names:  #遍历文件夹，如果已经写入config，则跳过，没有则写入False
        if i not in ymlContents:
            ymlContents[i] = False
    for i in ymlContents.copy():  #遍历配置文件，如果文件夹没有某文件，则也从这里剔除
        if i not in names:
            del ymlContents[i]

    with open("config.yml", "w", encoding="utf-8") as f:
        yaml.dump(ymlContents, f, Dumper=yaml.RoundTripDumper)


if __name__ == "__main__":
    getConfig()