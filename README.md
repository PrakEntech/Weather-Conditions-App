# Weather Conditions App

This is a simple weather application built using KivyMD that fetches and displays the current weather conditions for a specified area. The app uses web scraping techniques with BeautifulSoup and requests to retrieve weather information directly from Google Search.

## Features

- **User Input**: Enter the name of an area to get the current weather conditions.
- **Real-Time Data**: Fetches weather data, including temperature and other details, in real-time from Google Search.
- **Responsive UI**: The app has a simple and clean user interface designed with KivyMD, which is easy to navigate.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PrakEntech/Weather-Conditions-App.git
   cd Weather-Conditions-App
   ```

2. **Install the Required Dependencies**:
   Ensure you have Python installed, then install:
   ```bash
   pip install kivymd kivy beautifulsoup4 requests
   ```

3. **Run the App**:
   ```bash
   python main.py
   ```

## Usage

- Enter the area name in the text field and click the "CHECK" button.
- The app will display the current temperature and weather conditions of the specified area.

## Code Overview

- **KivyMD for UI**: The app uses KivyMD for a material design interface.
- **BeautifulSoup & Requests**: These libraries are used to scrape weather information from Google Search.

## Future Enhancements

- Add error handling for invalid area names or network issues.
- Improve the user interface with more customization options.
- Add support for more detailed weather information such as humidity, wind speed, etc.
