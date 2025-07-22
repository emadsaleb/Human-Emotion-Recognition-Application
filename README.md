

 Human Emotion Recognition App

This project is a Streamlit-based web app that detects and analyzes human emotions from *images or videos using DeepFace, a powerful face analysis framework built on top of deep learning models.



 Features

 Detect emotions in images and videos
 Upload `.jpg`, `.jpeg`, or `.png` images
 Upload `.mp4`, `.avi`, or `.mov` videos
 Emotion detection powered by DeepFace with models like VGG-Face, Facenet, OpenFace, etc.
   Display of real-time analysis results directly in the browser








 Project Structure


├── human_emotion_recognition.py   # Main app script
├── requirements.txt               # Required dependencies
├── README.md                      # This file




How It Works

Image Mode:

  * Upload an image.
  * The app analyzes it using DeepFace and returns the detected emotion.
* *Video Mode:

  * Upload a video.
  * The app processes every 20th frame, detects faces, and overlays the emotion label in real-time.



 Supported Emotions

DeepFace can detect the following emotions:

* Happy 😊
* Sad 😢
* Angry 😠
* Surprised 😲
* Fearful 😱
* Disgusted 🤢
* Neutral 😐


 






