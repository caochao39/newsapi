from newsapi.base_news import BaseNews
import logging
import http.client as http_client


class Everything(BaseNews):
    def __init__(self, API_KEY):
        super(Everything, self).__init__(API_KEY)
        self.endpoint = "https://newsapi.org/v2/everything"

    def get(self, q=None, sources=None, domains=None, date_from=None, date_to=None, language=None, sortBy=None, page=None, attributes_format=True):
        """
        Function for retrieving everything.  For more details please refer to: https://newsapi.org/docs/endpoints/everything
        :param q: Keywords or phrases to search for.
        :param sources: A comma-seperated string of identifiers (maximum 20) for the news sources or blogs you want headlines from.
        :param domains: A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com) to restrict the search to.
        :param date_from: A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2017-12-09 or 2017-12-09T20:12:24) Default: the oldest according to your plan.
        :param date_to: A date and optional time for the newest article allowed. This should be in ISO 8601 format (e.g. 2017-12-09 or 2017-12-09T20:12:24) Default: the newest according to your plan.
        :param language: The 2-letter ISO-639-1 code of the language you want to get headlines for. Possible options: ar en cn de es fr he it nl no pt ru sv ud . Default: all languages returned.
        :param sortBy: The order to sort the articles in. Possible options: relevancy, popularity, publishedAt. relevancy = articles more closely related to q come first. popularity = articles from popular sources and publishers come first. publishedAt = newest articles come first. Default: publishedAt
        :param page: (Int) Use this to page through the results. 20 articles are returned on a page.
        :param attributes_format: If true then returns a attribute dictionary format object, otherwise a jason string
        :return: A jason string that describes the News
        """

        ## For logging
        # http_client.HTTPConnection.debuglevel = 1
        # logging.basicConfig()
        # logging.getLogger().setLevel(logging.DEBUG)
        # requests_log = logging.getLogger("requests.packages.urllib3")
        # requests_log.setLevel(logging.DEBUG)
        # requests_log.propagate = True

        if q is not None:
            self.payload['q'] = q

        if sources is not None:
            self.payload['sources'] = sources

        if domains is not None:
            self.payload['domains'] = domains

        if date_from is not None:
            self.payload['from'] = date_from

        if date_to is not None:
            self.payload['to'] = date_to

        if language is not None:
            self.payload['language'] = language

        if sortBy is not None:
            self.payload['sortBy'] = sortBy

        if page is not None:
            self.payload['page'] = page

        r = self.requests.get(self.endpoint, params=self.payload)
        if r.status_code != 200:
            raise BaseException("Error Code: ", r.status_code, " Either server didn't respond or has resulted in zero results.")
        try:
            content = r.json()
        except ValueError:
            raise ValueError("No json data could be retrieved.")

        if attributes_format:
            return self.AttrDict(content)

        return content
