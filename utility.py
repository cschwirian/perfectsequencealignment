def read_fasta( filename, text=False ):

    if( text ):
        with open( filename, "rb" ) as sequence:
            header = sequence.readline().replace( b"\n", b"" ).replace( b">", b"" )
            sequence_string = sequence.read().replace( b"\n", b"" )
            return { header: sequence_string }
    else:
        with open( filename, "r" ) as sequence:
            header = sequence.readline().replace( "\n", "" ).replace( ">", "" )
            sequence_string = sequence.read().replace( "\n", "" )
            return { header: sequence_string }


def k_mers( sequence, k ):

    mer_list = []

    for index in range( len( sequence ) ):
        substring = sequence[index:index + k]
        if( len( substring ) != k ):
            break
        mer_list.append( substring )

    return mer_list
