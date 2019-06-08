# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g1ZZuOL9Cs8vrJM8VyvYchJC-R5Tt-Q1
"""

import tensorflow as tf
!pip install -U tensorboardcolab
from tensorboardcolab import *
import shutil

shutil.rmtree('./Graph', ignore_errors=True)
os.mkdir('./Graph')

tf.reset_default_graph()

tbc=TensorBoardColab()

const_15 = tf.constant(15.0, name = 'constant_15.0')
const_11 = tf.constant(11.0, name = 'constant_11.0')
const_60 = tf.constant(60.0, name = 'constant_60.0')

Addition = tf.add(const_11, const_15, name = 'Adding_constants')
Subtraction = tf.subtract(const_15, const_11, name = 'Subtracting_constants')
Multiplication = tf.multiply(const_15, const_11, name = 'Multiplying_constants')
Division = tf.div(const_15, const_60, name = 'Divide_constants')
Total_sum = tf.add_n([Addition, Subtraction, Multiplication, Division], name = 'total_sum')

with tf.Session() as sess:
  print("Total_Sum", sess.run(Total_sum ))

train_writer = tbc.get_writer();
train_writer.add_graph(sess.graph)

train_writer.flush();
tbc.close()

