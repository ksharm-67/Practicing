class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl[4] == 's':
            x = longUrl[5:] + '#'

        elif longUrl[:3] == 'ftp':
            x = longUrl[3:] + '$'

        else:
            x = longUrl[4:]
        return x


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl[-1] == '#':
            return "https" + shortUrl[:-1]
        elif shortUrl[-1] == '$':
            return "ftp" + shortUrl[:-1]
        else:
            return "http" + shortUrl
        

#Your Codec object will be instantiated and called as such:
codec = Codec()
codec.decode(codec.encode(url))