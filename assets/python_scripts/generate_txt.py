import cv2
import os

txt = open("label.txt", 'w')
for index in range(1870 * 0 + 1, 1870 * 1 + 1):
    file_name = str(index).zfill(6) + '.png'
    img = cv2.imread('camera2/period14_camera2_annotated/' + file_name)
    ball_loc = {}
    #get location
    rows = img.shape[0]
    cols = img.shape[1]
    ball_locs_one_frame = []
    for row in range(rows):
        for col in range(cols):
            if img.item(row, col, 0) == 0 and img.item(row, col, 1) == 0 and img.item(row, col, 2) == 255:
                ball_locs_one_frame.append((col, row))

    if len(ball_locs_one_frame) > 2:
        print(file_name)
        print("Error! There are more than 2 red pixels on one frame")
        exit(-1)
    elif len(ball_locs_one_frame) == 2:
        if abs(ball_locs_one_frame[0][0] - ball_locs_one_frame[1][0]) > 1 or abs(
                        ball_locs_one_frame[0][1] - ball_locs_one_frame[1][1]) > 1:
            print(file_name)
            print("Error! 2 red pixels on one frame. They are conjunct with each other.")
        else:
            ball_loc["x"] = ball_locs_one_frame[0][0]
            ball_loc["y"] = ball_locs_one_frame[0][1]
    elif len(ball_locs_one_frame) == 1:
        ball_loc["x"] = ball_locs_one_frame[0][0]
        ball_loc["y"] = ball_locs_one_frame[0][1]
    else:
        ball_loc["x"] = -1
        ball_loc["y"] = -1
        
    #get coordinates of box
    if ball_loc["x"] != -1 and ball_loc["y"] != -1:
        left_up_x = (ball_loc["x"] - 9) if (ball_loc["x"] - 9) > 1 else 1
        left_up_y = (ball_loc["y"] - 9) if (ball_loc["y"] - 9) > 1 else 1
        right_up_x = (ball_loc["x"] + 11) if (ball_loc["x"] + 11) < 801 else 801
        right_up_y = (ball_loc["y"] + 11) if (ball_loc["y"] + 11) < 601 else 601
    write_str = file_name + ' ' + 'basketball' + ' ' + str(left_up_x) + ' ' + str(left_up_y) + ' ' + str(right_up_x) + ' ' + str(right_up_y) + '\n'
    print('writing ')
    print(file_name)
    txt.write(write_str)    
txt.close()        