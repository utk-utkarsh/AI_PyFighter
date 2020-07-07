# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:05:37 2020

@author: Crucifier
"""

import keras
from keras.applications.mobilenet import MobileNet
from keras.layers import Dense, Input, Dropout
from keras.models import Model

mobile=keras.applications.mobilenet.MobileNet()
mobile.summary()