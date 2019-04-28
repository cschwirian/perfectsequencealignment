from utility import *


class Node:

    def __init__( self, mer ):
        self.mer = mer
        self.children = []


def search( mer_node_list, mer ):

    for index in range( len( mer_node_list ) ):
        if( mer_node_list[index].mer == mer ):
            return mer_node_list[index]

    return None


def tree_from_sequence( sequence, k ):

    mers = k_mers( sequence, k )

    root = Node( mers[0] )

    mer_node_list = [root]

    for index in range( 1, len( mers ) ):
        prev_mer = mers[index - 1]
        current_mer = mers[index]
        prev_node = search( mer_node_list, prev_mer )
        current_node = search( mer_node_list, current_mer )

        if( current_node != None ):
            prev_node.children.append( current_node )
        else:
            new_node = Node( current_mer )
            prev_node.children.append( new_node )
            mer_node_list.append( new_node )

    return root


def sequence_from_tree( root ):

    sequence = root.mer[0:len(root.mer) - 1]
    current_node = root

    while( current_node.children ):
        sequence += current_node.mer[-1]
        current_node = current_node.children.pop( 0 )

    sequence += current_node.mer[-1]

    return sequence


def psa( filename, k ):

    print( "Reading FASTA data...", end="" )
    sequence_data = read_fasta( filename )
    sequence = sequence_data[list(sequence_data)[0]]
    print( "Done." )

    print( "Assembling de Bruijn graph... ", end="" )
    root = tree_from_sequence( sequence, k )
    print( "Done." )

    print( "Assembling sequence from de Bruijn graph... ", end="" )
    assembled_sequence = sequence_from_tree( root )
    print( "Done." )

    if( sequence == assembled_sequence ):
        print( "Sequence assembled successfully." )
    else:
        print( "Sequence assembly failed." )




if( __name__ == "__main__" ):

    psa( "sequences/test3.fasta", 40 )
