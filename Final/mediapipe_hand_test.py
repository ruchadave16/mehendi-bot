"""
TODO
"""
import cv2
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mediapipe as mp

# For static images:
def Get_Landmark_Coordinates(IMAGE_FILES):
  """
  TODO

  Args:
    image_files: TODO
  
  Returns:
  TODO
  """
  mp_drawing = mp.solutions.drawing_utils
  mp_drawing_styles = mp.solutions.drawing_styles
  mp_hands = mp.solutions.hands

  with mp_hands.Hands(
      static_image_mode=True,
      max_num_hands=2,
      min_detection_confidence=0.5) as hands:
    for idx, file in enumerate(IMAGE_FILES):
      # Read an image, flip it around y-axis for correct handedness output (see
      # above).
      image = cv2.flip(cv2.imread(file), 1)
      # Convert the BGR image to RGB before processing.
      results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

      # Draw hand landmarks on the image.
      if not results.multi_hand_landmarks:
        continue
      image_height, image_width, _ = image.shape
      annotated_image = image.copy()
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            annotated_image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
      cv2.imwrite(
          f'{os.getcwd()}/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))

      width_landmarks = [
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width, 
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x * image_width]
      length_landmarks = [
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height, 
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image_height]
  return width_landmarks, length_landmarks