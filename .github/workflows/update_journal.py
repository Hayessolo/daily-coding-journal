import os 
from datetime import datetime
import random 

def get_daily_topic():
    topics = [
        "Data Structures", "Algorithms", "Design Patterns",
                "Testing", "DevOps", "Web Security",
                        "Performance Optimization", "Code Review",
                                "Documentation", "API Design"
    ]
    return random.choice(topics)

def create_daily_entry():
    today = datetime.now().strftime("+%Y-%m-%d ")
    topic = get_daily_topic()
    # Create templates directory if it doesn't exist
    os.makedirs("daily_progress", exist_ok=True)

    # Create or update the daily learning file
    entry_path = f"daily_progress/{today}.md"
    with open(entry_path, "w") as f:
        f.write(f"# Daily Learning Progress - {today}\n\n")
        f.write(f"## Focus Area: {topic}\n\n")
        f.write("### Today's Goals:\n")
        f.write("1. Research and understand core concepts\n")
        f.write("2. Complete practice exercises\n")
        f.write("3. Document key learnings\n\n")
        f.write("### Resources Used:\n")
        f.write("- Documentation\n")
        f.write("- Practice problems\n")
        f.write("- Code examples\n\n")
        f.write("### Progress Made:\n")
        f.write("- Initial research completed\n")
        f.write("- Basic concepts documented\n")
        f.write("- Practice exercises attempted\n\n")

    # Update the main README
    update_readme(today, topic)

def update_readme(date, topic):
    """Update the main README with the latest progress."""
    if not os.path.exists("README.md"):
        with open("README.md", "w") as f:
            f.write("# Learning Progress Tracker\n\n")
            f.write("This repository tracks my daily learning progress and coding practice.\n\n")
            f.write("## Recent Updates\n\n")
    
    with open("README.md", "r") as f:
        content = f.readlines()
    
    # Add new entry after the header
    insert_index = next((i for i, line in enumerate(content) if "## Recent Updates" in line), -1) + 1
    content.insert(insert_index, f"- {date}: Studied {topic}\n")
    
    with open("README.md", "w") as f:
        f.writelines(content)

if __name__ == "__main__":
    create_daily_entry()