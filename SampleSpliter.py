import random
import numpy as np
from numpy.core.records import array

sample_size = input('sample size>>')
sample_size = int(sample_size)

sample_rate = input('sample rate>>')
sample_rate = float(sample_rate)

start_id = input('start file name is 0?>>')

sample_arrray = []

if start_id == 'y':
    sample_arrray = range(0,sample_size)
else:
    sample_arrray = range(1,sample_size+1)


train_data_name = input('train data name>>')
validation_data_name = input('validation data name>>')

train_array = random.sample(sample_arrray,int(round(sample_size*sample_rate,0)))
validation_array = random.sample(sample_arrray,sample_size-len(train_array))

train_array.sort()
validation_array.sort()

#ファイルへの書き込み
with open('./'+train_data_name,'w') as f:
    for line in train_array:
        f.write(str(line).zfill(4)+'\n')

with open('./'+validation_data_name,'w') as f:
    for line in validation_array:
        f.write(str(line).zfill(4)+'\n')