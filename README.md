# ETL-Pipeline-Automation

**ETL Pipeline Overview:**

    Demonstrates the creation of an automated ETL pipeline using Python and pgAdmin4 database.
    Involves scraping data from Zalando website, cleaning it, and storing it in a CSV file.
    The CSV file is then loaded into the pgAdmin4 database.
    Entire pipeline is automated to run daily at a specified time.

**The Project Steps:**

**E(xtract)TL:**

      Utilized Python libraries requests and BeautifulSoup for web scraping.
      Collected data: Brand, Name, Price of shoes, and Date of collection.
      Records saved in a CSV file using the csv library.
  
**ET(ransform)L:**

    Used pandas for data transformation.
    Specifically removed all non-numeric values from the price field.
    Saved the transformed data back to a CSV file.
  
**ETL(oad):**

    Established a connection with pgAdmin4 database using psycopg2 library.
    Login details imported via configparser from a separate .ini file.
  
**Automating the ETL Pipeline:**

    Utilized schedule, time, and subprocess libraries in a separate Python file.
    ETL scripts run once a day at a specified time.

**Improvements:**

    Add a script to send an email if the price of any item reaches a desired point or trigger a warning for errors.
    For instance, changes in website structure leading to the spider being unable to locate expected values.
    About:



#Python, #PostgreSQL, #web scraping, #pgAdmin4, #ETL pipeline, #ETL automation.
