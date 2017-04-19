import webbrowser


class Movie():
	'''initialize a movie object with title, length, release year description,
	   poster image, and youtube trailer
	   '''
	def __init__(self, title, length, year, description, poster_image_url,
				 trailer_youtube_url):
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.year = year
		self.title = title
		self.length = length
		self.description = description


def list_youtube(movies):
	'''used for debugging only
	'''
	for movie in movies:
		print movie.title + ':' + movie.trailer_youtube_url
