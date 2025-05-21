# Import required libraries
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Constants for API access
OPENROUTER_API_KEY = "" #add openRouter API key here
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# ========== LLM Setup ==========

def setup_llm_client():
    """
    Initializes and returns a configured LLM client using OpenRouter.
    You can change the `model_name` to other models like Gemini, GPT-4, Mistral, etc.
    """
    return ChatOpenAI(
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
        model_name="deepseek/deepseek-chat-v3-0324:free"
    )

# ========== File Handling Utilities ==========

def read_file(file_path):
    """Reads and returns the contents of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_output(content, file_path):
    """Saves the provided content to a specified file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def load_template(file_path):
    """Loads the prompt template from a file."""
    return read_file(file_path)

# ========== Prompt Preparation ==========

def create_prompt_template(template_content):
    """Creates a PromptTemplate from the loaded template content."""
    return PromptTemplate(template=template_content)


def process_final_template(input_file, metadata_file, review_file, mapping_file, chain):
    """
    Processes the final template with all input files and saves the result.
    """
    if not all(os.path.exists(p) for p in [input_file, metadata_file, review_file, mapping_file]):
        print("Error: One or more input files do not exist.")
        return

    print(f"Running final template processing for")

    input_data = {
        'aspects_file': read_file(input_file),
        'user_location': "58.377861, 26.728766",  # Hardcoded location input
        'reviews_file': read_file(review_file),
        'user_prompt': "Find the best Italian restaurant near me",  # Try to make your own prompt
        'restaurant_metadata_file': read_file(metadata_file),
        'restaurant_mapping_file': read_file(mapping_file)
    }

    output = chain.invoke(input_data)

    print(output)

# ========== Main Runner ==========

def main():
    """Main entry point for processing using LLM pipeline."""
    # Step 1: Initialize the LLM client
    llm = setup_llm_client()

    # Step 2: Load and prepare the prompt template
    template_content = load_template("./templates/final_template.txt")
    prompt = create_prompt_template(template_content)

    # Step 3: Compose the full processing chain
    chain = prompt | llm | StrOutputParser()

    # Step 4: Define file paths
    aspects_file = "./input/aspects.txt"
    metadata_file = "./input/cleaned_dataset.txt"
    reviews_file = "./input/Reviews.txt"
    mapping_file = "./input/short_name.txt"

    # Step 5: Execute final processing
    process_final_template(aspects_file, metadata_file, reviews_file, mapping_file, chain)

# Run main
if __name__ == "__main__":
    main()
