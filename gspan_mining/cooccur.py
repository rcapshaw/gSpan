from collections import defaultdict, Counter
import qgrid
import pandas as pd
from gspan import gSpan, PDFS, Projected


if __name__ == '__main__':

    min_support = 1
    alt = True

    gs = gSpan(
        database_file_name='/data/experiments/DocRED/DataViewer/results/docred_train.data',
        min_support=min_support,
        min_num_vertices=2,
        # max_num_vertices=3,
        min_num_edges=1,
        max_ngraphs=10,
        is_undirected=False,
        verbose=False,
        visualize=False,
        where=True,
        alternative_support=alt
    )

    """Run the gSpan algorithm."""
    # gathered = gs.run(gather=True)
    # print(len(gathered))
    # print(list(pdfs.edge for pdfs in gathered[0]))
    gs.run()
    print(gs._report_df)
    gs._report_df.to_pickle(f'all_patterns_support_{min_support}{"_alt" if alt else ""}.pkl')

    widget = qgrid.show_grid(gs._report_df)
    display(widget)



    # print("IoU correlation (symmetric)")
    # intersection_support = min_support
    # iou_support = 0.70

    # for i, g1 in enumerate(gathered):
    #     for j, g2 in enumerate(gathered):
    #         if j <= i:
    #             continue
    #         # Method 1: Document-level
    #         a = [pdfs.gid for pdfs in g1]
    #         b = [pdfs.gid for pdfs in g2]
    #         it = len(set(a) & set(b))
    #         if it < intersection_support:
    #             continue
    #         un = len(set(a) | set(b))
    #         iou = it/un
    #         if iou < iou_support:
    #             continue
    #         print(f'{i}&{j}:{it}, {un}, {iou:.2f}')
    #
    # print("="*20)
    #
    # for i, g1 in enumerate(gathered):
    #     for j, g2 in enumerate(gathered):
    #         if j <= i:
    #             continue
    #         # Method 2: Instance-level
    #         a = [pdfs.gid for pdfs in g1]
    #         b = [pdfs.gid for pdfs in g2]
    #         a = Counter(a)
    #         b = Counter(b)
    #         c = list((Counter(a) & Counter(b)).elements())
    #         it = sum((a & b).values())
    #         if it < intersection_support:
    #             continue
    #         un = sum((a | b).values())
    #         iou = it/un
    #         if iou < iou_support:
    #             continue
    #         print(f'{i}&{j}:{it}, {un}, {iou:.2f}')
    # print("=" * 20)
    # print("=" * 20)
    # print("Percentage correlation (asymmetric)")
    # intersection_support = min_support
    # p_support = 0.70
    #
    # for i, g1 in enumerate(gathered):
    #     for j, g2 in enumerate(gathered):
    #         if j == i:
    #             continue
    #         # Method 1: Document-level
    #         a = [pdfs.gid for pdfs in g1]
    #         b = [pdfs.gid for pdfs in g2]
    #         it = len(set(a) & set(b))
    #         if it < intersection_support:
    #             continue
    #         un = len(set(a))
    #         p = it / un
    #         if p < p_support:
    #             continue
    #         print(f'{i}x{j}:{it}, {un}, {p:.2f}')
    #
    # print("=" * 20)
    #
    # for i, g1 in enumerate(gathered):
    #     for j, g2 in enumerate(gathered):
    #         if j == i:
    #             continue
    #         # Method 2: Instance-level
    #         a = [pdfs.gid for pdfs in g1]
    #         b = [pdfs.gid for pdfs in g2]
    #         a = Counter(a)
    #         b = Counter(b)
    #         c = list((Counter(a) & Counter(b)).elements())
    #         it = sum((a & b).values())
    #         if it < intersection_support:
    #             continue
    #         un = sum(a.values())
    #         p = it / un
    #         if p < p_support:
    #             continue
    #         print(f'{i}x{j}:{it}, {un}, {p:.2f}')





    # gs.run()

    # print(gathered)
