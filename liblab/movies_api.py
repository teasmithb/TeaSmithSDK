

from argparse import ArgumentParser
import requests


def main():
    # parse arguments from user
    parser = ArgumentParser(description="Communicate with Lords of the Rings API .")
    parser.add_argument('token',type=str, help='unique token to authenticate caller ')
    parser.add_argument('--movie_id', type=str, help='specified movie id, if not provided all movies will be returned')
    parser.add_argument('--quote', action="store_true", help='returns quote for the book specified,movie_id here is mandatory argument')
    args=parser.parse_args()
    

    def movies_get(id=None,quote=False):
        # call API endpoints based on arguments
        
        # use requests to call API
        endpoint = "https://the-one-api.dev/v2/movie"
        headers = {"Authorization": "Bearer {}".format(args.token)}
                
        if id is None and not quote:
            # gets movie GET for all movies
            print ( requests.get(endpoint,headers=headers).json())
        elif id and not quote:
            # return specified movie 
            endpoint+="/{}".format(str(id))
            print (requests.get(endpoint,headers=headers).json())
        elif id and quote:
            #calculate quote
            endpoint+="/{}/quote".format(str(id))
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

