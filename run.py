"""
Main runner script for the GreenThumb Goods AI Assistant project.
This script provides a menu to run different sections of the project.
"""

import os
import sys
import subprocess
import time

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the project header."""
    clear_screen()
    print("=" * 80)
    print("                   GREENTHUMB GOODS AI ASSISTANT")
    print("                   AI Engineer Take-Home Assessment")
    print("=" * 80)
    print("\nThis project demonstrates how to handle complex multi-intent customer queries")
    print("using OpenAI's API with different prompt engineering strategies.\n")
    
    # Check if API key is set
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from config import OPENAI_API_KEY
    
    if OPENAI_API_KEY == "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":
        print("⚠️  WARNING: OpenAI API key not set. Please edit config.py to add your API key.")
        print("             Without a valid API key, the OpenAI API calls will not work.\n")

def print_menu():
    """Print the main menu options."""
    print("\nPlease select an option:")
    print("1. Generate Dataset (Section 1)")
    print("2. Run Streamlit Interface (Section 2)")
    print("3. Test Prompt Engineering Strategies (Section 3)")
    print("4. View Summary Report (Section 4)")
    print("5. View Google Analytics Integration (Section 5)")
    print("6. Exit")
    
    return input("\nEnter your choice (1-6): ")

def run_dataset_generation():
    """Run the dataset generation script."""
    print("\nRunning dataset generation script...\n")
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "section1_dataset.py")
    subprocess.run([sys.executable, script_path])
    input("\nPress Enter to continue...")

def run_streamlit_interface():
    """Run the Streamlit interface."""
    print("\nStarting Streamlit interface...\n")
    print("The Streamlit interface will open in a new browser window.")
    print("Press Ctrl+C in this terminal when you want to stop the Streamlit server.\n")
    
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "section2_streamlit_app.py")
    
    try:
        subprocess.run(["streamlit", "run", script_path])
    except FileNotFoundError:
        print("\n⚠️  Streamlit not found. Installing Streamlit...")
        subprocess.run([sys.executable, "-m", "pip", "install", "streamlit"])
        time.sleep(2)
        print("\nRetrying Streamlit launch...")
        subprocess.run(["streamlit", "run", script_path])
    
    input("\nPress Enter to continue...")

def run_prompt_engineering():
    """Run the prompt engineering script."""
    print("\nTesting prompt engineering strategies...\n")
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "section3_prompt_engineering.py")
    subprocess.run([sys.executable, script_path])
    input("\nPress Enter to continue...")

def view_summary_report():
    """View the summary report."""
    print("\nViewing Summary Report (Section 4)...\n")
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "section4_summary_report.md")
    
    try:
        with open(report_path, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"⚠️  Report file not found: {report_path}")
    
    input("\nPress Enter to continue...")

def view_ga_integration():
    """View the Google Analytics integration document."""
    print("\nViewing Google Analytics Integration (Section 5)...\n")
    ga_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "section5_google_analytics.md")
    
    try:
        with open(ga_path, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"⚠️  Google Analytics document not found: {ga_path}")
    
    input("\nPress Enter to continue...")

def main():
    """Main function to run the project."""
    while True:
        print_header()
        choice = print_menu()
        
        if choice == '1':
            run_dataset_generation()
        elif choice == '2':
            run_streamlit_interface()
        elif choice == '3':
            run_prompt_engineering()
        elif choice == '4':
            view_summary_report()
        elif choice == '5':
            view_ga_integration()
        elif choice == '6':
            print("\nExiting program. Thank you for using the GreenThumb Goods AI Assistant!\n")
            break
        else:
            print("\n⚠️  Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
