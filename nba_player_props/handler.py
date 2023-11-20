from main import main


def handler(scrape_bool):
    try:
        results = main(scrape_bool)
    except Exception as err:
        raise err
    else:
        return results
