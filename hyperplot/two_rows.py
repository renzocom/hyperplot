import hypernetx as hnx
import matplotlib.pyplot as plt

def two_rows(decomposed_edges, nodelabels=None, nodecolors=None, nodeorder=None, nodesize=0.1, column_spacing=1,
                                subplot_width=14, subplot_height=3):
    '''
    Plots hypergraph using bipartite two row layout, where in the bottom row contains the
    nodes and the top row the edges.

    Parameters
    ----------
    decomposed_edges : dict ({order : list of edges})
        dictionary with list of edges for each multiplet order

    nodelabels : dict
        dictionary from node to node label

    nodecolors : dict
        dictionary from node to color
    nodeorder
    nodesize : float
    column_spacing : float
    subplot_width : int
    subplot_height : int

    Returns
    -------

    '''

    nrows = len(decomposed_edges.keys())
    fig, axs = plt.subplots(nrows, 1, figsize=(subplot_width, nrows * subplot_height))

    if nodelabels is not None:
        nodecolors = {nodelabels[node]: color for node, color in nodecolors.items()}

    for n, order in enumerate(decomposed_edges.keys()):
        edges = decomposed_edges[order]
        if nodelabels is not None:
            # refactors edge names in 'decomposed_edges' and 'nodecolor' using 'nodelabels'
            edges = [tuple([nodelabels[e] for e in edge]) for edge in edges]
        H = hnx.Hypergraph(edges)
        hnx.drawing.two_column.draw(H,
                                    with_node_labels=True,
                                    with_edge_labels=False,
                                    with_color=False,
                                    ax=axs[n],
                                    column_spacing=column_spacing,
                                    flip_orientation=True,
                                    edgecolor='tab:blue',
                                    nodecolor=nodecolors,
                                    nodeorder=nodeorder,
                                    nodesize=nodesize)

        axs[n].set_title(f'Multiplet Order: {order}', fontsize=16)

    #     axs[n].set_xlim(0,20)
    #     axs[n].set_ylim(-1,1)

    plt.tight_layout()

    # plt.savefig('two_rows.png', dpi=400)