"""
### NOTICE ###

You need to upload this file.
You can add any function you want in this file.

"""
import numpy as np
import tensorflow as tf
import math
import scipy.ndimage as ndimage
#import blosc

class Agent(object):
    def __init__(self, sess, min_action_set):
        self.sess = sess
        self.min_action_set = min_action_set
        self.round = 0
        numActions = len(self.min_action_set)
        self.x, self.y = self.build_dqn(numActions)

        self.a = tf.placeholder(tf.float32, shape=[None, numActions])
        self.y_ = tf.placeholder(tf.float32, [None])

        # Initialize variables
        self.sess.run(tf.initialize_all_variables())

        self.saver = tf.train.Saver(max_to_keep=25)
        self.saver.restore(self.sess, 'best_model.ckpt')


    def build_dqn(self,numActions):
        """
        # TODO
            You need to build your DQN here.
            And load the pre-trained model named as './best_model.ckpt'.
            For example, 
                saver.restore(self.sess, './best_model.ckpt')
        """
        name = 'policy'
        trainable = False
        # First layer takes a screen, and shrinks by 2x
        x = tf.placeholder(tf.uint8, shape=[None, 84, 84, 4], name="screens")

        x_normalized = tf.to_float(x) / 255.0

        # Second layer convolves 32 8x8 filters with stride 4 with relu
        with tf.variable_scope("cnn1_" + name):
            W_conv1, b_conv1 = self.makeLayerVariables([8, 8, 4, 32], trainable, "conv1")

            h_conv1 = tf.nn.relu(tf.nn.conv2d(x_normalized, W_conv1, strides=[1, 4, 4, 1], padding='VALID') + b_conv1, name="h_conv1")

        # Third layer convolves 64 4x4 filters with stride 2 with relu
        with tf.variable_scope("cnn2_" + name):
            W_conv2, b_conv2 = self.makeLayerVariables([4, 4, 32, 64], trainable, "conv2")

            h_conv2 = tf.nn.relu(tf.nn.conv2d(h_conv1, W_conv2, strides=[1, 2, 2, 1], padding='VALID') + b_conv2, name="h_conv2")

        # Fourth layer convolves 64 3x3 filters with stride 1 with relu
        with tf.variable_scope("cnn3_" + name):
            W_conv3, b_conv3 = self.makeLayerVariables([3, 3, 64, 64], trainable, "conv3")

            h_conv3 = tf.nn.relu(tf.nn.conv2d(h_conv2, W_conv3, strides=[1, 1, 1, 1], padding='VALID') + b_conv3, name="h_conv3")

        h_conv3_flat = tf.reshape(h_conv3, [-1, 7 * 7 * 64], name="h_conv3_flat")

        # Fifth layer is fully connected with 512 relu units
        with tf.variable_scope("fc1_" + name):
            W_fc1, b_fc1 = self.makeLayerVariables([7 * 7 * 64, 512], trainable, "fc1")

            h_fc1 = tf.nn.relu(tf.matmul(h_conv3_flat, W_fc1) + b_fc1, name="h_fc1")

        # Sixth (Output) layer is fully connected linear layer
        with tf.variable_scope("fc2_" + name):
            W_fc2, b_fc2 = self.makeLayerVariables([512, numActions], trainable, "fc2")

            y = tf.matmul(h_fc1, W_fc2) + b_fc2
        return x, y

    def makeLayerVariables(self, shape, trainable, name_suffix):
        stdv = 1.0 / math.sqrt(np.prod(shape[0:-1]))
        weights = tf.Variable(tf.random_uniform(shape, minval=-stdv, maxval=stdv), trainable=trainable, name='W_' + name_suffix)
        biases  = tf.Variable(tf.random_uniform([shape[-1]], minval=-stdv, maxval=stdv), trainable=trainable, name='W_' + name_suffix)
        return weights, biases

    def inference(self, screens):
        y = self.sess.run([self.y], {self.x: screens})
        q_values = np.squeeze(y)
        return np.argmax(q_values)

    def getSetting(self):
        """
        # TODO
            You can only modify these three parameters.
            Adding any other parameters are not allowed.
            1. action_repeat: number of time for repeating the same action 
            2. random_init_step: number of randomly initial steps
            3. screen_type: return 0 for RGB; return 1 for GrayScale
        """
        action_repeat = 4
        screen_type = 0
        return action_repeat, screen_type

    def play(self, screen):
        """
        # TODO
            The "action" is your DQN argmax ouput.
            The "min_action_set" is used to transform DQN argmax ouput into real action number.
            For example,
                 DQN output = [0.1, 0.2, 0.1, 0.6]
                 argmax = 3
                 min_action_set = [0, 1, 3, 4]
                 real action number = 4
        """
        self.round += 1
        screen = np.dot(screen, np.array([.299, .587, .114])).astype(np.uint8)
        screen = ndimage.zoom(screen, (0.4, 0.525))
        screen.resize((84, 84, 1))
        #screen = blosc.compress(np.reshape(screen, 84 * 84).tobytes(), typesize=1)
        if self.round > 3:
            self.screens = self.screens[:3]
            self.screens.insert(0,screen)
        else:
            self.screens = [screen,screen,screen,screen]
        s = []
        for i in range(4):
            s.append(np.reshape(np.fromstring(self.screens[i], dtype=np.uint8), (84, 84, 1)))
            #s.append(np.reshape(np.fromstring(blosc.decompress(self.screens[i]), dtype=np.uint8), (84, 84, 1)))
        screens = np.reshape(np.concatenate(s,axis=2), (1, 84, 84, 4))
        action = self.inference(screens)

        return self.min_action_set[action]
