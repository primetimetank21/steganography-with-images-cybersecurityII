#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:56:09 2020

@author: earltankardjr
"""

import matplotlib.pyplot as plt, matplotlib.image as mpimg, copy, numpy as np

# function that decodes the message from an image given the original image
def decodeImg(ogImg, newImg, index, length):
    byte_array = []                                 # list to store bytes
    for i in range(index, length + index):
        diff = newImg[0][i][0] - ogImg[0][i][0]     # difference between modified image and original image
        byte_array.append(int(diff))                # adds byte difference to list
    msg = "".join(map(chr, byte_array))             # converts the bytes back into characters
    return msg                                      # returns decoded message

# function that encodes the message and puts pieces in an image
def encodeImg(img, msg, index):
    encodedMsg = bytearray(msg, 'utf-8')            # converts message into list of bytes
    for byte in encodedMsg:
        img[0][index][0]+=byte                      # modifies pixels
        index+=1                                    # iterates to next pixel
    return (img, encodedMsg)                        # returns modified image and the encoded message

# function that displays the images
def plotImgs(img1, img2):
    f = plt.figure()                                # creates a figure to display both images (original and modified)
    f.add_subplot(1,2,1)                            # creates a place for original image
    plt.imshow((img1 * 255).astype(np.uint8))
    f.add_subplot(1,2,2)                            # creates a place for modified image
    plt.imshow((img2 * 255).astype(np.uint8))
    plt.show(block=True)                            # show images side-by-side (left: original, right: modified)


def main():
    imgPick =	np.random.randint(0,2)                                              # picks one of two images
    if imgPick == 0:
        img =   mpimg.imread('./ARROW.png')                                         # read in arrow image
    else:
        img =	mpimg.imread('./HAMburger.png')                                     # read in hamburger image
    img2    =   img.copy()                                                          # make a copy of image
    myStr   =   input('Enter message\t>> ')                                         # get message to encode
    idx     =   np.random.randint(0, high=len(img[0]) - len(myStr))                 # randomly selects which pixel to start placing message
    idxCopy =   copy.deepcopy(idx)                                                  # copy of index
    data    =   encodeImg(img2, myStr, idx)                                         # tuple containing: (image, encoded message)
    print('Encoded Text\t>> ', end='')                                              # prints encoded message
    for byte in data[1]:
        print(byte, end='')
    print('\nDecoded Text\t>> %s' % decodeImg(img, data[0], idxCopy, len(data[1]))) # prints decoded message
    plotImgs(img, img2)                                                             # plots images side by side

if __name__ == '__main__':
    main()
