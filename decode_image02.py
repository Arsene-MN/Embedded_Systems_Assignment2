# Import necessary libraries
from pylibdmtx.pylibdmtx import decode  
import cv2  

# Read the image containing the DataMatrix code in grayscale mode
image = cv2.imread("datamatrix_code.jpg", cv2.IMREAD_GRAYSCALE)  # Load the image in grayscale for decoding

# Decode the DataMatrix code(s) present in the image
decoded_objects = decode(image)  # Decode the DataMatrix codes in the image

# Loop through each decoded object and print the decoded data
for obj in decoded_objects:
    data = obj.data.decode("utf-8")  # Decode the data of each DataMatrix object to UTF-8
    print("Decoded Data:", data)  # Print the decoded data to the console

# Save the image after decoding (no annotation in this case, just saving the grayscale image)
output_file = "decoded_datamatrix_code.png"  # Define the file name for the saved image
cv2.imwrite(output_file, image)  # Save the image with the DataMatrix code in it
print(f"Annotated image saved as {output_file}")  # Print confirmation message

# Display the image with the DataMatrix code
cv2.imshow("Barcode with Annotation", image)  # Show the image in a window

# Wait for a key press to proceed
cv2.waitKey(0)  # Wait indefinitely for a key press

# Close all OpenCV windows
cv2.destroyAllWindows()  # Close any OpenCV windows that were opened
