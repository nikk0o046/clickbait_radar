# Clickbait Radar

A tool to analyze RSS feeds for clickbait content using OpenAI's GPT-4.

## Features

- Fetch and parse RSS feeds
- Analyze article titles for clickbait elements
- Score articles based on clickbait indicators
- Support for multiple RSS feeds
- Logging for monitoring and debugging

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/clickbait-radar.git
cd clickbait-radar
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package:
```bash
pip install -e .
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key_here
```

## Usage

The package provides a `RSSAnalyzer` class that can be used to fetch and analyze RSS feeds:

```python
from clickbait_radar.analyzer import RSSAnalyzer

analyzer = RSSAnalyzer()
entries = analyzer.fetch_feed("https://www.hs.fi/rss/suomi.xml", limit=5)

for entry in entries:
    analysis = analyzer.analyze_clickbait(entry["title"], entry["summary"] or "")
    # Process the analysis results as needed
```

## Logging

The package uses Python's built-in logging module with the following configuration:
- Log level: INFO
- Format: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`

## License

MIT License - see LICENSE file for details