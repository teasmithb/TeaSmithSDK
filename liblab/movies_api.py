

from argparse import ArgumentParser
import requests


def main():
    # parse arguments from user
    parser = ArgumentParser(description="Communicate with Lords of the Rings API.")
    parser.add_argument('token',type=str, help='unique token to authenticate caller, gets passed to an api as an Bearer token')
    parser.add_argument('--movie_id', type=str, help='specified movie id, if not provided all movies will be returned')
    parser.add_argument('--quote', action="store_true", help='returns quote for the book specified,movie_id here is mandatory argument')
    parser.add_argument('--limit',type=int, help='limit number of movies per page, ')
    parser.add_argument('--page',  type=int, help='movies to be displayed on particular page')
    parser.add_argument('--offset', type=int, help='offset value for the movies')
    parser.add_argument('--sort', action="store_true", help='if provided sort will be in ascending order, otherwise descending order')
    parser.add_argument('--param_name', type=str, help='parameter name to filter on')
    parser.add_argument('--match_str', type=str, help='match string to be compared with match and not match')
    parser.add_argument('--param_match', action="store_true", help='if provided param_name will be matched, param_name is mandatory here')
    parser.add_argument('--param_notmatch', action="store_true", help='if provided param_name will not be matched, param_name is mandatory here')
    parser.add_argument('--param_include', action="store_true", help='if provided param_name will be included, param_name is mandatory here')
    parser.add_argument('--param_exclude', action="store_true", help='if provided param_name will not be included, param_name is mandatory here')
    parser.add_argument('--param_exists', action="store_true", help='if provided param_name will be checked if it exists,param_name is mandatory here')
    parser.add_argument('--param_notexists', action="store_true", help='if provided param_name will be checked if it does not exists')
    parser.add_argument('--param_regex', type=str,  help='if provided param_regex will be checked, param_name is mandatory here')
    parser.add_argument('--param_noregex', type=str,  help='movies with regex wont be returned  param_name is mandatory here')
    parser.add_argument('--value', type=int,help='if provided value passed will be compared with the value from api using operation for the parameter') 
    parser.add_argument('--operation', nargs='*',type=str, default=['less than','equal','greater than','value'], help='param_name is mandatory to check operation')
    args=parser.parse_args()

    def check_pagination(endpoint):
        # checks for limit, page, offset values, if they are provided
        # appends query parameter to endpoint
        if args.limit:
            endpoint+="?limit={}".format(args.limit)
            return endpoint
        if args.page:
            endpoint+="?page={}".format(args.page)
            return endpoint
        if args.offset:
            endpoint+="?offset={}".format(args.offset)
            return endpoint
    def check_sorting(endpoint):
        # if sort is true ,use --param_name to sort in ascending order
        # if sort is false, user --param_name to sort in descending order
        # check to make sure param_name is provided, otherwise return error
        if args.sort and not args.param_name:
            print ("parameter name is required to sort parameter in ascending or descending order.")
        elif args.sort and args.param_name:
            endpoint+="?sort={}:asc".format(args.param_name)
            return endpoint
        elif args.sort and not args.param_name:
            endpoint+="?sort={}:desc".format(args.param_name)
            return endpoint 

    def check_filtering(endpoint):
        # filter
        if (args.param_exists or args.param_notexists or args.param_match or args.param_notmatch) and not args.param_name:
            print ("parameter name is required to sort parameter in ascending or descending order.")
        elif args.param_match and args.exists:
            endpoint+="?{}={}".format(args.param_name,args.match_str)
            return endpoint
        elif args.param_notmatch or args.param_exclude or args.param_notexists:
            endpoint+="?{}!={}".format(args.param_name,args.match_str)
            return endpoint
        elif args.param_regex:
            endpoint+="?{}={}".format(args.param_name,args.match_str)
            return endpoint
        elif args.param_noregex:
            endpoint+="?{}!={}".format(args.param_name,args.match_str)
            return endpoint  
        elif args.operation and args.value:
            operation = args.operation
            if operation == "less than":
                endpoint+="?{}<{}".format(args.param_name,args.value)
            elif operation == "greater than":
                endpoint+="?{}>{}".format(args.param_name,args.value)
            elif operation == "equal":
                endpoint+="?{}=>{}".format(args.param_name,args.value)
            return endpoint
    def movies_get(id=None,quote=False):
        # call API endpoints based on arguments
        
        # use requests to call API
        endpoint = "https://the-one-api.dev/v2/movie"
       
        
        headers = {"Authorization": "Bearer {}".format(args.token)}
                
        if id is None and not quote:
            print (endpoint)
            # gets movie GET for all movies
            if args.limit or args.offset or args.page:
                endpoint = check_pagination(endpoint)
            if args.sort:
                endpoint = check_sorting(endpoint)
            
            #endpoint = check_filtering(endpoint)
            print (endpoint)
            print ( requests.get(endpoint,headers=headers).json())
        elif id and not quote:
            # return specified movie 
            endpoint+="/{}".format(str(id))
            if args.limit or args.offset or args.page:
                endpoint = check_pagination(endpoint)
            if args.sort:
                endpoint = check_sorting(endpoint)
            endpoint = check_filtering(endpoint)
            print (requests.get(endpoint,headers=headers).json())
        elif id and quote:
            #calculate quote
            endpoint+="/{}/quote".format(str(id))
            if args.limit or args.offset or args.page:
                endpoint = check_pagination(endpoint)
            if args.sort:
                endpoint = check_sorting(endpoint)
            if args.param_match or  args.param_nomatch or args.param_include or  args.param_exclude or args.param_exists or args.param_notexists:
                endpoint =check_filtering(endpoint)

            print ( requests.get(endpoint,headers=headers).json())    
    #if --quote is passed and no movie_id, return error
    if args.quote and not args.movie_id:
        print ( "Movie id is mandatory to get quote for specific movie using API")
    
    elif args.movie_id and not args.quote :
        # use curl to call API that returns information for specic id
        return movies_get(id=args.movie_id)
    elif args.movie_id and args.quote:
        return movies_get(id=args.movie_id, quote = True) 
    else:
       # use curl to call API that returns all movies
       return movies_get()           
    
if __name__ == "__main__":
    main()

