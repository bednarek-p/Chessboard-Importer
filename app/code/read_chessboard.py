from image_final_crop import return_cropped_image
from prediction import return_fen
from fen_improved import FenImproved


class ReadChessboard:
    @staticmethod
    def read_chessboard(pil_image):
        try:
            cropped_photo = return_cropped_image(pil_image)
            fen = return_fen(cropped_photo)
            print(fen)
            fen_improved = FenImproved(fen)
            fen_improved.fen_improve_king()
            fen_improved.fen_improve_queen()
            fen_improved.fen_improve_knight()
            fen_improved.fen_improve_bishop()
            fen_improved.fen_improve_rook()
            new_fen = fen_improved.get_improved_fen()
            return new_fen
        except:
            return False
