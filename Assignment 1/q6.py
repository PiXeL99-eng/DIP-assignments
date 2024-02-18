import cv2

def rotate_image(image_path, rotation_angle):
    
    # Read the image and return a numpy array loaded with the image
    img = cv2.imread(image_path)
    cv2.imshow('Original Image', img)    # window_name, image
    cv2.waitKey(0)

    height, width = img.shape[:2]

    # Calculate the rotation matrix and rotate image
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), rotation_angle, 1)   # (center, angle, scale) returns rotated matrix
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))     # (input_image, transformation_matrix, size_of_output_img)

    cv2.imshow('Rotated Image', rotated_img)    # window_name, image
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

def check_intensity_class(image_path):
    
    # Read the image and return a numpy array loaded with the image
    img = cv2.imread(image_path)
    print("Intensity class:", type(img[0][0][0]))

def convert_to_double(image_path):
    
    # Read the image and return a numpy array loaded with the image
    img = cv2.imread(image_path)
    cv2.imshow('Original Image', img)    # window_name, image
    cv2.waitKey(0)

    img_double = img.astype('float64') / 255.0
    cv2.imshow('Converted image', img_double)    # window_name, image
    cv2.waitKey(0)

    print("Intensity class:", type(img_double[0][0][0]))

    # Close all windows
    cv2.destroyAllWindows()

def convert_to_binary(image_path):

    # Read the image and return a numpy array loaded with the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Original Image', img)    # window_name, image
    cv2.waitKey(0)

    threshold_val, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)     # (img, threshold_val, max_val_to_pixel, how_threshold_is_applied)
    cv2.imshow('Binary Image', binary_img)    # window_name, image
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

# Image path
image_path = r'C:\Users\sayan\Desktop\ETCE Eight Sem - Shortcut\DIP\DIP-assignments\Assignment 1\waterlilies.jpg'
rotation_angle = 45

# Call the function
rotate_image(image_path, rotation_angle)
check_intensity_class(image_path)
convert_to_double(image_path)
convert_to_binary(image_path)
