import hypernetx as hnx

def two_rows(decomposed_edges, labels, nodecolor=None, nodeorder=None, nodesize=0.1, column_spacing=1,
                                subplot_width=14, subplot_height=3):
    '''
    decomposed_edges : dict, {order : edges (list of tuples)}
    '''

    nrows = len(decomposed_edges.keys())
    fig, axs = plt.subplots(nrows, 1, figsize=(subplot_width, nrows * subplot_height))

    for n, order in enumerate(decomposed_edges.keys()):
        H = hnx.Hypergraph(decomposed_edges[order])

        hnx.drawing.two_column.draw(H, labels, with_edge_labels=False, with_color=False, ax=axs[n],
                                    column_spacing=column_spacing,
                                    flip_orientation=True, edgecolor='tab:blue', nodecolor=nodecolor,
                                    nodeorder=nodeorder, nodesize=nodesize)

        axs[n].set_title(f'Multiplet Order: {order}', fontsize=16)

    #     axs[n].set_xlim(0,20)
    #     axs[n].set_ylim(-1,1)

    plt.tight_layout()

    # plt.savefig('two_rows.png', dpi=400)