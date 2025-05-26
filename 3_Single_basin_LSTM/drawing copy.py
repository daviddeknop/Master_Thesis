import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_tree(ax, x=0, y=0, size=1):
    # Tree trunk
    trunk_width = 0.2 * size
    trunk_height = 0.4 * size
    trunk = patches.Rectangle((x - trunk_width/2, y), trunk_width, trunk_height, color='saddlebrown')
    ax.add_patch(trunk)

    # Tree foliage (3 overlapping circles)
    foliage_radius = 0.2 * size
    foliage1 = patches.Circle((x, y + trunk_height + 0.1 * size), foliage_radius, color='forestgreen')
    foliage2 = patches.Circle((x - 0.15 * size, y + trunk_height + 0.05 * size), foliage_radius, color='forestgreen')
    foliage3 = patches.Circle((x + 0.15 * size, y + trunk_height + 0.05 * size), foliage_radius, color='forestgreen')

    for foliage in [foliage1, foliage2, foliage3]:
        ax.add_patch(foliage)

# Create figure and axis
fig, ax = plt.subplots(figsize=(4, 6))

# Draw the tree
draw_tree(ax, x=0, y=0, size=1)

# Adjust plot limits and remove axes
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.axis('off')

# Save with transparent background
plt.savefig("tree_drawing_transparent.png", dpi=1000, bbox_inches='tight', transparent=True)
plt.show()
