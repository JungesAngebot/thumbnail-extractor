import requests

from extractor import config


def execute_kaltura_request(request):
    return requests.get(request).json()


def get_category_api_string():
    request_url = 'http://www.kaltura.com/api_v3/'
    request_url += '?service=category'
    request_url += '&action=list'
    request_url += '&ks='
    request_url += '{0}'
    request_url += '&format=1'
    request_url += '&filter:objectType=KalturaCategoryFilter'
    request_url += '&filter:parentIdIn={1}'.format(config.property('kaltura.ks'),
                                                   config.property('kaltura.category_root'))
    return request_url


def get_category_metadata_api_string(category_id):
    request_url = 'http://www.kaltura.com/api_v3/'
    request_url += '?service=metadata_metadata'
    request_url += '&action=list'
    request_url += '&ks='
    request_url += '%s'
    request_url += '&format=1'
    request_url += '&filter:objectIdEqual='
    request_url += '%s'
    request_url += '&filter:objectType=KalturaMetadataFilter'
    request_url += '&filter:metadataObjectTypeEqual=2'
    return request_url % (config.property('kaltura.ks'), category_id)
