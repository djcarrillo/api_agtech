

def Polygon(endpoint, **kward):

    dirs = {
           'available_companies': '/v3/reference/tickers',
           'price': f'/v1/open-close/{kward.get("stocksTicker", "")}/{kward.get("date", "")}'
    }

    return 'https://api.polygon.io'+dirs[endpoint]