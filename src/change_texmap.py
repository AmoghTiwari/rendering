import trimesh
import PIL
import cv2  
import numpy as np

mesh = trimesh.load("../data/3DHumans_sample/sample.obj")
##### NEW BLOCK ##### 
uv = mesh.visual.uv
img = cv2.imread("../data/3DHumans_sample/material_0.jpeg")
img = np.random.randint(0, 128, size=img.shape, dtype='uint8')
cv2.imwrite("random_tex.png", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = PIL.Image.fromarray(img)
material = trimesh.visual.texture.SimpleMaterial(img)
texture_visual = trimesh.visual.TextureVisuals(uv, material, img)
mesh.visual = texture_visual
# mesh = trimesh.Trimesh(vertices=mesh.vertices, faces=mesh.faces, visual=texture_visual, validate=True, process=False)
##### NEW BLOCK ##### 

mesh.show()
print(mesh.visual.uv.shape)
