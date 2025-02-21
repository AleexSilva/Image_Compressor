import streamlit as st
from PIL import Image
import io

# Set the Streamlit page title
st.title("Image Compressor (1MB)")

# Upload an image file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "peg", "png"])

if uploaded_file:
    # Open the image using PIL
    image = Image.open(uploaded_file)
    
    # Display the original image
    st.image(image, caption="Original Image", use_column_width=True)

    # Function to compress image
    def compress_image(image, quality=85):
        """Compress image to be under 1MB while keeping quality."""
        img_format = image.format if image.format else "JPEG"
        output = io.BytesIO()
        
        # Reduce quality in a loop until size < 1MB
        for q in range(85, 10, -5):
            output.seek(0)
            image.save(output, format=img_format, quality=q, optimize=True)
            size_kb = output.tell() / 1024  # Convert to KB
            
            if size_kb < 1000:  # Less than 1MB
                return output, q, size_kb
        
        return output, q, size_kb  # Return best attempt

    # Compress the image
    compressed_output, quality_used, final_size = compress_image(image)

    # Show compression details
    st.write(f"✅ **Compressed Image Size:** {final_size:.2f} KB (Quality: {quality_used})")

    # Convert BytesIO to download link
    st.download_button(
        label="Download Compressed Image",
        data=compressed_output.getvalue(),
        file_name="compressed_image.jpg",
        mime="image/jpeg"
    )

    # Show compressed image preview
    compressed_image = Image.open(compressed_output)
    st.image(compressed_image, caption="Compressed Image", use_column_width=True)
