# Simple node to contain mer data as well as ordered list of node's children to
# assist with assembly.
class Node:

    def __init__( self, mer ):
        self.mer = mer
        self.children = []


# Iteratively searches a list of mer nodes as recursive searching produced
# recursion depth limit errors.
def search( mer_node_list, mer ):

    for index in range( len( mer_node_list ) ):
        if( mer_node_list[index].mer == mer ):
            return mer_node_list[index]

    return None


# Builds temporary list of mer nodes to allow for iterative searching as
# recursive searching produced recursion depth limit errors.
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


# Build sequence from tree iteratively.
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
    print( "Done.", flush=True )

    print( "Assembling de Bruijn graph... ", end="", flush=True )
    root = tree_from_sequence( sequence, k )
    print( "Done.", flush=True )

    print( "Assembling sequence from de Bruijn graph... ", end="", flush=True )
    assembled_sequence = sequence_from_tree( root )
    print( "Done.", flush=True )

    if( sequence == assembled_sequence ):
        print( "Sequence assembled successfully.", flush=True )
    else:
        print( "Sequence assembly failed.", flush=True )


# Utility Functions
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




if( __name__ == "__main__" ):

    psa( "sequences/NC_004722.fasta", 40 )
