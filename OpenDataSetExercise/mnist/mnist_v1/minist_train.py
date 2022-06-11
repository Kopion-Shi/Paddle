# -*- coding: utf-8 -*-
# @Time    : 2022/6/11 12:06
# @Author  : 石鑫磊
# @Site    : 
# @File    : minist_train.py
# @Software: PyCharm 
# @Comment :
#加载飞桨和相关类库
import paddle
from paddle.nn import Linear
import paddle.nn.functional as F
import os
import numpy as np
import matplotlib.pyplot as plt