from urllib.parse import urlparse

network_name = 'Twitter'

def get_net_id(caller, url):
  try:
    urlparts = urlparse(url)
    splitpath = urlparts.path.split('/')
    if len(splitpath) < 2:
      return None
    return splitpath[1]
  except Exception as e:
    caller.logger.warn('Exception extracting ID from URL')
    caller.logger.warn(e)

def is_valid_result(caller, url):
  try:
    urlparts = urlparse(url)
    return (urlparts.scheme in ['http','https']) and (urlparts.netloc.find('twitter.com') > -1) and get_net_id(caller, url) != None 
  except Exception as e:
    caller.logger.warn('Exception extracting ID from URL')
    caller.logger.warn(e)
    return None
