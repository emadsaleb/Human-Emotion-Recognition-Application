
import streamlit as st
import cv2
from deepface import DeepFace
from PIL import Image
import numpy as np

st.title('Human Emotion Recognition')

options = st.selectbox('Choose an Option:', ('Image', 'Video'))

def Analyze_Emotion(image_or_video):
    try:
        analysis = DeepFace.analyze(image_or_video, actions = ['emotion'], enforce_detection= True)
        return analysis[0]['emotion']
    except ValueError as e:
       # st.write(f'Error: ', e)
        return None

if options == 'Image':
    upload = st.file_uploader('Please, Upload an Image...', type = ['png', 'jpg', 'jpeg'])

    if upload is not None:
        img = Image.open(upload)
        img_array = np.array(img)
        st.image(img_array, use_container_width= True, channels= 'RGB')

        #detect emotion
        emotion_scores = Analyze_Emotion(img_array)
        #st.write(emotion_scores)

        if emotion_scores:
            
            detected_emotion = max(emotion_scores, key = emotion_scores.get)
            st.write(f'Detected Emotion: ', {detected_emotion})
        else:
            st.write('No Face Detected')

import tempfile

if options == 'Video':
    upload = st.file_uploader('Upload Your Video...', type = ['mp4', 'mov', 'avi'])

    if upload is not None:
        with tempfile.NamedTemporaryFile(delete= False) as temp_video:
            temp_video.write(upload.read())
            video_name = temp_video.name
        video = cv2.VideoCapture(video_name) # 0 ----> open camera

        frame_rate = 20 #control how many frames
        frame_count = 0

        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break
            frame_count += 1

            #process and diaplay frames
            if frame_count % frame_rate == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                emotion_scores = Analyze_Emotion(frame_rgb)

                if emotion_scores:
                    detected_emotion = max(emotion_scores, key = emotion_scores.get)
                    cv2.putText(frame, detected_emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 3, (100,90,255), 2)
                else:
                    detected_emotion = 'No Face Detected'
                    cv2.putText(frame, detected_emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 3, (100,90,255), 2)
                st.image(frame, channels = 'BGR')
        video.release()
