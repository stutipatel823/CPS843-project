import cv2
def detect_qr_code(image_path):
    # Load the image from the file system
    loaded_image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)

    # Initialize QR code detector
    qr_code_detector = cv2.QRCodeDetector()
    
    qr_code_info, retrieval, points = qr_code_detector.detectAndDecode(grayscale_image)


    # Check if a QR code is detected
    if retrieval is not None:
        # Convert bounding box to int and reshape to a polygon
        print("QR code found!")

        points = retrieval.astype(int).reshape(-1, 2)

        # Determine the bounding rectangle of the QR code
        rect_x, rect_y, rect_width, rect_height = cv2.boundingRect(points)
        
        # Extract the QR code region of interest before drawing the border
        roi = loaded_image[rect_y:rect_y + rect_height, rect_x:rect_x + rect_width].copy()

        # Draw the bounding box on the image
        cv2.rectangle(loaded_image, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (0, 255, 0), 3)
        
        # Display the main image with the border
        cv2.imshow('Original with Border', loaded_image)
        
        # Print the coordinates and display the images
        print("Coordinates:\n", points)
        cv2.imshow('ROI', roi)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        # Notify if no QR code is found
        print("No QR code found in the image")

# Example usage
image_path = 'opencv/no.png'
detect_qr_code(image_path)
