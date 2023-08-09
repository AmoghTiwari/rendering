import trimesh

mesh = trimesh.load("../data/3DHumans_sample/sample.obj")
mesh.show()
print(mesh.visual.uv.shape)
