from keras_cv.models import StableDiffusion

model = StableDiffusion()
img = model.text_to_image("Iron Man making breakfast")
