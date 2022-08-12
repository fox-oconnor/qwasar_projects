# Create a backend app with a light web framework. 
# It will listen on port 8000. 
# All routes will answer in JSON format.
# Parse provided CSV.  
# Backend will serve six routes:
#   GET on / 
#       This route will parse the GET parameter genre, to be able to filter by movie genre.
#       curl "http://localhost:8080?genre=action"
#   GET on /action
#       This route will only serve action movies.
#       curl "http://localhost:8080/action" 
#   GET on /adventure
#       This route will only serve adventure movies. 
#       curl "http://localhost:8080/adventure"
#   GET on /comedy
#       This route will serve only comedy movies.
#       curl "http://localhost:8080/comedy"
#   GET on /drama
#       This route will serve only drama movies. 
#       curl "http://localhost:8080/drama"
#   GET on /romance
#       This route will only serve romance movies.  
#       curl "http://localhost:8080/romance" 


