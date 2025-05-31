# OpenAI API Template Model

A simple chatbot template that integrates OpenAI for language models with Python based graphical user interfaces. This project provides a solid foundation for building interactive AI chatbots using either Pygame or PyQt5 frameworks.

##  Features

-  **Direct OpenAI API Integration** - Seamless connection to OpenAI language models
-  **Dual GUI Options** - Choose between Pygame or PyQt5 interfaces (Optional)
-  **Real time Conversations** - Instant AI responses with conversation history
-  **Highly Customizable** - Easy to modify and extend functionality
-  **Session Management** - Persistent conversation memory during runtime
-  **Flexible Configuration** - Adjustable AI parameters and UI settings
-  **Secure API Key Management** - Environment variable support for security (Optional)

##  Prerequisites

Before you begin, ensure you have the following installed and configured:

- **Python 3.7+** (Python 3.8+ recommended)
- **OpenAI Account** with API access
- **Valid OpenAI API Key** 
- **pip** (Python package installer)
- **Git** (for cloning the repository)

##  Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/rexzea/openai-API-Template-Model.git
cd openai-API-Template-Model
```

### Step 2: Set Up Virtual Environment (Highly Recommended)

Creating a virtual environment isolates your project dependencies:

**For Windows:**
```bash
python -m venv chatbot_env
chatbot_env\Scripts\activate
```

**For macOS/Linux:**
```bash
python3 -m venv chatbot_env
source chatbot_env/bin/activate
```

You should see `(chatbot_env)` in your terminal prompt, indicating the virtual environment is active.

### Step 3: Install Required Dependencies

**Option A: Install from requirements.txt (Recommended)**
```bash
pip install -r requirements.txt
```

**Option B: Manual Installation**
```bash
pip install openai>=1.0.0
pip install pygame>=2.1.0
pip install PyQt5>=5.15.0
pip install python-dotenv>=0.19.0
pip install requests>=2.25.0
```

### Step 4: Verify Installation

Test if all packages are installed correctly:

```bash
python -c "import openai, pygame, PyQt5, dotenv; print('All packages installed successfully!')"
```

##  OpenAI API Setup (Detailed Guide)

### Step 1: Create OpenAI Account and Get API Key

1. **Visit OpenAI Platform**
   - Go to [https://platform.openai.com/](https://platform.openai.com/)
   - Sign up for a new account or log in to existing account

2. **Navigate to API Keys**
   - Click on your profile icon (top right corner)
   - Select "View API Keys" or go to [API Keys page](https://platform.openai.com/api-keys)

3. **Create New API Key**
   - Click "Create new secret key"
   - Give it a descriptive name ("Chatbot Project")
   - Copy the generated API key immediately (you wont see it again!!!)

4. **Set Up Billing (Important!)**
   - Go to [Billing settings](https://platform.openai.com/account/billing)
   - Add a payment method
   - Set usage limits to avoid unexpected charges

### Step 2: Configure API Key in Your Project

**Method 1: Environment Variables (Recommended for Security)**

1. Create a `.env` file in your project root directory:
```bash
touch .env  # On Windows: type nul > .env
```

2. Add your API key to the `.env` file:
```env
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_ORG_ID=your-org-id-here  # Optional, if you have one
```

3. The application will automatically load this file using pythondotenv.

**Method 2: System Environment Variables**

**Windows (Command Prompt):**
```cmd
setx OPENAI_API_KEY "sk-your-actual-api-key-here"
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="sk-your-actual-api-key-here"
```

**macOS/Linux:**
```bash
export OPENAI_API_KEY="sk-your-actual-api-key-here"
# Add to ~/.bashrc or ~/.zshrc for persistence
echo 'export OPENAI_API_KEY="sk-your-actual-api-key-here"' >> ~/.bashrc
```

**Method 3: Direct Configuration (Not Recommended for Production)**

Edit the `config.py` file:
```python
# config.py
OPENAI_API_KEY = "sk-your-actual-api-key-here"  # Replace with your key
```

** Security Warning:** Never commit your API key to version control. Always use `.env` files or environment variables for production applications.

##  Running the Application

### Option 1: Pygame Version (Lightweight, Game-like Interface)

```bash
python main_pygame.py
```

**Features of Pygame Version:**
- Fast rendering and smooth animations
- Customizable themes and colors
- Ideal for simple, game-like interfaces
- Lower system resource usage

### Option 2: PyQt5 Version (Professional Desktop Interface)

```bash
python main_pyqt.py
```

**Features of PyQt5 Version:**
- Native desktop application look and feel
- Advanced UI components (menus, toolbars, dialogs)
- Better text rendering and input handling
- More professional appearance

### Command Line Arguments (Advanced)

You can pass configuration options directly:

```bash
python main_pygame.py --model gpt-4 --temperature 0.8 --max-tokens 200
python main_pyqt.py --debug --verbose
```



## Configuration Options

### Basic Configuration (`config.py`)

```python
# OpenAI Model Settings
MODEL = "gpt-3.5-turbo"        # Options: gpt-3.5-turbo, gpt-4, gpt-4-turbo
MAX_TOKENS = 150               # Maximum response length
TEMPERATURE = 0.7              # Creativity level (0.0-2.0)
TOP_P = 1.0                    # Nucleus sampling parameter
FREQUENCY_PENALTY = 0.0        # Reduce repetition (-2.0 to 2.0)
PRESENCE_PENALTY = 0.0         # Encourage new topics (-2.0 to 2.0)

# UI Settings
WINDOW_WIDTH = 800             # Application window width
WINDOW_HEIGHT = 600            # Application window height
THEME = "dark"                 # UI theme: "dark" or "light"
FONT_SIZE = 12                 # Text font size

# Conversation Settings
MAX_CONVERSATION_HISTORY = 10  # Number of messages to remember
SAVE_CONVERSATIONS = True      # Save chat history to file
AUTO_SCROLL = True             # Auto-scroll to latest message
```

### Advanced Configuration (For you)

**Custom System Prompts:**
```python
# In openai_client.py
SYSTEM_PROMPTS = {
    "default": "You are a helpful AI assistant.",
    "creative": "You are a creative writing assistant.",
    "technical": "You are a technical support specialist.",
    "friendly": "You are a friendly and casual conversation partner."
}
```

**API Rate Limiting:**
```python
# In config.py
API_RATE_LIMIT = 60            # Requests per minute
REQUEST_TIMEOUT = 30           # Seconds before timeout
RETRY_ATTEMPTS = 3             # Number of retry attempts
```

## Usage Tutorial

### Basic Usage

1. **Launch the Application**
   ```bash
   python main_pygame.py  # or main_pyqt.py
   ```

2. **Start Chatting**
   - Type your message in the input field
   - Press Enter or click the "Send" button
   - Wait for AI response (usually 2-5 seconds)

3. **View Conversation History**
   - Scroll up to see previous messages
   - Use arrow keys to navigate through input history

### Advanced Features (For you)

**Conversation Commands:**
- `/clear` - Clear conversation history
- `/save` - Save current conversation to file
- `/load` - Load previous conversation
- `/model gpt-4` - Switch AI model mid-conversation
- `/temp 0.9` - Adjust temperature (creativity)
- `/help` - Show available commands

**Keyboard Shortcuts:**
- `Ctrl+Enter` - Send message
- `Ctrl+L` - Clear conversation
- `Ctrl+S` - Save conversation
- `Ctrl+Q` - Quit application
- `Up/Down` - Navigate input history

##  Customization Guide

### Modifying AI Personality

Edit the system message in `chatbot/openai_client.py`:

```python
def create_system_message(personality="default"):
    personalities = {
        "default": "You are a helpful AI assistant.",
        "poet": "You are a creative poet who speaks in verse.",
        "scientist": "You are a knowledgeable scientist who explains complex topics simply.",
        "comedian": "You are a witty comedian who adds humor to conversations."
    }
    
    return {
        "role": "system",
        "content": personalities.get(personality, personalities["default"])
    }
```

### Customizing the UI

**Pygame Customization (`gui_pygame.py`):**
```python
# Colors
BACKGROUND_COLOR = (30, 30, 30)      # Dqrk gray background
TEXT_COLOR = (255, 255, 255)         # White text
USER_MESSAGE_COLOR = (0, 120, 215)   # Blue for user messages
AI_MESSAGE_COLOR = (80, 80, 80)      # Gray for AI messages

# Fonts
FONT_FAMILY = "Arial"
FONT_SIZE = 14
```

**PyQt5 Customization (`gui_pyqt.py`):**
```python
# Stylesheet
DARK_THEME = """
QMainWindow {
    background-color: #2b2b2b;
    color: #ffffff;
}
QTextEdit {
    background-color: #1e1e1e;
    border: 1px solid #404040;
    border-radius: 5px;
}
"""
```

### Adding New Features

**Example: Adding Voice Input**

1. Install speech recognition:
```bash
pip install SpeechRecognition pyaudio
```

2. Add to your GUI class:
```python
import speech_recognition as sr

def voice_input(self):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            self.input_field.setText(text)
        except sr.UnknownValueError:
            print("Could not understand audio")
```

##  Complete Requirements

Create or update your `requirements.txt`:

```txt
# Core dependencies
openai>=1.0.0
python-dotenv>=0.19.0
requests>=2.25.0

# GUI frameworks
pygame>=2.1.0
PyQt5>=5.15.0

# Optional dependencies
colorama>=0.4.4          # Colored terminal output
tiktoken>=0.3.0          # Token counting for OpenAI
pydantic>=1.8.0          # Data validation
loguru>=0.6.0            # Advanced logging

# Development dependencies (optional)
pytest>=6.0.0            # Testing framework
black>=21.0.0            # Code formatting
flake8>=3.8.0            # Code linting
```

##  Comprehensive Troubleshooting

### Common Installation Issues

**Issue: "No module named 'openai'"**
```bash
# Solution: Reinstall OpenAI package
pip uninstall openai
pip install openai>=1.0.0
```

**Issue: "Microsoft Visual C++ 14.0 is required" (Windows)**
```bash
# Solution: Install Visual Studio Build Tools
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

**Issue: "pygame not found" on Linux**
```bash
# Solution: Install system dependencies
sudo apt-get update
sudo apt-get install python3-pygame
# Or compile from source:
sudo apt-get install python3-dev libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev
```

### API-Related Issues

**Issue: "Authentication Error - Invalid API Key"**
- Verify your API key is correct and active
- Check if your API key has expired
- Ensure no extra spaces or characters in the key
- Test with a simple API call:
```python
import openai
client = openai.OpenAI(api_key="your-key-here")
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=10
)
print(response.choices[0].message.content)
```

**Issue: "Rate limit exceeded"**
- You've hit OpenAI's usage limits
- Wait for the limit to reset (usually 1 minute)
- Implement rate limiting in your code:
```python
import time
from openai import RateLimitError

def make_api_call_with_retry(client, **kwargs):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(**kwargs)
        except RateLimitError:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise
```

**Issue: "Insufficient quota"**
- Your OpenAI account has run out of credits
- Add more credits to your account
- Check your usage at https://platform.openai.com/usage

### Runtime Issues

**Issue: Application freezes during API calls**
```python
# Solution: Implement threading
import threading
from PyQt5.QtCore import QThread, pyqtSignal

class APIThread(QThread):
    response_ready = pyqtSignal(str)
    
    def __init__(self, message):
        super().__init__()
        self.message = message
    
    def run(self):
        # Make API call in separate thread
        response = self.openai_client.get_response(self.message)
        self.response_ready.emit(response)
```

**Issue: Memory usage grows over time**
```python
# Solution: Limit conversation history
class ConversationManager:
    def __init__(self, max_history=50):
        self.messages = []
        self.max_history = max_history
    
    def add_message(self, message):
        self.messages.append(message)
        if len(self.messages) > self.max_history:
            self.messages = self.messages[-self.max_history:]
```

##  Cost Management

### Understanding OpenAI Pricing (as of 2024)

**GPT-3.5-turbo:**
- Input: $0.0005 per 1K tokens
- Output: $0.0015 per 1K tokens

**GPT-4:**
- Input: $0.01 per 1K tokens  
- Output: $0.03 per 1K tokens

**GPT-4-turbo:**
- Input: $0.01 per 1K tokens
- Output: $0.03 per 1K tokens

### Cost Estimation Tool

```python
def estimate_cost(prompt, response, model="gpt-3.5-turbo"):
    import tiktoken
    
    encoding = tiktoken.encoding_for_model(model)
    prompt_tokens = len(encoding.encode(prompt))
    response_tokens = len(encoding.encode(response))
    
    rates = {
        "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
        "gpt-4": {"input": 0.01, "output": 0.03},
        "gpt-4-turbo": {"input": 0.01, "output": 0.03}
    }
    
    rate = rates.get(model, rates["gpt-3.5-turbo"])
    cost = (prompt_tokens * rate["input"] + response_tokens * rate["output"]) / 1000
    
    return {
        "prompt_tokens": prompt_tokens,
        "response_tokens": response_tokens,
        "total_tokens": prompt_tokens + response_tokens,
        "estimated_cost": cost
    }
```

### Usage Monitoring

```python
class UsageTracker:
    def __init__(self):
        self.total_tokens = 0
        self.total_cost = 0.0
        self.requests = 0
    
    def log_usage(self, prompt_tokens, response_tokens, model):
        self.total_tokens += prompt_tokens + response_tokens
        self.requests += 1
        cost = self.calculate_cost(prompt_tokens, response_tokens, model)
        self.total_cost += cost
        
        print(f"Request #{self.requests}")
        print(f"Tokens used: {prompt_tokens + response_tokens}")
        print(f"Cost: ${cost:.4f}")
        print(f"Total cost: ${self.total_cost:.4f}")
```

##  Testing Your Installation

Create a test script (`test_setup.py`):

```python
#!/usr/bin/env python3
"""
Test script to verify OpenAI API Template Model setup
"""

import os
import sys
from dotenv import load_dotenv

def test_imports():
    """Test if all required packages can be imported"""
    try:
        import openai
        import pygame
        import PyQt5
        print("All packages imported successfully")
        return True
    except ImportError as e:
        print(f"Import error: {e}")
        return False

def test_api_key():
    """Test if OpenAI API key is configured"""
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key and api_key.startswith('sk-'):
        print("API key found and properly formatted")
        return True
    else:
        print("API key not found or improperly formatted")
        return False

def test_api_connection():
    """Test actual connection to OpenAI API"""
    try:
        from openai import OpenAI
        client = OpenAI()
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'API test successful'"}],
            max_tokens=10
        )
        
        if response.choices[0].message.content:
            print("API connection successful")
            print(f"Response: {response.choices[0].message.content}")
            return True
    except Exception as e:
        print(f"API connection failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing OpenAI API Template Model Setup...")
    print("-" * 50)
    
    tests = [test_imports, test_api_key, test_api_connection]
    results = [test() for test in tests]
    
    print("-" * 50)
    if all(results):
        print("All tests passed! Your setup is ready.")
    else:
        print("Some tests failed. Please check the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

Run the test:
```bash
python test_setup.py
```

## Contributing Guidelines

We welcome contributions! Here's how to get started:

### Development Setup

1. **Fork and Clone**
```bash
git clone https://github.com/rexzea/openai-API-Template-Model.git
cd openai-API-Template-Model
git remote add upstream https://github.com/original/openai-API-Template-Model.git
```

2. **Create Development Environment**
```bash
python -m venv dev_env
source dev_env/bin/activate  # On Windows: dev_env\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

3. **Install Pre-commit Hooks**
```bash
pip install pre-commit
pre-commit install
```

### Code Style

We use Black for code formatting and flake8 for linting:

```bash
# Format code
black chatbot/

# Check linting
flake8 chatbot/

# Run tests
pytest tests/
```

### Submitting Changes

1. Create a feature branch:
```bash
git checkout -b feature/new-feature
```

2. Make your changes and test them

3. Commit with a descriptive message:
```bash
git commit -m "Add new feature that does X"
```

4. Push and create a Pull Request:
```bash
git push origin feature/new-feature
```

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

##  Support and Community

### Getting Help

1. **GitHub Issues**: [Create an issue](https://github.com/rexzea/openai-API-Template-Model/issues) for bugs or feature requests

2. **Discussions**: Join our [GitHub Discussions](https://github.com/rexzea/openai-API-Template-Model/discussions) for questions and community support

3. **Email Support**: futzfarry@gmail.com



## Acknowledgments

**Special Thanks:**
- [OpenAI](https://openai.com/) for providing the incredible GPT models
- [Pygame](https://pygame.org/) team for the excellent game development framework  
- [Riverbank Computing](https://riverbankcomputing.com/) for PyQt5
- The Python community for continuous support and inspiration

**Contributors:**
- Rexzea - Project Creator


---

## Quick Start Summary

For the impatient developers:

```bash
# 1. Clone and setup
git clone https://github.com/rexzea/openai-API-Template-Model.git
cd openai-API-Template-Model
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure API key
echo "OPENAI_API_KEY=sk-your-key-here" > .env

# 4. Run the app
python main_pygame.py  # or main_pyqt.py

# 5. Start chatting!
```

**Happy Coding and Welcome to the Future of AI Chatbots!** 
