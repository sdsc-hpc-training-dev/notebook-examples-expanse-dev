# SDSC Expanse Notebook:Web_Scraping
This guide provides instructions for Expanse users on how to run notebooks related to web scraping.
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. The web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser.

This chapter will show you how to implement Web Scraping function in a Jupyter Notebook. Enjoy\
  **Listof Content**
- [Launch Galyleo](##launch-galyleo)
- [Import Module](##import_module)
- [Environment Modules](##environment-modules)
- [Install Modules](##install-modules)
- [Location](##location)

## Import Module:
- requests
- json
- pprint
- BeautifulSoup
- time

## Launch Galyleo
For specific information about launching Galyleo, please refer to [this GitHub repository](https://github.com/mkandes/galyleo).

## Environment Modules
By utilizing `--env-modules`, we can load any software installed in Expanse. 
For instance, executing this command line will load CPU modules and Anaconda3 within the Jupyter session.
  - CPU:
`--env-modules cpu/0.17.3b,anaconda3`
```
galyleo launch --account abc123 --partition shared --cpus 2 --memory 4 --time-limit 00:30:00 --env-modules cpu/0.17.3b,anaconda3/2021.05
```
Also this command line loads GPU modules and Anaconda3 in the Jupyter session to run in a GPU environment.
 - GPU:
`--env-modules  gpu/0.17.3b,anaconda3/2021.05`
```
galyleo launch --account abc123 —partition gpu-shared --cpus 10 --memory 92 --gpus 1 --time-limit 00:30:00  --env-modules  gpu/0.17.3b,anaconda3/2021.05 --bind /oasis,/scratch --nv
```

## Install Modules
To run  notebooks Web_Scraping and Recommendation_System notebooks, need to install additional package.
- sentence-transformers
`!pip install -U sentence-transformers`

## Location 

Web_Scraping\
├── [Web_Scraping_and_Recommendation_System.ipynb](./web_scraping_and_recommendation_system.ipynb)\
├── README.md

