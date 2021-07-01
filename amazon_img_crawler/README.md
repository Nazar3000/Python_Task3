a Python/Scrapy-based web crawler, which will recursively 
walk over the first page of Amazon and download all images 
and then convert it all into one jpg format.

Requirements: 
1.The environment requires an installed version of python 3
2.Scrapy==2.5.0
3.Pillow==8.2.0

**RUN**
1. Transfer all rights to the image_crawler directory to your user 
   (use command sudo chown-R user:user /dir)
2. Run the command in image_crawler directory: pip install -r requirements.txt 
3. in amazon_img.py insert a link to the page with the goods you need in var "url_of_products" 
4. Run the command in amazon_img_crawler directory: scrapy crawl amazon_img
5. Enjoy the uploaded images in folder "img_dir"


