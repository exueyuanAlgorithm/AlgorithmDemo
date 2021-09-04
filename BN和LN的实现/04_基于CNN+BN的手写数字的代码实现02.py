# -- encoding:utf-8 --
"""
Create on 19/5/25 10:06
"""

import os
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 定义外部传入的参数
tf.app.flags.DEFINE_bool(flag_name="is_train",
                         default_value=True,
                         docstring="给定是否是训练操作，True表示训练，False表示预测！！")
tf.app.flags.DEFINE_string(flag_name="checkpoint_dir",
                           default_value="./models_bn2",
                           docstring="给定模型存储的文件夹，默认为./models_bn2")
tf.app.flags.DEFINE_string(flag_name="logdir",
                           default_value="./graph_bn2",
                           docstring="给定模型日志存储的路径，默认为./graph_bn2")
tf.app.flags.DEFINE_integer(flag_name="batch_size",
                            default_value=16,
                            docstring="给定训练的时候每个批次的样本数目，默认为16.")
tf.app.flags.DEFINE_integer(flag_name="store_per_batch",
                            default_value=100,
                            docstring="给定每隔多少个批次进行一次模型持久化的操作，默认为100")
tf.app.flags.DEFINE_integer(flag_name="validation_per_batch",
                            default_value=100,
                            docstring="给定每隔多少个批次进行一次模型的验证操作，默认为100")
tf.app.flags.DEFINE_float(flag_name="learning_rate",
                          default_value=0.01,
                          docstring="给定模型的学习率，默认0.01")
FLAGS = tf.app.flags.FLAGS


def batch_normalization(net, shape, is_training, moving_decay=0.9, eps=1e-8):
    with tf.variable_scope("BN"):
        return tf.layers.batch_normalization(net, training=is_training,
                                             momentum=moving_decay, epsilon=eps)


def create_dir_with_not_exits(dir_path):
    """
    如果文件的文件夹路径不存在，直接创建
    :param dir_path:
    :return:
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def create_model(input_x, is_training):
    """
    构建模型
    :param input_x: 占位符，格式为[None, 784]
    :return:
    """
    # 定义一个网络结构: input -> conv -> relu -> pooling -> conv -> relu -> pooling -> FC -> relu -> FC
    with tf.variable_scope("net"):
        with tf.variable_scope("Input"):
            # 这里定义一些图像的处理方式，包括：格式转换、基础处理(大小、剪切...)
            net = tf.reshape(input_x, shape=[-1, 28, 28, 1])
            print(net.get_shape())

            # 可视化图像
            tf.summary.image(name='image', tensor=net, max_outputs=5)
        with tf.variable_scope("Conv1"):
            """
            def conv2d(input, filter, strides, padding, use_cudnn_on_gpu=True, data_format="NHWC", name=None):
                input：输入的tensor对象，会对该值进行卷积操作。默认形状为：[batch_size, height, width, channels]， batch_size表示一个批次中的样本数目，height表示一个feature map的高度，width表示一个feature map的宽度，channels表示一个图像的feature map的数量。一般简写为NHWC。当data_format的格式为NHWC的时候，使用默认的形状，如果给给data_format给定位NCHW，那么input的格式为:[batch_size, channels, height, width]
                filter: 卷积核Tensor对象(w)，格式要求是一个4维的Tensor对象(一般为变量), 格式为: [height, width, in_channels, out_channels]，height和width表示窗口的高度宽度，in_channels就是输入对象的通道数目，out_channels给定当前卷积之后的通道数目，也就是我们理论中所说的卷积核的数目。
                strides: 给定卷积窗口的滑动步长，格式和data_format有关，是一个数组。格式: [batch, in_height, in_width, in_channels]或者[batch, in_channels, in_height, in_width], 其中batch和in_channels必须为1，in_height和in_width分别给定在高度和宽度上的滑动窗口大小。
                padding：是否进行数据的填充操作，可选值：SAME表示进行最小填充，VALID表示不进行填充，直接删除多余的像素值。TensorFlow中有一个特征的值，当步长为1，padding为SAME的时候，卷积是不改变的feature map大小的。
                data_format：给定数据格式是NHWC还是NCHW，默认是NHWC
            """
            filter = tf.get_variable(name='w', shape=[3, 3, 1, 10])
            bias = tf.get_variable(name='b', shape=[10])
            net = tf.nn.conv2d(input=net, filter=filter, strides=[1, 1, 1, 1], padding='SAME')
            net = tf.nn.bias_add(net, bias)
            shape = net.get_shape()
            print(shape)

            # 加入批归一化
            net = batch_normalization(net, shape, is_training)
            shape = net.get_shape()
            print(shape)

            # 对于卷积之后的值做一个可视化操作
            for k in range(shape[-1]):
                image_tensor = tf.reshape(net[:, :, :, k], shape=[-1, shape[1], shape[2], 1])
                tf.summary.image(name='image', tensor=image_tensor, max_outputs=5)
        with tf.variable_scope("Relu1"):
            net = tf.nn.relu(net)
            print(net.get_shape())

            # 对于卷积之后的值做一个可视化操作
            shape = net.get_shape()
            for k in range(shape[-1]):
                image_tensor = tf.reshape(net[:, :, :, k], shape=[-1, shape[1], shape[2], 1])
                tf.summary.image(name='image', tensor=image_tensor, max_outputs=5)
        with tf.variable_scope("Pooling1"):
            """
            def max_pool(value, ksize, strides, padding, data_format="NHWC", name=None):
                value: 给定需要进行池化的tensor对象， 默认形状为：[batch_size, height, width, channels]， batch_size表示一个批次中的样本数目，height表示一个feature map的高度，width表示一个feature map的宽度，channels表示一个图像的feature map的数量。一般简写为NHWC。当data_format的格式为NHWC的时候，使用默认的形状，如果给给data_format给定位NCHW，那么input的格式为:[batch_size, channels, height, width]
                ksize: 包含四个整数的数组, 形状为: data_format为NHWC[batch, in_height, in_width, in_channels]或者data_format值为NCHW[batch, in_channels, in_height, in_width]; 要求batch和in_channels必须为1，in_height和in_width指定的就是池化窗口的高度和宽度
                strides: 给定卷积窗口的滑动步长，格式和data_format有关，是一个数组。格式: [batch, in_height, in_width, in_channels]或者[batch, in_channels, in_height, in_width], 其中batch和in_channels必须为1，in_height和in_width分别给定在高度和宽度上的滑动窗口大小。
                padding：是否进行数据的填充操作，可选值：SAME表示进行最小填充，VALID表示不进行填充，直接删除多余的像素值。TensorFlow中有一个特征的值，当步长为1，padding为SAME的时候，池化是不改变的feature map大小的。
                data_format：给定数据格式是NHWC还是NCHW，默认是NHWC
            """
            # ksize：池化的窗口形状；strides：窗口的滑动大小。
            net = tf.nn.max_pool(value=net, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
            print(net.get_shape())

            # 对于卷积之后的值做一个可视化操作
            shape = net.get_shape()
            for k in range(shape[-1]):
                image_tensor = tf.reshape(net[:, :, :, k], shape=[-1, shape[1], shape[2], 1])
                tf.summary.image(name='image', tensor=image_tensor, max_outputs=5)
        with tf.variable_scope("Conv2"):
            filter = tf.get_variable(name='w', shape=[3, 3, 10, 20])
            bias = tf.get_variable(name='b', shape=[20])
            net = tf.nn.conv2d(input=net, filter=filter, strides=[1, 1, 1, 1], padding='SAME')
            net = tf.nn.bias_add(net, bias)
            shape = net.get_shape()
            print(shape)

            # 加入批归一化
            net = batch_normalization(net, shape, is_training)
            shape = net.get_shape()
            print(shape)

            # 对于卷积之后的值做一个可视化操作
            for k in range(shape[-1]):
                image_tensor = tf.reshape(net[:, :, :, k], shape=[-1, shape[1], shape[2], 1])
                tf.summary.image(name='image', tensor=image_tensor, max_outputs=5)
        with tf.variable_scope("Relu2"):
            net = tf.nn.relu(net)
            print(net.get_shape())

            # 对于卷积之后的值做一个可视化操作
            shape = net.get_shape()
            for k in range(shape[-1]):
                image_tensor = tf.reshape(net[:, :, :, k], shape=[-1, shape[1], shape[2], 1])
                tf.summary.image(name='image', tensor=image_tensor, max_outputs=5)
        with tf.variable_scope("Pooling2"):
            net = tf.nn.max_pool(value=net, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
            print(net.get_shape())

            # 对于卷积之后的值做一个可视化操作
            shape = net.get_shape()
            for k in range(shape[-1]):
                image_tensor = tf.reshape(net[:, :, :, k], shape=[-1, shape[1], shape[2], 1])
                tf.summary.image(name='image', tensor=image_tensor, max_outputs=5)
        with tf.variable_scope("FC1"):
            shape = net.get_shape()
            dim_size = shape[1] * shape[2] * shape[3]
            net = tf.reshape(net, shape=[-1, dim_size])
            w = tf.get_variable(name='w', shape=[dim_size, 500])
            b = tf.get_variable(name='b', shape=[500])
            net = tf.matmul(net, w) + b
            net = tf.nn.relu(net)
        with tf.variable_scope("FC2"):
            w = tf.get_variable(name='w', shape=[500, 10])
            b = tf.get_variable(name='b', shape=[10])
            logits = tf.matmul(net, w) + b
        with tf.variable_scope("Prediction"):
            # 每行的最大值对应的下标就是当前样本的预测值
            predictions = tf.argmax(logits, axis=1)

    return logits, predictions


def create_loss(labels, logits):
    """
    基于给定的实际值labels和预测值logits进行一个交叉熵损失函数的构建
    :param labels:  是经过哑编码之后的Tensor对象，形状为[n_samples, n_class]
    :param logits:  是神经网络的最原始的输出，形状为[n_samples, n_class], 每一行最大值那个位置对应的就是预测类别，没有经过softmax函数转换。
    :return:
    """
    with tf.name_scope("loss"):
        # loss = tf.reduce_mean(-tf.log(tf.reduce_sum(labels * tf.nn.softmax(logits))))
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=logits))
        tf.summary.scalar('loss', loss)
    return loss


def create_train_op(loss, learning_rate=0.01, global_step=None):
    """
    基于给定的损失函数构建一个优化器，优化器的目的就是让这个损失函数最小化
    :param loss:
    :param learning_rate:
    :param global_step:
    :return:
    """
    with tf.name_scope("train"):
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
        update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
        with tf.control_dependencies(update_ops):
            train_op = optimizer.minimize(loss, global_step=global_step)
    return train_op


def create_accuracy(labels, predictions):
    """
    基于给定的实际值和预测值，计算准确率
    :param labels:  是经过哑编码之后的Tensor对象，形状为[n_samples, n_class]
    :param predictions: 实际的预测类别下标，形状为[n_samples,]
    :return:
    """
    with tf.name_scope("accuracy"):
        # 获取实际的类别下标，形状为[n_samples,]
        y_labels = tf.argmax(labels, 1)
        # 计算准确率
        accuracy = tf.reduce_mean(tf.cast(tf.equal(y_labels, predictions), tf.float32))
        tf.summary.scalar('accuracy', accuracy)
    return accuracy


def train():
    # 对于文件是否存在做一个检测
    create_dir_with_not_exits(FLAGS.checkpoint_dir)
    create_dir_with_not_exits(FLAGS.logdir)

    with tf.Graph().as_default():
        # 一、执行图的构建
        # 0. 相关输入Tensor对象的构建
        input_x = tf.placeholder(dtype=tf.float32, shape=[None, 784], name='input_x')
        input_y = tf.placeholder(dtype=tf.float32, shape=[None, 10], name='input_y')
        is_training = tf.placeholder_with_default(False, shape=[], name='is_training')
        global_step = tf.train.get_or_create_global_step()

        # 1. 网络结构的构建
        logits, predictions = create_model(input_x, is_training)
        # 2. 构建损失函数
        loss = create_loss(input_y, logits)
        # 3. 构建优化器
        train_op = create_train_op(loss,
                                   learning_rate=FLAGS.learning_rate,
                                   global_step=global_step)
        # 4. 构建评估指标
        accuracy = create_accuracy(input_y, predictions)

        # 二、执行图的运行/训练(数据加载、训练、持久化、可视化、模型的恢复....)
        with tf.Session() as sess:
            # a. 创建一个持久化对象(默认会将所有的模型参数全部持久化，因为不是所有的都需要的，最好仅仅持久化的训练的模型参数)
            var_list = tf.trainable_variables()
            # 是因为global_step这个变量是不参与模型训练的，所以模型不会持久化，这里加入之后，可以明确也持久化这个变量。
            var_list.append(global_step)
            saver = tf.train.Saver(var_list=var_list)

            # a. 变量的初始化操作(所有的非训练变量的初始化 + 持久化的变量恢复)
            # 所有变量初始化(如果有持久化的，后面做了持久化后，会覆盖的)
            sess.run(tf.global_variables_initializer())
            # 做模型的恢复操作
            ckpt = tf.train.get_checkpoint_state(FLAGS.checkpoint_dir)
            if ckpt and ckpt.model_checkpoint_path:
                print("进行模型恢复操作...")
                # 恢复模型
                saver.restore(sess, ckpt.model_checkpoint_path)
                # 恢复checkpoint的管理信息
                saver.recover_last_checkpoints(ckpt.all_model_checkpoint_paths)

            # 获取一个日志输出对象
            train_logdir = os.path.join(FLAGS.logdir, 'train')
            validation_logdir = os.path.join(FLAGS.logdir, 'validation')
            train_writer = tf.summary.FileWriter(logdir=train_logdir, graph=sess.graph)
            validation_writer = tf.summary.FileWriter(logdir=validation_logdir, graph=sess.graph)
            # 获取所有的summary输出操作
            summary = tf.summary.merge_all()

            # b. 训练数据的产生/获取（基于numpy随机产生<可以先考虑一个固定的数据集>）
            mnist = input_data.read_data_sets(
                train_dir='../datas/mnist',  # 给定本地磁盘的数据存储路径
                one_hot=True,  # 给定返回的数据中是否对Y做哑编码
                validation_size=5000  # 给定验证数据集的大小
            )

            # c. 模型训练
            batch_size = FLAGS.batch_size
            step = sess.run(global_step)
            vn_accuracy_ = 0
            while True:
                # 开始模型训练
                x_train, y_train = mnist.train.next_batch(batch_size=batch_size)
                _, loss_, accuracy_, summary_ = sess.run([train_op, loss, accuracy, summary], feed_dict={
                    input_x: x_train,
                    input_y: y_train,
                    is_training: True
                })
                print("第{}次训练后模型的损失函数为:{}, 准确率:{}".format(step, loss_, accuracy_))
                train_writer.add_summary(summary_, global_step=step)

                # 持久化
                if step % FLAGS.store_per_batch == 0:
                    file_name = 'model_%.3f_%.3f_.ckpt' % (loss_, accuracy_)
                    save_path = os.path.join(FLAGS.checkpoint_dir, file_name)
                    saver.save(sess, save_path=save_path, global_step=step)

                if step % FLAGS.validation_per_batch == 0:
                    vn_loss_, vn_accuracy_, vn_summary_ = sess.run([loss, accuracy, summary],
                                                                   feed_dict={
                                                                       input_x: mnist.validation.images,
                                                                       input_y: mnist.validation.labels
                                                                   })
                    print("第{}次训练后模型在验证数据上的损失函数为:{}, 准确率:{}".format(step,
                                                                    vn_loss_,
                                                                    vn_accuracy_))
                    validation_writer.add_summary(vn_summary_, global_step=step)

                # 退出训练（要求当前的训练数据集上的准确率至少为0.8，然后最近一次验证数据上的准确率为0.8）
                if accuracy_ > 0.99 and vn_accuracy_ > 0.99:
                    # 退出之前再做一次持久化操作
                    file_name = 'model_%.3f_%.3f_.ckpt' % (loss_, accuracy_)
                    save_path = os.path.join(FLAGS.checkpoint_dir, file_name)
                    saver.save(sess, save_path=save_path, global_step=step)
                    break
                step += 1
            # 关闭输出流
            train_writer.close()
            validation_writer.close()


def prediction():
    # TODO: 参考以前的代码自己把这个区域的内容填充一下。我下周晚上讲。
    # 做一个预测(预测的评估，对mnist.test这个里面的数据进行评估效果的查看)
    with tf.Graph().as_default():
        pass


def main(_):
    if FLAGS.is_train:
        # 进入训练的代码执行中
        print("开始进行模型训练运行.....")
        train()
    else:
        # 进入测试、预测的代码执行中
        print("开始进行模型验证、测试代码运行.....")
        prediction()
    print("Done!!!!")


if __name__ == '__main__':
    # 默认情况下，直接调用当前py文件中的main函数
    tf.app.run()
