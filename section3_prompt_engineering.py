"""
Section 3: Prompt Engineering Approach for GreenThumb Goods
This script implements two distinct prompt engineering strategies for handling complex customer queries.
"""

import json
import os
import sys
import random
from openai import OpenAI

# Import configuration
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OPENAI_API_KEY

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Load the dataset
def load_dataset(file_path):
    """Load the GreenThumb Goods dataset from a JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Strategy A: Zero-shot with detailed instructions and context
def create_zero_shot_prompt(query, product_info, policy_info):
    """
    Create a zero-shot prompt with detailed instructions and context.
    
    Args:
        query: The customer query
        product_info: Dictionary containing product information
        policy_info: Dictionary containing policy information
    
    Returns:
        A formatted prompt string
    """
    prompt = f"""You are a customer service AI assistant for GreenThumb Goods, a company specializing in gardening supplies and sustainable products. Your task is to provide helpful, accurate, and friendly responses to customer queries.

COMPANY CONTEXT:
GreenThumb Goods is committed to sustainability and offers a wide range of eco-friendly gardening products and home goods. The company values customer satisfaction and environmental responsibility.

AVAILABLE PRODUCT CATEGORIES:
- Plants (herb kits, succulents, seedlings, etc.)
- Tools (garden tools, lights, composting equipment, etc.)
- Soil & Fertilizers (organic soils, natural fertilizers, etc.)
- Eco-Home Products (sustainable kitchen items, reusable goods, etc.)

COMPANY POLICIES:
1. Returns: {policy_info['returns']}
2. Shipping: {policy_info['shipping']}
3. Sustainability: {policy_info['sustainability']}
4. Rewards Program: {policy_info['rewards']}
5. Warranty: {policy_info['warranty']}

INSTRUCTIONS:
- Identify all intents in the customer's query (product inquiries, policy questions, etc.)
- Provide accurate information about products and policies
- If the query contains multiple questions, address each one separately
- Be friendly and professional in your tone
- If you don't have specific information about a product, acknowledge this and offer to connect the customer with a specialist
- For complaints, show empathy and offer clear next steps for resolution

CUSTOMER QUERY:
{query}

Please provide a comprehensive response addressing all aspects of the customer's query.
"""
    return prompt

# Strategy B: Few-shot learning with examples
def create_few_shot_prompt(query, examples):
    """
    Create a few-shot prompt with examples.
    
    Args:
        query: The customer query
        examples: List of example query-response pairs
    
    Returns:
        A formatted prompt string
    """
    prompt = """You are a customer service AI assistant for GreenThumb Goods, a company specializing in gardening supplies and sustainable products. Your task is to provide helpful, accurate, and friendly responses to customer queries.

Here are some examples of how to respond to complex customer queries:

"""
    
    # Add examples
    for i, example in enumerate(examples, 1):
        prompt += f"Example {i}:\nCustomer: {example['query']}\nResponse: {example['response']}\n\n"
    
    # Add the current query
    prompt += f"Now, please respond to this customer query in a similar style:\nCustomer: {query}\nResponse:"
    
    return prompt

# Select challenging queries for testing
def select_challenging_queries(dataset, n=5):
    """
    Select n challenging multi-intent queries from the dataset.
    
    Args:
        dataset: The full dataset
        n: Number of queries to select
    
    Returns:
        List of selected queries
    """
    # Filter for queries with at least 2 intents
    complex_queries = [item for item in dataset if len(item['intents']) >= 2]
    
    # Sort by complexity (number of intents)
    complex_queries.sort(key=lambda x: len(x['intents']), reverse=True)
    
    # Select top n
    selected = complex_queries[:n]
    
    return selected

# Get response from OpenAI API
def get_openai_response(prompt):
    """
    Get a response from the OpenAI API.
    
    Args:
        prompt: The formatted prompt
    
    Returns:
        The response from the API
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling OpenAI API: {str(e)}\n\nThis would normally return a response from the OpenAI API. Please ensure your API key is set correctly in config.py."

# Main function to test prompt strategies
def main():
    # Set up output directory
    output_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(output_dir, 'greenthumb_dataset.json')
    
    # Check if dataset exists, if not, try to find it in parent directory
    if not os.path.exists(dataset_path):
        parent_dir = os.path.dirname(output_dir)
        dataset_path = os.path.join(parent_dir, 'greenthumb_dataset.json')
        if not os.path.exists(dataset_path):
            print("Dataset file not found. Please run section1_dataset.py first.")
            return
    
    # Load dataset
    print("Loading dataset...")
    dataset = load_dataset(dataset_path)
    
    # Product and policy information
    product_info = {
        "plants": [
            {"name": "Organic Herb Garden Starter Kit", "price": 29.99, "description": "Complete kit with 6 herb varieties, organic soil, and biodegradable pots"},
            {"name": "Indoor Succulent Collection", "price": 34.99, "description": "Set of 5 low-maintenance succulents in decorative ceramic pots"}
        ],
        "tools": [
            {"name": "Ergonomic Garden Tool Set", "price": 49.99, "description": "Set of 3 ergonomic hand tools with sustainable bamboo handles"},
            {"name": "Compost Tumbler", "price": 129.99, "description": "Dual-chamber compost tumbler with 80-gallon capacity"}
        ]
    }
    
    policy_info = {
        "returns": "GreenThumb Goods offers a 30-day satisfaction guarantee on all products. Plants and perishable items must be returned within 7 days with proof of purchase.",
        "shipping": "Free shipping on orders over $50 within the continental US. Standard shipping (3-5 business days) is $5.99.",
        "sustainability": "All GreenThumb Goods packaging is either recyclable, biodegradable, or made from recycled materials.",
        "rewards": "GreenThumb Rewards members earn 1 point per dollar spent. 100 points can be redeemed for a $5 discount.",
        "warranty": "Garden tools carry a 2-year warranty against manufacturing defects. Electronic items have a 1-year warranty."
    }
    
    # Select challenging queries
    print("Selecting challenging queries...")
    challenging_queries = select_challenging_queries(dataset)
    
    # Select examples for few-shot learning
    few_shot_examples = random.sample(dataset, 3)
    
    # Test both strategies
    print("Testing prompt strategies...")
    results = []
    
    for i, query_item in enumerate(challenging_queries):
        query = query_item['query']
        print(f"\nQuery {i+1}: {query}")
        
        # Strategy A: Zero-shot with detailed instructions
        print("Testing Strategy A: Zero-shot with detailed instructions...")
        zero_shot_prompt = create_zero_shot_prompt(query, product_info, policy_info)
        zero_shot_response = get_openai_response(zero_shot_prompt)
        
        # Strategy B: Few-shot learning with examples
        print("Testing Strategy B: Few-shot learning with examples...")
        few_shot_prompt = create_few_shot_prompt(query, few_shot_examples)
        few_shot_response = get_openai_response(few_shot_prompt)
        
        # Store results
        results.append({
            "query": query,
            "intents": query_item['intents'],
            "zero_shot_prompt": zero_shot_prompt,
            "zero_shot_response": zero_shot_response,
            "few_shot_prompt": few_shot_prompt,
            "few_shot_response": few_shot_response
        })
    
    # Save results
    results_path = os.path.join(output_dir, 'prompt_engineering_results.json')
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nPrompt engineering testing complete. Results saved to {results_path}")
    
    # Display example prompts
    print("\nExample Zero-Shot Prompt:")
    print(create_zero_shot_prompt("I'm interested in starting a herb garden. What products do you recommend? Also, what's your return policy?", product_info, policy_info))
    
    print("\nExample Few-Shot Prompt:")
    print(create_few_shot_prompt("I'm interested in starting a herb garden. What products do you recommend? Also, what's your return policy?", few_shot_examples[:2]))
    
    return results

if __name__ == "__main__":
    main()
