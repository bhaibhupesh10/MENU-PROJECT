#!/usr/bin/env python3

import cgitb
cgitb.enable()

import sys
import os
from flask import Flask, render_template, request, send_file
import cv2
from PIL import Image
import numpy as np
import logging

# Set up logging
logging.basicConfig(filename='/var/www/cgi-bin/app.log', level=logging.DEBUG)

app = Flask(__name__, template_folder='/var/www/html/menu/templates')  # Update the path to your templates folder

# Step 1: Capture a Photo Using OpenCV
def capture_image():
    try:
        cap = cv2.VideoCapture(0)  # Open the webcam
        if not cap.isOpened():
            logging.error("Error: Could not open webcam.")
            return False, None
        ret, frame = cap.read()    # Capture a single frame
        cap.release()              # Release the webcam
        if ret:
            cv2.imwrite('/tmp/captured_image.jpg', frame)  # Save the captured image
        return ret, frame
    except Exception as e:
        logging.error(f"Error in capture_image: {e}")
        return False, None

# Step 2: Crop a Part of the Image Using Pillow
def crop_image(image_path, left, top, right, bottom):
    try:
        image = Image.open(image_path)  # Open the image file
        cropped_image = image.crop((left, top, right, bottom))  # Crop the image
        cropped_image.save('/tmp/cropped_image.png')  # Save the cropped image
        return cropped_image
    except Exception as e:
        logging.error(f"Error in crop_image: {e}")
        return None

# Step 3: Overlay the Cropped Image on the Original Using OpenCV
def overlay_images(original_img_path, cropped_img_path, x_offset, y_offset):
    try:
        original_img = cv2.imread(original_img_path)  # Load the original image
        cropped_img = Image.open(cropped_img_path).convert("RGBA")  # Load the cropped image with alpha channel
        original_img_pil = Image.fromarray(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)).convert("RGBA")

        # Overlay the cropped image on the original image
        original_img_pil.paste(cropped_img, (x_offset, y_offset), cropped_img)
        combined = cv2.cvtColor(np.array(original_img_pil), cv2.COLOR_RGBA2BGRA)

        # Save and return the combined image
        cv2.imwrite('/tmp/overlayed_image.png', combined)
        return '/tmp/overlayed_image.png'
    except Exception as e:
        logging.error(f"Error in overlay_images: {e}")
        return None

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        logging.error(f"Error in index route: {e}")
        return "Error loading index page."

@app.route('/process', methods=['POST'])
def process():
    # Capture image
    ret, frame = capture_image()
    if not ret or frame is None:
        return "Failed to capture image"

    # Define crop coordinates (example: central 200x200 area)
    height, width, _ = frame.shape
    left = width // 4
    top = height // 4
    right = left + 200
    bottom = top + 200

    # Crop the image
    cropped_image = crop_image('/tmp/captured_image.jpg', left, top, right, bottom)
    if cropped_image is None:
        return "Failed to crop image"

    # Define the position to overlay the cropped image
    x_offset = 50
    y_offset = 50

    # Overlay the cropped image on the original image
    result_image_path = overlay_images('/tmp/captured_image.jpg', '/tmp/cropped_image.png', x_offset, y_offset)
    if result_image_path is None:
        return "Failed to overlay images"

    # Send the result image as a response
    try:
        return send_file(result_image_path, mimetype='image/png')
    except Exception as e:
        logging.error(f"Error in sending file: {e}")
        return "Failed to send image file"

if __name__ == '__main__':
    if 'GATEWAY_INTERFACE' in os.environ:
        CGIHandler().run(app)
    else:
        app.run()

