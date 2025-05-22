"""
Section 1: Dataset Creation for GreenThumb Goods
This script generates a dataset of 50 complex multi-intent customer queries
along with appropriate responses for a gardening and sustainable products company.
"""

import json
import pandas as pd
import random
from datetime import datetime
import os
import sys
import openai
# Import configuration
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Define product categories and specific products
products = {
    "plants": [
        {"name": "Organic Herb Garden Starter Kit", "price": 29.99, "description": "Complete kit with 6 herb varieties, organic soil, and biodegradable pots"},
        {"name": "Indoor Succulent Collection", "price": 34.99, "description": "Set of 5 low-maintenance succulents in decorative ceramic pots"},
        {"name": "Heirloom Tomato Plant Set", "price": 19.99, "description": "3 varieties of non-GMO heirloom tomato seedlings ready for transplanting"},
        {"name": "Japanese Maple Bonsai", "price": 89.99, "description": "5-year-old bonsai with care instructions and decorative pot"},
        {"name": "Butterfly Garden Seed Mix", "price": 12.99, "description": "Mix of wildflowers that attract butterflies and pollinators"}
    ],
    "tools": [
        {"name": "Ergonomic Garden Tool Set", "price": 49.99, "description": "Set of 3 ergonomic hand tools with sustainable bamboo handles"},
        {"name": "Solar-Powered Garden Lights", "price": 39.99, "description": "Pack of 6 solar LED path lights with dusk-to-dawn sensor"},
        {"name": "Compost Tumbler", "price": 129.99, "description": "Dual-chamber compost tumbler with 80-gallon capacity"},
        {"name": "Rainwater Collection System", "price": 159.99, "description": "Complete system with 50-gallon barrel and diverter"},
        {"name": "Bamboo Garden Stakes", "price": 15.99, "description": "Pack of 25 biodegradable plant supports"}
    ],
    "soil_fertilizers": [
        {"name": "Organic Vegetable Garden Soil", "price": 24.99, "description": "25-quart bag of certified organic soil for vegetable gardens"},
        {"name": "Worm Casting Fertilizer", "price": 19.99, "description": "5-pound bag of natural worm castings for all plants"},
        {"name": "Mycorrhizal Root Booster", "price": 29.99, "description": "Beneficial fungi supplement for stronger root systems"},
        {"name": "Compost Tea Brewing Kit", "price": 45.99, "description": "Complete kit for brewing nutrient-rich compost tea"},
        {"name": "Organic Bone Meal", "price": 14.99, "description": "3-pound bag of slow-release phosphorus fertilizer"}
    ],
    "eco_home": [
        {"name": "Bamboo Kitchen Utensil Set", "price": 32.99, "description": "Set of 5 sustainable bamboo cooking utensils"},
        {"name": "Beeswax Food Wraps", "price": 18.99, "description": "Pack of 3 reusable food wraps in various sizes"},
        {"name": "Recycled Glass Drinking Set", "price": 39.99, "description": "Set of 4 tumblers and carafe made from recycled glass"},
        {"name": "Natural Fiber Dish Brushes", "price": 12.99, "description": "Set of 3 biodegradable coconut fiber dish brushes"},
        {"name": "Organic Cotton Produce Bags", "price": 16.99, "description": "Set of 5 washable mesh bags for grocery shopping"}
    ]
}

# Define company policies
policies = {
    "returns": "GreenThumb Goods offers a 30-day satisfaction guarantee on all products. Plants and perishable items must be returned within 7 days with proof of purchase. Return shipping is the responsibility of the customer unless the item arrived damaged or defective.",
    "shipping": "Free shipping on orders over $50 within the continental US. Standard shipping (3-5 business days) is $5.99. Express shipping (1-2 business days) is available for $12.99. Alaska, Hawaii, and international shipping have additional fees.",
    "sustainability": "All GreenThumb Goods packaging is either recyclable, biodegradable, or made from recycled materials. We offset carbon emissions from shipping through our tree-planting initiative. Our facilities run on 100% renewable energy.",
    "rewards": "GreenThumb Rewards members earn 1 point per dollar spent. 100 points can be redeemed for a $5 discount. Members also receive exclusive offers and early access to new products. Annual membership fee is $25, which includes a welcome gift.",
    "warranty": "Garden tools carry a 2-year warranty against manufacturing defects. Electronic items have a 1-year warranty. Plants are guaranteed to arrive in healthy condition; claims must be filed with photos within 48 hours of delivery."
}

# Define common customer intents
intents = [
    "product_inquiry",
    "price_comparison",
    "availability_check",
    "policy_question",
    "care_instructions",
    "compatibility_check",
    "recommendation_request",
    "complaint",
    "return_process",
    "shipping_inquiry"
]

# Generate complex multi-intent queries
def generate_complex_query():
    """Generate a complex multi-intent customer query with appropriate response."""
    # Select 2-3 intents for a complex query
    num_intents = random.randint(2, 3)
    selected_intents = random.sample(intents, num_intents)
    
    # Select random products and categories for reference
    category1 = random.choice(list(products.keys()))
    product1 = random.choice(products[category1])
    category2 = random.choice(list(products.keys()))
    product2 = random.choice(products[category2])
    
    # Select a random policy
    policy_key = random.choice(list(policies.keys()))
    policy = policies[policy_key]
    
    # Generate query based on selected intents
    query_parts = []
    
    if "product_inquiry" in selected_intents:
        inquiries = [
            f"Can you tell me more about the {product1['name']}?",
            f"What are the specifications of the {product1['name']}?",
            f"I'm interested in the {product1['name']}, what can you tell me about it?",
            f"Does the {product1['name']} come with a warranty?",
            f"What materials is the {product1['name']} made from?"
        ]
        query_parts.append(random.choice(inquiries))
    
    if "price_comparison" in selected_intents:
        comparisons = [
            f"How does the price of {product1['name']} compare to {product2['name']}?",
            f"Which is more cost-effective, the {product1['name']} or the {product2['name']}?",
            f"I'm trying to decide between {product1['name']} and {product2['name']} based on price and quality.",
            f"Is the {product1['name']} worth the extra cost over the {product2['name']}?",
            f"Do you have any cheaper alternatives to the {product1['name']}?"
        ]
        query_parts.append(random.choice(comparisons))
    
    if "availability_check" in selected_intents:
        availability = [
            f"Is the {product1['name']} currently in stock?",
            f"When will you restock the {product1['name']} if it's sold out?",
            f"Can I pre-order the {product1['name']} if it's not available?",
            f"Do you have the {product1['name']} available for immediate shipping?",
            f"What's the estimated delivery time for the {product1['name']}?"
        ]
        query_parts.append(random.choice(availability))
    
    if "policy_question" in selected_intents:
        policy_questions = [
            f"What's your return policy for {category1} items?",
            f"How does your shipping policy work for orders containing {product1['name']}?",
            f"Can you explain your sustainability practices regarding packaging?",
            f"How does the rewards program work if I purchase both {product1['name']} and {product2['name']}?",
            f"What's covered under the warranty for the {product1['name']}?"
        ]
        query_parts.append(random.choice(policy_questions))
    
    if "care_instructions" in selected_intents:
        care = [
            f"How should I care for the {product1['name']} after purchase?",
            f"What maintenance is required for the {product1['name']}?",
            f"How often should I water/clean/maintain the {product1['name']}?",
            f"Are there special storage requirements for the {product1['name']}?",
            f"What's the best way to ensure the {product1['name']} lasts a long time?"
        ]
        query_parts.append(random.choice(care))
    
    if "compatibility_check" in selected_intents:
        compatibility = [
            f"Will the {product1['name']} work well with the {product2['name']}?",
            f"Is the {product1['name']} compatible with my existing {category2} items?",
            f"Can I use the {product1['name']} in conjunction with the {product2['name']}?",
            f"Are there any known issues using the {product1['name']} with {product2['name']}?",
            f"Do I need any adapters or additional items to use the {product1['name']} with my {category2} setup?"
        ]
        query_parts.append(random.choice(compatibility))
    
    if "recommendation_request" in selected_intents:
        recommendations = [
            f"What would you recommend for someone new to gardening who's interested in {category1}?",
            f"I'm looking for the best {category1} for a small apartment balcony, any suggestions?",
            f"Can you recommend a {category1} that would complement my existing {product2['name']}?",
            f"What's your most popular {category1} item for beginners?",
            f"I need a gift for a sustainability enthusiast who loves {category1}, what do you suggest?"
        ]
        query_parts.append(random.choice(recommendations))
    
    if "complaint" in selected_intents:
        complaints = [
            f"The {product1['name']} I received doesn't match the description on your website.",
            f"My {product1['name']} arrived damaged, and I'm not satisfied with the customer service response.",
            f"I've been waiting for my {product1['name']} for over two weeks now, what's the delay?",
            f"The quality of the {product1['name']} doesn't justify the price you're charging.",
            f"The {product1['name']} stopped working after just a few uses, is this normal?"
        ]
        query_parts.append(random.choice(complaints))
    
    if "return_process" in selected_intents:
        returns = [
            f"How do I initiate a return for the {product1['name']} I purchased last week?",
            f"What's the process for exchanging my {product1['name']} for a different size/color/model?",
            f"Will I get a full refund if I return the {product1['name']} within the 30-day window?",
            f"Do I need the original packaging to return the {product1['name']}?",
            f"Can I return the {product1['name']} to your physical store if I bought it online?"
        ]
        query_parts.append(random.choice(returns))
    
    if "shipping_inquiry" in selected_intents:
        shipping = [
            f"How much would shipping cost for the {product1['name']} to California?",
            f"Do you offer expedited shipping for the {product1['name']}?",
            f"Can I track my {product1['name']} order once it's shipped?",
            f"Do you ship the {product1['name']} internationally?",
            f"What shipping carrier do you use for delivering the {product1['name']}?"
        ]
        query_parts.append(random.choice(shipping))
    
    # Combine query parts with connecting phrases
    connectors = [
        " Also, ", 
        " Additionally, ", 
        " By the way, ", 
        " One more thing, ", 
        " I'm also wondering, ",
        " While we're at it, ",
        " And I'd like to know, ",
        " Could you also tell me ",
        " I'd also like to ask about ",
        " On a related note, "
    ]
    
    # Shuffle query parts to make it more natural
    random.shuffle(query_parts)
    
    # Connect the parts
    complex_query = query_parts[0]
    for i in range(1, len(query_parts)):
        complex_query += random.choice(connectors) + query_parts[i].lower()
    
    # Generate appropriate response
    response_parts = []
    
    # Add greeting
    greetings = [
        "Thank you for reaching out to GreenThumb Goods! ",
        "Hello from GreenThumb Goods! ",
        "We appreciate your interest in our products. ",
        "Thanks for your questions about our products and services. ",
        "I'd be happy to help with your inquiries. "
    ]
    response = random.choice(greetings)
    
    # Address each intent in the query
    for intent in selected_intents:
        if intent == "product_inquiry":
            response_parts.append(f"Regarding the {product1['name']}, it's priced at ${product1['price']} and {product1['description']}.")
        
        elif intent == "price_comparison":
            response_parts.append(f"When comparing the {product1['name']} (${product1['price']}) with the {product2['name']} (${product2['price']}), the price difference reflects their different features and benefits. The {product1['name']} {product1['description']}, while the {product2['name']} {product2['description']}.")
        
        elif intent == "availability_check":
            availability_responses = [
                f"The {product1['name']} is currently in stock and ready to ship within 1-2 business days.",
                f"We're temporarily out of stock on the {product1['name']}, but we expect to restock within 2 weeks. You can sign up for email notifications on the product page.",
                f"We have limited quantities of the {product1['name']} available, so we recommend placing your order soon if you're interested."
            ]
            response_parts.append(random.choice(availability_responses))
        
        elif intent == "policy_question":
            if "return" in query_parts[selected_intents.index(intent)].lower():
                response_parts.append(f"Regarding our return policy: {policies['returns']}")
            elif "shipping" in query_parts[selected_intents.index(intent)].lower():
                response_parts.append(f"About our shipping policy: {policies['shipping']}")
            elif "sustainability" in query_parts[selected_intents.index(intent)].lower():
                response_parts.append(f"Our sustainability commitment: {policies['sustainability']}")
            elif "reward" in query_parts[selected_intents.index(intent)].lower():
                response_parts.append(f"About our rewards program: {policies['rewards']}")
            elif "warranty" in query_parts[selected_intents.index(intent)].lower():
                response_parts.append(f"Regarding our warranty policy: {policies['warranty']}")
            else:
                response_parts.append(f"Regarding our policies: {policies[policy_key]}")
        
        elif intent == "care_instructions":
            care_responses = [
                f"For the {product1['name']}, we recommend regular maintenance to ensure longevity. Specific care instructions are included with your purchase, and you can also find them on our website under the product details.",
                f"The {product1['name']} requires minimal maintenance. We suggest [specific care instructions based on product type] for best results.",
                f"To keep your {product1['name']} in optimal condition, please follow the care guide included in the packaging. Generally, [basic care tip relevant to product category]."
            ]
            response_parts.append(random.choice(care_responses))
        
        elif intent == "compatibility_check":
            compatibility_responses = [
                f"The {product1['name']} is designed to work seamlessly with the {product2['name']} and other products in our {category2} line.",
                f"While the {product1['name']} and {product2['name']} can be used together, you might need [additional accessory] for optimal performance.",
                f"Yes, the {product1['name']} is fully compatible with your existing {category2} items, including the {product2['name']}."
            ]
            response_parts.append(random.choice(compatibility_responses))
        
        elif intent == "recommendation_request":
            recommendation_responses = [
                f"For someone new to {category1}, I'd recommend starting with our {product1['name']}. It's user-friendly and provides excellent value for beginners.",
                f"Based on your interest in {category1} for a small space, our {product1['name']} would be perfect as it's compact yet effective.",
                f"As a popular gift for sustainability enthusiasts, our {product1['name']} consistently receives excellent feedback. It complements existing {category2} setups beautifully."
            ]
            response_parts.append(random.choice(recommendation_responses))
        
        elif intent == "complaint":
            complaint_responses = [
                f"I'm sorry to hear about your experience with the {product1['name']}. We stand behind the quality of our products and would like to make this right. Please email our customer service team at support@greenthumbgoods.com with your order number and photos of the issue, and we'll resolve this promptly.",
                f"We apologize for the delay with your {product1['name']} order. Let me check the status for you right away. Please provide your order number, and I'll investigate the cause of the delay and provide an updated delivery estimate.",
                f"I understand your frustration with the {product1['name']}. Quality is our top priority, and we'd like to address this issue immediately. Please contact our support team at 1-800-GREEN-THUMB, and they'll arrange a replacement or refund."
            ]
            response_parts.append(random.choice(complaint_responses))
        
        elif intent == "return_process":
            return_responses = [
                f"To return your {product1['name']}, please visit our Returns Center on the website and follow the simple process: 1) Enter your order number and email, 2) Select the item(s) to return, 3) Print the prepaid return label if eligible, and 4) Drop off the package at any authorized shipping location.",
                f"Returns for the {product1['name']} can be initiated through your account on our website. Go to Order History, select the relevant order, and click 'Return Items'. You'll receive a confirmation email with further instructions.",
                f"For returning the {product1['name']}, you have 30 days from the delivery date. Original packaging is preferred but not required. Once we receive the return, refunds typically process within 5-7 business days to your original payment method."
            ]
            response_parts.append(random.choice(return_responses))
        
        elif intent == "shipping_inquiry":
            shipping_responses = [
                f"Shipping for the {product1['name']} to California would fall under our standard shipping policy: {policies['shipping']}",
                f"Yes, we offer expedited shipping for the {product1['name']} at $12.99, which typically delivers within 1-2 business days depending on your location.",
                f"All orders, including the {product1['name']}, come with tracking information that will be emailed to you once your order ships. You can also track your order through your account on our website."
            ]
            response_parts.append(random.choice(shipping_responses))
    
    # Combine response parts
    for part in response_parts:
        response += part + " "
    
    # Add closing
    closings = [
        "Is there anything else I can help you with today?",
        "Please let me know if you have any other questions!",
        "We hope this information helps with your decision.",
        "Thank you for choosing GreenThumb Goods for your sustainable living needs.",
        "We're here if you need any further assistance."
    ]
    response += random.choice(closings)
    
    return {
        "query": complex_query,
        "response": response,
        "intents": selected_intents,
        "products_mentioned": [product1['name'], product2['name']],
        "categories_mentioned": [category1, category2],
        "policies_mentioned": policy_key if "policy_question" in selected_intents else None
    }

def main():
    """Generate the dataset and save it to files."""
    print("Generating dataset of 50 complex multi-intent customer queries...")
    
    # Generate 50 complex queries and responses
    dataset = []
    for i in range(50):
        dataset.append(generate_complex_query())
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Save dataset as JSON
    json_path = os.path.join(output_dir, 'greenthumb_dataset.json')
    with open(json_path, 'w') as f:
        json.dump(dataset, f, indent=2)
    
    # Save dataset as CSV
    df = pd.DataFrame([{
        'query': item['query'],
        'response': item['response'],
        'intents': ','.join(item['intents']),
        'products_mentioned': ','.join(item['products_mentioned']),
        'categories_mentioned': ','.join(item['categories_mentioned']),
        'policies_mentioned': item['policies_mentioned'] if item['policies_mentioned'] else ''
    } for item in dataset])
    
    csv_path = os.path.join(output_dir, 'greenthumb_dataset.csv')
    df.to_csv(csv_path, index=False)
    
    print(f"Dataset created with {len(dataset)} complex queries.")
    print(f"Files saved: {json_path} and {csv_path}")
    
    # Display a few examples
    print("\nExample queries:")
    for i in range(3):
        print(f"\nQuery {i+1}: {dataset[i]['query']}")
        print(f"Response: {dataset[i]['response']}")
        print(f"Intents: {', '.join(dataset[i]['intents'])}")
    
    return dataset

if __name__ == "__main__":
    main()
