# Import necessary libraries
from pyzbar.pyzbar import decode
import cv2
import numpy as np

# Read the image containing the barcode
image = cv2.imread("image01.png")  # Load the image into a variable

# Decode the barcode(s) present in the image
barcodes = decode(image)  # Decode the barcodes from the image

# Loop through each barcode detected in the image
for barcode in barcodes:
    # Extract the data from the barcode and decode it to UTF-8
    data = barcode.data.decode("utf-8")  
    print(f"Barcode Data: {data}")  # Print the decoded data to the console

    # Draw a rectangle around the barcode
    points = barcode.polygon  # Get the points of the barcode's bounding box
    points = [(point.x, point.y) for point in points]  # Convert the points to tuples (x, y)
    cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)  # Draw a green polygon around the barcode

    # Annotate the decoded barcode data beside the bounding box
    x, y = points[0]  # Take the first point of the bounding box as a reference for text positioning
    cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  # Add green text with the decoded barcode data above the bounding box

# Display the image with the barcode highlighted and annotated
cv2.imshow("Barcode with Annotation", image)  # Show the image in a window

# Wait for a key press to proceed
key = cv2.waitKey(0)  # Wait indefinitely for a key press

# Save the annotated image once a key is pressed
output_file = "decoded_barcode.png"  # Define the file name for the saved image
cv2.imwrite(output_file, image)  # Save the annotated image to the file
print(f"Annotated image saved as {output_file}")  # Print confirmation message

# Close all OpenCV windows
cv2.destroyAllWindows()  # Close any OpenCV windows that were opened
