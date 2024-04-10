

import os

import cv2
import numpy as np

weights_path = os.path.abspath("assets/yolov3.weights")
config_path = os.path.abspath("assets/yolov3.cfg")
coco_names_path = os.path.abspath("assets/coco.names")
def detect_vehicles_yolo(image_path: str, conf_threshold: float = 0.5, nms_threshold: float = 0.4) -> tuple[dict[str, int], np.ndarray]:
    print("Loading YOLO...")

    # Load YOLO
    net = cv2.dnn.readNet(weights_path, config_path)

    print("Loading YOLO...")

    # Read class names
    
    with open(coco_names_path, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Load image
    print(f"Loading image: {image_path}"  f"\nImage shape: {image.shape}")
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers) # type: ignore

    # Initialize variables
    class_ids = []
    confidences = []
    boxes = []

    # Process detections
    for out in outs: 
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold:
                # Object detected
                print(f"Detected {classes[class_id]} with confidence: {confidence}") 

                # Center coordinates
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-max suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    # Count vehicles
    vehicle_count = {
        'car': 0,
        'motorcycle': 0,
        'bus': 0,
        'truck': 0
    }
    
    for i in indices:
        print(f"Detected )")
        i = i[0]
        class_id = class_ids[i]
        label = classes[class_id]
        if label in vehicle_count.keys():
            vehicle_count[label] += 1

    # Draw bounding boxes
    for i in indices:
        i = i[0]
        box = boxes[i]
        x, y, w, h = box
        if classes[class_ids[i]] in vehicle_count.keys():
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) # type: ignore

    return vehicle_count, image

# Example usage
image_path = os.path.abspath("assets/image.jpg")
vehicle_counts, image_with_boxes = detect_vehicles_yolo(image_path) # type: ignore

print(  f"Vehicle counts: {vehicle_counts}"  f"\nImage saved: {os.path.abspath('image_with_boxes.jpg')}")

# Display the image with bounding boxes
cv2.imshow("Image with Bounding Boxes", image_with_boxes) # type: ignore
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.destroyAllWindows()
