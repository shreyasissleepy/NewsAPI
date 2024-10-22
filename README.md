# 🌍 NewsAPI - Fetch News from Multiple Sources with Ease 📰

![PyPI](https://img.shields.io/pypi/v/NewsAPI?style=flat-square)
![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg?style=flat-square)
![Build Status](https://img.shields.io/github/actions/workflow/status/shreyasissleepy/NewsAPI/ci.yml?branch=main&style=flat-square)

## 🔥 Overview

**NewsAPI** is a Python package that allows you to easily fetch the latest news articles from popular sources like **BBC**, **ABP News**, and **India Today**. Whether you're building a news aggregator or just looking for easy access to headlines, NewsAPI provides a simple interface to gather data with minimal setup.

### Features:
- 🌐 Fetch news from **BBC**, **ABP News**, and **India Today**.
- 🔍 Optional keyword-based news search for bbc (e.g., "technology", "politics").
- 🛠️ Simple API interface.
- 📦 Lightweight and easy to integrate into your project.

---

## 🚀 Usage

Using **NewsAPI** to fetch news is super simple. Here’s a quick guide:

### Fetch the Latest News from BBC:

```python
from wrapper_news_api import NewsAPI

# Create an instance of the NewsAPI class
news_api = NewsAPI()

# Fetch news from BBC
bbc_news = news_api.bbc() #bbc(),abp(),india_today()

for article in bbc_news:
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}")
    print("---")
```

## 📦 Installation

Install the latest version from [PyPI](https://pypi.org/project/NewsAPI/):

```bash
pip install wrapper_news_api
