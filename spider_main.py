#!/usr/bin/env python -t
# -*- coding: UTF-8 -*-
from baike_spider import url_manager,html_downloader,html_parser,html_outputer
import urllib

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "craw %d : %s" % (count, urllib.unquote(new_url.encode('utf-8')))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
               
                if count == 1000:
                    break
                count = count + 1
            except KeyboardInterrupt:
                print "KeyboardInterrupt, exit gracefully"
                break
            except:
                print "craw failed"
                #print new_url,html_cont
                raise


        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
