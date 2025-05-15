# AI-Powered-Food-Safari
🍽️ AI-Powered Restaurant Recommender

This project implements an intelligent restaurant recommendation system that leverages natural language processing (NLP) and aspect-based sentiment analysis to rank restaurants based on user preferences, multilingual reviews, and restaurant metadata.

🚀 What It Does

Accepts a user prompt (e.g., “cheap vegetarian places near me with great service”)  
Analyzes customer reviews (English, Estonian, Russian) to extract sentiment for specific aspects (e.g., food quality, service)  
Dynamically weights aspects based on the user’s input  
Scores each restaurant using both review sentiment and metadata (location, rating, takeout options, etc.)  
Produces a ranked Top 5 list with explanations  
📂 Input Files  

ASPECTS_FILE: Lists all aspects to evaluate (e.g., Food Quality, Ambience)  
REVIEWS_FILE: Restaurant reviews with sentiment analysis  
RESTAURANT_METADATA_FILE: Info like location, rating, price level  
RESTAURANT_MAPPING_FILE: Maps short names to full restaurant names  
USER_LOCATION: Coordinates to assess proximity  
USER_PROMPT: Natural language query from the user  
