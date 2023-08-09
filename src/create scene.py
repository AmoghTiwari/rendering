import trimesh

mesh = trimesh.load("../data/3DHumans_sample/sample.obj")
# mesh.show()
# print(mesh.visual.uv.shape)

scene = trimesh.scene.Scene()
scene.add_geometry(mesh)
scene.show()