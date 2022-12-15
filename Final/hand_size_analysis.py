"""
TODO
"""

def Get_Hand_Width(width_landmarks):
    """
    TODO
    
    Args:
        width_landmarks: TODO
    
    Returns:
    TODO
    """
    hand_width = abs(width_landmarks[0] - width_landmarks[1])
    return hand_width

def Get_Hand_Length(length_landmarks):
    """
    TODO
    
    Args:
        length_landmarks: TODO
    
    Returns:
    TODO
    """
    hand_length = abs(length_landmarks[0] - length_landmarks[1])
    return hand_length