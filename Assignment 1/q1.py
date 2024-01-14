import cv2

def crop_and_display_image(image_path, cropped_dimensions):

    # Read the image and return a numpy array loaded with the image
    img = cv2.imread(image_path)

    # Crop the image according to the specified rectangle [x, y, width, height]
    x, y, w, h = cropped_dimensions

    cropped_img = img[y:y+h, x:x+w]

    # Display the cropped image
    cv2.imshow('Cropped Image', cropped_img)    # window_name, image

    # Wait for the user to press a key
    cv2.waitKey(0)

    # Close all windows
    # You can call destroyWindow() or destroyAllWindows() to close the window and de-allocate any associated memory usage. 
    # For a simple program, you do not really have to call these functions because all the resources and windows of the application 
    # are closed automatically by the operating system upon exit.
    
    cv2.destroyAllWindows()

# Image path and crop rectangle
image_path = r'C:\Users\sayan\Desktop\ETCE Eight Sem - Shortcut\DIP\DIP-assignments\Assignment 1\winter.jpg'
cropped_dimensions = [100, 100, 200, 200]  # [x, y, width, height]

# Call the function
crop_and_display_image(image_path, cropped_dimensions)
