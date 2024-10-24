---
title: Smart Course Search Tool
emoji: 🕵
colorFrom: yellow
colorTo: red
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
license: mit
short_description: Smart Course Search Tool for Free Courses on Analytics Vidhy
---

# Smart Course Search Tool

Welcome to the **Smart Course Search Tool** repository! This project is designed to help users find relevant free courses from Analytics Vidhya's platform based on search queries. The tool leverages state-of-the-art NLP techniques and embedding models to provide real-time search results that match user input.

This project has been developed using **Streamlit** and is deployed on **Hugging Face Spaces**.

## Features
- **Web Scraping**: The tool scrapes free courses from Analytics Vidhya’s website and stores them in a CSV file (`free_courses.csv`), which is used for future searches.
- **Real-Time Search**: Users can type in a query and get real-time suggestions of courses that match their input.
- **Sentence Embeddings**: Each course’s title and description are transformed into embeddings using the pre-trained `all-MiniLM-L6-v2` model from the **SentenceTransformers** library.
- **Efficient Search**: The course embeddings are indexed using **FAISS** for fast retrieval of relevant courses based on similarity with the search query.
- **Streamlit Interface**: A simple and interactive web interface where users can view course titles, descriptions, and images, with direct links to the course page.

## Installation

To run this project locally, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/smart-course-search-tool.git
   cd smart-course-search-tool
   ```

2. **Install the required libraries**:
   Make sure you have Python 3.7+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

   The app will be running locally at `http://localhost:8501/`.

## Usage

1. **Search Courses**: 
   - Once the app is loaded, you will see a search input box.
   - Start typing your search query (e.g., "machine learning", "python"), and the app will provide suggestions in real-time.
   
2. **View Course Details**: 
   - Each search result includes the course title, description, and a clickable link that directs you to the course page.
   - An image of the course is also displayed for a more visual experience.

3. **Scraping New Courses**:
   - If the `free_courses.csv` file is missing or outdated, the tool will scrape the latest courses from Analytics Vidhya’s website and save them to the CSV file for future searches.

## Key Technologies

- **Streamlit**: For building the interactive user interface.
- **BeautifulSoup**: For scraping course data from Analytics Vidhya's website.
- **FAISS**: For efficient similarity search over course embeddings.
- **SentenceTransformers**: For generating sentence embeddings using the `all-MiniLM-L6-v2` model.
- **Hugging Face Spaces**: For hosting and deploying the application.

## File Structure

- `app.py`: The main Streamlit application script.
- `scrape_courses.py`: The script responsible for scraping courses from the web.
- `requirements.txt`: List of required Python libraries for running the project.
- `free_courses.csv`: A CSV file storing the scraped courses (if already available).

## Future Improvements

- **Pagination**: Improve the user interface by adding pagination for large numbers of search results.
- **Advanced Filters**: Add more filters such as course duration, difficulty level, or course rating to refine search results.
- **Course Update Notifications**: Implement a feature to notify users when new courses are available.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and make changes as you like. Pull requests are warmly appreciated.

## License

This project is licensed under the MIT License.
