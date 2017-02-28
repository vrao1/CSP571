import imdb  #IMDB package 
import json	 #To save the output
import time	 #To set sleep time 

def movie_info(id):  #function that will get the data
	director_list=[] #list for saving multiple director names
	writer_list=[]	 #list for saving multiple writer names
	cast_list=[]	 #list for saving multiple cast names
	cert_list=[]	 #list for saving multiple certifications
	gen_list=[] 	 #list for saving multiple genres

	i=imdb.IMDb()  	#instance
	item = i.get_movie(id) #getting movie object into item variable 

	try:
		title = item["title"]	#get the title
	except:
		title=None

	try:	
		year=item.get('year') 	#get the year
	except:
		year=None

	try:
		rating= item["rating"]	 #get the rating
	except:
		rating=None

	try:
		director=item["director"]	 #get the director(s)
		num_dir=len(director)		#check how many names are there
		for i in range(num_dir): #separate names and save in list
			dir=director[i]
			dir_n=dir['name']
			director_list.append(dir_n)
	except:
		director_list=None

	try:
		writer=item["writer"] 		#get the writer(s)
		num_wir=len(writer)	  	 	#check how many names are there
		for i in range(num_wir):	#separate names and save in list
			wri=writer[i]
			wri_n=wri['name']
			writer_list.append(wri_n)
	except:
		writer_list=None

	try:
		cast=item["cast"]			#get the cast
		num_cast=len(cast)			#check how many names are there
		for i in range(num_cast):	#separate names and save in list
			cst=cast[i]
			cst_n=cst['name']
			cast_list.append(cst_n)
	except:
		cast_list=None

	try:
		runtime= item["runtime"] 	#get the runtime
	except:
		runtime=None

	try:
		mpaa=item.get('mpaa')		#get MPAA
	except:
		mpaa=None

	try:
		certification=item["certification"] 	#get the certifications
		num_cer=len(certification)				#check how many are there
		for i in range(num_cer):				#separate them
			cert_list.append(certification[i])
	except:
		cert_list=None

	try:
		poster= item.get('full-size cover url')  #get the poster image url
	except:
		poster=None
	try:
		kind= item.get('kind') 				#get the type of the item
	except:
		kind=None
	try:
		genre=item["genre"]					#get the genres
		num_gen=len(genre)					#check how many are there
		for i in range(num_gen):			#separate them
			gen_list.append(genre[i])
	except:
		gen_list=None

	#create a dictionary to make saving in json easy
	moviess= dict([('id', id),('title', title),('year',year),('rating', rating),('director', director_list),('writer', writer_list),('cast', cast_list),
	('runtime', runtime),('kind',kind),('mpaa',mpaa),('certification', cert_list),('poster',poster),('genre', gen_list)])	
	#open output file and write the output
	with open('moviesdata.json', 'a+') as fp:
		json.dump(moviess, fp)
	print "finished writing", id
		
def load_movie_ids():		#load the ids 
    try:
        with open("sampleIds.txt", "r") as f:
            if f.mode == 'r':
				movieids =f.read()
				movie_ints = [ int(x) for x in movieids.split() ]	#converting to int as get_movie reads int input
				return movie_ints
    except:
        print "Cannot load the movie metadata file!"
        return None

def get_data():			#call function for ids in loop with sleep time
    movieids = load_movie_ids()
    for j in movieids:
		time.sleep(10)
		movie_info(j)
	
get_data()