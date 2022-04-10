# Web-crawler-practice
* The project is the example how to download images form the prefered website by web crawler technique.

## Requirement libraries 
```
pip install bs4
pip install pandas
pip install requests
```
## Programming explaination
### getBasicData.py
* The getBasicData.py can get each hyperlink of the parant page, and save the records for further use to download images.

### downloadPicV2.py
* The downloadPicV2.py will download the images of each sub-child page based on the records from getBasicData.py.
