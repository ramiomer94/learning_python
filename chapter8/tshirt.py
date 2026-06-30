def make_shirt(size, message) :
    print("The size of the t-shirt is " + size + "." +
        "\nThe message printed on the t-shirt is: " +
        "'" + message + "'")

make_shirt('medium', 'Why always me?')
make_shirt(message='Why always me?', size='large')

def make_shirt(size='Large', message='I love Python') :
    print("The size of the t-shirt is " + size + "." +
        "\nThe message printed on the t-shirt is: " +
        "'" + message + "'")

make_shirt();
make_shirt(size='Medium')

make_shirt(message='I love C')
make_shirt(size='Small', message='I love Java')