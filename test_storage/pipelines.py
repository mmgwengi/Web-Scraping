# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import csv

# class TestStoragePipeline:
#     def process_item(self, item, spider):
#         return item


import csv
class TestStoragePipeline(object):
    def process_item(self, item, spider):
        # get category and use it as filename        
        filename = r'C:\Users\marth\Data Science\Webscraping\test_storage\test_storage\test_storage\spiders\test_out.csv'
        # filename = '/data/data/user/gweng001/scrapeddata_2021/'+item['Category'] + '.csv'
        # open file for appending        
        with open(filename, 'a',newline='') as f:
            writer = csv.writer(f)
            # write only pdf url and page it was found in             
            row = [item['url'], item['page']]
            writer.writerow(row)

        # write all data in row            
        # warning: item is dictionary so item.values() don't have to return always values in the same order            #writer.writerow(item.values())
        return item