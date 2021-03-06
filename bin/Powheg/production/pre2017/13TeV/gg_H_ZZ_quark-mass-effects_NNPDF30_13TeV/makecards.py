#!/usr/bin/env python

parameters = (
  (115, 0.00312, 59.0),
  (120, 0.00351, 59.5),
  (124, 0.00394, 59.9),
  (125, 0.00407, 60.0),
  (126, 0.00421, 60.1),
  (130, 0.00491, 60.5),
  (135, 0.00618, 61.0),
  (140, 0.00817, 61.5),
  (145, 0.0114, 62.0),
  (150, 0.0173, 62.5),
  (155, 0.0309, 63.0),
  (160, 0.0831, 63.5),
  (165, 0.246, 64.0),
  (170, 0.38, 64.5),
  (175, 0.501, 65.0),
  (180, 0.631, 65.5),
  (190, 1.04, 66.5),
  (200, 1.43, 67.5),
  (210, 1.85, 68.5),
  (230, 2.82, 70.5),
  (250, 4.04, 72.5),
  (270, 5.55, 74.5),
  (300, 8.43, 77.5),
  (350, 15.2, 82.5),
  (400, 29.2, 87.5),
  (450, 46.8, 92.5),
  (500, 68.0, 97.5),
  (550, 93.0, 102.5),
  (600, 123.0, 107.5),
  (700, 199.0, 117.5),
  (750, 247.0, 122.5),
  (800, 304.0, 127.5),
  (900, 449.0, 137.5),
  (1000, 647.0, 147.5),
  (1500, 750.0, 197.5),
  (2000, 1000.0, 247.5),
  (2500, 1250.0, 297.5),
  (3000, 1500.0, 347.5),
)

with open("gg_H_ZZ_quark-mass-effects_NNPDF30_13TeV_template.input") as f:
  template = f.read()

dct = {}

for dct["mass"], dct["width"], dct["hfact"] in parameters:
  if dct["mass"] < 300:
    dct.update(ncall1=50000, itmx1=5, ncall2=50000, foldcsi=1, foldy=1, foldphi=1)
  else:
    dct.update(ncall1=550000, itmx1=7, ncall2=75000, foldcsi=2, foldy=5, foldphi=2)

  with open("gg_H_ZZ_quark-mass-effects_NNPDF30_13TeV_M{}.input".format(dct["mass"]), "w") as f:
    f.write(template.format(**dct))
