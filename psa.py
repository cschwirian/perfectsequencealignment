from utility import *


class Node:

    def __init__( self, mer ):
        self.mer = mer
        self.children = []


def search( root, mer ):

    if( root.mer == mer ):
        return root
    else:
        return search_helper( root, mer )


def search_helper( root, mer ):

    if( not root.children ):
        return None

    for child in root.children:
        if( child.mer == mer ):
            return child

        result = search_helper( child, mer )
        if( result != None ):
            return result

    return None


def tree_from_sequence( sequence, k ):

    k_mers = k_mers( sequence, k )

    root = None( k_mers[0] )

    for index in range( 1, len( k_mers ) ):
        prev_mer = k_mers[index - 1]
        current_mer = k_mers[index]
        prev_node = search( root, prev_mer )
        current_node = search( root, current_mer )

        if( current_node != None ):
            prev_node.children.append( current_node )
        else:
            prev_node.children.append( Node( current_mer ) )

    return root


def sequence_from_tree( root ):

    sequence = root.mer[0:len(root.mer) - 1]
    sequence += sequence_helper( root )
    return sequence

def sequence_helper( root ):

    if( not root.children ):
        return root.name[-1]

    next_node = root.children[0]
    root.children.pop( 0 )

    return root.name[-1] + sequence_helper( next_node )


def psa( filename, k ):

    sequence_data = read_fasta( filename )
    sequence = list(sequence_data)[0]

    root = tree_from_sequence( sequence, k )
    assembled_sequence = sequence_from_tree( root )

    print( sequence == assembled_sequence )





if( __name__ == "__main__" ):

    psa( "sequences/NC_004722.fasta", 50 )
