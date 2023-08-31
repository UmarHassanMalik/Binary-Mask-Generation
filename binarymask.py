testing_dir = '/kaggle/input/newdataset/test'
mask_files = [f for f in os.listdir(testing_dir) if f.lower().endswith('.png')]

for mask_file in mask_files:
    mask_path = os.path.join(testing_dir, mask_file)  
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    binary_data = mask.tobytes()
    image_shape = (512, 512)
    reshaped_image = np.frombuffer(binary_data, dtype=np.uint8).reshape(image_shape)
    masked_image = cv2.addWeighted(img, 1, reshaped_image, 0.5, 0)
    mask_image.append(masked_image)
    y_test.append(reshaped_image)
mask_image = np.array(mask_image)
