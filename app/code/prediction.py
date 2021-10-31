from keras.models import load_model
import numpy as np
import chess

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)


def cut_photo_to_64(img):
    images = []
    for j in range(1200,0,-150): #columns
        for i in range(0,1200,150): # rows
            images.append(img[j-150:j, i:i+150])
    return images


def return_fen(img):
    images = cut_photo_to_64(img)
    fen_ref = {0: chess.Piece(chess.BISHOP,False), 1: chess.Piece(chess.KING,False),
    2: chess.Piece(chess.KNIGHT,False), 3: chess.Piece(chess.PAWN,False),
    4: chess.Piece(chess.QUEEN,False), 5: chess.Piece(chess.ROOK,False),
    6: '.', 7: chess.Piece(chess.BISHOP,True), 8: chess.Piece(chess.KING,True),
    9: chess.Piece(chess.KNIGHT,True), 10: chess.Piece(chess.PAWN,True),
    11: chess.Piece(chess.QUEEN,True), 12: chess.Piece(chess.ROOK,True)}

    pred = []
    model = load_model('./data/models/model_VGG16.h5')
    for i in range (64):
        images[i] = np.expand_dims(images[i], axis=0)
        out = model.predict(images[i])
        top_pred = np.argmax(out)
        pred.append(fen_ref[top_pred])

    board = chess.Board('8/8/8/8/8/8/8/8')
    for i in range(64):
        if pred[i] != '.':
            board.set_piece_at(i,pred[i])

    return board.fen()
