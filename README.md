# scRNA_benchmarking

## Course Project Proposal

### 📌 Title  
**Benchmarking Large Language Models Against Standard Tools for Single-Cell RNA Sequencing Analysis**

### 🧪 Problem Statement  
The specific problem we aim to address in this research project is whether large language models (LLMs) such as ChatGPT and DeepSeq.AI can provide insights into scRNA-seq data comparable to or exceeding traditional bioinformatics tools. Specifically, we will assess their ability to:  
- 🏷️ Classify cell types  
- 🧬 Identify differentially expressed genes  
- 🔬 Analyze biological pathways  

These capabilities will be compared to widely used computational methods in the field, such as **Seurat** and **Scanpy**.

### 🎯 Hypothesis  
LLMs applied to scRNA-seq data can generate biologically meaningful insights that are **competitive with or superior** to conventional computational tools in terms of **accuracy, interpretability, and ease of use**.

### 🎯 Objectives  
1. **Benchmark LLMs** (ChatGPT, DeepSeq.AI, and potentially LLama) against standard scRNA-seq analysis pipelines (**Seurat in R, Scanpy in Python**) across multiple datasets.  
2. **Evaluate performance** of LLMs on known annotated datasets and assess their capability in interpreting **ambiguous datasets** where cell annotations are unclear or missing.

### 🚀 Significance of the Project  
This project is interesting because it explores the potential of LLMs in bioinformatics, a field traditionally dominated by domain-specific statistical and machine learning approaches.  
If LLMs can effectively analyze scRNA-seq data, they could:  
✅ Democratize access to advanced bioinformatics analysis  
✅ Reduce computational costs  
✅ Provide novel insights into cellular heterogeneity  

### 📚 Previous Work  
Previous studies have investigated LLMs in various biomedical applications, including:  
- 🏗️ **Protein structure prediction**  
- 📖 **Literature mining**  
- 🏥 **Clinical text generation**  

A recent *Nature Methods* paper suggested that **ChatGPT outperformed standard tools** in certain bioinformatics tasks, but **rigorous benchmarking against scRNA-seq tools remains limited**.  
Traditional scRNA-seq analysis relies on **clustering, dimensionality reduction, and differential expression analysis**, which have been optimized over years of research.

### 📊 Datasets  
We plan to analyze multiple scRNA-seq datasets, including:  
- **Publicly available annotated datasets** from the [Human Cell Atlas](https://explore.data.humancellatlas.org/projects?filter=%5B%7B%22categoryKey%22%3A%22nucleicAcidSource%22%2C%22value%22%3A%5B%22single+cell%22%5D%7D%5D) or **10x Genomics**  
- A **novel or less-explored dataset** to test the LLMs' ability to infer meaningful insights where standard annotations are lacking.

### 🧬 Bioinformatics Techniques  
We plan to use several bioinformatics techniques in our analysis, including:  
- **Preprocessing**: Quality control, normalization, and feature selection using **Seurat** or **Scanpy**.  
- **Dimensionality Reduction**: **PCA, t-SNE, UMAP**.  
- **Clustering and Cell Type Identification**: **Leiden/Louvain clustering, marker gene analysis**.  
- **Differential Expression Analysis**: **Wilcoxon rank-sum test, pseudotime analysis**.  
- **Benchmarking**: Comparing **LLM-generated insights** with standard bioinformatics pipelines in terms of **accuracy and biological interpretability**.  
  - This will most likely involve using a **BLEU score**.

---

### 🏗️ Repository Structure  
```bash
📂 scRNA_benchmarking
│── 📄 README.md  # Project overview
│── 📂 data/      # Datasets used for analysis
│── 📂 scripts/   # Code for processing and benchmarking
│── 📂 results/   # Analysis results
│── 📂 notebooks/ # Jupyter Notebooks for exploratory analysis
