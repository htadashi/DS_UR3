from ds_tools.nonlinear_ds import *

models_dir = './learned_models/'
model_name = 'Demonstration_Antonio.yml'

lpv_ds     = lpv_DS(filename=models_dir+model_name,order_type='C')    
ds_fun     = lambda x: lpv_ds.get_ds(x)         

print(ds_fun([[1.0],[1.0],[1.0]]))