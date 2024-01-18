import requests
import pandas as pd

result_offset = 0
result = []
url = "https://api.qasa.se/graphql"
querystring = {"q": "HomeSearchQuery"}
headers = {
    "authority": "api.qasa.se",
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "origin": "https://bostad.blocket.se",
    "priority": "u=1, i",
    "referer": "https://bostad.blocket.se/",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
}

for x in range(0, 350):  # Set the range from 0 to 350 to ensure all potential listings can be retrieved if necessary."
    payload = {
        "operationName": "HomeSearchQuery",
        "variables": {
            "limit": 50,  # blocket has a limit of 50 per request
            "platform": "blocket",
            "searchParams": {
                "areaIdentifier": [""],  # Modify this to scrape from a specific area
                "rentalType": ["long_term"]
            },
            "offset": result_offset,
            "order": "DESCENDING",
            "orderBy": "PUBLISHED_AT"
        },
        "query": '''
            query HomeSearchQuery($offset: Int, $limit: Int, $platform: PlatformEnum, $order: HomeSearchOrderEnum, $orderBy: HomeSearchOrderByEnum, $searchParams: HomeSearchParamsInput!) {
              homeSearch(
                platform: $platform
                searchParams: $searchParams
                order: $order
                orderBy: $orderBy
              ) {
                filterHomesOffset(offset: $offset, limit: $limit) {
                  pagesCount
                  totalCount
                  hasNextPage
                  hasPreviousPage
                  nodes {
                    firsthand
                    rent
                    tenantBaseFee
                    location {
                      locality
                    }
                    roomCount
                    squareMeters
                    studentHome
                    type
                    tenantCount
                  }
                  __typename
                }
                __typename
              }
            }
        '''
    }

    result_offset += 50  # increase the offset so we get the next 50 results

    response = requests.post(url, json=payload, headers=headers, params=querystring)

    data = response.json()
    print(data)
    for listings in data["data"]["homeSearch"]["filterHomesOffset"]["nodes"]:
        result.append(listings)  # add the response to the result

    if not data["data"]["homeSearch"]["filterHomesOffset"]["hasNextPage"]:  # checks if there is another page and breaks if there isn't.
        break

listings_df = pd.json_normalize(result)

listings_df.to_csv("blocket_data_visby.csv")
