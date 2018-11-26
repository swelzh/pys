import tensorflow as tf 

classifier  = tf.estimator.LinearClassifier()

classifier.train(input_fn=train_inpu_fn, steps=2000)

predications = classifier.predict(input_fn=predict_input_fn)