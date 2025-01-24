
import re
from typing import List
from langchain_core.prompts.prompt import PromptTemplate
from langchain.globals import set_debug
from config.application_factory import get_embeddings_instance, get_llm

set_debug(True)

def get_word_embedding(word) -> List[float]:
    embeddings = get_embeddings_instance()
    return embeddings.embed_query(word)

def get_keywords_for_lyrics(lyrics: str) -> List[str]:  
    
    prompt_template = """
    You are a skilled poet and literary analyst with a profound understanding of language, emotion, and artistic expression. Your task is to analyze the following song lyrics and answer a series of questions designed to explore their deeper meanings. Please ensure your responses are thoughtful, nuanced, and devoid of explicit names or direct quotes from the text. Focus on interpretation rather than summarization. 
    Give only short phrases as response, do not build whole sentences.
    Given the following 9 questions, produce a list with exactly 9 answers.\n\n

    1. Central Themes: What is the song about, and what are its central ideas?
    2. Emotional Impact: What feelings does the text evoke in its listener or reader?
    3. Narrator: Who is the speaker or narrator in the song, and what is their role?
    4. Perspective: From which perspective is the narrative delivered (e.g., first-person, omniscient, etc.)?
    5. Core Message: Summarize the main message or essence of the song in a few words.
    6. Certainty: How confidently or ambiguously is the message portrayed?
    7. Language: What is the language style (e.g., formal, colloquial, poetic, etc.)?
    8. Tone: Describe the tone or mood conveyed by the words.
    9. Universal Human Experiences: Identify the top three central human experiences expressed in the song. 

    Song lyrics: "{lyrics}"

    """

    # Initialize a Parser optionally:
    # parser = None
    prompt = PromptTemplate(
        input_variables=["lyrics"],
      #  partial_variables={"format_instructions": parser.get_format_instructions()},
        template=prompt_template,
    )

    llm = get_llm()
    chain = prompt | llm

    chain_result = chain.invoke({"lyrics": lyrics})

    print()
    print("CHAIN RESULT:")
    print(chain_result.content)
    
    result = chain_result.content.splitlines()
    result = [item.strip() for item in result if item.strip()]
    for i, item in enumerate(result):
        result[i] = remove_starting_number(item)

    print()
    print("final result:")
    print(result)

    return result

# Define a function to remove starting numbers and a period
def remove_starting_number(input_string):
    # Regex pattern to match starting numbers, a period, and optional spaces
    pattern = r"^\d+\.\s*"
    # Use re.sub to replace the matched pattern with an empty string
    return re.sub(pattern, "", input_string)
