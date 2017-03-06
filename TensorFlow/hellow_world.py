import tensorflow as tf

# build network model
hello_constant = tf.constant('Hello')

# run operations
with tf.Session() as sess:

    output = sess.run(hello_constant)
    print(output)
