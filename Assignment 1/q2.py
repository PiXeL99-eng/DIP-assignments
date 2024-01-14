import cv2

def convert_to_grayscale(image_path):
    
    # Read the image and return a numpy array loaded with the image
    img = cv2.imread(image_path)
    cv2.imshow('Original Image', img)    # window_name, image
    cv2.waitKey(0)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', gray_img)    # window_name, image
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

# Image path
image_path = r'C:\Users\sayan\Desktop\ETCE Eight Sem - Shortcut\DIP\DIP-assignments\Assignment 1\waterlilies.jpg'

# Call the function
convert_to_grayscale(image_path)
