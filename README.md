# Content Based Movie Recommendation System using Streamlit
![Python](https://img.shields.io/badge/Python-3.10-blue) ![Frontend](https://img.shields.io/badge/Frontend-Streamlit-red) ![API](https://img.shields.io/badge/API-TMDB-fcba03) ![API](https://img.shields.io/badge/ML-Numpy_|_Pandas_|_NLTK_|_Scikit_learn-237a3b)

A content-based recommender system that recommends movies similar to the movie the user likes using cosine similarity score.

The Recommendations are made by computing similarity scores for movies using cosine similarity. For each movie tags are created by combining various details like genre of the movie, title, top cast, director and then they are converted to vectors using which similarity matrix is formed. Then for any searched movie the movies with the largest similarity score with it are sorted and then recommended.

## System Architecture

![System Architecture](https://raw.githubusercontent.com/soumadeep-dey/Movie-Recommendation-System/8ae1db904d3aad26bfcc4c08b35eb9f7692639f2/image/System%20Architecture.jpg)

## How Cosine Similarity works?

  Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

  ![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)

## Similarity Score :

   How does it decide which item is most similar to the item user likes? Here come the similarity scores.

   It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)
