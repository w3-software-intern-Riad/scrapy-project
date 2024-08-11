import os
import requests
from sqlalchemy.orm import sessionmaker
from .model import Hotel, db_connect, create_table

class SQLAlchemyPipeline:

    def open_spider(self, spider):
        # Connect to the database and create tables
        self.engine = db_connect()
        create_table(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.image_folder = 'images'
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)

    def close_spider(self, spider):
        # Dispose of the engine to close all connections
        self.engine.dispose()

    def process_item(self, item, spider):
        session = self.Session()

        # Download and save images
        image_paths = []
        if item['images']:
            for url in item['images']:
                image_name = url.split('/')[-1]
                image_path = os.path.join(self.image_folder, image_name)
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        with open(image_path, 'wb') as f:
                            f.write(response.content)
                        image_paths.append(image_name)
                except Exception as e:
                    spider.logger.error(f"Failed to download image {url}: {e}")

        # Save item to the database
        hotel = Hotel(
            propertyTitle=item['propertyTitle'],
            latitude=item['latitude'],
            longitude=item['longitude'],
            location=item['location'],
            rating=item['rating'],
            price=item['price'],
            roomType=item['roomType'],
            images=image_paths  # Store image names
        )

        try:
            session.add(hotel)
            session.commit()
        except Exception as e:
            session.rollback()
            spider.logger.error(f"Error saving item to database: {e}")
        finally:
            session.close()  # Close the session after processing the item

        return item
