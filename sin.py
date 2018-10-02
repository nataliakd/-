#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  #импортирование модуля math
import numpy  #импортирование модуля numpy
import matplotlib.pyplot as mpp #импортируем модуль и переназываем его для краткости


if __name__=='__main__':  
    arguments = numpy.r_[0:200:0.1] #создаем массив аргументов
    mpp.plot(  #строим график
        arguments,  #передаем массив аргументов
        [math.sin(a) * math.sin(a/20.0) for a in arguments]  #задаем массив значений для каждого аргумента
    )
    mpp.show()  #выводим на экран график
