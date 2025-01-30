🎮 Interactive Sudoku Solver with AI-Powered Image Recognition
Unleash the power of automation to solve Sudoku puzzles instantly! This GUI application uses deep learning to extract, solve, and visualize Sudoku puzzles from images.

✨ Key Features
🖼️ Image-to-Sudoku Conversion: Upload any Sudoku image and let the system digitize it.

🧠 Custom Trained Digit Recognition Model: State-of-the-art CNN model for accurate digit extraction.

⚡ Lightning-Fast Solver: Backtracking algorithm optimized for speed and efficiency.

📤 Downloadable Results: Export the solved Sudoku as an image or view it directly in the app.

🖥️ User-Friendly GUI: Built with Kivy.KivyMD for seamless interaction.

🚀 How It Works
Upload: Submit your unsolved Sudoku image (supports JPG/PNG).

Preprocessing: Advanced image processing (thresholding, grid detection) to isolate cells.

Digit Extraction: Custom CNN model predicts digits from preprocessed cells.

Solving: Algorithmic magic solves the puzzle in milliseconds.

Visualize & Download: See the solution instantly or save it for later!

🛠️ Tech Stack
Deep Learning: TensorFlow/Keras for training the digit recognition model.

GUI: Kivy, KivyMD for an intuitive interface.

Backend: Python for logic and NumPy for matrix operations.


📸 Demo

Input: ![sudoku_100](https://github.com/user-attachments/assets/b0c10b63-5f5b-42ad-98fa-a5113a9c0828)


Output: ![Generated_Sudoku___________](https://github.com/user-attachments/assets/ff608ecb-6f19-4091-9ca1-d169462fb208)


