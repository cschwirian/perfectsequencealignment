from utility import *


class Node:

    def __init__( self ):
        self.name = "test"


def psa( filename, k ):

    sequence_data = read_fasta( filename )
    sequence = list(sequence_data)[0]

    k_mers = k_mers( sequence, k )

    print( k_mers )



if( __name__ == "__main__" ):

    psa( "sequences/NC_004722.fasta", 50 )
