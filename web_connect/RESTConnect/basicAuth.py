from base64 import b64encode

class BasicAuth:

    def __init__(self,appKey):
        self.appKey = bytes(appKey,"utf-8")
        self.buildHeader()

    def buildHeader(self):
        userString = self.appKey+b":"
        encodedUserString = b64encode(userString)
        decodedUserString = encodedUserString.decode("ascii")
        self.basicAuthHeader = {"Authorization": "Basic " + decodedUserString}
