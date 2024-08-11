# Billboard Top 100 Playlist Creator:

This Python script allows you to create a Spotify playlist with the Billboard Top 100 hits from a specific date of your choice. Simply input the desired date, 
and the script will scrape the Billboard Hot 100 chart for that day and generate a playlist on your Spotify account.

[![Watch the video](https://via.placeholder.com/100x100)](https://github.com/user-attachments/assets/e0c20088-dce0-4cb4-9d24-de10c42a43b5)

**The playlist will appear in your Spotify account after it's finished running**:
<img width="910" alt="Screenshot 2024-08-11 at 11 43 45 AM" src="https://github.com/user-attachments/assets/d9125fed-040b-417b-b594-c29b98b3fb44">


## Features:

- **Billboard Scraper**: Retrieves the top 100 songs from Billboard's Hot 100 chart for the specified date.
- **Spotify Integration**: Automatically creates a playlist with the retrieved songs on your Spotify account.
- **User Input**: Allows you to select any date (in YYYY-MM-DD format) to create a playlist from that day's hits.

## Prerequisites:

- **Python 3.x**
- **BeautifulSoup**: For scraping the Billboard website.
- **requests**: For making HTTP requests.
- **spotipy**: For interacting with the Spotify API.
- A **Spotify Developer Account** with access to the API (you'll need your `SPOTIFY_ID`, `SPOTIFY_SECRET`, and `SPOTIFY_USERNAME`).

## Installation:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
2. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
3. **Install the required Python libraries**:
   ```bash
   pip install beautifulsoup4 requests spotipy

## Set up environment variables:

- SPOTIFY_ID: Your Spotify client ID.
- SPOTIFY_SECRET: Your Spotify client secret.
- SPOTIFY_USERNAME: Your Spotify username.

## Usage:

**Run the script**:
python main.py


## How It Works:
- **Song List Creation**: The script scrapes the Billboard Hot 100 chart for the specified date using BeautifulSoup, filtering out irrelevant text.
- **Spotify Playlist Creation**: It then uses the Spotify API to search for each song on Spotify and compiles them into a new playlist in your account.
