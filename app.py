import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
import pygame

# Loading the pre-trained TensorFlow model
model = tf.keras.models.load_model('gesture_model.h5')
model.summary()