import matplotlib.pyplot as plt
import networkx as nx
from networkx import NetworkXException

import hyperplot.tools

def planar(decomposed_edges, nodes=None, nodelabels=None):
    '''
    Plots hypergraph using random planar layout.

    Parameters
    ----------
    decomposed_edges : dict ({order : list of edges})
        dictionary with list of edges for each multiplet order

    nodelabels : dict
        dictionary from node to node label

    '''
    ncols = len(decomposed_edges.keys())

    # Setup multiplot style
    fig, axs = plt.subplots(1, ncols, figsize=(5 * ncols, 5))
    if ncols == 1:
        axs = [axs]  # Ugly hack
    for ax in axs:
        ax.axis('off')
    #     fig.patch.set_facecolor('#003049')

    orders = decomposed_edges.keys()

    if nodes is None:
        tmp = [[list(e) for e in edges] for edges in decomposed_edges.values()]
        nodes = list(set(sum(sum(tmp, []), [])))

    if nodelabels is not None:
        nodes = [nodelabels[n] for n in nodes]

    for n, order in enumerate(orders):
        edges = decomposed_edges[order]

        if nodelabels is not None:
            # refactors edge names in 'decomposed_edges' and 'nodecolor' using 'nodelabels'
            edges = [tuple([nodelabels[e] for e in edge]) for edge in edges]

        g = hyperplot.tools.create_hypergraph(nodes, edges, remove_isolated_nodes=True)

        # I like planar layout, but it cannot be used in general
        try:
            pos = nx.planar_layout(g)
        except NetworkXException:
            pos = nx.spring_layout(g, k=1)

        # Plot true nodes in orange, star-expansion edges in red
        nodes = g.connected_nodes
        extra_nodes = set(g.nodes) - set(g.connected_nodes)
        nx.draw_networkx_nodes(g, pos, node_size=200, nodelist=nodes,
                               ax=axs[n], node_color='#f77f00')
        nx.draw_networkx_nodes(g, pos, node_size=100, nodelist=extra_nodes,
                               ax=axs[n], node_color='#3486eb')
        nx.draw_networkx_edges(g, pos, ax=axs[n], edge_color='#3486eb',
                               connectionstyle='arc3,rad=0.05', arrowstyle='-')

        # Draw labels only for true nodes
        labels = {node: str(node) for node in nodes}
        nx.draw_networkx_labels(g, pos, labels, ax=axs[n])

        axs[n].set_title(f'Multiplet Order: {n + 3}')