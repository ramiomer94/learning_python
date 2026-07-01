def make_great(magicians) :
    great_magicians = []
    for magician in magicians :
        great_magicians.append("the Great " + magician)
    return great_magicians

        

def show_magicians(magicians) :
    for magician in magicians :
        print("Hello " + magician.title() + 
            ", I enjoyed the show you put on.")
        

magicians_list = ['messi', 'maradona', 'zidan', 'ronaldinho']
modified_magicians_list = make_great(magicians_list[:])

print("\nThe following is the original magicians list: ")
show_magicians(magicians_list)

print("\nThe following is the list of the modified magicians list: ")
show_magicians(modified_magicians_list)


