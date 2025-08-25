# 📰 NavChronicles
NavChronicles is a Streamlit-based news application that fetches and displays the latest news articles from various sources using the [NewsAPI](https://newsapi.org/). It provides an intuitive interface for staying updated with current events across various topics.

## 🚀 Features

- **Interactive UI**: Clean, modern interface built with Streamlit
- **Real-time News Fetching**: Get the latest articles using NewsAPI
- **Topic-based Search**: Search for news by keywords or topics
- **Customizable Results**: Choose how many articles to display (5-20)
- **Article Details**: View titles, descriptions, sources, images, and publication dates
- **Direct Article Links**: Access full articles with one click
- **Responsive Design**: Optimized for various screen sizes
- **Expandable Help Sections**: User-friendly documentation within the app

## 🛠 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- NewsAPI account ([Register here](https://newsapi.org/register))

### 1. Clone the repository

 ```bash
git clone https://github.com/vanshikarana06/navchronicles.git
cd navchronicles
```
### 2. Install dependencies
 ```bash
pip install -r requirements.txt
```

### 🔑 API Key Setup

Go to NewsAPI.org and register for a free account
Get a free api key and use your own api key in the place of API_KEY.

## ▶️ Usage
Run the application with:
 ```bash

streamlit run app.py
```

Open the provided local URL (default: http://localhost:8501) in your browser.

## 📋 Example Search

Enter a topic in the sidebar (e.g., "technology", "sports", "politics")

Select the number of articles to display (5–20)

Click "Search News"

You'll see for each article:

📰 Headline

🖼 Image (if available)

🏷 Source and publication time

📖 Description

🔗 Direct link to full article
## 📸 Screenshot

Here’s how **NavChronicles** looks in action:

![NavChronicles Screenshot](images/screenshot.png)


## 📂 Project Structure
```
navchronicles/
├── file.py            # Main Streamlit application
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
└── images/
    └── images/Screenshot 2025-08-24 232144.png
```


## 🧩 Dependencies

Key dependencies include:

- streamlit - Web application framework

- requests - HTTP requests for API calls

- python-dotenv - Environment variable management (optional)

- pytz - Timezone handling (optional)

See requirements.txt for the complete list.

## 👩‍💻 Contributors
This project is created and maintained by:

Vanshika Rana - https://github.com/vanshikarana06 
Vanshika Rana - https://github.com/VR-47
