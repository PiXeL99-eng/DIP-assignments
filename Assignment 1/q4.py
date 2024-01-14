import cv2

def show_image(image_path):
    
    # Read the image and return a numpy array loaded with the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Original Image', img)    # window_name, image
    cv2.waitKey(0)

    subsampled_img = img[::2, ::2]  # taking every 2nd pixel row wise and column wise
    cv2.imshow('Subsampled Image', subsampled_img)    # window_name, image
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

# Image path
image_path = r'C:\Users\sayan\Desktop\ETCE Eight Sem - Shortcut\DIP\DIP-assignments\Assignment 1\waterlilies.jpg'

# Call the function
show_image(image_path)
