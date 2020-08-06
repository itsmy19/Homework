class cache(object):
    def __init__(self, fun):
        self.fun = fun
        self.cache = {}

    def __call__(self, *args, **kwargs):
        key  = str(args) + str(kwargs)
        try:
            return self.cache[key]
        except KeyError:
            self.cache[key] = rval = self.fun(*args, **kwargs)
            return rval
        except TypeError:
            return self.fun(*args, **kwargs)

def get_url_src(url):
    return urllib.urlopen(url).read()
