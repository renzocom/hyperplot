import matplotlib.pyplot as plt
import networkx as nx
from networkx import NetworkXException

def planar(hypergraph):
    '''
    Plots hypergraph using random planar layout.

    Parameters
    ----------
    hypergraph : dict
        decomposed hypergraph. dict from order to hypergraph.

    '''
    ncols = len(hypergraph.keys())

    # Setup multiplot style
    fig, axs = plt.subplots(1, ncols, figsize=(5 * ncols, 5))
    if ncols == 1:
        axs = [axs]  # Ugly hack
    for ax in axs:
        ax.axis('off')
    #     fig.patch.set_facecolor('#003049')

    for i, g in enumerate(hypergraph.values()):

        # I like planar layout, but it cannot be used in general
        try:
            pos = nx.planar_layout(g)
        except NetworkXException:
            pos = nx.spring_layout(g, k=1)

        # Plot true nodes in orange, star-expansion edges in red
        nodes = g.connected_nodes
        extra_nodes = set(g.nodes) - set(g.connected_nodes)
        nx.draw_networkx_nodes(g, pos, node_size=200, nodelist=nodes,
                               ax=axs[i], node_color='#f77f00')
        nx.draw_networkx_nodes(g, pos, node_size=100, nodelist=extra_nodes,
                               ax=axs[i], node_color='#3486eb')

        nx.draw_networkx_edges(g, pos, ax=axs[i], edge_color='#3486eb',
                               connectionstyle='arc3,rad=0.05', arrowstyle='-')

        # Draw labels only for true nodes
        labels = {node: str(node) for node in nodes}
        nx.draw_networkx_labels(g, pos, labels, ax=axs[i])

        axs[i].set_title(f'Multiplet Order: {i + 3}')