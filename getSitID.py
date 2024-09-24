import requests
import json
from configparser import ConfigParser

def get_site_ids():

  f = 'config.ini'
  config = ConfigParser()
  config.read(f)
  
  token = conf['token']['token']
  org = config['org']['orgId']
  
  baseUrl = config['url']['baseUrl']
  
  getAllSites = baseUrl + '/api/v1/orgs/' + org + '/sites'
  
  headers = {
    "Accept": "application/json",
    "Authorization": token
  }
  
  print(f"Getting all of the available sites attached to the Org ID: {org}")
  response = requests.get(getAllSites, headers=headers).json()
  
  siteDictionary = {
  }
  
  for data in response:
    siteDictionary[data['name']] = data['id]
    
  return siteDictionary
