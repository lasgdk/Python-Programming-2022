# Nasdaq API key: fq1yTytdsip7_cqG5gCd
import nasdaqdatalink
mydata = nasdaqdatalink.get("FRED/GDP")

nasdaqdatalink.ApiConfig.api_key = "fq1yTytdsip7_cqG5gCd"
mydata = nasdaqdatalink.get("FRED/GDP")

print(mydata)