# Import necessary libraries
import cv2  
import numpy as np 

# Load the image
image = cv2.imread("image04.png")  # Read the image from file

# Check if the image is loaded correctly
if image is None:
    print("Error: Image not loaded correctly.")  # Print error message if image is not loaded
    exit()  # Exit the program if image is not loaded

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale for easier processing

# Apply adaptive thresholding to improve contrast
gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)  # Apply adaptive thresholding to make the QR code more distinguishable

# Initialize QR code detector
detector = cv2.QRCodeDetector()  # Create a QRCodeDetector object for detecting and decoding QR codes

# Detect and decode the QR code
data, points, _ = detector.detectAndDecode(gray)  # Detect and decode the QR code in the image

# Print detected points of the QR code (if any)
print(f"Points detected: {points}")

# If QR code data is detected, display it and draw the bounding box around it
if data:
    print(f"QR Code Data: {data}")  # Print the decoded data
    if points is not None:
        points = points.astype(int)  # Convert points to integer values
        cv2.polylines(image, [points], True, (0, 255, 0), 2)  # Draw a green polygon around the QR code
else:
    print("No QR code detected.")  # Print message if no QR code is detected

# Display the result with bounding box (if QR code was detected)
cv2.imshow("QR Code", image)  # Show the image in a window
cv2.waitKey(0)  # Wait indefinitely for a key press
cv2.destroyAllWindows()  # Close any OpenCV windows that were opened
