"""
Python Practice Plan
Author: GitHub Copilot
Purpose: A daily practice guide for learning Python and full-stack development.
"""

paths = [
    {
        "name": "Python Fundamentals",
        "topics": [
            "variables, data types, operators",
            "control flow: if, for, while",
            "functions and modules",
            "data structures: list, tuple, dict, set",
            "file I/O and exceptions"
        ],
        "goal": "Build strong basics for all Python work."
    },
    {
        "name": "Object-Oriented Programming",
        "topics": [
            "classes and objects",
            "methods and attributes",
            "inheritance and polymorphism",
            "encapsulation and special methods"
        ],
        "goal": "Design reusable code and understand common Python patterns."
    },
    {
        "name": "Web Development",
        "topics": [
            "Flask or Django basics",
            "HTTP methods and routing",
            "templates and forms",
            "REST APIs and JSON",
            "basic frontend integration"
        ],
        "goal": "Create web applications and learn backend/frontend flow."
    },
    {
        "name": "Frontend and JavaScript Basics",
        "topics": [
            "HTML/CSS fundamentals",
            "JavaScript variables and functions",
            "DOM manipulation",
            "fetch/AJAX for API calls",
            "basic React concepts (optional)"
        ],
        "goal": "Understand the browser side to build full-stack apps."
    },
    {
        "name": "Data and Automation",
        "topics": [
            "pandas and NumPy basics",
            "data visualization with Matplotlib/Seaborn",
            "web scraping with BeautifulSoup",
            "automation with scripts and schedulers"
        ],
        "goal": "Use Python to process data and automate repetitive tasks."
    },
    {
        "name": "Version Control and Deployment",
        "topics": [
            "Git and GitHub workflows",
            "virtual environments",
            "deploying web apps (Heroku, Vercel, or similar)",
            "basic CI/CD concepts"
        ],
        "goal": "Keep code organized and learn how to publish projects."
    }
]

practice_plan = {
    "week_1": {
        "focus": "Python Fundamentals",
        "daily": [
            "Day 1: variables, types, and basic operations",
            "Day 2: conditions and loops",
            "Day 3: functions and return values",
            "Day 4: lists, tuples, and sets",
            "Day 5: dictionaries and nested structures",
            "Day 6: file reading/writing",
            "Day 7: small project - calculator or note logger"
        ]
    },
    "week_2": {
        "focus": "OOP and Modules",
        "daily": [
            "Day 1: classes and object creation",
            "Day 2: methods, attributes, and constructors",
            "Day 3: inheritance and composition",
            "Day 4: special methods and dunder methods",
            "Day 5: modules and package structure",
            "Day 6: build a contact manager class project",
            "Day 7: review and refactor code"
        ]
    },
    "week_3": {
        "focus": "Web Development Basics",
        "daily": [
            "Day 1: install Flask and build a hello world app",
            "Day 2: routes, templates, and forms",
            "Day 3: build a simple CRUD app",
            "Day 4: learn JSON and API responses",
            "Day 5: add frontend form handling",
            "Day 6: deploy a simple app locally",
            "Day 7: review and document the project"
        ]
    },
    "week_4": {
        "focus": "Frontend and Integration",
        "daily": [
            "Day 1: HTML structure and CSS basics",
            "Day 2: JavaScript variables and functions",
            "Day 3: DOM manipulation and events",
            "Day 4: fetch API and AJAX requests",
            "Day 5: connect frontend to the Flask backend",
            "Day 6: build a small full-stack page",
            "Day 7: review, test, and improve UI"
        ]
    }
}

practice_questions = [
    "Write a function that reverses a string without using built-in reverse methods.",
    "Create a program to count word frequency in a text file.",
    "Build a number guessing game using while loops and random numbers.",
    "Write a class for a student record with methods to calculate average marks.",
    "Create a Flask app that accepts form input and displays the result.",
    "Build a script to scrape headlines from a news website using BeautifulSoup.",
    "Write a program that reads a CSV file and summarizes the data.",
    "Make a REST API endpoint that returns JSON data and accepts POST requests.",
    "Use Git to initialize a repository, commit changes, and push to GitHub.",
    "Create a simple HTML page that calls an API endpoint and shows data in the browser."
]

advanced_questions = [
    "Implement a decorator that logs function execution time.",
    "Write a generator function to produce an infinite sequence of prime numbers.",
    "Build a command-line tool that parses arguments and processes files.",
    "Create a custom exception class and use it in a validation flow.",
    "Write a threaded script that downloads files concurrently.",
    "Develop a small Flask app with user authentication.",
    "Create a data analysis script using pandas and visualize results with Matplotlib.",
    "Build a REST API client that consumes an external JSON API and displays results.",
    "Write unit tests for a set of functions using pytest or unittest.",
    "Refactor an existing script to use classes, modules, and better structure."
]

beginner_projects = [
    {
        "name": "Daily Python Tracker",
        "description": "Log your daily learning, topics covered, and questions in a simple file.",
        "milestones": [
            "Create the tracker file and write the first entry",
            "Track 7 days of practice",
            "Review and summarize the first week"
        ]
    },
    {
        "name": "Calculator App",
        "description": "Build a console calculator that performs arithmetic and handles invalid input.",
        "milestones": [
            "Implement add, subtract, multiply, divide",
            "Add input validation and error handling",
            "Refactor using functions or classes"
        ]
    },
    {
        "name": "Contact Manager",
        "description": "Create a small program to add, update, delete, and list contacts.",
        "milestones": [
            "Store contacts in a list or dictionary",
            "Add search and edit features",
            "Save and load contacts from a file"
        ]
    }
]

weekly_checklist = {
    "week_1": [
        "Review basic Python syntax every day",
        "Solve one beginner coding problem",
        "Write a short summary of what you learned",
        "Commit your code to Git at least once"
    ],
    "week_2": [
        "Practice classes and objects with a simple project",
        "Build or refactor a small module",
        "Write tests for one function or class",
        "Review your code and improve readability"
    ],
    "week_3": [
        "Create a basic Flask app and run it locally",
        "Add a route and render a template",
        "Use JSON responses in one endpoint",
        "Document your app and save notes"
    ],
    "week_4": [
        "Learn HTML/CSS structure and JavaScript basics",
        "Connect frontend code to your backend",
        "Build a small full-stack page",
        "Deploy or share your project for feedback"
    ]
}

web_app_learning_path = {
    "name": "Small Web App Learning Path",
    "steps": [
        "Choose a simple idea: todo app, notes app, or budget tracker",
        "Build backend routes using Flask and return HTML or JSON",
        "Create a frontend page with HTML and CSS",
        "Use JavaScript fetch() to call your backend API",
        "Add data persistence using files or a database",
        "Test the app, fix bugs, and document the project"
    ],
    "goal": "Learn full-stack development with a practical app you can extend."
}

weekly_checklist = {
    "week_1": [
        "Review basic Python syntax every day",
        "Solve one beginner coding problem",
        "Write a short summary of what you learned",
        "Commit your code to Git at least once"
    ],
    "week_2": [
        "Practice classes and objects with a simple project",
        "Build or refactor a small module",
        "Write tests for one function or class",
        "Review your code and improve readability"
    ],
    "week_3": [
        "Create a basic Flask app and run it locally",
        "Add a route and render a template",
        "Use JSON responses in one endpoint",
        "Document your app and save notes"
    ],
    "week_4": [
        "Learn HTML/CSS structure and JavaScript basics",
        "Connect frontend code to your backend",
        "Build a small full-stack page",
        "Deploy or share your project for feedback"
    ]
}

daily_itinerary = {
    "Week 1": [
        "Day 1: fundamentals_practice.ipynb - variables and data types",
        "Day 2: fundamentals_practice.ipynb - conditions and loops",
        "Day 3: fundamentals_practice.ipynb - functions and text processing",
        "Day 4: fundamentals_practice.ipynb - lists, tuples, sets",
        "Day 5: fundamentals_practice.ipynb - dictionaries and file I/O",
        "Day 6: fundamentals_practice.ipynb - practical exercises",
        "Day 7: fundamentals_practice.ipynb - review and practice"
    ],
    "Week 2": [
        "Day 1: oop_practice.ipynb - classes and objects",
        "Day 2: oop_practice.ipynb - methods and attributes",
        "Day 3: oop_practice.ipynb - inheritance and polymorphism",
        "Day 4: oop_practice.ipynb - special methods",
        "Day 5: oop_practice.ipynb - practice projects",
        "Day 6: oop_practice.ipynb - refactor and test code",
        "Day 7: oop_practice.ipynb - review and improve"
    ],
    "Week 3": [
        "Day 1: web_development_practice.ipynb - Flask hello world",
        "Day 2: web_development_practice.ipynb - routing and JSON",
        "Day 3: web_development_practice.ipynb - forms and responses",
        "Day 4: frontend_practice.ipynb - HTML structure",
        "Day 5: frontend_practice.ipynb - CSS styling",
        "Day 6: frontend_practice.ipynb - JavaScript fetch examples",
        "Day 7: frontend_practice.ipynb - integrate backend and frontend"
    ],
    "Week 4": [
        "Day 1: data_automation_practice.ipynb - pandas basics",
        "Day 2: data_automation_practice.ipynb - summarize and visualize data",
        "Day 3: data_automation_practice.ipynb - simple parsing and automation",
        "Day 4: web_development_practice.ipynb - API improvements",
        "Day 5: frontend_practice.ipynb - UI improvements",
        "Day 6: data_automation_practice.ipynb - practice projects",
        "Day 7: Review all notebooks and prepare next projects"
    ]
}


def show_paths():
    print("\nSuggested learning paths:")
    for path in paths:
        print(f"\n- {path['name']}")
        print(f"  Goal: {path['goal']}")
        for topic in path['topics']:
            print(f"    * {topic}")


def show_plan():
    print("\n30-day practice plan:")
    for week_name, week in practice_plan.items():
        print(f"\n{week_name.replace('_', ' ').title()}: {week['focus']}")
        for day in week['daily']:
            print(f"  - {day}")


def show_questions():
    print("\nPractice questions and exercises:")
    for idx, question in enumerate(practice_questions, start=1):
        print(f"  {idx}. {question}")


def show_advanced_questions():
    print("\nAdvanced Python questions:")
    for idx, question in enumerate(advanced_questions, start=1):
        print(f"  {idx}. {question}")


def show_beginner_projects():
    print("\nBeginner project tracker:")
    for project in beginner_projects:
        print(f"\n- {project['name']}")
        print(f"  Description: {project['description']}")
        print("  Milestones:")
        for milestone in project['milestones']:
            print(f"    * {milestone}")


def show_checklist():
    print("\nWeekly checklist:")
    for week_name, tasks in weekly_checklist.items():
        print(f"\n{week_name.replace('_', ' ').title()}")
        for task in tasks:
            print(f"  - {task}")


def show_web_app_path():
    print(f"\nWeb app learning path: {web_app_learning_path['name']}")
    print(f"  Goal: {web_app_learning_path['goal']}")
    for step in web_app_learning_path['steps']:
        print(f"  - {step}")


def show_itinerary():
    print("\nDaily notebook itinerary:")
    for week_name, days in daily_itinerary.items():
        print(f"\n{week_name}")
        for day in days:
            print(f"  - {day}")


def main():
    print("Python Practice Plan for Full-Stack Learning")
    show_paths()
    show_plan()
    show_questions()
    show_advanced_questions()
    show_beginner_projects()
    show_checklist()
    show_web_app_path()
    show_itinerary()


if __name__ == "__main__":
    main()
