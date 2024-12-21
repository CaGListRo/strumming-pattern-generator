# Strumming Pattern Generator

This project is a simple Python application that generates random strumming patterns using the `pygame` library. The application displays arrows (up and down) to represent the strumming directions, with customizable visual elements like a background image and arrow graphics.

## Features

- **Random Strumming Patterns**: Randomly generates upward and downward strumming arrows.
- **Interactive GUI**: Displays the strumming pattern on a graphical interface with lines separating each arrow.
- **Customizable Assets**: Allows loading custom background and arrow images.
- **Frame Control**: Runs at a fixed frame rate of 30 FPS for smooth visuals.

## Requirements

- Python 3.9 or higher
- `pygame` library

Install `pygame` using pip:

```bash
pip install pygame
```

## How to Run

1. Clone the repository or copy the script.
2. Ensure the required image assets are in the same directory as the script:
   - `arrow.png`: Arrow image used for both upward and downward arrows.
   - `background.png`: Background image for the application.
3. Run the script:

```bash
python script_name.py
```

## Files

- **`arrow.png`**: A PNG image representing an arrow pointing downwards. The script rotates it 180° to create upward arrows.
- **`background.png`**: A PNG image used as the background for the application.

## How It Works

1. **Initialization**:

   - Initializes the `pygame` library.
   - Sets up the display window with a resolution of `480x223`.

2. **Event Handling**:

   - Handles user input and events (e.g., closing the application).

3. **Arrow Generation**:

   - Randomly decides whether to draw upward or downward arrows in predefined positions.

4. **Drawing**:

   - Displays the background, arrows, and lines dividing each section.

5. **Main Loop**:
   - Continuously updates the screen at 30 FPS until the application is closed.

## Customization

- **Arrow and Background Images**: Replace `arrow.png` and `background.png` with your own images to customize the visuals.
- **Frame Rate**: Modify the `FPS` constant to adjust the frame rate.
- **Display Resolution**: Change the dimensions in `pg.display.set_mode()` for a different screen size.

## License

This project is open-source and can be used or modified as needed.

## Acknowledgments

- Built with the `pygame` library.
- Inspired by guitar strumming patterns.

---

Enjoy creating and exploring random strumming patterns!
