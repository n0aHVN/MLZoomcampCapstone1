import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow import keras
from tensorflow.keras.applications.xception import Xception # type: ignore
from tensorflow.keras.applications.xception import preprocess_input
from tensorflow.keras.applications.xception import decode_predictions
from tensorflow.keras.preprocessing.image import load_img, ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras import layers, models, losses, optimizers

inner_size = 128
lr = 1e-05
droprate=0.5

train_gen = ImageDataGenerator(
    preprocessing_function=preprocess_input
)

train_ds = train_gen.flow_from_directory(
    './data/train',
    target_size=(150, 150),
    batch_size=20
)


val_gen = ImageDataGenerator(preprocessing_function=preprocess_input)

val_ds = train_gen.flow_from_directory(
    './data/test',
    target_size=(150, 150),
    batch_size=20,
    shuffle=False
)

def make_model(
        base_model = Xception(
            weights='imagenet',
            include_top=False,
            input_shape=(150, 150, 3)
        ),
        dense_inner_size = 64,
        learning_rate = 0.001,
        droprate = 0
):
    
    ########################
    inputs = keras.Input(shape=(150, 150, 3))
    base = base_model(inputs, training = False)
    vectors = layers.GlobalAveragePooling2D()(base)
    inner = layers.Dense(dense_inner_size, activation='relu')(vectors)
    drop = keras.layers.Dropout(droprate)(inner)
    
    outputs = keras.layers.Dense(5)(drop)
    model = keras.Model(inputs, outputs)

    '][==]'
    ########################
    
    optimizer = optimizers.Adam(learning_rate=learning_rate)
    loss = losses.CategoricalCrossentropy(from_logits=True)

    model.compile(
        optimizer=optimizer,
        loss=loss,
        metrics=['accuracy']
    )

    return model

model = make_model(
    dense_inner_size = inner_size,
    learning_rate= lr,
    droprate=droprate
)
checkpoint = keras.callbacks.ModelCheckpoint(
    './models/xception_{epoch:02d}_{val_accuracy:.3f}.h5',
    save_best_only=True,
    monitor='val_accuracy',
    mode='max'
)
history = model.fit(train_ds, 
                    epochs = 50, 
                    validation_data = val_ds, 
                    callbacks=[checkpoint]
)
