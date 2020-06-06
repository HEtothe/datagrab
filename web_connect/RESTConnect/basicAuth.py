from base64 import b64encode

class BasicAuth:

    def __init__(appKey):
        self.appKey = appKey
        self.buildHeader()

    def buildHeader(self):
        userString = self.appKey+":"
        encodedUserString = b64encode(userString)
        decodedUserString = encodedUserString.decode("ascii")
        self.basicAuthHeader = {"Authorization": "Basic " + decodedUserString}
