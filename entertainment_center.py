import fresh_tomatoes
import media 

fried_green = media.Movie("Fried Green Tomatoes", 
						  "Evelyn feels stuck in a marriage that's long lost its spark and finds the courage to take control of her life through the stories her friend Ms. Threadgood tells her of two women in the 1930's.", 
						  "http://cdn.playbuzz.com/cdn/b37e8846-a42d-4988-8bf7-c0915f3634d9/95ad624b-1c4d-48ef-840e-aa8f7c372cd1.jpg",
						  "https://www.youtube.com/watch?v=wwYDQG0c-cs")

prenom = media.Movie("Le Prenom",
					 "A dinner between friends turns dramatic when Vincent reveals the name of the baby he and his wife are expecting.",
					 "http://www.bruel.be/films/affiches/aff_prenom_pre2_grand.jpg",
					 "https://www.youtube.com/watch?v=FX2ukwKgWlo")

placard = media.Movie("Le Placard",
					  "An accountant at a condom factory fakes coming out to save his job with unexpected consequences.",
					  "http://fr.web.img3.acsta.net/r_640_600/b_1_d6d6d6/medias/nmedia/18/36/38/15/19649866.jpg",
					  "https://www.youtube.com/watch?v=EetZcl4KBLk")

harry_potter = media.Movie("Harry Potter and the Sorcerer's Stone",
						   "Where Hermione's battle against the patriarchy began.",
						   "http://img2.wikia.nocookie.net/__cb20101208171110/harrypotter/images/0/0e/Philostone.jpg",
						   "https://www.youtube.com/watch?v=JXWBuoYc8SI")

mean_girls = media.Movie("Mean Girls",
						 "After being homeschooled in Africa, Cady Heron discovers the social heirarchy of the American high school.",
						 "http://www.movpins.com/big/MV5BMjE1MDQ4MjI1OV5BMl5BanBnXkFtZTcwNzcwODAzMw/mean-girls-(2004).jpg",
						 "https://www.youtube.com/watch?v=KAOmTMCtGkI")

philadelphia_story = media.Movie("The Philadelphia Story",
								 "A Philadelphia socialite, her wealthy fiance, her alcoholic ex, and an unassuming journalist sort out their affections on the eve of her wedding.",
								 "http://www.reviewstl.com/wp-content/uploads/2015/02/the-philadelphia-story-poster-large.jpg",
								 "https://www.youtube.com/watch?v=6CtquHsxoZo")

movies = [fried_green, placard, prenom, harry_potter,mean_girls, philadelphia_story]

fresh_tomatoes.open_movies_page(movies)