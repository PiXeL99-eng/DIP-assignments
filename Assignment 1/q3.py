import cv2

# [fp=y(end:-1:1,:)]

def flip_image(image_path):
    
    # Read the image and return a numpy array loaded with the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Original Gray Image', img)    # window_name, image
    cv2.waitKey(0)

    flipped_img = img[::-1, :]  # upside-down image
    cv2.imshow('Flipped Image', flipped_img)    # window_name, image
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

# Image path
image_path = r'C:\Users\sayan\Desktop\ETCE Eight Sem - Shortcut\DIP\DIP-assignments\Assignment 1\winter.jpg'

# Call the function
flip_image(image_path)
