# scRNA_benchmarking
Course Project Proposal
Title?
Benchmarking Large Language Models Against Standard Tools for Single-Cell RNA Sequencing Analysis
What specific problem would the team like to investigate?
The specific problem we aim to address in this research project is whether large language models (LLMs) such as ChatGPT and DeepSeq.AI can provide insights into scRNA-seq data comparable to or exceeding traditional bioinformatics tools. Specifically, we will assess their ability to classify cell types, identify differentially expressed genes, and analyze biological pathways compared to widely used computational methods in the field.
What is the main hypothesis?
LLMs applied to scRNA-seq data can generate biologically meaningful insights that are competitive with or superior to conventional computational tools in terms of accuracy, interpretability, and ease of use.
What are two major objectives related to the hypothesis?
The two major objectives related to the hypothesis are as follows:
Benchmark LLMs (ChatGPT and DeepSeq.AI, maybe LLama) against standard scRNA-seq analysis pipelines (e.g., Seurat in R, Scanpy in Python) across multiple datasets.
Evaluate the performance of LLMs on known annotated datasets and assess their capability in interpreting ambiguous datasets where cell annotations are unclear or missing.
Why is this project interesting?
This project is interesting because it explores the potential of LLMs in bioinformatics, a field traditionally dominated by domain-specific statistical and machine learning approaches. If LLMs can effectively analyze scRNA-seq data, they could democratize access to advanced bioinformatics analysis, reduce computational costs, and provide novel insights into cellular heterogeneity.
What has been done before to address the problem?
Previous studies have investigated LLMs in various biomedical applications, including protein structure prediction, literature mining, and clinical text generation. A recent Nature Methods paper suggested that ChatGPT outperformed standard tools in certain bioinformatics tasks, but rigorous benchmarking against scRNA-seq tools remains limited. Traditional scRNA-seq analysis relies on methods such as clustering, dimensionality reduction, and differential expression analysis, which have been optimized over years of research.
What data or datasets would the team like to analyze?
We plan to analyze multiple scRNA-seq datasets, including:
Publicly available annotated datasets from the Human Cell Atlas or 10x Genomics
https://explore.data.humancellatlas.org/projects?filter=%5B%7B%22categoryKey%22%3A%22nucleicAcidSource%22%2C%22value%22%3A%5B%22single+cell%22%5D%7D%5D
A novel or less-explored dataset to test the LLMs' ability to infer meaningful insights where standard annotations are lacking.
What bioinformatics techniques would the team like to learn and use?
We plan to use several bioinformatics techniques in our analysis, including:
Preprocessing: Quality control, normalization, and feature selection using Seurat or Scanpy.
Dimensionality Reduction: PCA, t-SNE, UMAP.
Clustering and Cell Type Identification: Leiden/Louvain clustering, marker gene analysis.
Differential Expression Analysis: Wilcoxon rank-sum test, pseudotime analysis.
Benchmarking: Comparing LLM-generated insights with standard bioinformatics pipelines in terms of accuracy and biological interpretability. This will most likely involve using a BLEU score. 
