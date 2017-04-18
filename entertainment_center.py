import fresh_tomatoes
import media

lucky_number_sleven=media.Movie('Lucky Number Slevin', '110 minutes', '2007'
,'''A case of mistaken identity lands Slevin into the middle of a war being
plotted by two of the city\'s most rival crime bosses.''',
'''https://images-na.ssl-images-amazon.com/images/M/MV5BZjczMWI1YWMtYTZjOS00ZDc5LWE2MWItMTY3ZGUxNzFkNjJmL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,675,1000_AL_.jpg'''
,'https://www.youtube.com/watch?v=fVIUEcizkPc')

goodfellas=media.Movie('GoodFellas', '146 minutes', '1990'
, 'Henry Hill and his friends work their way up through the mob hierarchy.'
,'''https://images-na.ssl-images-amazon.com/images/M/MV5BNThjMzczMjctZmIwOC00NTQ4LWJhZWItZDdhNTk5ZTdiMWFlXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,669,1000_AL_.jpg'''
,'https://www.youtube.com/watch?v=qo5jJpHtI1Y')

extremely_loud=media.Movie('Extremely Loud & Incredibly Close', '129 minutes'
,'2011', '''A nine-year-old amateur inventor, Francophile, and pacifist searches
 New York City for the lock that matches a mysterious key left behind by his
 father, who died in the World Trade Center on September 11, 2001.'''
,'''https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzYwMTE3NV5BMl5BanBnXkFtZTcwMDY2NzU4Ng@@._V1_.jpg'''
,'https://www.youtube.com/watch?v=51z9UzDSacg')

eternal_sunshine=media.Movie('Eternal Sunshine of the Spotless Mind'
, '108 minutes', '2004', '''When their relationship turns sour, a couple
undergoes a procedure to have each other erased from their memories. But it
is only through the process of loss that they discover what they had to begin
with.'''
,'''https://images-na.ssl-images-amazon.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg'''
,'https://www.youtube.com/watch?v=rb9a00bXf-U')

cube=media.Movie("Cube", '90 minutes', '1997', '''Six complete strangers of
widely varying personality characteristics are involuntarily placed in an
endless kafkaesque maze containing deadly traps.'''
,'''https://images-na.ssl-images-amazon.com/images/M/MV5BZTIyZGM3NDItMTNmNS00Yzc4LTg2MzItOWY4MTE1NDlmZDIyXkEyXkFqcGdeQXVyMTAwMzUyOTc@._V1_.jpg'''
,'https://www.youtube.com/watch?v=YAWSkYqqkMA')

the_departed=media.Movie('The Departed', '151 minutes', '2006','''An undercover cop and
a mole in the police attempt to identify each other while infiltrating an
Irish gang in South Boston.'''
,'''https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_.jpg'''
,'https://www.youtube.com/watch?v=n4O3x5BH18E')

movies=[lucky_number_sleven, goodfellas, extremely_loud, eternal_sunshine, cube, the_departed]


fresh_tomatoes.open_movies_page(movies)
