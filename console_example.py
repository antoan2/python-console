#!/usr/bin/env python2.7
# Simple example of a command line tool that just list the movies or display the movie id
import cmd
from tabulate import tabulate

MOVIES = {1: 'batman', 2: 'robin_et_batman', 3: 'batman_et_robin'}
NAMES_TO_ID = {movie_name: movie_id for movie_id, movie_name in MOVIES.items()}

print "The database of movies:"
print tabulate(MOVIES.items())

class Shell(cmd.Cmd):

    MOVIES = MOVIES
    NAMES_TO_ID = NAMES_TO_ID

    intro = "Welcome message ! Type help for more infos"
    prompt = "(Simple example RFFP) "

    # Get all movies function
    def do_get_movies(self, arg):
        print tabulate(self.MOVIES.items())

    def help_get_movies(self, arg):
        print "Get all movies"

    # Get the id of a specific movie
    def do_get_movie(self, movie_name):
        print 'movie_name :', movie_name
        print 'movie_id : ', self.NAMES_TO_ID[movie_name]

    def help_get_movie(self):
        print 'Display the name and the id of the selected movie'

    def complete_get_movie(self, text, line, begidx, endidx):
        if not text:
            completions = self.NAMES_TO_ID.keys()
        else:
            completions = [ f
                            for f in self.NAMES_TO_ID
                            if f.startswith(text)
                            ]
        return completions

    def do_exit(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('Good bye !')
        return True

    def do_EOF(self, arg):
        print "exit"
        return self.do_exit(arg)

if __name__=="__main__":
    Shell().cmdloop()
