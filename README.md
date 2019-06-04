# Internet-Analytics-Labs
Labwork for the course Internet Analytics (COM-308) @EPFL (spring 2019).

## Lab 1: Introduction
Getting familiar with python, Spark, Numpy, Networkx that will be used in following lab assignments.

## Lab 2: Networks: structure, evolution, processes
* Exploring some real world networks and verifying the expected properties common to large networks.
* Sampling nodes from a network to compute network-wide statistics in sublinear time.
* Simulating epidemics and analyzing their spread and devising heuristics to fight them.
* PageRank: computing scores of nodes and trying to artificially 'boost' ranks of certain nodes.

## Lab 3: Embedding and Recommending
Here we analyze a movie dataset from MovieLens (https://movielens.org/). We use genres the movies are attributed to (19 in total), and tags (1128 in total), each of which have some given 'relevance' with a movie. Examples of genres are 'Adventure', 'Comedy', 'Thriller', and for tags - 'touching', 'gangsters', 'so bad it's funny'.
* **Dimensionality Reduction**: performing PCA to find a small set of tag vectors that best describe the entire dataset (remember that normally each movie is a point in 1128 dimensions (each tag is a dimension)). Each 'important' vector then can be thought of as representing a *concept*.
* **Recommender Systems**: Using collaborative filtering to recommend movies to users.
* **Clustering**: finding clusters of movies according to 1. tags (based on projections on vectors computed in DimRed) and 2. provided genres.

## Lab 4: Text Representation and Information Retrieval
We analyze two corpuses of textual data - (1) the course descriptions in EFPL course catalog and (2) wikipedia for schools. Concepts used:
* **(VSM) Vector Space Models**: Pre-processing real-world data, bag-of-words representation, computing TF-IDF and implementing document search based on it.
* **(LSI) Latent Semeantix Indexing**: Topic exctraction, document similarity search (query-based) and document-document similarity metric.
* **(LDA) Latent Dirichlet allocation**: Powerful topic extraction, applied on a large wikipedia-for-schools dataset.
