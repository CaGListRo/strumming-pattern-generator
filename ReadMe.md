# Strumming Pattern Generator with Metronome

This project is an enhanced Python application that combines a **strumming pattern generator** with a **metronome**. It provides options for generating visual and audio representations of musical patterns, including adjustable metronome sounds for beats and strumming.

## Features

### 1. Metronome Mode

- Plays a metronome sound for 4/4 time signatures.
- The first beat has a distinct tone compared to other beats.

### 2. Strumming Pattern Mode

- Generates random strumming patterns.
- Plays different sounds for downstrokes and upstrokes.

### 3. Interactive GUI

- Adjustable BPM (Beats Per Minute) through buttons.
- Checkboxes to toggle features like sound, metronome mode, or strumming mode.
- Visual indicators for beats and strumming slots.

### 4. Customizable Assets

- Includes options to replace images (background, arrows, checkboxes) and sounds.

## Requirements

- Python 3.9 or higher
- `pygame` library

Install `pygame` using pip:

```bash
pip install pygame
```

## How to Run

1. Clone the repository or copy the scripts.
2. Ensure the required assets are in the same directory as the scripts:
   - **Images**: `icon.png`, `arrow.png`, `background.png`, `check_box_0.png`, `check_box_1.png`
   - **Sounds**: `metronom click 1.wav`, `metronom click 2.wav`
3. Run the script `strumming.py`:

```bash
python strumming.py
```

## Files Overview

### Scripts

- **`button.py`**: Defines a `Button` class for GUI buttons.
- **`check_box.py`**: Defines a `CheckBox` class for toggling settings.
- **`strumming.py`**: Main application script that integrates the metronome and strumming pattern generator.

### Assets

- **Images**:
  - `icon.png`: Application icon.
  - `arrow.png`: Arrow images for up and down strumming patterns.
  - `background.png`: Background image for the GUI.
  - `check_box_0.png` & `check_box_1.png`: Checkbox states.
- **Sounds**:
  - `metronom click 1.wav`: Sound for the first beat or downstroke.
  - `metronom click 2.wav`: Sound for other beats or upstrokes.

## How It Works

### Initialization

- Sets up the `pygame` environment, window, and assets.
- Configures buttons, checkboxes, and slot indicators.

### Metronome Mode

- Plays distinct sounds for the first beat and the remaining beats in a 4/4 measure.
- Visual slot indicators highlight the current beat.

### Strumming Pattern Mode

- Randomly generates up and down arrows for strumming.
- Plays different sounds for upstrokes and downstrokes.

### Controls

- **Buttons**:
  - Adjust BPM with `+1`, `+10`, `-1`, and `-10` buttons.
  - Start/Stop playback with `|>` and `[]` buttons.
  - Regenerate strumming patterns with the `(Re)Generate` button.
- **Checkboxes**:
  - Toggle sound with the `Sound` checkbox.
  - Switch between `4/4` metronome and `Strum` mode using respective checkboxes.

## Customization

- **Images**: Replace the provided image files with your own for a personalized appearance.
- **Sounds**: Substitute the `.wav` files to customize the metronome and strumming sounds.
- **BPM Limits**: Adjust the maximum and minimum BPM in the `check_elements` method in `strumming.py`.

## License

This project is open-source and can be freely used or modified.

## Acknowledgments

- Built using the `pygame` library.
- Inspired by guitar strumming patterns and rhythmic practice tools.

---

Enjoy experimenting with custom strumming patterns and metronome settings!
