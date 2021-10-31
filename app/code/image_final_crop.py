import cv2

import image_intersections as inter
import image_corners as corners
import image_crop as crop
import image_lines as lines_lib

def return_cropped_image(img):
    color_img = img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(3):
        img, _tmp1, scale = crop.image_resize(img)
        ############## POINT 1 - FIND POSSIBLE LINES###############################
        ## GENERATING LINES
        all_lines = lines_lib.pSLID(img)
        raw_lines = lines_lib.generate_all_possible_lines(img, all_lines)
        lines = lines_lib.slid_tendency(raw_lines) #addition similar lines
        ###########################################################################

        ############ POINT 2 - FIND POINTS - INTERSECTIONS#########################
        points = inter.INTERSECTIONS(img,lines) ## GENERATING intersection points
        ###########################################################################

        ############ POINT 3 - FIND CHESSBOARD CORNERS#############################
        # GENERATING inner points
        inner_points = corners.find_inner_corners(img,points,lines)
        # calculating outer points
        four_points = corners.find_outer_corners(inner_points,img)
        print(four_points)
        ###########################################################################

        ########### POINT 4 - CROPPING IMAGE#######################################
        img = crop.crop(four_points,img) #crop small image
        pts = crop.image_scale(four_points,scale)#rescale points to orig image
        color_img = crop.crop(pts,color_img) # crop orig image
        ###########################################################################
    return color_img
