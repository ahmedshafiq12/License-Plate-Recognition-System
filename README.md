### License Plate Recognition System

## Description
The License Plate Recognition (LPR) System is a computer vision project designed to detect and recognize license plates in images or video streams. The system utilizes a pipeline that processes each frame of a video. It begins by detecting vehicles using a pre-trained YOLO model, followed by detecting license plates within the detected vehicles using a custom-trained model. Subsequently, detected plates are assigned to their corresponding vehicles, and the contents of the plates are read using the PaddleOCR English pretrained model. Vehicle tracking is achieved using bytetrack, and the details of tracking are saved.

## Sample Output Video with Visualization
https://github.com/theonlyshafiq/License-Plate-Recognition-System/assets/63657698/3a287c0f-164b-44a1-a632-e92de745965f

## Features
- Detects license plates from video streams.
- Extracts alphanumeric characters from the detected license plates.
- Associates detected plates with their respective vehicles.
- Utilizes a custom-trained license plate detection model.
- Reads license plate contents using the PaddleOCR English pretrained model.
- Tracks vehicles using ByteTrack algorithm.

## Technologies Used
- Python
- OpenCV (Open Source Computer Vision Library)
- YOLO (You Only Look Once) object detection model
- PaddleOCR English pretrained model
- ByteTrack algorithm

## Training the License Plate Detection Model
To train the license plate detection model, a custom dataset was used. The training process and the dataset can be found in the following resources:
- [Training Notebook](https://www.kaggle.com/code/ahmedshafiq12/license-plate-detector-training)
- [Dataset](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/theonlyshafiq/License-Plate-Recognition-System.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   
## Usage
1. Run the main script with the following command:
   ```
   python main.py -i input_video.mp4 -d
   ```
   - `-i`: Specify the input video file path.
   - `-d`: (Optional) Display the output while the video is being processed.

2. Follow the instructions to provide the input video stream.

3. View the output with detected cars and recognized characters.

## Contributions
Contributions to the project are welcome. Please feel free to fork the repository, make changes, and submit a pull request.
