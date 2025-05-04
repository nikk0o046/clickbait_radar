"""Main analyzer for clickbait detection."""

import os
from typing import List, Dict

import yaml
from jinja2 import Template
from openai import OpenAI
from dotenv import load_dotenv

from .feed import parse_feed

# Load OpenAI API key
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Load prompt template
with open(os.path.join(os.path.dirname(__file__), 'prompts', 'clickbait.yaml')) as f:
    prompt_config = yaml.safe_load(f)
    system_prompt = prompt_config['system']
    prompt_template = Template(prompt_config['template'])


def analyze_feed(url: str, limit: int = 5) -> List[Dict]:
    """Analyze RSS feed for clickbait content."""
    entries = parse_feed(url, limit)
    results = []
    
    for entry in entries:
        prompt = prompt_template.render(
            title=entry['title'],
            content=entry['content']
        )
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        
        entry['analysis'] = response.choices[0].message.content
        results.append(entry)
    
    return results 