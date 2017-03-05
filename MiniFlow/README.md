* MiniFlow

A simple implementation of Tensorflow from Udacity course.


** Network Layer

All nodes in the same layer are calculated the same way, so they are combined
together as a matrix calculation. There are input layer, linear trasform layer
, activation function layer, and cost function layer.

In each layer, there are two required member functions, `forward` propagation
and `backward` propagation.

*Forward propagation*

This function performs whatever math we want to be in the layer.

*Backward propagation*

This function calculates the graident based on the output value and the
gradient(error) from the next layer.

** Network training

*Topological sort*

We should perform the algorithm on the layers in a certain order, in order to
propagation the calculated values along the network.

*Weight update*

The network calculate the result from the input layer to the output layer. We
then use the 'predicted' result and the expected result to find the errors.
The errors can be propagated backwards for calculating the grandients for each
layer. With the gradients in hand, we can adjust the weights in the layers.

