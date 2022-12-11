

def Get_Hand_Width(width_landmarks):
    hand_width = abs(width_landmarks[0] - width_landmarks[1])
    return hand_width

def Get_Hand_Length(length_landmarks):
    hand_length = abs(length_landmarks[0] - length_landmarks[1])
    return hand_length