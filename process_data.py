import os
import datetime
import cbpro
import pathlib

from PIL import Image
from shutil import copyfile


def convert_filename(windows_filename):
    return '-'.join(windows_filename.split('-')
                    [0:3]) + ' ' + ':'.join(windows_filename.split('-')[3:])


def crop_and_scale_image(file_location, new_location, base_width=300):
    original = Image.open(file_location)
    width, height = original.size
    # Crop Params (left, upper, right, lower).
    cropped_img = original.crop((0, 159, 759, 689))
    wpercent = (base_width / float(cropped_img.size[0]))
    hsize = int((float(cropped_img.size[1]) * float(wpercent)))
    scaled_img = cropped_img.resize((base_width, hsize), Image.ANTIALIAS)
    scaled_img.save(new_location, 'jpeg')
    return True


def choose_images(images_location, screenshot_duration):
    # We take screenshot at every 10 seconds, 6 in a minute.
    # Select a screenshot that is between second_start and second_end.
    images = []
    for filename in sorted(os.listdir(images_location)):
        if not filename.endswith('.jpg'):
            continue
        better_filename = convert_filename(filename)
        parsed_date_time = datetime.datetime.fromisoformat(
            better_filename.split('.jpg')[0])
        if parsed_date_time.second >= screenshot_duration[0] and parsed_date_time.second <= screenshot_duration[1]:
            images.append((parsed_date_time, filename))
    return images


# candle1 should be before candle2 so that we compare future.
def long_or_short(candle1, candle2, threshold=15):
    # Long if high is greater for next candle ( ohclv)
    if candle1[2] < candle2[2] and candle2[2] - candle1[2] >= threshold:
        return 1
    if candle1[4] > candle2[4] and candle1[4] - candle2[4] >= threshold:
        return -1
    return 0


# Max 300 candles of start and end date should not be more than 5 hours ->
# 60 * 5
def fetch_gdax_data(start_date, end_date, sort=True):
    public_client = cbpro.PublicClient()
    start_date = datetime.datetime.fromisoformat(start_date)
    end_date = datetime.datetime.fromisoformat(end_date)
    delta = datetime.timedelta(hours=5)
    candles = []
    while start_date <= end_date:
        candles += public_client.get_product_historic_rates(
            'BTC-USD',
            start=str(start_date),
            end=str(start_date + delta),
            granularity=60)
        start_date += delta
    if sort:
        return sorted(candles, key=lambda candle: candle[0])
    return candles


def run_crop_and_scale(screenshots_path, scaled_screenshots_path, screenshot_duration):
    scaled_count = len(
        list(pathlib.Path(scaled_screenshots_path).glob('*.jpg')))
    if scaled_count:
        print('Found', scaled_count, 'scaled images, skipping processing.')
        return True
    counter = 0
    for image in choose_images(screenshots_path, screenshot_duration):
        crop_and_scale_image(screenshots_path +
                             image[1], scaled_screenshots_path + str(image[0]) + '.jpg')
        counter += 1
    print('Image Crop and Scaling Done, Processed', counter, 'images.')


def make_subdirectories(path):
    if len(os.listdir(path)) >= 3:
        return True
    os.mkdir(path + 'long')
    os.mkdir(path + 'short')
    os.mkdir(path + 'nothing')
    return True


# Select minimum and maximum datetime from file and query gdax for the data with 1 minutes extra delta.
# Calculate Long/Short Position using those candles and label the images
# at end with _0, _1, _-1
def get_position_details(scaled_screenshots_path, screenshot_duration):
    all_files = choose_images(scaled_screenshots_path, screenshot_duration)
    min_file_datetime, max_file_datetime = all_files[0][
        0], all_files[-1][0] + datetime.timedelta(minutes=1)
    gdax_candles = fetch_gdax_data(
        str(min_file_datetime), str(max_file_datetime))
    positions = {}
    for idx in range(len(gdax_candles) - 1):
        parsed_datetime = datetime.datetime.fromtimestamp(gdax_candles[idx][0])
        positions[str(parsed_datetime)] = long_or_short(
            gdax_candles[idx], gdax_candles[idx + 1])
    return positions


# Using the positions we figure out if image is in that candle.
# Copy the image to path/long, path/short, path/nothing.
def move_to_label_subdirectories(scaled_screenshots_path, positions, label_directory):
    for filename in os.listdir(scaled_screenshots_path):
        if not filename.endswith('.jpg'):
            continue
        parsed_filename = str(datetime.datetime.fromisoformat(
            filename.split('.jpg')[0]).replace(second=0, microsecond=0))
        try:
            if positions[parsed_filename] == 0:  # nothing
                copyfile(scaled_screenshots_path + filename,
                         label_directory + '/nothing/' + filename)
            if positions[parsed_filename] == -1:  # short
                copyfile(scaled_screenshots_path + filename,
                         label_directory + '/short/' + filename)
            if positions[parsed_filename] == 1:  # long
                copyfile(scaled_screenshots_path + filename,
                         label_directory + '/long/' + filename)
        except:
            pass  # Future data don't need it.

screenshots_path = '/Users/abhishekgahlot/Dropbox/screenshots/'
scaled_screenshots_path = '/Users/abhishekgahlot/Documents/mangoshake/new_scaled/'
train_path = '/Users/abhishekgahlot/Documents/mangoshake/new_train/'
screenshot_duration = (40, 50)

run_crop_and_scale(screenshots_path, scaled_screenshots_path,
                   screenshot_duration)
positions = get_position_details(scaled_screenshots_path, screenshot_duration)
move_to_label_subdirectories(scaled_screenshots_path, positions, train_path)
