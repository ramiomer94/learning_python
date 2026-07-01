def make_album(artist_name, album_title, number_tracks='') :
    album = {'artist' : artist_name, 'title' : album_title}
    if number_tracks :
        album['n_tracks'] = number_tracks
    return album

album_0 = make_album('drake', 'views')
print(album_0)

album_1 = make_album('post malone', 'stoney')
print(album_1)

album_2 = make_album('dua lipa', 'cool')
print(album_2)

album_3 = make_album('juice wrld', 'goodbye & good riddance', number_tracks=16)
print(album_3)

while True :
    print("\nplease enter your favorite album's information")
    print("(enter 'q' at any time to quit)")

    artist_n = input("Please enter artist's name: ")
    if artist_n == 'q' :
        break
    
    a_title = input("Please enter the album's title: ")
    if a_title == 'q' :
        break

    album_info = make_album(artist_n, a_title)
    print(album_info)