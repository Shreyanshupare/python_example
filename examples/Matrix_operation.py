import tensorflow as tf
sess = tf.InteractiveSession()
x = tf.constant([[2,5,3,-5],
                 [0,3,-2,5],
                 [4,3,5,3],
                 [6,1,4,0]])
y = tf.constant([[4,-7,4,-3,4],
                 [6,4,-7,4,7],
                 [2,3,2,1,4],
                 [1,5,5,5,2]])
floatx = tf.constant([[2.,5.,3.,-5.],
                 [0.,3.,-2.,5.],
                 [4.,3.,5.,3.],
                 [6.,1.,4.,0.]])
print(tf.transpose(x).eval())

print(tf.matmul(x,y).eval())
print(tf.matrix_determinant(floatx).eval())
print(tf.matrix_inverse(floatx).eval())
print(tf.matrix_solve(floatx,[[1],[1],[1],[1]]).eval())

