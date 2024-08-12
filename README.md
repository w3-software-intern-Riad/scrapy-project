# Hotel Data Scraper

This project is a web scraper built using Scrapy to collect hotel data from ```"https://uk.trip.com/hotels/?locale=en-GB&curr=GBP",```. The scraped data includes details like property title, rating, location, latitude, longitude, room type, price, and images. The data is stored in a PostgreSQL database, and SQLAlchemy is used as the ORM for database operations.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)

- [How to Start the Project](#how-to-start-the-project)
- [Contributing](#contributing)
- [License](#license)

## Features

- Scrapes hotel data, including:
  - Property Title
  - Rating
  - Location (Address, Latitude, Longitude)
  - Room Type
  - Price
  - Images
- Stores scraped data in a PostgreSQL database.
- Uses SQLAlchemy as an ORM for managing database operations.

## Technologies Used

- Python
- Scrapy
- PostgreSQL
- SQLAlchemy
- psycopg2 (PostgreSQL adapter)
- Other Python libraries (see `requirements.txt`)

## Installation

### Prerequisites

- Python 3.x installed on your system.
- PostgreSQL database setup and running.
- Git installed on your system.

### Clone the Repository

```bash
git clone https://github.com/w3-software-intern-Riad/scrapy-project.git
cd scrapy-project 
```
### Set Up a Virtual Environment

``` bash 
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### Install the Required Packages
```bash
pip install -r requirement.txt

```
### Setup database connection 
```change the connection string in .env file```
### How to Start the Project
```bash
cd hotelscraper
scrapy crawl <your_spider_name>
```
# Important note
``` If the data is not successfully retrieved during the initial run, please initiate the crawl again```
### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.
### License
This project is licensed under the MIT License. See the LICENSE file for details.




