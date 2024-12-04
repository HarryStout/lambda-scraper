import json
import logging
import newspaper

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def scraper():
    url = 'https://www.nytimes.com/live/2021/10/25/us/biden-spending-bill-negotiations'
    
    article = newspaper.Article(url=url, language='en')
    article.download()
    article.parse()

    article ={
        "title": str(article.title),
        "text": str(article.text),
        "authors": article.authors,
        "published_date": str(article.publish_date),
        "top_image": str(article.top_image),
        "videos": article.movies,
        "keywords": article.keywords,
        "summary": str(article.summary)
    }

    logger.info(article["title"] \
         + "\n\t\t" + article["published_date"] \
         + "\n\n"\
         + "\n" + article["text"]\
         + "\n\n")
    
def scraper_handler(event, context):
    if event['Success'] == True:
        logger.info("All is OK. Starting Scraper.")
        scraper()
        return {
            'statusCode': 200,
            'body': event
        }
    else:
        raise Exception('Success is False', event)