def plot_hypergraph_areas(decomposed_edges, labelslist, edgecolor=None, nodecolor=None, linewidth=1):
    nrows = len(decomposed_edges.keys())
    fig, axs = plt.subplots(1, nrows, figsize=(5 * nrows, 5))

    orders = decomposed_edges.keys()
    for n, order in enumerate(orders):
        H = hnx.Hypergraph(decomposed_edges[order])

        if len(decomposed_edges[order]) == 0:
            hnx.drawing.draw(H, ax=axs[n])
            axs[n].set_title(f'Multiplet Order: {order}')
            print(f'Order {order} has no edges.')
        else:
            # get vals
            if edgecolor is None:
                edges_kwargs = {}
            elif isinstance(edgecolor, dict):
                cmap = plt.cm.viridis
                alpha = .8
                edge_elements = [tuple(H.edges[edge].elements) for edge in H.edges]
                vals = np.array([edgecolor[e] for e in edge_elements])
                norm = plt.Normalize(vals.min(), vals.max())
                edgecolor = cmap(norm(vals)) * (1, 1, 1, alpha)
                edges_kwargs = dict(edgecolors=edgecolor, linewidth=linewidth)
            else:
                edges_kwargs = dict(edgecolors=edgecolor, linewidth=linewidth)

            if nodecolor is None:
                nodecolor = 'black'
            if isinstance(nodecolor, dict):
                nodes = list(H.nodes)
                nodecol_nodes = np.array([nodecolor[labelslist.index(nodes[node])] for node in range(len(nodes))])

            hnx.drawing.draw(H,
                             label_alpha=0,
                             with_edge_labels=False,
                             with_node_labels=True,
                             nodes_kwargs={
                                 'facecolors': nodecol_nodes
                             },
                             edges_kwargs=edges_kwargs,
                             node_labels_kwargs={
                                 'fontsize': 14,
                             },
                             ax=axs[n])

            axs[n].set_title(f'Multiplet Order: {order}')
#     plt.savefig('hypergraph.png', dpi=400)