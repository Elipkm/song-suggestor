
- Prerequisites
   - Set the following environment variables for OpenAi LLM 
      - OPENAI_API_KEY
      - OPENAI_ORGANIZATION
   - Run a local Elasticsearch (on port 9200)
1. Run Backend
   - cd song_suggestor_backend 
   - py src/main_server.py 
2. Run Setup to embed the demo song data - keywords into local elasticsearch
   - curl -X POST http://localhost:5000/api/setup
3. Run Frontend with ng serve
   - cd song_suggestor_ui
   - ng serve

 Technologies and Versions used:
   - Python: 3.10.7
   - ElasticSearch: 8.12.1
   - Angular: 19
   - PrimeNG
   - node: v22.12.0
   - npm: 11.0.0
   - LLM: gpt-4o-mini


Project Presentation:
# How to find new music recommendations by analyzing song lyrics with the use of an LLM.

## Introduction
Last summer I wondered what can be done with an LLM like ChatGPT. I had the idea to build an app for finding similar music based on one favorite song. After working on it as a hobby side project for more than half a year now, I am ready to present some results, nice findings and a few surprises. I would like to share with you what I have learned by implementing my own suggestion algorithm.

## Table of Contents
The idea
Challenges
Song analysis with LLM
A new approach
The suggestion algorithm 
The dataset
Demo
Conclusion

## The Idea
I would like to start by providing a better understanding of the suggestion idea. To keep things simple I thought it would certainly be interesting to just take the lyrics of a song as input data and based on the words trying to suggest similar songs. In my mind popular algorithms use many other features of a song like the genre, the year, user information and musical data. By intentionally ignoring all this extra information I hoped to get some pretty cool suggestion results by opening the possibility to other worlds by focusing solely on the song's meaning and story.  

## Challenges
One of the main challenges in realising this project is to come up with a big dataset of songs. 
The following questions were asked. How many songs should be available for the program to choose for as a suggestion? Where can the song title, artist and lyrics be found? How many songs can be analyzed with the OpenAI API on a reasonable budget and how long will it take to process these? 
The next big challenge is to develop a concept for parsing songs into a measurable and comparable format and in combination working on the algorithm that finds the recommendations based on the newly created format specification. 

## Song analysis with LLM
I knew right from the start that such an experiment would be possible by using a LLM. I made several prompts to ChatGPT in the past just because I was curious and asked it to analyze a song's lyrics. The results were most of the time phenomenal and impressive. 
Just to give you a quick glimpse into one of the answers: 
“Overall, these lyrics effectively convey a deep sense of pain, struggle, and the feeling of being lost or abandoned. The emotional weight of the words, combined with the imagery and repetition, creates a poignant narrative of facing life's battles and the toll it takes on one's spirit.”.  
This makes it clear that a LLM can differentiate whether the text is happy or sad. Whether a song feels angry or hopeful and so on.
Now we know that LLM has the capability to draw beautiful conclusions from a song's lyrics and is really good at extracting the meaning by understanding the words and the context. 

In order to work with these great responses a format needs to be specified and outlined. The format has to be comparable.
My first idea was to let the AI generate ten adjectives for each song. 
Examples:
confident, aggressive, boastful,  gritty,  playful,  defiant,  celebratory,  raw,  urban,  dynamic

hopeless, desperate, addicted, escapist, reflective, ambitious, stressful, conflicted, tense, defiant

intense,  defiant,  nostalgic,  aggressive,  confident,  chaotic,  resilient,  confrontational,  proud,  reflective

Based on these generated keywords a filter and search is possible. After carefully testing the suggestion results by using a test dataset it turns out that one word descriptions are far too imprecise to find meaningful results. I have tried to rank the adjectives by importance but for the search result it did not make any good difference. 

After this realization I have tried a few things like extending the keywords to short phrases or establishing a mixture of keywords that catch the dominant themes and descriptions to enable detailed search. 
No solution seemed good enough, so I decided to step back and review the concept of a keywords-based analysis and tried to look for new perspectives.

## A new approach
Now if you ask an AI to extract the meaning based on just the songtext, what are the options? Are there any other points that can be assessed besides the broad classification of ‘meaning’? I have found many components that can be analysed. 
The following list are some valid options.
central themes
which emotions are delivered
Narrative perspective
is there a message?
How ambiguous or certain is the message portrayed?
What about the language?
tonality and expression?
Are there stylistic devices used? (e.g. metaphors, personifications, alliterations, anaphora)
structure (verse, refrain..)
Are the verses short or long?
what about rhymes?
After having a definition of available features we can define which features are wanted for the suggestion and which are not useful. At the end I formulated the following recipe defining nine different categories or features to be analyzed. 

   1. Central Themes: What is the song about, and what are its central ideas?
    2. Emotional Impact: What feelings does the text evoke in its listener or reader?
    3. Narrator: Who is the speaker or narrator in the song, and what is their role?
    4. Perspective: From which perspective is the narrative delivered (e.g. first-person)?
    5. Core Message: Summarize the main message or essence of the song in a few words.
    6. Certainty: How confidently or ambiguously is the message portrayed?
    7. Language: What is the language style (e.g., formal, colloquial, poetic, etc.)?
    8. Tone: Describe the tone or mood conveyed by the words.
    9. Universal Human Experiences: Identify the top three central human experiences expressed in the song.

By working with categories an easy segregation is made possible. Comparison is easier because we can compare the same categories for each song and the effects of each category are easily seen. 

Here are two songs analyzed according to this formula.
Example 1:
    1. Central Themes: Love, longing, loss, hope.
    2. Emotional Impact: Nostalgia, yearning, sadness, warmth.
    3. Narrator: A reflective lover, expressing vulnerability.
    4. Perspective: First-person perspective.
    5. Core Message: Love transcends distance and time.
    6. Certainty: Ambiguously hopeful yet tinged with regret.
    7. Language: Poetic, evocative, intimate.
    8. Tone: Melancholic yet hopeful.
    9. Universal Human Experiences: Love, loss, longing


Example 2:
    1. Central Themes: Friendship, nostalgia, connection.
    2. Emotional Impact: Warmth, longing, joy.
    3. Narrator: A reflective observer, reconnecting.
    4. Perspective: First-person perspective.
    5. Core Message: Reunions with cherished memories.
    6. Certainty: Confidently nostalgic.
    7. Language: Poetic, conversational.
    8. Tone: Sentimental, uplifting.
    9. Universal Human Experiences: Friendship, memory, recognition.

## The suggestion algorithm
The suggestion algorithm I developed aligns perfectly with the previously defined category-schema. Each new song is analyzed according to the categories. For each category a similarity search is performed. The songs with the best matches in all categories summed up are the recommendation results. 
In order to optimize the algorithm further an option to give each category a weight representing the importance is implemented. 
I found out that to properly rank the categories a look at the dataset at hand is helpful. 
The first factor for deciding how important the category is for my suggestion strategy is the significance the category values represent compared to the other categories. I analysed the values and assigned a score for the perceived significance. Then looking at the whole dataset I have tried to assess the uniqueness in a category's values.  The combination of a perceived significance and the uniqueness in the dataset made it possible to assign a reasonable weight. For example by using this technique I realised that the category “Perspective” is not suitable for my dataset because about 95% of all songs I have processed use the first-person perspective. That means this category does not enable new search possibilities.

## The dataset 
Equally important to analyzing and comparing is the provided datasource. My first attempt was to process randomly selected songs from an exported music database. Testing the suggestion results based on this random dataset I was not really satisfied. Because I realized it is hard to tell if the suggestion is bad because the algorithm does not work or just because the dataset contains some poorly produced songs. 
To solve this issue I processed a dataset of about 9000 songs that were present in the Billboard weekly top 100 charts. By using this constraint on the dataset a consistent high quality was assured. Now the results were pretty neat. 
Nonetheless it is important to keep in mind that the algorithm can only possibly make recommendations by choosing from the dataset provided. Consequently if a request with an exotic flavour comes in and there is simply no good match in the database then the algorithm will take the best guess - a second choice.

I restricted the size for testing to about 10.000 songs each time, to test the ideas quickly. The usage of ChaGpt (OpenAI) api costs about 1,8$ per 10.000 songs and it takes about an hour.

## Demo

<img width="1918" height="901" alt="example_suggestion" src="https://github.com/user-attachments/assets/eee9e4e0-4bc0-466b-afc4-233b9d5f52d2" />


<img width="1886" height="901" alt="example_suggestion_result" src="https://github.com/user-attachments/assets/1f38bf2a-c2c4-4d6b-a329-fa573ae000ef" />

<img width="1883" height="907" alt="example_suggestion_result_explain" src="https://github.com/user-attachments/assets/76176e83-2a12-4be1-b656-caad138607b8" />




