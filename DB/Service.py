from Actor import Actor

class Service:
    
    def main():
        print(Actor.getAllActors())
        print(Actor.getMoviesByActor('THORA', 'TEMPLE'))
        print(Actor.getMoviesByYear('THORA', 'TEMPLE'))
        print(Actor.getActorsByDirector('JAMES CAMERON'))


if __name__ == "__main__":
    Service.main()