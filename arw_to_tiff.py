import rawpy
import imageio
import glob

path = '/home/aman/Codes/DATASETS/archive/Sony/long/*.ARW'
image_list = []
for filename in glob.glob(path):
    raw_img = rawpy.imread(filename)
    image_list.append(raw_img)

print(len(image_list))
res = [i.postprocess(demosaic_algorithm=None,
                               no_auto_bright=False,
                               fbdd_noise_reduction=rawpy.FBDDNoiseReductionMode.Off,
                               half_size=False,
                               four_color_rgb=False,
                               dcb_iterations=0,
                               dcb_enhance=False, 
                               noise_thr=None,
                               median_filter_passes=0,
                               use_camera_wb=True,
                               output_bps=8,
                               user_flip=None,
                               user_black=None,
                               user_sat=None, 
                               exp_shift=None,
                               exp_preserve_highlights=0.0,
                               no_auto_scale=False, 
                               gamma=None, 
                               chromatic_aberration=None, 
                     bad_pixels_path=None) for i in image_list[:10]]
