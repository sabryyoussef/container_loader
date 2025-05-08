# 20-foot Container Loader

## Overview

This is a Streamlit application designed to simulate the loading process of a standard 20-foot container. The app allows users to input goods' dimensions and weight, then determines if the goods can fit within the container's remaining volume and payload capacity.

## Features

- Calculate whether goods can fit within the available container space.
- Track remaining container volume and payload capacity after each load.
- User-friendly interface built with Streamlit.
- Displays error messages when loading exceeds the container's capabilities.

## Technical Details

### Container Class

This class models a 20-foot container with the following attributes:
- **Length:** 20 feet
- **Width:** 8 feet
- **Height:** 8.5 feet
- **Volume:** 1,170 cubic feet (approx.)
- **Payload Capacity:** 61,700 lbs

### Methods

- **`load_goods(length, width, height, weight)`**: Checks if the goods can fit in the container and updates the remaining capacity.

### Streamlit App

- **Title:** "20-foot Container Loader"
- **Features:**
  - Input fields for goods' dimensions (length, width, height) and weight.
  - Form submission to attempt loading goods.
  - Displays the container's remaining volume and payload capacity.

## Setup and Installation

### Requirements

- Python 3.7 or above
- Streamlit library

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/container-loader.git
   cd container-loader
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the app in your web browser (Streamlit will provide a local URL).
2. Enter the goods' dimensions (length, width, height) and weight in the form.
3. Click "Load Goods" to check if the goods can be loaded into the container.
4. View the container's remaining capacity and error messages (if any).

## Example

- **Input:**
  - Length: 4 ft
  - Width: 4 ft
  - Height: 4 ft
  - Weight: 500 lbs

- **Output:**
  - Successful load message with updated remaining volume and payload.

## Author Information

- **Author:** Sabry Youssef
- **Contact:** 01000059085

## License

This project is licensed under the MIT License.
