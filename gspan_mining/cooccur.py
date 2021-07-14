from collections import defaultdict

from gspan import gSpan, PDFS, Projected


if __name__ == '__main__':
    gs = gSpan(
        database_file_name='/data/experiments/DocRED/DataViewer/results/docred_train.data',
        min_support=10,
        min_num_vertices=2,
        max_num_vertices=float('inf'),
        min_num_edges=1,
        max_ngraphs=float('inf'),
        is_undirected=False,
        verbose=False,
        visualize=False,
        where=True
    )

    """Run the gSpan algorithm."""
    gathered = gs.run(gather=True)
    print(len(gathered))

    for g in gathered:
        print(gs._get_support(g))


    # print(gathered)
