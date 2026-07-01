magicians = ['messi', 'maradona', 'zidan', 'ronaldinho']

def make_great(magicians) :
    for i in range(len(magicians)) :
        magicians[i] = "the Great " + magicians[i] 

def show_magicians(magicians) :
    for magician in magicians :
        print("Hello " + magician.title() + 
            ", I enjoyed the show you put on.")
        

make_great(magicians)
show_magicians(magicians)


