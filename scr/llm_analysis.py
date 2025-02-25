import os
import pandas as pd
import scanpy as sc
from dotenv import load_dotenv
import argparse
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize LLMs with API keys: TODO fill in the .env file
openai_api_key = os.getenv("OPENAI_API_KEY")
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
if not openai_api_key or not deepseek_api_key:
    raise ValueError("API key for OpenAI or DeepSeek not found in .env file!")

# Initialize GPT-4
gpt_llm = ChatOpenAI(model_name="gpt-4", temperature=0.7, openai_api_key=openai_api_key) # Can change model

# Initialize DeepSeek
deepseek_client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com") # https://api-docs.deepseek.com/

# Load scRNA-seq Data
def load_data(file_path: str):
    """Loads scRNA-seq data based on file type."""
    if file_path.endswith(".csv.gz"):
        return pd.read_csv(file_path, compression="gzip")
    elif file_path.endswith(".h5"):
        return sc.read_h5ad(file_path)
    elif file_path.endswith(".rds"):
        raise NotImplementedError("RDS files require conversion from R.") # Reminder!
    else:
        raise ValueError("Unsupported file format.")

# Define Prompt for GPT-4
gpt_prompt_template = PromptTemplate(
    input_variables=["data_summary"],
    template="Analyze the following scRNA-seq data and provide insights on cell types, marker genes, and pathway enrichment:\n{data_summary}"
)

# Create LLM Chain for GPT-4
gpt_llm_chain = LLMChain(llm=gpt_llm, prompt=gpt_prompt_template)

# DeepSeek API
def run_deepseek_analysis(data_summary):
    """
    Runs DeepSeek analysis on scRNA-seq data using the DeepSeek API.
        * The deepseek-chat model has been upgraded to DeepSeek-V3. The API remains unchanged. 
        You can invoke DeepSeek-V3 by specifying model='deepseek-chat'.
        * deepseek-reasoner is the latest reasoning model, DeepSeek-R1, released by DeepSeek. 
        You can invoke DeepSeek-R1 by specifying model='deepseek-reasoner'.
    """
    response = deepseek_client.chat.completions.create(
        model="deepseek-reasoner", # Can change: "deepseek-reasoner" OR "deepseek-chat"
        messages=[
            {"role": "system", "content": "You are a helpful assistant for scRNA-seq analysis."},
            {"role": "user", "content": f"Analyze the following data:\n{data_summary}"}
        ],
        stream=False
    )
    return response.choices[0].message.content # Must test!

# Benchmark LLM vs. Traditional Analysis
def benchmark_analysis(data, model_choice):
    """Runs analysis on scRNA-seq data using the selected model."""
    data_summary = str(data.head())  # Summarize dataset for model (TBD - placeholder for now)
    if model_choice == "gpt4":
        llm_result = gpt_llm_chain.run({"data_summary": data_summary})
    elif model_choice == "deepseek":
        llm_result = run_deepseek_analysis(data_summary)
    elif model_choice == "both":
        gpt_result = gpt_llm_chain.run({"data_summary": data_summary})
        deepseek_result = run_deepseek_analysis(data_summary)
        llm_result = {"GPT-4": gpt_result, "DeepSeek": deepseek_result}
    else:
        raise ValueError("Invalid model choice. Please select 'gpt4', 'deepseek', or 'both'.")
    
    return llm_result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run scRNA-seq analysis using GPT-4, DeepSeek, or both.")
    parser.add_argument("model", choices=["gpt4", "deepseek", "both"], help="Choose the model(s) to use")
    parser.add_argument("data_file", help="Path to the scRNA-seq data file")
    args = parser.parse_args()

    # If data file exists
    if os.path.exists(args.data_file):
        sc_data = load_data(args.data_file)
        
        # Run selected model(s)
        analysis_output = benchmark_analysis(sc_data, args.model)
        print("\nAnalysis Output:\n", analysis_output)
    else:
        print(f"Error: Data file {args.data_file} not found.")
