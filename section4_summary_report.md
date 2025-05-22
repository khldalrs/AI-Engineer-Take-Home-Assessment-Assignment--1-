# GreenThumb Goods AI Assistant: Summary Report

## Problem Statement
GreenThumb Goods, an e-commerce company specializing in gardening and sustainable products, is facing challenges with their customer service chatbot. The current system struggles to handle complex, multi-intent customer queries that combine product inquiries with policy questions. This leads to customer frustration, abandoned carts, and increased support tickets. The company needs an AI solution that can effectively address these complex queries to improve customer satisfaction and conversion rates.

## Methods Explored

### Method 1: Fine-Tuning Approach
We explored a fine-tuning process using OpenAI's API to adapt a pre-trained language model to GreenThumb Goods' specific domain. This approach involved:
- Creating a dataset of 50 complex multi-intent customer queries with appropriate responses
- Conceptually setting up a training pipeline that would fine-tune the model on this dataset
- Implementing a Streamlit interface for customer interactions with the model

### Method 2: Prompt Engineering Approach
We designed two distinct prompt engineering strategies to leverage existing LLM capabilities:
- **Strategy A: Zero-shot with detailed instructions** - Providing comprehensive context about products, policies, and response guidelines
- **Strategy B: Few-shot learning** - Including 3-5 examples of complex queries and ideal responses directly in the prompt
- Both strategies were tested on challenging multi-intent queries from our dataset

## Key Findings

### Accuracy on Complex Queries
- Fine-tuning would excel at consistent handling of query patterns present in the training data
- Prompt engineering offers more flexibility for novel query combinations
- Zero-shot performs well with clear instructions, while few-shot provides better response formatting

### Cost Considerations
- Fine-tuning has higher upfront development costs but lower per-query inference costs
- Prompt engineering requires minimal initial investment but higher ongoing API costs
- Development time is significantly shorter for prompt engineering solutions

### Maintenance Requirements
- Fine-tuning requires retraining when product catalog or policies change
- Prompt engineering allows immediate updates to product/policy information
- Long-term maintenance is more complex for fine-tuned models

### Flexibility
- Prompt engineering adapts more readily to new query types and seasonal changes
- Fine-tuning provides more consistent responses but less adaptability
- A hybrid approach offers the best balance of consistency and flexibility

## Recommendation

Based on my analysis, I recommend that GreenThumb Goods implement a **hybrid approach, starting with prompt engineering as the initial solution**. This recommendation is based on:

1. **Lower initial investment** allowing for faster deployment and earlier feedback collection
2. **Greater flexibility** to accommodate seasonal product changes and policy updates
3. **Iterative improvement path** that collects real customer queries to build a high-quality dataset for future fine-tuning
4. **Risk mitigation** through faster iterations based on customer feedback