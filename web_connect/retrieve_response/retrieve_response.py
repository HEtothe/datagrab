import requests
from requests.exceptions import (
    Timeout,
    HTTPError,
    ConnectionError,
    TooManyRedirects,
    RequestException
    )

class RetrievedResponse:
    """

    """

    def __init__(self, url, headers=None, params=None):
        self.url = url
        self.headers = headers
        self.params = params

    def getResponse(self, timeout=15):
        """
        Uses self.url to generate a request response.
        Creates self.response
        """

        try:
            self.response = requests.get(self.url, timeout=timeout,
            headers=self.headers,
            params=self.params)

        except Timeout:
            # Server taking too long to respond
            self.errorMsg = "Your URL {} did not response in time, exiting.\n"\
                  "Try increasing the timeout kwarg.".format(self.url)

        except HTTPError:
            #Invalid HTTP response - probably the result of URL typo
            self.errorMsg = \
                "Your URL {} produced an invalid HTTP response, exiting."\
                .format(self.url)

        except ConnectionError:
            #DNS failure, refused connection etc.
            self.errorMsg = "We encountered a network problem, exiting."

        except TooManyRedirects:
            #url has redirected more than the configured maximum
            self.errorMsg = "We were redirected too many times when using url {},"\
                  "try a different one."\
                  .format(self.url)

        except RequestException:
            #Catastrophic unknown error type
            self.errorMsg = "We encountered a problem, exiting."

    def validateResponse(self):
        """ensures that the response code is 200"""
        assert self.response.status_code==200, "Data not retrieved,"\
                        " response code {}".format(self.response.status_code)

    def getValidate(self, timeout=15):
        "Combined implementation of getResponse and validateResponse"
        self.getResponse(timeout=timeout)

        if hasattr(self, "response"):
            self.validateResponse()

        else:
            print("The HTTP request failed.")
            print("This is most often due to not inputting the full URL,"\
            "which should include the protocol (e.g. http://) and 'www.'")
            print(self.errorMsg)
