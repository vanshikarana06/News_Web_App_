import streamlit as st
import requests
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="NavChronicles",
    page_icon="📰",
    layout="wide"
)

# Hardcoded API key (replace with your actual API key)
API_KEY = '47bff7b8ff4d4ebbbe3e97b4cc000f80'  # Replace 'your_api_key_here' with your actual API key


def fetch_news(api_key, topic, max_articles=10):
    # Calculate dates for past 30 days
    today = datetime.today()
    thirty_days_ago = today - timedelta(days=30)
    from_date = thirty_days_ago.strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')

    url = "https://newsapi.org/v2/everything"

    params = {
        'q': topic,
        'from': from_date,
        'to': to_date,
        'sortBy': 'publishedAt',  # Sort by publication time
        'language': 'en',
        'pageSize': max_articles,
        'apiKey': api_key
    }
    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            articles = response.json().get('articles', [])
            return articles, None
        else:
            return None, f"Error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return None, f"Network error: {str(e)}"
    except Exception as e:
        return None, f"Unexpected error: {str(e)}"


def format_date(published_at):
    """Format the published date to a readable format"""
    try:
        date_obj = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')
        return date_obj.strftime('%B %d, %Y at %I:%M %p')
    except:
        return published_at


def main():
    # Header
    st.title("📰 NavChronicles")

    # Introduction section
    _, exp_col, _ = st.columns([1, 3, 1])
    with exp_col:
        with st.expander("📖 How to Use NavChronicles**"):
            st.markdown("""
                        Welcome to NavChronicles! 📰

                        This app allows you to fetch the latest news articles based on your interests. 
                        Simply enter a topic, and NavChronicles will provide you with the most recent articles from various sources.

                        To get started, enter your desired topic in the sidebar and click the "Search News" button. 
                        You can also customize the number of articles displayed.

                        Happy reading! 📚
                        """)

            st.info("""
                    This app utilizes the [NewsAPI](https://newsapi.org/) to fetch articles. 
                    For a comprehensive reference of available endpoints and parameters, please refer to the official documentation.
                    """)

    # Sidebar for inputs
    with st.sidebar:
        st.header("Configuration")

        # Topic input
        topic = st.text_input(
            "Enter the topic you want news about:",
            placeholder="e.g., technology, politics, sports...",
            help="Enter keywords to search for news articles"
        )

        # Number of articles slider
        max_articles = st.slider(
            "Number of articles to display:",
            min_value=5,
            max_value=20,
            value=10
        )

        # Search button
        search_button = st.button("Search News", type="primary")

        # Info section
        st.markdown("---")

    # Main content area
    if search_button:
        if not topic:
            st.error("Please enter a topic to search for")
            return

        # Show loading spinner
        with st.spinner("Fetching news articles..."):
            articles, error = fetch_news(API_KEY, topic, max_articles)

        if error:
            st.error(error)
        elif not articles:
            st.warning("No articles found for this topic in the last 30 days.")
        else:
            st.success(f"Found {len(articles)} articles about '{topic}'")

            # Display articles with source and time
            for i, article in enumerate(articles, 1):
                # Create columns for better layout
                col1, col2 = st.columns([3, 1])

                with col1:
                    st.subheader(f"{article['title']}")

                with col2:
                    # Display source and time
                    if article['source']['name']:
                        st.write(f"Source: {article['source']['name']}")
                    if article['publishedAt']:
                        formatted_date = format_date(article['publishedAt'])
                        st.write(f"Published: {formatted_date}")  # Show image if available
                if article.get('urlToImage'):
                    st.image(article['urlToImage'], caption=article['title'])

                # Show description if available
                if article.get('description'):
                    st.write(article['description'])

                # Link to full article
                st.write(f"🔗 [Read full article]({article['url']})")

                # Separator between articles
                st.markdown("---")

    # Initial state message
    else:
        st.info("Enter your topic in the sidebar to get started!")

        # Show sample of what the app will display
        with st.expander("📋 What information will be shown?"):
            st.write("""
            For each news article, you'll see:
            - Title: The headline of the article
            - Source: The news organization that published it
            - Publication Time: When the article was published
            - Image: If available
            - Description: Summary of the article
            - Link: Direct URL to the full article
            """)


if __name__ == "_main_":
    main()
