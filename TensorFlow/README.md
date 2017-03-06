* TensorFlow

** Session

- tf.Session

** Variables and types

- tf.placeholder and feed_dict
- tf.cast

** Math

- tf.add, tf.subtract, tf.mul, ...
- tf.matmul, ...


** Terminology

- Logits

- SoftMax

- One-hot encoding
```
lb = sklearn.preprocessing.LabelBinarizer()
lb.fit(labels)
lb.transform(labels)
```

- Cross entropy
```
cross_entropy = - tf.reduce_sum(tf.mul(one_hot, tf.log(softmax)))
```

- Loss = avg(cross entropy)

- Normalized inputs and initial weights

1. Inputs: mean=0, equal variance
2. Inital weights: random, mean=0, equal variance
```
# a bad example
a = 1000000000
for i in range(1000000):
    a = a + 1e-6
print(a - 1000000000)
> 0.953674316406
```

- Stochastic gradient descent and mini-batching

- Momentum and learning rate decay


