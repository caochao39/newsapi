from newsapi.base_news import BaseNews
import logging
import http.client as http_client


class TopHeadLines(BaseNews):
    def __init__(self, API_KEY):
        super(TopHeadLines, self).__init__(API_KEY)
        self.endpoint = "https://newsapi.org/v2/top-headlines"

    def get(self, sources=None, q=None, category=None, language=None, country=None, attributes_format=True):
        '''
        Function for retrieving top headlines. For more details please refer to: https://newsapi.org/docs/endpoints/top-headlines
        :param sources: A comma-seperated string of identifiers (maximum 20) for the news sources or blogs you want headlines from.
        :param q: Keywords or phrase to search for.
        :param category: The category you want to get headlines for. Possible options: business entertainment gaming general health-and-medical music politics science-and-nature sport technology Default: all categories returned.
        :param language: The 2-letter ISO-639-1 code of the language you want to get headlines for. Possible options: ar en cn de es fr he it nl no pt ru sv ud Default: all languages returned.
        :param country: The 2-letter ISO 3166-1 code of the country you want to get headlines for. Possible options: araubrcacndeesfrgbhkieinisitnlnopkrusasvusza Default: all countries returned.
        :param attributes_format: If true then returns a attribute dictionary format object, otherwise a jason string
        :return: A jason string that describes the News
        '''

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

        if category is not None:
            self.payload['category'] = category

        if language is not None:
            self.payload['language'] = language

        if country is not None:
            self.payload['country'] = country

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
