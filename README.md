# Hand Gesture to Text App

This Python app recognizes hand gestures in real-time using your webcam and displays corresponding text on the screen. It uses the **Mediapipe Hands** model to detect hand landmarks and maps specific gestures to predefined text.

---

## Requirements
- Python 3.7 or later
- OpenCV (`opencv-python`)
- Mediapipe (`mediapipe`)
- Numpy (`numpy`)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/NamanXbnPro/Gesture-to-text-using-python-Flask-.git
2. Install dependencies
   `pip install -r requirement.txt`
   {Altertnatively, if it's desired to be installed manually line by line}
   `pip install opencv-python mediapipe numpy`

## Usage 
1. Run the app

   Navigate to source folder
   `python gesture_to_text.py`
   `python3 gesture_to_text.py` {Alternatively}
2. Perform Gestures:

    The app will open your webcam and display the video feed.

    Perform the following gestures in front of the camera:

        Thumbs Up: Thumb extended, other fingers closed.

        Peace Sign: Index and middle fingers extended, others closed.

        Fist: All fingers closed.

        Open Hand: All fingers extended.

        OK Sign: Thumb and index finger tips close, forming a circle.

        Swag Sign: Thumb and pinky finger extended, others closed.

        Heart Sign: Index and middle fingers bent to form a heart shape.

3.View the Output:

    The recognized gesture text will be displayed at the top of the screen.

    For example:

        If you show a thumbs up, the text "Thumbs Up: Good Job!" will appear.

        If you show a heart sign, the text "Heart Sign: Love!" will appear.

4.Quit the App:

    Press the q key to close the app.


# Adding new Gestures 
  o add new gestures:

    Open the gesture_to_text.py file.

    Add a new condition in the recognize_gesture function to detect the gesture using hand landmarks.

    Map the gesture to a new text or action.

For example, to add a "Rock On" gesture:
 `# Rock On: Index and pinky fingers extended, others closed
if (index_tip.y < index_pip.y and
    pinky_tip.y < pinky_pip.y and
    middle_tip.y > middle_pip.y and
    ring_tip.y > ring_pip.y):
    return "Rock On: Rock and Roll!"` 



# Help for Creation and activation of virtual enviroment
  
### Refer to these links and look for your device os: 
  [https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/](url)
                                                    
  [https://docs.python.org/3/library/venv.html](url)
