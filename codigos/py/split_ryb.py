import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.cvtColor(cv2.imread('exemplo.png'), cv2.COLOR_BGR2RGB)

# Separate channels
r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
y = (r.astype(float) + g.astype(float)) / 2  # Yellow channel

# Plot all channels
fig, ax = plt.subplots(2, 2, figsize=(10, 8))
for i, (channel, title, color) in enumerate([
    (r, 'Red', 'Reds'),
    (g, 'Green', 'Greens'), 
    (b, 'Blue', 'Blues'),
    (y, 'Yellow', 'YlOrBr')
]):
    ax[i//2, i%2].imshow(channel, cmap=color)
    ax[i//2, i%2].set_title(title, fontsize=12)
    ax[i//2, i%2].axis('off')

plt.tight_layout()
plt.show()
