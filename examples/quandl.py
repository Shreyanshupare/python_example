import quandl

data = quandl.get("BP/OIL_REF_CAP_PHL", authtoken="g1_EsyhPLz9BjczfmiLz")
print(data)
