import numpy as np


from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import Session
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import VGG16
from keras.layers import Dense, Flatten
from keras.models import Model
from keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, confusion_matrix



#CONSTANTS
IMAGE_SIZE = (150, 150)
BATCH_SIZE = 32
EPOCHS = 50

########################################################
# GPU config (memory allocation errors fix)
config = ConfigProto()
config.gpu_options.allow_growth = True
session = Session(config=config)




########################################################
#Settings for train and validation datagens
train_datagen = ImageDataGenerator(
        rotation_range=5,
        rescale=1./255,
        horizontal_flip=True,
        fill_mode='nearest'
)


validation_datagen = ImageDataGenerator(rescale=1./255)


#######################################################
#Fitting data from local directories
train_gen = train_datagen.flow_from_directory(
        './data/train',
        target_size = IMAGE_SIZE,
        batch_size = BATCH_SIZE,
        class_mode = 'categorical',
        color_mode = 'rgb',
        shuffle=True
)

validation_gen = validation_datagen.flow_from_directory(
        './data/test',
        target_size = IMAGE_SIZE,
        batch_size = BATCH_SIZE,
        class_mode = 'categorical',
        color_mode = 'rgb',
        shuffle=False
)

#################################################
#EARLY STOPPING
callback = EarlyStopping(monitor='val_loss', patience=5)


#################################################
#################################################
#Using transfer learning
#Our base model will be VGG16

model = VGG16(weights='imagenet')
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(150,150,3))

# Freeze convolutional layers
for layer in base_model.layers:
    layer.trainable = False

# New block of convolutional layers
x = base_model.output
x = Flatten()(x)  # flatten from convolution tensor output (from VGG16)
x = Dense(500, activation='relu')(x)

x = Dense(500, activation='relu')(x)
predictions = Dense(13, activation='softmax')(x) # match number of classes predicted

#This model we are training
model = Model(inputs=base_model.input, outputs=predictions)
model.compile(optimizer='adam', loss='categorical_crossentropy',
                 metrics=['categorical_accuracy'])

model.summary()


history = model.fit(
        train_gen,
        epochs=EPOCHS,
        callbacks=[callback],
        verbose = 1,
        validation_data=validation_gen
)

#saving our trained model to a file
model.save('model_VGG16.h5')






#####################################################################
#Generating learning report

validation_gen.reset()
Y_prediction = model.predict_generator(validation_gen)
classes = validation_gen.classes[validation_gen.index_array]
y_prediction_argument = np.argmax(Y_prediction, axis= -1)
print(sum(y_prediction_argument==classes)/800)

target_names = ['Black Bishop', 'Black King', 'Black Knight', 'Black Pawn',
                'Black Queen', 'Black Rook', 'Empty', 'White Bishop', 'White King',
                'White Knight', 'White Pawn', 'White Queen', 'White Rook']

print('~~~~~~~~~~~~~~~~~~~~~~CLASSIFICATION REPORT~~~~~~~~~~~~~~~~~~~~')
print(classification_report(validation_gen.classes[validation_gen.index_array],
                            y_prediction_argument, target_names=target_names))

print('~~~~~~~~~~~~~~~~~~~~~~CONFUSION MATRIX~~~~~~~~~~~~~~~~~~~~~~~~~')
print(confusion_matrix(classes,y_prediction_argument))
