# Pragyan-AI-Summarization

A powerful AI-driven text summarization tool built with JavaScript and Python backends. This project leverages artificial intelligence to automatically generate concise summaries of lengthy texts while preserving key information.

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **AI-Powered Summarization**: Intelligent text summarization using advanced NLP techniques
- **Multiple Input Formats**: Support for various text sources
- **Configurable Summary Length**: Control the length and detail level of generated summaries
- **Fast Processing**: Optimized for quick summarization of large texts
- **Easy Integration**: Simple API for easy integration into other projects

## 🛠️ Technology Stack

- **Frontend/Backend**: JavaScript (88.1%)
- **Backend Processing**: Python (11.9%)
- **AI/ML Framework**: NLP-based summarization engine

## 📦 Installation

### Prerequisites

- Node.js (v14 or higher)
- Python (v3.7 or higher)
- npm or yarn

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nikita-Parjane27/Pragyan-AI-Summarization.git
   cd Pragyan-AI-Summarization
   ```

2. **Install JavaScript dependencies**
   ```bash
   npm install
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## 🚀 Usage

### Basic Summarization

```javascript
// JavaScript example
const summarizer = require('./summarizer');

const text = "Your long text here...";
const summary = await summarizer.summarize(text);
console.log(summary);
```

### With Custom Parameters

```javascript
const summary = await summarizer.summarize(text, {
  length: 'short',      // 'short', 'medium', 'long'
  maxSentences: 5,
  language: 'en'
});
```

### Python Backend

```python
from summarizer import Summarizer

summarizer = Summarizer()
summary = summarizer.summarize(text, length='medium')
print(summary)
```

## 📁 Project Structure

```
Pragyan-AI-Summarization/
├── src/
│   ├── js/                 # JavaScript source files
│   │   ├── api/           # API endpoints
│   │   ├── models/        # Data models
│   │   └── utils/         # Utility functions
│   ├── python/            # Python source files
│   │   ├── summarizer/    # Core summarization module
│   │   ├── nlp/           # NLP processing
│   │   └── utils/         # Utility functions
├── tests/                 # Test files
├── docs/                  # Documentation
├── package.json          # Node.js dependencies
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🧪 Testing

Run tests with:

```bash
# JavaScript tests
npm test

# Python tests
python -m pytest tests/
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Nikita Parjane**
- GitHub: [@Nikita-Parjane27](https://github.com/Nikita-Parjane27)

## 📞 Support

For support, please open an issue on the [GitHub Issues](https://github.com/Nikita-Parjane27/Pragyan-AI-Summarization/issues) page.

---

**Note**: This is an AI summarization project. Ensure you have the necessary dependencies installed and configured before running the application.
