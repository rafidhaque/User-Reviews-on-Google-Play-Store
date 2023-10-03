from google_play_scraper import Sort, reviews_all


'''
    "Telecash": "com.datasoftbd.telecashcustomerapp",
    "SureCash": "com.progoti.surecash",
    "Upay": "bd.com.upay.customer",
    "Rocket": "com.dbbl.mbs.apps.main",
    "Nagad": "com.konasl.nagad"
'''

app_list = {
    "BKash": "com.bKash.customerapp"
    }

for app_name, app_domain in app_list.items():
    results = reviews_all(
        app_domain,
        sleep_milliseconds=0, # defaults to 0
        lang='en', # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    )


    f = open(app_name + "2.csv", "a", encoding="utf-8-sig")

    for result in results:
        if result['content'] == None:
            continue
        f.write(result['content'])
        f.write("\n")


    f.close()
