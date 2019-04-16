def read_fasta( filename, text=True ):

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

    mers = []

    for index in range( len( sequence ) - k + 1 ):
        mers.append( sequence[index:index + k] )

    return mers
