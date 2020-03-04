# Movie Ratings!

#  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:

# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.

rating = input("""
Out of the following ratings, how would you rate the film?
PG, 12, 15, 18
> """)

if rating.upper() == "PG":
    print("You selected PG")
elif rating == "12":
    print("You selected 12")
elif rating == "15":
    print("You selected 15")
elif rating == "18":
    print("You selected 18")
