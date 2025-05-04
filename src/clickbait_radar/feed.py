"""Simple RSS feed parser."""

import feedparser
from datetime import datetime
from typing import List, Dict


def parse_feed(url: str, limit: int = 5) -> List[Dict]:
    """Parse RSS feed and return entries sorted by date (newest first)."""
    feed = feedparser.parse(url)
    entries = []
    
    for entry in feed.entries:
        entries.append({
            'title': entry.title,
            'link': entry.link,
            'content': entry.summary if hasattr(entry, 'summary') else '',
            'date': entry.published_parsed if hasattr(entry, 'published_parsed') else None
        })
    
    # Sort by date (newest first) and limit
    entries.sort(key=lambda x: x['date'] if x['date'] else datetime.min, reverse=True)
    return entries[:limit] 