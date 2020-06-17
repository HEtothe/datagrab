from base64 import b64encode

class BasicAuth:
    """Class to create a BasicAuth-style header dictionary for use with
    BasicAuth API's.

    Parameters:
        appKey: string
        The API key as given to you by the API provider
    """

    def __init__(self,appKey):
        "Converts appKey to bites and executes buildHeader method"

        self.appKey = bytes(appKey,"utf-8")
        self.buildHeader()

    def buildHeader(self):
        """Creates a basic auth header, by encoding bytes to base64 and then
        decoding to ascii.

        Has format "Authorization": "Basic <ascii-decoded key>" per the standard

        Note that it does not currently support basic auth use cases where a
        password is also required.

        Creates attribute self.basicAuthHeader

        Arguments: none
        """
        userString = self.appKey+b":"
        encodedUserString = b64encode(userString)
        decodedUserString = encodedUserString.decode("ascii")
        self.basicAuthHeader = {"Authorization": "Basic " + decodedUserString}
