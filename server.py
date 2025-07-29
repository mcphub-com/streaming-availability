import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability'

mcp = FastMCP('streaming-availability')

@mcp.tool()
def search_shows_by_filters(country: Annotated[str, Field(description='ISO 3166-1 alpha-2 code of the target country. See /countries endpoint to get the list of supported countries.')],
                            cursor: Annotated[Union[str, None], Field(description='Cursor is used for pagination. After each request, the response includes a hasMore boolean field to tell if there are more results that did not fit into the returned list. If it is set as true, to get the rest of the result set, send a new request (with the same parameters for other fields), and set the cursor parameter as the nextCursor value of the response of the previous request. Do not forget to escape the cursor value before putting it into a query as it might contain characters such as ?and &. The first request naturally does not require a cursor parameter.')] = None,
                            year_max: Annotated[Union[int, float, None], Field(description='Maximum release/air year of the shows.')] = None,
                            series_granularity: Annotated[Union[str, None], Field(description='series_granularity determines the level of detail for series. It does not affect movies. If series_granularity is show, then the output will not include season and episode info. If series_granularity is season, then the output will include season info but not episode info. If series_granularity is episode, then the output will include season and episode info. If you do not need season and episode info, then it is recommended to set series_granularity as show to reduce the size of the response and increase the performance of the endpoint. If you need deep links for individual seasons and episodes, then you should set series_granularity as episode. In this case response will include full streaming info for seasons and episodes, similar to the streaming info for movies and series; including deep links into seasons and episodes, individual subtitle/audio and video quality info etc.')] = None,
                            genres: Annotated[Union[str, None], Field(description='A comma seperated list of genre ids to only search within the shows in those genre. See /genres endpoint to see the available genres and their ids. Use genres_relation parameter to specify between returning shows that have at least one of the given genres or returning shows that have all of the given genres.')] = None,
                            order_direction: Annotated[Union[str, None], Field(description='Determines whether to order the results in ascending or descending order. Default value when ordering alphabetically or based on dates/times is asc. Default value when ordering by rating or popularity is desc.')] = None,
                            order_by: Annotated[Union[str, None], Field(description='Determines the ordering of the shows. Make sure to set descending_order parameter as true when ordering by popularity or rating so that shows with the highest popularity or rating will be returned first.')] = None,
                            year_min: Annotated[Union[int, float, None], Field(description='Minimum release/air year of the shows.')] = None,
                            show_original_language: Annotated[Union[str, None], Field(description='ISO 639-1 language code to only search within the shows whose original language matches with the provided language.')] = None,
                            keyword: Annotated[Union[str, None], Field(description='A keyword to only search within the shows have that keyword in their overview or title.')] = None,
                            genres_relation: Annotated[Union[str, None], Field(description='Only used when there are multiple genres supplied in genres parameter. When or, the endpoint returns any show that has at least one of the given genres. When and, it only returns the shows that have all of the given genres.')] = None,
                            output_language: Annotated[Union[str, None], Field(description='ISO 639-1 code of the output language. Determines in which language the output will be in.')] = None,
                            catalogs: Annotated[Union[str, None], Field(description='A comma separated list of up to 32 catalogs to search in. See /countries endpoint to get the supported services in each country and their ids. When multiple catalogs are passed as a comma separated list, any show that is in at least one of the catalogs will be included in the result. If no catalogs are passed, the endpoint will search in all the available catalogs in the country. Syntax of the catalogs supplied in the list can be as the followings: <sevice_id>: Searches in the entire catalog of that service, including (if applicable) rentable, buyable shows or shows available through addons e.g. netflix, prime, apple <sevice_id>.<streaming_option_type>: Only returns the shows that are available in that service with the given streaming option type. Valid streaming option types are subscription, free, rent, buy and addon e.g. peacock.free only returns the shows on Peacock that are free to watch, prime.subscription only returns the shows on Prime Video that are available to watch with a Prime subscription. hulu.addon only returns the shows on Hulu that are available via an addon, prime.rent only returns the shows on Prime Video that are rentable. <sevice_id>.addon.<addon_id>: Only returns the shows that are available in that service with the given addon. Check /countries endpoint to fetch the available addons for a service in each country. Some sample values are: hulu.addon.hbo, prime.addon.hbomaxus.')] = None,
                            rating_max: Annotated[Union[int, float, None], Field(description='Maximum rating of the shows. Minimum: 0 Maximum: 100')] = None,
                            show_type: Annotated[Union[str, None], Field(description='Type of shows to search in. If not supplied, both movies and series will be included in the search results.')] = None,
                            rating_min: Annotated[Union[int, float, None], Field(description='Minimum rating of the shows. Minimum: 0 Maximum: 100')] = None) -> dict: 
    '''Search through the catalog of the given streaming services in the given country. Provides filters such as show language, genres, keyword and release year. Output includes all the information about the shows, such as title, IMDb ID, TMDb ID, release year, deep links to streaming services, available subtitles, audios, available video quality and many more! Apart from the info about the given country-service combinations, output also includes information about streaming availability in the other services for the given country. Streaming availability info from the other countries are not included in the response. When `show_type` is `movie` or `series_granularity` is `show`, items per page is 20. When `show_type` is `series` and `series_granularity` is `episode` items per page is 10. Otherwise, items per page is 15.'''
    url = 'https://streaming-availability.p.rapidapi.com/shows/search/filters'
    headers = {'x-rapidapi-host': 'streaming-availability.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'cursor': cursor,
        'year_max': year_max,
        'series_granularity': series_granularity,
        'genres': genres,
        'order_direction': order_direction,
        'order_by': order_by,
        'year_min': year_min,
        'show_original_language': show_original_language,
        'keyword': keyword,
        'genres_relation': genres_relation,
        'output_language': output_language,
        'catalogs': catalogs,
        'rating_max': rating_max,
        'show_type': show_type,
        'rating_min': rating_min,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_shows_by_title(country: Annotated[str, Field(description='ISO 3166-1 alpha-2 code of the target country. See /countries endpoint to get the list of supported countries.')],
                          title: Annotated[str, Field(description='Title phrase to search for.')],
                          series_granularity: Annotated[Union[str, None], Field(description='series_granularity determines the level of detail for series. It does not affect movies. If series_granularity is show, then the output will not include season and episode info. If series_granularity is season, then the output will include season info but not episode info. If series_granularity is episode, then the output will include season and episode info. If you do not need season and episode info, then it is recommended to set series_granularity as show to reduce the size of the response and increase the performance of the endpoint. If you need deep links for individual seasons and episodes, then you should set series_granularity as episode. In this case response will include full streaming info for seasons and episodes, similar to the streaming info for movies and series; including deep links into seasons and episodes, individual subtitle/audio and video quality info etc.')] = None,
                          show_type: Annotated[Union[str, None], Field(description='Type of shows to search in. If not supplied, both movies and series will be included in the search results.')] = None,
                          output_language: Annotated[Union[str, None], Field(description='ISO 639-1 code of the output language. Determines in which language the output will be in.')] = None) -> dict: 
    '''Search for movies and series by a title. Maximum amount of items returned are `20` unless there are more than 20 shows with the exact given title input. In that case all the items have 100% match with the title will be returned. Streaming availability info for the target country is included in the response, but not for the other countries. Results might include shows that are not streamable in the target country. Only criteria for the search are the title and the show type. No pagination is supported.'''
    url = 'https://streaming-availability.p.rapidapi.com/shows/search/title'
    headers = {'x-rapidapi-host': 'streaming-availability.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'title': title,
        'series_granularity': series_granularity,
        'show_type': show_type,
        'output_language': output_language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_show(series_granularity: Annotated[Union[str, None], Field(description='series_granularity determines the level of detail for series. It does not affect movies. If series_granularity is show, then the output will not include season and episode info. If series_granularity is season, then the output will include season info but not episode info. If series_granularity is episode, then the output will include season and episode info. If you do not need season and episode info, then it is recommended to set series_granularity as show to reduce the size of the response and increase the performance of the endpoint. If you need deep links for individual seasons and episodes, then you should set series_granularity as episode. In this case response will include full streaming info for seasons and episodes, similar to the streaming info for movies and series; including deep links into seasons and episodes, individual subtitle/audio and video quality info etc.')] = None,
             output_language: Annotated[Union[str, None], Field(description='ISO 639-1 code of the output language. Determines in which language the output will be in.')] = None,
             country: Annotated[Union[str, None], Field(description='ISO 3166-1 alpha-2 code of the optional target country. If this parameter is not supplied, global streaming availability across all the countries will be returned. If it is supplied, only the streaming availability info from the given country will be returned. If you are only interested in the streaming availability in a single country, then it is recommended to use this parameter to reduce the size of the response and increase the performance of the endpoint. See /countries endpoint to get the list of supported countries.')] = None) -> dict: 
    '''Get the details of a show via `id`, `imdbId` or `tmdbId`, including the global streaming availability info.'''
    url = 'https://streaming-availability.p.rapidapi.com/shows/%7Bid%7D'
    headers = {'x-rapidapi-host': 'streaming-availability.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'series_granularity': series_granularity,
        'output_language': output_language,
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_countries(output_language: Annotated[Union[str, None], Field(description='ISO 639-1 code of the output language. Determines in which language the output will be in.')] = None) -> dict: 
    '''Get all the supported countries and the list of the supported services and their details for each country. Details of services include names, logos, supported streaming types (subscription, rent, buy, free etc.) and list of available addons/channels.'''
    url = 'https://streaming-availability.p.rapidapi.com/countries'
    headers = {'x-rapidapi-host': 'streaming-availability.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'output_language': output_language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_country(output_language: Annotated[Union[str, None], Field(description='ISO 639-1 code of the output language. Determines in which language the output will be in.')] = None) -> dict: 
    '''Get a country and the list of the supported services and their details. Details of services include names, logos, supported streaming types (subscription, rent, buy, free etc.) and list of available addons/channels.'''
    url = 'https://streaming-availability.p.rapidapi.com/countries/%7Bcountry-code%7D'
    headers = {'x-rapidapi-host': 'streaming-availability.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'output_language': output_language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_genres(output_language: Annotated[Union[str, None], Field(description='ISO 639-1 code of the output language. Determines in which language the output will be in.')] = None) -> dict: 
    '''Get the list of supported genres.'''
    url = 'https://streaming-availability.p.rapidapi.com/genres'
    headers = {'x-rapidapi-host': 'streaming-availability.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'output_language': output_language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_changes(change_type: Annotated[str, Field(description='Type of changes to query.')],
                country: Annotated[str, Field(description='ISO 3166-1 alpha-2 code of the target country. See /countries endpoint to get the list of supported countries.')],
                item_type: Annotated[str, Field(description='Type of items to search in. If item_type is show, you can use show_type parameter to only search for movies or series.')],
                output_language: Annotated[Union[str, None], Field(description='ISO 639-1 code of the output language. Determines in which language the output will be in.')] = None,
                order_direction: Annotated[Union[str, None], Field(description='Determines whether to order the results in ascending or descending order.')] = None,
                include_unknown_dates: Annotated[Union[bool, None], Field(description='Whether to include the changes with unknown dates. past changes such as new, removed or updated will always have a timestamp thus this parameter does not affect them. future changes such as expiring or upcoming may not have a timestamp if the exact date is not known (e.g. some services do not explicitly state the exact date of some of the upcoming/expiring shows). If set as true, the changes with unknown dates will be included in the response. If set as false, the changes with unknown dates will be excluded from the response. When ordering, the changes with unknown dates will be treated as if their timestamp is 0. Thus, they will appear first in the ascending order and last in the descending order.')] = None,
                cursor: Annotated[Union[str, None], Field(description='Cursor is used for pagination. After each request, the response includes a hasMore boolean field to tell if there are more results that did not fit into the returned list. If it is set as true, to get the rest of the result set, send a new request (with the same parameters for other fields), and set the cursor parameter as the nextCursor value of the response of the previous request. Do not forget to escape the cursor value before putting it into a query as it might contain characters such as ?and &. The first request naturally does not require a cursor parameter.')] = None,
                _from: Annotated[Union[int, float, None], Field(description='Unix Time Stamp to only query the changes happened/happening after this date (inclusive). For past changes such as new, removed or updated, the timestamp must be between today and 31 days ago. For future changes such as expiring or upcoming, the timestamp must be between today and 31 days from now in the future. If not supplied, the default value for past changes is 31 days ago, and for future changes is today. Minimum: -9223372036854776000 Maximum: 9223372036854776000')] = None,
                to: Annotated[Union[int, float, None], Field(description='Unix Time Stamp to only query the changes happened/happening before this date (inclusive). For past changes such as new, removed or updated, the timestamp must be between today and 31 days ago. For future changes such as expiring or upcoming, the timestamp must be between today and 31 days from now in the future. If not supplied, the default value for past changes is today, and for future changes is 31 days from now. Minimum: -9223372036854776000 Maximum: 9223372036854776000')] = None,
                show_type: Annotated[Union[str, None], Field(description='Type of shows to search in. If not supplied, both movies and series will be included in the search results.')] = None,
                catalogs: Annotated[Union[str, None], Field(description='A comma separated list of up to 32 catalogs to search in. See /countries endpoint to get the supported services in each country and their ids. When multiple catalogs are passed as a comma separated list, any show that is in at least one of the catalogs will be included in the result. If no catalogs are passed, the endpoint will search in all the available catalogs in the country. Syntax of the catalogs supplied in the list can be as the followings: <sevice_id>: Searches in the entire catalog of that service, including (if applicable) rentable, buyable shows or shows available through addons e.g. netflix, prime, apple <sevice_id>.<streaming_option_type>: Only returns the shows that are available in that service with the given streaming option type. Valid streaming option types are subscription, free, rent, buy and addon e.g. peacock.free only returns the shows on Peacock that are free to watch, prime.subscription only returns the shows on Prime Video that are available to watch with a Prime subscription. hulu.addon only returns the shows on Hulu that are available via an addon, prime.rent only returns the shows on Prime Video that are rentable. <sevice_id>.addon.<addon_id>: Only returns the shows that are available in that service with the given addon. Check /countries endpoint to fetch the available addons for a service in each country. Some sample values are: hulu.addon.hbo, prime.addon.hbomaxus.')] = None) -> dict: 
    '''Query the new, removed, updated, expiring or upcoming movies/series/seasons/episodes in a given list of streaming services. Results are ordered by the date of the changes. Changes listed per page is `25`. Changes are listed under `changes` field, and shows affected by these changes are listed under `shows` field.'''
    url = 'https://streaming-availability.p.rapidapi.com/changes'
    headers = {'x-rapidapi-host': 'streaming-availability.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'change_type': change_type,
        'country': country,
        'item_type': item_type,
        'output_language': output_language,
        'order_direction': order_direction,
        'include_unknown_dates': include_unknown_dates,
        'cursor': cursor,
        'from': _from,
        'to': to,
        'show_type': show_type,
        'catalogs': catalogs,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
