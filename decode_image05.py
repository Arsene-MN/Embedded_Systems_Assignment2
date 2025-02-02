# Import necessary libraries
import cv2  
from pyzbar.pyzbar import decode 

# Read the image containing the barcode(s)
image = cv2.imread("image05.png")  # Load the image from file

# Check if the image was loaded correctly
if image is None:
    print("Error: Image not loaded correctly.")  # Print an error message if the image isn't loaded
    exit()  # Exit the program if the image is not loaded

# Convert the image to grayscale for easier processing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

# Detect and decode barcodes, including Aztec codes
decoded_objects = decode(gray)  # Use pyzbar's decode function to detect and decode barcodes

# If any barcodes are detected, process them
if decoded_objects:
    for obj in decoded_objects:
        # Print the decoded data for the detected Aztec code
        print(f"Detected Aztec Code: {obj.data.decode('utf-8')}")  # Decode and print the barcode's data
        
        # Draw a rectangle around the detected Aztec code
        points = obj.polygon  # Get the polygon points of the detected code
        if len(points) == 4:  # Check if the barcode has 4 points (a quadrilateral)
            # Extract the points' coordinates and convert them to integers
            pts = [(point.x, point.y) for point in points]  
            pts = [tuple(map(int, pt)) for pt in pts]  # Convert points to integer tuples
            # Draw a green polygon around the barcode
            cv2.polylines(image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)  # Draw the bounding box around the Aztec code
else:
    print("No Aztec code detected.")  # Print a message if no Aztec code is detected

# Display the image with the detected Aztec code highlighted
cv2.imshow("Aztec Code", image)  # Show the image in a window
cv2.waitKey(0)  # Wait indefinitely for a key press
cv2.destroyAllWindows()  # Close any OpenCV windows that were opened
