_base_ = './rtmdet-r_l_syncbn_fast_1xb8_36e_dota.py'

deepen_factor = 1.33
widen_factor = 1.25

model = dict(
    backbone=dict(deepen_factor=deepen_factor, widen_factor=widen_factor),
    neck=dict(deepen_factor=deepen_factor, widen_factor=widen_factor),
    bbox_head=dict(head_module=dict(widen_factor=widen_factor)))
