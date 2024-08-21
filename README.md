Task no 2: 
The code is designed to help us gather articles from various news sources and save them into a CSV file. Here’s how it works step by step:

Import Libraries: The code begins by bringing in three key tools:
1) feedparser: This tool helps us read and understand the RSS feed, which is like a news list from websites.
2) Article from newspaper3k: This tool is used to fetch and read the full content of each article.
3) csv: This tool allows us to save the article data into a CSV file, which is a common format for spreadsheets.

Parse RSS Feeds:
1) We define a function called parse_rss_feed that takes a URL of an RSS feed as input.
2) The function uses feedparser to read the feed and look for articles. If no articles are found, it prints a message and returns an empty list.
   
Extract Article Details:
1) For each article in the feed, the function retrieves the URL of the article and tries to download and read it using newspaper3k.
2) It extracts important details like the article’s title, author(s), publish date, and the main text of the article.
3) If any errors occur while processing an article, it prints an error message and continues with the next one.
4) All successfully extracted article details are added to a list.
   
Save Data to CSV:
1) Another function, save_as_csv, takes the list of article details and writes them into a CSV file.
2) It creates a file with columns for the title, author, publish date, and content of each article.
3) This makes it easy to review and analyze the collected articles later.
   
Run the Process:
1) We define a list of RSS feed URLs from different news sources.
2) The script processes each URL, retrieves the articles, and if there are any articles, it saves them into a CSV file.
3) It prints messages to let us know how many articles were saved or if no articles were found for a particular feed.
4) This code automates the process of collecting and organizing news articles from multiple sources, making it easier to manage and analyze news content efficiently.

Task no 3:
This project involved an in-depth analysis of public bike-sharing data to identify and visualize key ridership trends. Leveraging Power BI, I performed extensive data cleaning and transformation on daily and hourly datasets, enabling the discovery of peak usage periods, top stations, and patterns among different user types. The project utilized advanced visualizations, such as time series charts and heatmaps, to reveal how factors like weather, holidays, and workdays influence ridership. The resulting dashboard provided critical insights into user behavior, facilitating data-driven decisions to enhance the efficiency and effectiveness of bike-sharing services. As I'm still new to this area, I apologize if any key points were missed or if further refinement is needed.

Task no 5:
In this project, I explored the All India Pincode Directory dataset, which offers detailed insights into postal services across India. Using Tableau, I visualized the distribution of pincodes by state, region, and office type, and created interactive dashboards to facilitate analysis. These visualizations effectively illustrated postal coverage, delivery status, and infrastructure distribution, providing a clear view of regional service disparities. Advanced mapping and charting techniques allowed me to identify areas with dense postal services and regions that require improvement. The findings support strategic planning efforts to enhance the reach and efficiency of postal services.

As a beginner, if there are any mistakes or issues in my approach or execution, I apologize and would appreciate any feedback or guidance to improve.

note : during task no 5 i faced issue regarding the dataset download so i contacted to the CODEVO team they halped but that dataset was not that much impressive so i had choosen the pincode dataset as it was musch effient for me to be worked. but in that dataset 4 rows was having NA values in that so i used pandas to soleve that issue so kindly also check that as change.py file ok thank you .
