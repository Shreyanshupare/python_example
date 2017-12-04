import tensorflow as tf
sess = tf.InteractiveSession()
x = tf.constant([[2,5,3,-5],
                 [0,3,-2,5],
                 [4,3,5,3],
                 [6,1,4,0]])
print(tf.shape(x).eval())
print("--------")
print(tf.size(x).eval())
print("--------")
print(tf.rank(x).eval())
print("--------")
print(tf.reshape(x,[8,2]).eval())
print("--------")
print(tf.squeeze(x).eval())
print("--------")
print("----++++++++++++++++++++++++----")

t_matrix = tf.constant([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
t_array = tf.constant([1,2,3,4,9,8,6,5])
t_array2 = tf.constant([2,3,4,5,6,7,8,9])

print(tf.slice(t_matrix,[1,1],[2,2]).eval())
#print(tf.split(0,2,t_array))
print(tf.tile([1,2],[3]).eval())
