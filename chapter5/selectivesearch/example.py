# -*- coding: utf-8 -*-
import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch
from skimage import io


def main():

    img = io.imread("../example/person.jpg")  # 载入图片

    # perform selective search
    img_lbl, regions = selectivesearch.selective_search(
        img, scale=500, sigma=0.9, min_size=10)

    # 根据具体情况过滤找到的区域
    candidates = set()
    for r in regions:
        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            continue
        # excluding regions smaller than 2000 pixels
        if r['size'] < 100:
            continue
        # distorted rects
        # x, y, w, h = r['rect']
        # if w / h > 1.2 or h / w > 1.2:
            # continue
        candidates.add(r['rect'])

    print(regions)
    # 显示通过selective search算法找到的候选框
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    ax.imshow(img)
    for x, y, w, h in candidates:
        print(x, y, w, h)
        rect = mpatches.Rectangle(
            (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
        ax.add_patch(rect)
    plt.show()

if __name__ == "__main__":
    main()
