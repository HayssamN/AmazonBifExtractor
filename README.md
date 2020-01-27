# AmazonBifExtractor
Amazon videos service displays an image for a specific time in the video whenever the mouse hovers over the time slider.
A binary bif file containing the images for specific time offsets is downloaded on the client side and blob url is generated from it whenever the mouse hovers over the time slider.

This script extracts the images from the Amazon Bif file. 

Here the mouse hover on the time slider at minute 04:25
![amz_shot](/images/amz_shot.png)


# Usage
1. Open Chrom/Firefox/Edge Developer tools (F12)
2. Navigate to Amazon video.
3. Search and download the bif file from Network tab.

![amz_bif](/images/amz_bif.png)

4. Use the script as follows to extract the images.
```bash
$ ./bif_extractor.py  ~/Downloads/amazon/MrBean/mr_bean.bif 
152 images with multiplier of 10000 milliseconds.
```

Extracted images
![amz_mrbean](/images/mrbean_imgs.png)