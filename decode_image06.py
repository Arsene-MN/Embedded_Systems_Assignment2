# Import necessary libraries
from pyzbar.pyzbar import decode
import cv2  
import numpy as np 

# Read the image containing the barcode(s)
image = cv2.imread("image06.png")  # Load the image from file

# Decode the barcode(s) in the image
barcodes = decode(image)  # Use pyzbar's decode function to detect and decode barcodes

# Loop through each detected barcode and process it
for barcode in barcodes:
    # Decode the barcode data to a UTF-8 string
    data = barcode.data.decode("utf-8")  
    print(f"Barcode Data: {data}")  # Print the decoded barcode data

    # Get the polygon points that define the barcode's bounding box
    points = barcode.polygon
    points = [(point.x, point.y) for point in points]  # Convert points to (x, y) tuples

    # Draw a polygon (bounding box) around the barcode on the image
    cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)  # Draw a green polygon

    # Annotate the barcode with the decoded data beside the bounding box
    x, y = points[0]  # Use the first point in the bounding box as the position for the annotation
    cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  # Add green text above the bounding box

# Display the image with the barcode highlighted and annotated
cv2.imshow("Barcode with Annotation", image)  # Show the image in a window

# Wait for a key press to continue
key = cv2.waitKey(0)  # Wait for a key press

# Save the annotated image to a file when a key is pressed
output_file = "decoded_barcode.png"  # Define the output file name
cv2.imwrite(output_file, image)  # Save the annotated image to the file
print(f"Annotated image saved as {output_file}")  # Print a message confirming the save

# Close all OpenCV windows
cv2.destroyAllWindows()  # Close any OpenCV windows that were opened
