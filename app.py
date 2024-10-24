import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from PIL import Image
import io
import os

# Function to scrape free courses from the Analytics Vidhya site or load existing CSV
@st.cache_data
def scrape_courses():
    file_path = 'free_courses.csv'
    
    # Check if 'free_courses.csv' exists
    if os.path.exists(file_path):
        # Load from CSV if it exists
        return pd.read_csv(file_path)
    
    else:
        # If CSV doesn't exist, scrape the data and save it to CSV
        st.write("Scraping course data from the website...")
        base_url = "https://courses.analyticsvidhya.com/collections/courses?page="
        page = 1
        courses = []
        
        while True:
            url = f"{base_url}{page}"
            response = requests.get(url)
            
            if response.status_code != 200:
                break
            
            soup = BeautifulSoup(response.text, 'html.parser')
            course_items = soup.find_all('li', class_='products__list-item')
            
            if not course_items:
                break
            
            for course in course_items:
                title = course.find('h3').text.strip()
                description = course.find('h4').text.strip()
                link = course.find('a')['href']
                img_src = course.find('img')['src']
                
                courses.append({
                    "title": title,
                    "description": description,
                    "link": link,
                    "img_src": img_src
                })
            
            page += 1
        
        # Convert list to DataFrame and save to CSV
        courses_df = pd.DataFrame(courses)
        courses_df.to_csv(file_path, index=False)
        st.write(f"Data saved to '{file_path}' with {len(courses)} courses.")
        return courses_df

# Scrape the courses
st.title("Smart Course Search Tool")
st.markdown("Find the most relevant free courses on **Analytics Vidhya** with images, descriptions, and direct links.")

st.write("Scraping course data... This may take a moment.")
courses_df = scrape_courses()
courses_df['combined'] = courses_df['title'] + " " + courses_df['description']

# Pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for the course descriptions
embeddings = model.encode(courses_df['combined'].tolist())

# Create FAISS index for efficient searching
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings).astype('float32'))

# Search courses based on query
def search_courses(query, k=5):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding).astype('float32'), k=k)
    results = courses_df.iloc[indices[0]]
    
    courses = []
    for _, row in results.iterrows():
        course_info = {
            'title': row['title'],
            'description': row['description'],
            'link': row['link'],
            'image': row['img_src']
        }
        courses.append(course_info)
    
    return courses

# Streamlit Search Interface
query = st.text_input("Enter search query (e.g., 'machine learning', 'python')")

if query:
    st.write(f"Showing results for: **{query}**")
    results = search_courses(query)
    
    for course in results:
        st.markdown(f"### [{course['title']}]({course['link']})")
        st.write(course['description'])
        
        # Display course image
        try:
            image_data = requests.get(course['image']).content
            image = Image.open(io.BytesIO(image_data))
            st.image(image, use_column_width=True)
        except Exception as e:
            st.write("Could not load image.")

    st.write(f"Found {len(results)} relevant courses.")
else:
    st.write("Enter a query to search for courses.")

