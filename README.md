# housing-data-web-crawer
This repository contains a web crawler that scrapes house advertisement data from a commercial web site in Sri Lanka

### Prerequisite
Install Scrapy (See [https://docs.scrapy.org/en/latest/](https://docs.scrapy.org/en/latest/) for more details)

Using conda

    conda install -c conda-forge scrapy

Using pip

    pip install Scrapy

### How to run
To run te housedata spider, execute below command. The output will be written to the output.json.

    scrapy crawl housedata -o output.json



