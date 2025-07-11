
# Rock Paper Scissors Game with Mediapipe and OpenCV

This is a real-time Rock Paper Scissors game implemented using Python, OpenCV, and Mediapipe. The game allows players to compete against the computer by making hand gestures (Rock, Paper, Scissors) captured via a webcam. The system detects the player's gesture, generates a random move for the computer, and determines the winner based on classic Rock Paper Scissors rules.

## How It Works

### 1. **Technology Stack**
- **Python**: The primary programming language for the project.
- **OpenCV**: Used for capturing and processing video frames from the webcam.
- **Mediapipe**: Utilizes the Hands module to detect and track hand landmarks in real-time, enabling gesture recognition.
- **Random**: Generates random moves for the computer.

### 2. **Game Mechanics**
- The game captures video input from the webcam and processes each frame to detect hand gestures.
- Mediapipe's Hand Landmarker identifies 21 key landmarks on the hand, which are analyzed to classify the gesture as "Rock" (closed fist), "Paper" (open hand), or "Scissors" (index and middle fingers extended).
- The computer randomly selects its move from the three options.
- The result is displayed on the screen, and the score is updated accordingly:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
  - Same gestures result in a tie.

### 3. **Implementation Steps**
1. **Setup**:
   - Initialize the webcam using OpenCV (`cv2.VideoCapture`).
   - Configure Mediapipe's Hands model to detect hand landmarks with a minimum detection confidence.

2. **Hand Gesture Detection**:
   - Convert each frame from BGR (OpenCV format) to RGB for Mediapipe processing.
   - Use Mediapipe to detect hand landmarks and draw them on the frame for visualization.
   - Analyze landmark positions (e.g., finger tips vs. joints) to determine the gesture:
     - Rock: All fingers closed.
     - Paper: All fingers extended.
     - Scissors: Index and middle fingers extended, others closed.

3. **Game Logic**:
   - Compare the player's gesture with the computer's random move.
   - Display the result (Win, Lose, or Tie) and update the score on the screen using OpenCV's text rendering.

4. **User Interaction**:
   - Press 'q' to quit the game.
   - Move your hand in and out of the frame to start a new round.

### 4. **Requirements**
- Python 3.x
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- NumPy (`pip install numpy`)

### 5. **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/phamkiet000/Rock_Paper_Scissor.git
   cd Rock_Paper_Scissor
